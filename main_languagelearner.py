#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

#check if the version of Python is correct
from python_version_check import check_version
check_version((3, 4, 3))

VERSION_NUMBER = (2, 0, 1)

import re

from textual_data import *
from telegramHigh import TelegramHigh
from language_support import LanguageSupport
from database_manager import DB_Manager
from button_handler import getMainMenu

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

		if message == "/start":
			bot.sendMessage(chat_id=chat_id
				,message=lS(START_MESSAGE)
				,key_markup=MMKM
				)

		elif message == "/words" or message == lS(WORD_LIST_BUTTON):
			def formatWordData(word_list):
				result = ""
				for word in word_list:
					result += "/{0} {1}; {2}\n".format(word["ID"],word["word"],word["translation"])
				return result

			course = databases.getUserCourse(chat_id=chat_id)
			if course == None:
				msg = "You haven't selected a course yet!"
			else:
				word_list = databases.getUserWordList(course=course)
				if not word_list:
					msg = "No words in this course yet"
				else:
					msg = formatWordData(word_list)
			bot.sendMessage(chat_id=chat_id
				,message=msg
				,key_markup=MMKM
				)
		elif message == "/courses":
			courses_list = databases.getUserCoursesList(chat_id)
			if courses_list:
				formatted_list = [("/setcourse" + str(i["ID"]) + " " 
					+ "/courseinfo" + str(i["ID"]) + " " + 
					i["name"]) for i in courses_list]
				msg = "\n".join(formatted_list)
			else:
				msg = "You have no courses yet!"
			bot.sendMessage(chat_id=chat_id
				, message=msg
				, key_markup=MMKM
				)
		elif re.match("^addcourse ", message):
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
		elif re.match("^add ", message):
			course = databases.getUserCourse(chat_id=chat_id)
			if course == None:
				msg = "You haven't selected the course yet!"
			else:
				databases.addWordEntry(data=message[4:], course=course)
				msg = lS(WORD_ADDED_MESSAGE)
			bot.sendMessage(chat_id=chat_id
				,message=msg
				,key_markup=MMKM
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