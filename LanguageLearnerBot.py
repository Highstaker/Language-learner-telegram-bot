#!/usr/bin/python3

# TODO:
# -database mode: show all the answers for a particular entry. Good to refresh an entry you don't remember.
# -put certain messages (for example, main menu welcome) into separate globals, for convenience of editing.
# -spam protection. Maybe drop excessive messages.
# --make bot universal, for databases of any depth. Maybe make the script be ableto work with various databases which can be chosen at runtime.

VERSION_NUMBER = (1,0,2)

from DATABASE import DATABASE
import telegram
from multiprocessing import Process, Queue, Lock
from time import time, sleep
from random import randint, choice
import os
import logging
import socket

#if a connection is lost and getUpdates takes too long, an error is raised
socket.setdefaulttimeout(30)

logging.basicConfig(format = u'[%(asctime)s] %(filename)s[LINE:%(lineno)d]# %(levelname)-8s  %(message)s', 
	level = logging.WARNING)

#################
####PARAMETERS
################

HELP_MESSAGE = '''This bot helps you remember Spanish verb conjugations
			'''
MAIN_MENU_WELCOME_MESSAGE = 'Welcome!'

MAIN_MENU_KEY_MARKUP = [["/help"],["/begin"]]
INGAME_KEY_MARKUP = [["/hint"]]

#For how long a user process lives without user input until it terminates
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

	def getUpdates(self):
		'''
		Gets updates. Retries if it fails.
		'''
		#if getting updates fails - retry
		while True:
			try:
				updates = self.bot.getUpdates(offset=self.LAST_UPDATE_ID, timeout=1)
			except Exception as e:
				logging.error("Could not read updates. Retrying! Error: " + str(e))
				continue
			break
		return updates

	def processMessage(self,message):
		'''
		Processes a message and returns a tuple
		First element - message to display
		Second element - custom keyboard markup to show. None to hide custom keyboard.
		'''

		def getCurDict(modeLevel):
			if not modeLevel:
				return DATABASE
			else:
				cur_dict = DATABASE
				for i in modeLevel:
					cur_dict = cur_dict[i]
				return cur_dict

		def generateButtons(dict1):
			def split_list(alist,max_size=1):
				"""Yield successive n-sized chunks from l."""
				for i in range(0, len(alist), max_size):
					yield alist[i:i+max_size]
			list1 = list(dict1.keys())
			list1.remove("_metadata")
			return list(split_list(list1,3)) + [["Random","Back"]]

		return_text = "ы"
		return_key_markup = "Same"
		# return_modeLevel = None

		cur_dict = getCurDict(self.modeLevel)

		if self.modeLevel == None:
			#Main menu
			if message == '/help':
				return_text = HELP_MESSAGE
			elif message == '/begin':
				return_text = cur_dict['_metadata']['Prompt']
				return_key_markup = generateButtons(cur_dict)
				self.modeLevel = []
			else:
				return_text = "Unknown command"

		elif isinstance(cur_dict,dict):
			#we are not at the bottom yet!
			if message in cur_dict.keys():
				if isinstance(cur_dict[message],dict):
					return_text = cur_dict[message]['_metadata']['Prompt']
					self.modeLevel = self.modeLevel + [message]
					return_key_markup = generateButtons(getCurDict(self.modeLevel))
				else:
					#hit the bottom
					self.modeLevel = self.modeLevel + [message]
					self.form_index = 0 #reset an index that shows which word you are at in the game
					return_text = "Conjugate!\n" + getCurDict(self.modeLevel)[self.form_index][0]
					return_key_markup = INGAME_KEY_MARKUP
			else:
				return_text = "Unknown command"



		elif isinstance(cur_dict,list):
			#to be remade

			# display the right answer
			if message == "/hint":
				return_text = "The correct answer is: " + cur_dict[self.form_index][1]

			else:
				#Mobile devices may start a word with a capital letter. Make input lowercase
				message = message.lower()

				if message == cur_dict[self.form_index][1]:
					#correct
					self.form_index += 1
					return_text = "Correct!\n" + cur_dict[self.form_index][0] if self.form_index < len(cur_dict) else ""

					if self.form_index >= len(cur_dict):
						#Session complete, reset
						return_text += "\nSession complete!"
						self.modeLevel = None
						return_key_markup = MAIN_MENU_KEY_MARKUP
				else:
					#incorrect
					return_text = "Incorrect! Try again!"

		return (return_text,return_key_markup)


	def user_process(self,ID,q):
		'''
		A process working with a user
		'''
		start_timer = time()
		# self.mode = "Main"
		self.modeLevel = None

		self.sendMessage(ID,MAIN_MENU_WELCOME_MESSAGE)

		while time() - start_timer < MAX_PROCESS_TIME:
			if not q.empty():
				message = q.get()

				#process message
				result = self.processMessage(message)
				self.sendMessage(chat_id=ID,
					text=result[0],
					key_markup=None if (result[1] == "Same") else result[1]
					)

				#restart timer
				start_timer = time()

			#A delay to prevent the process from eating CPU resources
			sleep(0.5)

		#send this message to the user when the process is terminated
		self.sendMessage(ID,"Thank you for coming. Type anything to restart the communication.",[["Start"]])

	def sendMessage(self,chat_id,text,key_markup=MAIN_MENU_KEY_MARKUP):
		'''
		Send message to user. Retry on error. Fail on long message.
		'''
		logging.warning("Replying to " + str(chat_id) + ": " + text)
		while True:
			try:
				self.bot.sendChatAction(chat_id,telegram.ChatAction.TYPING)
				self.bot.sendMessage(chat_id=chat_id,
					text=text,
					parse_mode='Markdown',
					reply_markup=telegram.ReplyKeyboardMarkup(key_markup)
					)
			except Exception as e:
				if "Message is too long" in str(e):
					self.sendMessage(chat_id=chat_id
						,text="Error: Message is too long!"
						)
					break
				else:
					logging.error("Could not send message. Retrying! Error: " + str(e))
					continue
			break

	def createUser(self,ID,process,queue):
		'''
		Adds the data about the user, handling process and queue to the users dictionary
		'''
		#lock here! Not needed? (because this function is not called from child processes)
		self.users[ID] = (process,queue)
		#unlock here! Not needed? (because this function is not called from child processes)

	def echo(self):
		bot = self.bot

		updates = self.getUpdates()
		# debug([i.message.text for i in updates])

		#clean non-responding users from the database.
		tempUser = dict(self.users) #because error comes out if dictionary change size during loop
		for user in tempUser:
			if not self.users[user][0].is_alive():
				logging.warning('deleting user ' + str(user))
				del self.users[user]
		del tempUser #freeing memory

		for update in updates:
			chat_id = update.message.chat_id
			Message = update.message
			message = Message.text

			try:
				user = self.users[chat_id]
			except KeyError:
				logging.warning("creating user" + str(chat_id))
				q = Queue()
				p = Process(target=self.user_process, args=(chat_id,q,))
				self.createUser(chat_id,p,q)
				p.start()
				#q.put(message)#not needed, because we don't need to process /start or any random message
			else:
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