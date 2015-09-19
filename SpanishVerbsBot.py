#!/usr/bin/python3

# TODO:
# -mobile devices may start a word with capital letter. Implement a check for the first letter of the word.
# +put VERBS into separate file.
# -put certain messages (for example, main menu welcome) into separate globals, for convenience of editing.
# +read bot token from a separate file.
# -implement hints
# -spam protection. Maybe drop excessive messages.
# --make bot universal, for databases of any depth. Maybe make the script be ableto work with various databases which can be chosen at runtime.

from VERBS import VERBS
import telegram
from multiprocessing import Process, Queue, Lock
from time import time, sleep
from random import randint, choice
import os

DEBUG = True
def debug(*msg):
	if DEBUG:
		print('[DEBUG]', msg)

#################
####PARAMETERS
################

HELP_MESSAGE = '''This bot helps you remember Spanish verb conjugations
			'''
MAIN_MENU_WELCOME_MESSAGE = 'Welcome!'

MAIN_MENU_MARKUP = [["/help"],["/begin"]]
REG_IRREG_MARKUP = [['Regular','Irregular'],['Random','Back']]
CONJ_PICK_MARKUP = [["Conjugation_1","Conjugation_2","Conjugation_3","Irregular"],["Random",'Back']]

MAX_PROCESS_TIME = 120

#get token from a "token" file located in the same directory as the script.
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'token'),'r') as f:
	BOT_TOKEN = f.read().replace("\n","")

class TelegramBot():
	"""docstring for TelegramBot"""

	LAST_UPDATE_ID = None

	users = {}

	lock = Lock()

	def __init__(self, token):
		super(TelegramBot, self).__init__()
		self.bot = telegram.Bot(token)

	def process_message(self,message):
		'''
		Processes a message and returns a tuple
		First element - message to display
		Second element - custom keyboard markup to show. None to hide custom keyboard.
		'''
		debug("mode",self.mode)
		if self.mode == "Main":
			if message == '/help':
				return (HELP_MESSAGE,"Same",None)
			elif message == '/begin':
				return ("Regular (pick conjugation) or Irregular?",CONJ_PICK_MARKUP,"Conj")
			else:
				return ("Unknown command","Same",None)

		elif self.mode == "Conj":

			def generate_verb_buttons(conj):
				def split_list(alist,max_size=1):
					"""Yield successive n-sized chunks from l."""
					for i in range(0, len(alist), max_size):
						yield alist[i:i+max_size]
				list1 = list(VERBS[conj].keys())
				return list(split_list(list1,3)) + [["Random","Back"]]

			eligible_messages = ['Conjugation_1','Conjugation_2','Conjugation_3','Irregular']
			if message in eligible_messages:
				self.conj = message
				return ("Which verb?", generate_verb_buttons(self.conj),"PickVerb")
			elif message == "Random":
				self.conj = choice(eligible_messages)
				return (self.conj.replace("_"," ") + " is picked.\nWhich verb?",generate_verb_buttons(self.conj),"PickVerb")
			elif message == "Back":
				return (MAIN_MENU_WELCOME_MESSAGE,MAIN_MENU_MARKUP,"Main")
			else:
				return ("Unknown command. Try again!","Same",None)


		elif self.mode == "PickVerb":

			def generate_tense_buttons(conj,verb):
				def split_list(alist,max_size=1):
					"""Yield successive n-sized chunks from l."""
					for i in range(0, len(alist), max_size):
						yield alist[i:i+max_size]
				list1 = list(VERBS[conj][verb].keys())
				return list(split_list(list1,3)) + [["Random","Back"]]

			if message == "Back":
				return (MAIN_MENU_WELCOME_MESSAGE,MAIN_MENU_MARKUP,"Main")
			else:
				try:
					self.verb = message if message != "Random" else choice(list(VERBS[self.conj].keys()))
					tenses = list(VERBS[self.conj][self.verb].keys())
					return ("Which tense?", generate_tense_buttons(self.conj,self.verb) , "PickTense")
				except KeyError:
					return ("Unknown command. Try again!","Same",None)
					

		elif self.mode == "PickTense":
			if message == "Back":
				return (MAIN_MENU_WELCOME_MESSAGE,MAIN_MENU_MARKUP,"Main")
			else:
				try:
					self.tense = message if message != "Random" else choice(list(VERBS[self.conj][self.verb].keys()))
					list1 = VERBS[self.conj][self.verb][self.tense]
					self.form_index = 0
					return("The verb is: " + self.verb + "\nThe tense is: " + self.tense.replace("_"," ") + "\nConjugate!",None,"Game")
				except KeyError:
					return ("Could not process message. Try again!","Same",None)

		elif self.mode == "Game":
			forms = VERBS[self.conj][self.verb][self.tense]
			if message.replace("A","á").replace("O","ó").replace("I","í").replace("U","ú").replace("E","é").replace("N","ñ").replace("UU","ü") == forms[self.form_index][1]:
				self.form_index += 1
				return( ( "Correct!" + "\n" + forms[self.form_index][0] ) if (self.form_index < len(forms)) else "Correct!\nAll forms completed!"
					,None if ( self.form_index < len(forms) ) else MAIN_MENU_MARKUP
					,None if (self.form_index< len(forms)) else "Main")
			else:
				return("Incorrect!",None,None)


	def user_process(self,ID,q):
		'''
		A process working with a user
		'''
		start_timer = time()
		self.mode = "Main"

		self.send_message(MAIN_MENU_WELCOME_MESSAGE,ID,MAIN_MENU_MARKUP)

		while time() - start_timer < MAX_PROCESS_TIME:
			if not q.empty():
				message = q.get()

				#process message
				result = self.process_message(message)
				if result[2]:
					self.mode = result[2]
				self.send_message(result[0],ID,result[1])

				#restart timer
				start_timer = time()

			#A delay to prevent the process from eating CPU resources
			sleep(0.5)

		#send this message to the user when the process is terminated
		self.send_message("Thank you for coming. Type anything to restart the communication.",ID)


		# self.delete_user(ID)

	def send_message(self,message,chat_id,keyboard_markup=None):
		'''
		Sends a message
		'''
		#lock here!
		self.lock.acquire()
		debug('sending', message, chat_id)
		self.bot.sendMessage(chat_id=chat_id,
			text=message,
			reply_markup=(telegram.ReplyKeyboardMarkup(keyboard_markup) if keyboard_markup else telegram.ReplyKeyboardHide()) if keyboard_markup!="Same" else None
			)
		#unlock here!
		self.lock.release()

	def delete_user(self,ID):
		'''
		Deletes the user data from the users dictionary
		'''
		#lock here!
		debug("deleting user",ID)
		del self.users[ID]#doesn't delete?
		debug(self.users)
		#unlock here!

	def create_user(self,ID,process,queue):
		'''
		Adds the data about the user, handling process and queue to the users dictionary
		'''
		#lock here!
		self.users[ID] = (process,queue)
		#unlock here!

	def echo(self):
		bot = self.bot

		updates = bot.getUpdates(offset=self.LAST_UPDATE_ID, timeout=3)
		debug([i.message.text for i in updates])

		#clean non-responding users from the database.
		tempUser = dict(self.users) #because error comes out if dictionary change size during loop
		for user in tempUser:
			if not self.users[user][0].is_alive():
				debug('deleting user ', user)
				del self.users[user]

		for update in updates:
			chat_id = update.message.chat_id
			Message = update.message
			message = Message.text

			try:
				debug('try', self.users)
				user = self.users[chat_id]
			except KeyError:
				debug("creating user",chat_id)
				q = Queue()
				p = Process(target=self.user_process, args=(chat_id,q,))
				self.create_user(chat_id,p,q)
				p.start()
				q.put(message)
			else:
				debug('Sending data to user process', chat_id)
				q = user[1]
				q.put(message)

			# Updates global offset to get the new updates
			self.LAST_UPDATE_ID = update.update_id + 1

def main():
	bot = TelegramBot(BOT_TOKEN)

	while True:
		bot.echo()

if __name__ == '__main__':
	main()