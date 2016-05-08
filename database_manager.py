#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import os
from os import path
import sqlite3
from time import time
from random import choice

from textual_data import DATABASE_PATH
from utils import SQLiteUtils
getSQLiteType = SQLiteUtils.getSQLiteType

class DB_Manager(object):
	"""docstring for DB_Manager"""
	def __init__(self, db_filename=None):
		super(DB_Manager, self).__init__()

		os.makedirs(path.dirname(DATABASE_PATH),exist_ok=True)
		if not db_filename:
			self.filename = DATABASE_PATH
		else:
			self.filename = db_filename

		if not path.isfile(self.filename):
			self._createTables()

	def initializeUser(self,chat_id):
		"""
		Create a user entry, if it doesn't exist yet. Do nothing if there is one.
		"""
		command = "INSERT INTO users (chat_id, lang, admin) VALUES ({0},'EN',0);".format(chat_id)

		try:
			self._run_command(command)
		except sqlite3.IntegrityError:
			# if user already exists, do nothing
			pass

	def getLanguage(self, chat_id):
		"""
		Returns an interface language selected by a user
		"""
		command = "SELECT lang FROM users WHERE chat_id={0};".format(chat_id)

		data = self._run_command(command)

		return data[0][0]

	def setLanguage(self, chat_id, lang):
		"""
		Sets the interface language for the user
		:param chat_id:
		:param lang:
		:return:
		"""

		command = "UPDATE users SET lang='{0}' WHERE chat_id={1};".format(lang,chat_id)

		self._run_command(command)

	def askRefreshWord(self,chat_id,course):
		"""
		Sets the user to answer state. Returns the promt.
		"""
		# time to wait since last refresh for each level
		LEVEL_TIMES = (0,
					   14400,#4h
					   43200,#12h
					   86400,#1d
					   259200,#3d
					   604800,#1w
					   1209600,#2w
					   2419200,#1m
					   4838400,#2m
					   7257600,#3m
					   )

		data = self.getCourseWordList(course)

		refreshable = list()
		min_time_till_refresh = float("inf") # if all words are fresh, take the minimum time till refresh and return it
		for Word in data:
			try:
				level_time = LEVEL_TIMES[Word["level"]]
			except IndexError:
				level_time = LEVEL_TIMES[len(LEVEL_TIMES)-1]

			time_left = (Word["last_refresh"] + level_time) - time()
			if time_left < 0:
				refreshable.append(Word)
			else:
				if time_left < min_time_till_refresh:
					min_time_till_refresh = time_left

		if refreshable:
			the_word = choice(refreshable)

			self.setUserAnswerState(chat_id, the_word["ID"])

			result = the_word["translation"]
		else:
			try:
				result = int(min_time_till_refresh)
			except OverflowError:
				result = None

		return result, len(refreshable)

	def incrementWordLevel(self, ID):
		"""
		Adds one to word level. Usually called after correct answer
		"""
		command = "UPDATE words SET level=level+1 WHERE ID={0}".format(ID)

		self._run_command(command)

	def resetWordLevel(self, ID):
		"""
		Resets the word level to zero. Usually called after wrong answer
		"""
		command = "UPDATE words SET level=0 WHERE ID={0}".format(ID)

		self._run_command(command)

	def updateWordRefreshTime(self,ID):
		"""
		Sets the "last_updated" field for a word to current time
		:param ID:
		:return:
		"""
		command = "UPDATE words SET last_refresh={0} WHERE ID={1}".format(int(time()), ID)

		self._run_command(command)

	def nullifyUserAnswerState(self, chat_id):
		"""
		Reset the user's answer state. Means return to main menu
		"""
		command = "UPDATE users SET answer_state=NULL WHERE chat_id={0};".format(chat_id)

		self._run_command(command)

	def setUserAnswerState(self, chat_id, ID):
		"""
		Sets the answer state for a user. GEnerally used to show the ID of a word to refresh.
		"""
		command = "UPDATE users SET answer_state={0} WHERE chat_id={1};".format(ID, chat_id)

		self._run_command(command)

	def getUserAnswerState(self, chat_id):
		"""
		Returns the answer state for a user
		"""
		command = "SELECT answer_state FROM users WHERE chat_id={0};".format(chat_id)

		data = self._run_command(command)

		return data[0][0]

	def getUserCourse(self, chat_id):
		"""
		Returns the ID of the course selected by a user
		"""
		command = "SELECT cur_course FROM users WHERE chat_id={0};".format(chat_id)

		data = self._run_command(command)

		return data[0][0]

	def getUserCoursesList(self, chat_id):
		"""
		Returns the list of dictionaries containing data about all courses created by user 
		"""
		command = "SELECT ID, name, description FROM courses WHERE author_id={0};".format(chat_id)

		data = self._run_command(command)

		if not data:
			return None

		result = []
		for i in data:
			result.append({"ID": i[0], 
				"name": i[1],
				"description": i[2] if i[2] else "",
				})

		return result

	def deleteWord(self,chat_id, index):
		"""
		Deletes a word, but only if it belongs to the specified user user
		"""
		command = """DELETE FROM words WHERE ID IN 
		(SELECT words.ID FROM words JOIN courses ON words.course=courses.ID 
			WHERE words.ID={0} and courses.author_id={1});""".format(index,chat_id)

		self._run_command(command)


	def setUserCourse(self, chat_id, course):
		"""
		Set the current course for a user
		:param chat_id:
		:param course: course ID
		:return:
		"""
		command = "UPDATE users SET cur_course={0} WHERE chat_id={1};".format(course, chat_id)

		self._run_command(command)

	def getCourseWordList(self, course):
		"""
		Returns a list of words in the course.
		"""
		command = "SELECT ID, word, translation, last_refresh, level FROM words WHERE course={0};".format(course)

		data = self._run_command(command)

		result = list()
		for word_data in data:
			result.append({"ID": word_data[0],
			 "word": word_data[1],
			  "translation": word_data[2],
			  "last_refresh": word_data[3],
			  "level": word_data[4]
			  })

		return result

	def getWordData(self, ID):
		"""
		Returns data for a word with given ID
		"""
		command = "SELECT word, translation, last_refresh, level FROM words WHERE ID={0};".format(ID)

		data = self._run_command(command)

		try:
			data = data[0]
		except TypeError:
			return None

		result = {"word": data[0],
			"translation": data[1],
			"last_refresh": data[2],
			"level": data[3]
			}

		return result


	def addCourse(self, chat_id, course):
		"""
		Adds a course.
		:course: a course name
		"""
		command = """INSERT INTO courses (name, author_id, description) 
										VALUES ('{0}',{1},'');""".format(course, chat_id)

		self._run_command(command)

	def getCourseData(self, course):
		"""
		Returns a dictionary containing information about the course
		"""
		if course == None:
			return None
		command = "SELECT name, description, author_id FROM courses WHERE id ={0};".format(course)

		data = self._run_command(command)

		if not data:
			return None

		data = data[0]
		result = {"name": data[0] if data[0] else "", 
		"description": data[1] if data[1] else "", 
		"author_id": data[2]}

		return result

	def addWordEntry(self, data, course):
		"""
		Adds a word to words table. Returns False if the input format is incorrect
		:chat_id: user that entered the word
		:data: unparsed data about the word
		:course: a course ID which this word belongs to
		"""

		def parseWordData(Data):
			divisor = "@@"
			result = Data.split(divisor)

			if len(result) < 2:
				return None, None
			else:
				result = [i.strip("\t\n\r ") for i in result]
				if not result[0] or not result[1]:
					return None, None

				return result[0], result[1]

		word, translation = parseWordData(data)

		if not word:
			return False
		else:
			command = "INSERT INTO words (word, translation, level, course, last_refresh)" \
					  " VALUES ('{0}','{1}',0, {2}, 0);".format(word, translation, course)

			self._run_command(command)
			return True

	def _addColumn(self, table, column, init_data):
		"""
		Adds a column to the table, if it doesn't exist
		:param column: name of the new column
		:param init_data: data to be put in that column. Used to determine the type
		:return:
		"""
		command = "ALTER TABLE " + table + " ADD COLUMN " + str(column) + " " + getSQLiteType(init_data)
		try:
			self._run_command(command)
		except sqlite3.OperationalError:
			print("Column " + str(column) + " already exists!")

	def _createTables(self):
		self._createUserTable()
		self._createCoursesTable()
		self._createWordsTable()

	def _createWordsTable(self):
		"""
		Creates a table of words. 
		word is the word itself. The one that the player will need to input.
		translation will be shown in the promt.
		last refresh is the time (time()) when user refreshed this word.
		level determines how long to wait before the next refresh.
		course - ID of a course this word belongs to
		"""
		command = """CREATE TABLE words (ID INTEGER PRIMARY KEY,
			word TEXT,
			translation TEXT,
			last_refresh INTEGER,
			level INTEGER,
			course INTEGER
			);
"""

		self._run_command(command)

	def _createCoursesTable(self):
		"""
		Creates a table of courses. 
		name is a string name of the course
		author_id is chat_id of the user who created the course
		decription - is thedescription of the course
		"""
		command = """CREATE TABLE courses (ID INTEGER PRIMARY KEY,
			name TEXT,
			author_id INTEGER,
			description TEXT
			);
"""

		self._run_command(command)


	def _createUserTable(self):
		"""
		Creates a table of users. 
		lang is the interface language.
		admin can be is 0 or 1.
		cur_course is the course currently selected by user to learn.
		"""

		command = """CREATE TABLE users (chat_id INTEGER PRIMARY KEY,
			lang TEXT,
			admin INTEGER,
			cur_course INTEGER,
			answer_state INTEGER
			);
"""

		self._run_command(command)


	def _run_command(self, command):
		"""
		Runs a given command and returns the output.
		:param command:
		:return:
		"""
		conn = sqlite3.connect(self.filename)
		cursor = conn.execute(command)
		data =[i for i in cursor]
		conn.commit()
		conn.close()

		return data

#############
# tests######
#############

import unittest
class Tests(unittest.TestCase):

	def test_common(self):
		test_db_filename = "databases/test.db"

		try:
			db = DB_Manager(test_db_filename)
			db.initializeUser(111)
			db.initializeUser(111)
			db.initializeUser(222)

			# print("getLanguage 111", db.getLanguage(111))
			self.assertEqual(db.getLanguage(111), "EN")
			db.setLanguage(111,"RU")
			# print("getLanguage 111", db.getLanguage(111))
			self.assertEqual(db.getLanguage(111), "RU")
			# print("getLanguage 222", db.getLanguage(222))
			self.assertEqual(db.getLanguage(222), "EN")

			# print("getUserCourse 111", db.getUserCourse(111))
			self.assertEqual(db.getCourseData(None),None)
			self.assertEqual(db.getCourseData(1),None)
			self.assertEqual(db.getUserCourse(111), None)
			db.addCourse(111, "Deutsch")
			db.setUserCourse(111, 1)
			self.assertEqual(db.getCourseData(1),{"name":"Deutsch", 'description': "", "author_id": 111})
			# print("getUserCourse 111", db.getUserCourse(111))
			self.assertEqual(db.getUserCourse(111), 1)

			self.assertEqual(db.getCourseWordList(course=1),list())
			db.addWordEntry(data="hello@@привет",course=1)
			db.addWordEntry(data="goodbye@@пока",course=1)
			self.assertEqual(db.getCourseWordList(course=1),[{"ID": 1, "word": "hello", "translation": "привет"},
				{"ID": 2, "word": "goodbye", "translation": "пока"}])

		finally:
			os.remove(test_db_filename)

if __name__ == '__main__':
	unittest.main()