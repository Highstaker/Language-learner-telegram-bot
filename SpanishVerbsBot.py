#!/usr/bin/python3

import telegram
from multiprocessing import Process, Queue, Lock
from time import time, sleep
from random import randint, choice

DEBUG = True
def debug(*msg):
	if DEBUG:
		print('[DEBUG]', msg)

#################
####PARAMETERS
################

VERBS = {
"Conjugation_1" : {
"bailar" : { "Presente" :[("yo","bailo"),("tu","bailas"), ("el/ella","baila"),("nosotros", "bailamos"),("vosotros", "bailáis") ,("ellos", "bailan")]
,"Pretérito_imperfecto":[("yo","bailaba"),("tu","bailabas"), ("el/ella","bailaba"),("nosotros", "bailábamos"),("vosotros", "bailabais") ,("ellos", "bailaban")]
,"Pretérito_simple": [("yo","bailé"),("tu","bailaste"), ("el/ella","bailó"),("nosotros", "bailamos"),("vosotros", "bailasteis") ,("ellos", "bailaron")]
,"Futuro" :[("yo","bailaré"),("tu","bailarás"), ("el/ella","bailará"),("nosotros", "bailaremos"),("vosotros", "bailaréis") ,("ellos", "bailarán")]
,"Potencial":[("yo","bailaría"),("tu","bailarías"), ("el/ella","bailaría"),("nosotros", "bailaríamos"),("vosotros", "bailaríais") ,("ellos", "bailarían")]
,"Presente_de_subjuntivo": [("yo","baile"),("tu","bailes"), ("el/ella","baile"),("nosotros", "bailemos"),("vosotros", "bailéis") ,("ellos", "bailen")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","bailara"),("tu","bailaras"), ("el/ella","bailara"),("nosotros", "bailáramos"),("vosotros", "bailarais") ,("ellos", "bailaran")]
,"Modo_imperativo_afirmativo":[("tu","baila"), ("usted","baile"),("nosotros", "bailemos"),("vosotros", "bailad") ,("ustedes", "bailen")]
}
}
,"Conjugation_2" : {
"comer" : { "Presente" :[("yo","como"), ("tu","comes"),("el/ella", "come"),("nosotros", "comemos"), ("vosotros","coméis") ,("ellos", "comen")]
,"Pretérito_imperfecto":[("yo","comía"), ("tu","comías"),("el/ella", "comía"),("nosotros", "comíamos"), ("vosotros","comíais") ,("ellos", "comían")]
,"Pretérito_simple": [("yo","comí"), ("tu","comiste"),("el/ella", "comió"),("nosotros", "comimos"), ("vosotros","comisteis") ,("ellos", "comieron")]
,"Futuro" :[("yo","comeré"), ("tu","comerás"),("el/ella", "comerá"),("nosotros", "comeremos"), ("vosotros","comeréis") ,("ellos", "comerán")]
,"Potencial":[("yo","comería"), ("tu","comerías"),("el/ella", "comería"),("nosotros", "comeríamos"), ("vosotros","comeríais") ,("ellos", "comerían")]
,"Presente_de_subjuntivo": [("yo","coma"), ("tu","comas"),("el/ella", "coma"),("nosotros", "comamos"), ("vosotros","comáis") ,("ellos", "coman")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","comiera"), ("tu","comieras"),("el/ella", "comiera"),("nosotros", "comiéramos"), ("vosotros","comierais") ,("ellos", "comieran")]
,"Modo_imperativo_afirmativo": [("tu","come"), ("usted","coma"),("nosotros", "comamos"),("vosotros", "comed") ,("ustedes", "coman")]
}
}
,"Conjugation_3" : {
"vivir" : { "Presente" :[("yo","vivo"), ("tu","vives"),("el/ella", "vive"),("nosotros", "vivimos"), ("vosotros","vivís") ,("ellos", "viven")]
,"Pretérito_imperfecto":[("yo","vivía"), ("tu","vivías"),("el/ella", "vivía"),("nosotros", "vivíamos"), ("vosotros","vivíais") ,("ellos", "vivían")]
,"Pretérito_simple": [("yo","viví"), ("tu","viviste"),("el/ella", "vivió"),("nosotros", "vivimos"), ("vosotros","vivisteis") ,("ellos", "vivieron")]
,"Futuro" :[("yo","viviré"), ("tu","vivirás"),("el/ella", "vivirá"),("nosotros", "viviremos"), ("vosotros","viviréis") ,("ellos", "vivirán")]
,"Potencial":[("yo","viviría"), ("tu","vivirías"),("el/ella", "viviría"),("nosotros", "viviríamos"), ("vosotros","viviríais") ,("ellos", "vivirían")]
,"Presente_de_subjuntivo": [("yo","viva"), ("tu","vivas"),("el/ella", "viva"),("nosotros", "vivamos"), ("vosotros","viváis") ,("ellos", "vivan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","viviera"), ("tu","vivieras"),("el/ella", "viviera"),("nosotros", "viviéramos"), ("vosotros","vivierais") ,("ellos", "vivieran")]
,"Modo_imperativo_afirmativo": [("tu","vive"), ("usted","viva"),("nosotros", "vivamos"),("vosotros", "vivid") ,("ustedes", "vivan")]
}
}
,"Irregular":{
	"ir" : {
 "Presente" :[("yo","voy"), ("tu","vas"),("el/ella", "va"),("nosotros", "vamos"), ("vosotros","vais") ,("ellos", "van")]
,"Pretérito_imperfecto":[("yo","iba"), ("tu","ibas"),("el/ella", "iba"),("nosotros", "íbamos"), ("vosotros","ibais") ,("ellos", "iban")]
,"Pretérito_simple": [("yo","fui"), ("tu","fuiste"),("el/ella", "fue"),("nosotros", "fuimos"), ("vosotros","fuisteis") ,("ellos", "fueron")]
,"Futuro" :[("yo","iré"), ("tu","irás"),("el/ella", "irá"),("nosotros", "iremos"), ("vosotros","iréis") ,("ellos", "irán")]
,"Potencial":[("yo","iría"), ("tu","irías"),("el/ella", "iría"),("nosotros", "iríamos"), ("vosotros","iríais") ,("ellos", "irían")]
,"Presente_de_subjuntivo": [("yo","vaya"), ("tu","vayas"),("el/ella", "vaya"),("nosotros", "vayamos"), ("vosotros","vayáis") ,("ellos", "vayan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","fuera"), ("tu","fueras"),("el/ella", "fuera"),("nosotros", "fuéramos"), ("vosotros","fuerais") ,("ellos", "fueran")]
,"Modo_imperativo_afirmativo": [("tu","ve"), ("usted","vaya"),("nosotros", "vayamos"),("vosotros", "id") ,("ustedes", "vayan")]

}
} 
}

HELP_MESSAGE = '''This bot helps you remember Spanish verb conjugations
			'''

MAIN_MENU_MARKUP = [["/help"],["/begin"]]
REG_IRREG_MARKUP = [['Regular','Irregular'],['Random','Back']]
CONJ_PICK_MARKUP = [["Conjugation_1","Conjugation_2","Conjugation_3","Irregular"],["Random",'Back']]

MAX_PROCESS_TIME = 120

BOT_TOKEN = "132890499:AAFiiuze1SrX0v-_50qmBa5bMx6AVCqXSYY"



class TelegramBot():
	"""docstring for TelegramBot"""

	LAST_UPDATE_ID = None

	users = {}

	lock = Lock()

	def __init__(self, token):
		super(TelegramBot, self).__init__()
		self.bot = telegram.Bot(token)

	def process_message(self,message,mode):
		'''
		Processes a message and returns a tuple
		First element - message to display
		Second element - custom keyboard markup to show. None to hide custom keyboard.
		Third element - the mode to switch to. None if no mode-switching required
		'''
		debug("mode",mode)
		if mode == "Main":
			if message == '/help':
				return (HELP_MESSAGE,"Same",None)
			elif message == '/begin':
				return ("Regular (pick conjugation) or Irregular?",CONJ_PICK_MARKUP,"Conj")
			else:
				return ("Unknown command","Same",None)

		elif mode == "Conj":

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
				return ("Which verb?", generate_verb_buttons(message),"PickVerb")
			elif message == "Random":
				self.conj = choice(eligible_messages)
				return (conj.replace("_"," ") + " is picked.\nWhich verb?",generate_verb_buttons(conj),"PickVerb")
			else:
				return ("Unknown command. Try again!","Same",None)


		elif mode == "PickVerb":

			def generate_tense_buttons(conj,verb):
				def split_list(alist,max_size=1):
					"""Yield successive n-sized chunks from l."""
					for i in range(0, len(alist), max_size):
						yield alist[i:i+max_size]
				list1 = list(VERBS[conj][verb].keys())
				return list(split_list(list1,3)) + [["Random","Back"]]

			if message == "Random":
				pass
			elif message == "Back":
				pass
			else:
				try:
					tenses = list(VERBS[self.conj][message].keys())
					self.verb = message
					return ("Which tense?", generate_tense_buttons(self.conj,message) , "PickTense")
				except KeyError:
					return ("Unknown command. Try again!","Same",None)
					

		elif mode == "PickTense":
			conj = mode[0]#extracting tense from mode
			if message == "Random":
				pass
			else:
				try:
					list1 = VERBS[self.conj][self.verb][message]
					self.tense = tense = message
					self.form_index = 0
					return("The verb is: " + self.verb + "\nThe tense is: " + tense.replace("_"," ") + "\nConjugate!",None,"Game")
				except KeyError:
					return ("Could not process message. Try again!","Same",None)

		elif mode == "Game":
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
		mode = "Main"

		self.send_message("Welcome!",ID,MAIN_MENU_MARKUP)

		while time() - start_timer < MAX_PROCESS_TIME:
			if not q.empty():
				message = q.get()

				#process message
				result = self.process_message(message,mode)
				if result[2]:
					mode = result[2]
				self.send_message(result[0],ID,result[1])

				#restart timer
				start_timer = time()


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

		try:
			debug("self.conj",self.conj)
		except Exception as e:
			debug(e)

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