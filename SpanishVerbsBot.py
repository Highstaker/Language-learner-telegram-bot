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
"Regular" : {
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
CONJ_PICK_MARKUP = [["Conjugation_1","Conjugation_2","Conjugation_3"],["Random",'Back']]

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
				return (HELP_MESSAGE,MAIN_MENU_MARKUP,None)
			elif message == '/begin':
				return ("Regular or Irregular?",REG_IRREG_MARKUP,"Reg/Irreg?")
			else:
				return ("Unknown command",MAIN_MENU_MARKUP,None)
		elif mode == "Reg/Irreg?":
			if message == "Regular":
				return ("Which conjugation?",CONJ_PICK_MARKUP,"ConjN?")
			elif message == "Irregular":
				def split_list(alist,max_size=1):
					"""Yield successive n-sized chunks from l."""
					for i in range(0, len(alist), max_size):
						yield alist[i:i+max_size]
				return ("Which irregular verb?",list(split_list(list(VERBS["Irregular"].keys()),5)) + [["Random","Back"]],"PickVerb")
			else:
				return ("Unknown command. Try again!","Same",None)
		elif mode == "PickVerb":
			if message == "Random":
				pass
			elif message == "Back":
				pass
			else:
				try:
					tenses = list(VERBS["Irregular"][message].keys())
				except KeyError:
					pass
					
		elif mode == "ConjN?":
			def generate_tense_buttons(conj):
				def split_list(alist,max_size=1):
					"""Yield successive n-sized chunks from l."""
					for i in range(0, len(alist), max_size):
						yield alist[i:i+max_size]
				list1 = list(VERBS["Regular"]["Conjugation_"+str(conj)][list(VERBS["Regular"]["Conjugation_"+str(conj)].keys())[0]].keys())
				return list(split_list(list1,3)) + [["Random","Back"]]
			if "Conjugation" in message:
				try:
					conj = int(message.split("_")[1])
					if conj in range(1,4): 
						#[1,2,3]
						return ("Which tense?",  generate_tense_buttons(conj),str(conj) + "PickTense")
				except Exception as e:
					debug(e)
					return ("Could not process message. Try again!",CONJ_PICK_MARKUP,None)
			elif message == "Random":
				conj = randint(1,3)
				return ("Conjugation " + str(conj) + " is picked.\nWhich tense?",generate_tense_buttons(conj),str(conj) + "PickTense")
			else:
				return ("Unknown command. Try again!",CONJ_PICK_MARKUP,None)
		elif "PickTense" in mode:
			conj = mode[0]#extracting tense from mode
			if message == "Random":
				pass
			else:
				try:
					list1 = VERBS["Regular"]["Conjugation_" + str(conj)]
					verb = choice(list(list1.keys()))
					list2 = list1[verb]
					tense = message
					list2[tense]
					return("The verb is: " + verb + "\nThe tense is: " + tense.replace("_"," ") + "\nConjugate!",None,"Game " + "Regular " + "Conjugation_" + str(conj) + " " + verb + " " + tense + " " + "0")
				except KeyError:
					return ("Could not process message. Try again!","Same",None)
		elif "Game" in mode:
			parse = mode.split()
			if parse[1] == "Regular":
				debug('parse',parse)
				# sleep(60)
				list1 = VERBS["Regular"][parse[2]][parse[3]][parse[4]]
				if message.replace("A","á").replace("O","ó").replace("I","í").replace("U","ú").replace("E","é").replace("N","ñ").replace("UU","ü") == list1[int(parse[5])][1]:
					return( ( "Correct!" + "\n" + list1[int(parse[5])+1][0] ) if (int(parse[5])+1 < len(list1)) else "Correct!\nAll forms completed!"
						,None if ( int(parse[5])+1 < len(list1) ) else MAIN_MENU_MARKUP
						,"Game " + "Regular " + parse[2] + " " + parse[3] + " " + parse[4] + " " + str(int(parse[5])+1) if (int(parse[5])+1 < len(list1)) else "Main")
				else:
					return("Incorrect!",None,None)
			elif parse[2] == "Irregular":
				pass


	def user_process(self,ID,q):
		'''
		A process working with a user
		'''
		start_timer = time()
		mode = "Main"

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