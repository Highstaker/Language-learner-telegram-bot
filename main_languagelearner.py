#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

#check if the version of Python is correct
from python_version_check import check_version
check_version((3, 4, 3))

VERSION_NUMBER = (2, 1, 10)

import re

from textual_data import *
from telegramHigh import TelegramHigh
from language_support import LanguageSupport
from database_manager import DB_Manager
from button_handler import getMainMenu
import utils

class LanguageLearner(object):
	"""docstring for LanguageLearner"""
	def __init__(self, token):
		super(LanguageLearner, self).__init__()

		self.bot = TelegramHigh(token)

		self.databases = DB_Manager()

	def run(self):
		self.bot.start(processingFunction=self.processingRoutine)

	def processingRoutine(self, u):
		bot = self.bot
		Message = u.message
		message = Message.text
		message_id = Message.message_id
		chat_id = Message.chat_id
		databases = self.databases

		# # initialize the user's params if they are not present yet
		databases.initializeUser(chat_id=chat_id)

		# language support class for convenience
		LS = LanguageSupport(databases.getLanguage(chat_id=chat_id))
		lS = LS.languageSupport
		allv = LS.allVariants
		MM = getMainMenu()
		MMKM = lS(MM)

		user_answer_state = databases.getUserAnswerState(chat_id)

		if user_answer_state:
			the_word = databases.getWordData(ID=user_answer_state)["word"]
			if message.lower() == the_word.lower():
				databases.incrementWordLevel(ID=user_answer_state)
				msg = "Correct!"
			else:
				databases.resetWordLevel(ID=user_answer_state)
				msg = "Wrong! The correct answer is {0}".format(the_word)
			databases.updateWordRefreshTime(ID=user_answer_state)
			databases.nullifyUserAnswerState(chat_id)
			bot.sendMessage(chat_id=chat_id
				,message=msg
				,key_markup=MMKM
				)
		else:
			if message == "/start":
				bot.sendMessage(chat_id=chat_id
					,message=lS(START_MESSAGE)
					,key_markup=MMKM
					)
			elif message == "/help" or message == lS(HELP_BUTTON):
				bot.sendMessage(chat_id=chat_id
								, message=lS(HELP_MESSAGE)
								, key_markup=MMKM
								, markdown=True
								)
			elif message == "/about" or message == lS(ABOUT_BUTTON):
				bot.sendMessage(chat_id=chat_id
								, message=lS(ABOUT_MESSAGE).format(".".join([str(i) for i in VERSION_NUMBER]))
								, key_markup=MMKM
								, markdown=True
								)
			elif message == "/otherbots" or message == lS(OTHER_BOTS_BUTTON):
				bot.sendMessage(chat_id=chat_id
								, message=lS(OTHER_BOTS_MESSAGE)
								, key_markup=MMKM
								, markdown=True
								)
			elif message == "/refresh" or message == lS(REFRESH_BUTTON):
				course = databases.getUserCourse(chat_id)
				if course == None:
					msg = "No course is set!"
				else:
					result, number_of_refreshable_words = databases.askRefreshWord(chat_id, course)
					if isinstance(result, str):
						msg = "Words left to refresh: {}\n\n".format(number_of_refreshable_words)
						msg += result
					elif isinstance(result, int):
						msg = "Everything is fresh in this course!\n"\
						+ "Till next refresh: {}".format(utils.secondsToText(result))
					else:
						msg = "Unknown error!"
				bot.sendMessage(chat_id=chat_id
					, message=msg
					, key_markup=None
					)

			elif message == "/words" or message == lS(WORD_LIST_BUTTON):
				def formatWordData(word_list):
					result = ""
					for word in word_list:
						result += "№{0} {1}; {2}\n".format(word["ID"],word["word"],word["translation"])
					return result

				course = databases.getUserCourse(chat_id=chat_id)
				if course == None:
					msg = "You haven't selected a course yet!"
				else:
					word_list = databases.getCourseWordList(course=course)
					if not word_list:
						msg = "No words in this course yet"
					else:
						msg = formatWordData(word_list)
				bot.sendMessage(chat_id=chat_id
					,message=msg
					,key_markup=MMKM
					)
			elif message == "/courses" or message == lS(COURSES_LIST_BUTTON):
				courses_list = databases.getUserCoursesList(chat_id)
				selected_course = databases.getUserCourse(chat_id)
				if courses_list:
					formatted_list = [(
						("(*)" if selected_course == i["ID"] else "/setcourse" + str(i["ID"]))
						+ " "
						# + "/courseinfo" + str(i["ID"]) + " "
						+ i["name"]) for i in courses_list]
					msg = "\n".join(formatted_list)
				else:
					msg = "You have no courses yet!"
				bot.sendMessage(chat_id=chat_id
					, message=msg
					, key_markup=MMKM
					)
			elif re.match("^addcourse ", message, re.IGNORECASE):
				databases.addCourse(chat_id=chat_id, course=message[10:])
				bot.sendMessage(chat_id=chat_id
								, message=lS(COURSE_ADDED_MESSAGE)
								, key_markup=MMKM
								)
			elif re.fullmatch("^/setcourse[0-9]*$", message):
				course_data = databases.getCourseData(course=message[len("/setcourse"):])
				if not course_data:
					msg = "Course doesn't exist!"
				else:
					course_name = course_data["name"]			
					databases.setUserCourse(chat_id,course=message[len('/setcourse'):])
					msg = lS(COURSE_SET_MESSAGE).format(course_name)
				bot.sendMessage(chat_id=chat_id
					, message=msg
					, key_markup=MMKM
					)
			elif re.match("^add ", message, re.IGNORECASE):
				course = databases.getUserCourse(chat_id=chat_id)
				if course == None:
					msg = "You haven't selected the course yet!"
				else:
					status = databases.addWordEntry(data=message[4:], course=course)
					if status:
						msg = lS(WORD_ADDED_MESSAGE)
					else:
						msg = lS(INCORRECT_FORMAT_MESSAGE)
				bot.sendMessage(chat_id=chat_id
					,message=msg
					,key_markup=MMKM
					)
			elif re.fullmatch("^/del[0-9]*", message):
				databases.deleteWord(chat_id=chat_id, index=message[4:])
				msg = "Word deleted!"
				bot.sendMessage(chat_id=chat_id
					,message=msg
					,key_markup=MMKM
					)
			elif message == RU_LANG_BUTTON:
				databases.setLanguage(chat_id, 'RU')
				LS = LanguageSupport("RU")
				bot.sendMessage(chat_id=chat_id
								, message="Сообщения бота будут отображаться на русском языке."
								, key_markup=LS.languageSupport(MM)
								)
			elif message == EN_LANG_BUTTON:
				databases.setLanguage(chat_id, 'EN')
				LS = LanguageSupport("EN")
				bot.sendMessage(chat_id=chat_id
								, message="Bot messages will be shown in English."
								, key_markup=LS.languageSupport(MM)
								)
			else:
				bot.sendMessage(chat_id=chat_id,
					message=lS(UNKNOWN_COMMAND_MESSAGE)
					,key_markup=MMKM
					)




def main():
	ll = LanguageLearner(BOT_TOKEN)


	ll.run()

if __name__ == '__main__':
	main()