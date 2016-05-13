#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

class SQLiteUtils:

	@staticmethod
	def getSQLiteType(param):
		"""
		Returns the SQLite type of a given parameter
		:param param: a parameter a type of which should be returned
		:return: a string representing an SQLite type
		"""
		if isinstance(param, str):
			result = "TEXT"
		elif isinstance(param, int):
			result = "INTEGER"
		elif isinstance(param,float):
			result = "DECIMAL"
		else:
			result = "BLOB"

		return result

	@staticmethod
	def escapeText(text):
		return text.replace("'", "''")


class DictUtils:
	@staticmethod
	def replaceKey(dic, oldkey, newkey):
		try:
			dic[newkey] = dic.pop(oldkey)
		except KeyError:
			raise KeyError("Could not replace key {0}. It was not found!".format(oldkey))

	@staticmethod
	def dictGetCaseInsensitive(dic, key):
		result = None
		try:
			# maybe it already exists as-is
			result = dic[key]
		except KeyError:
			error_message = "The key was not found, even case-insensitively"
			if isinstance(key, str):
				# try to find case-insensitively
				upper_key = key.upper()
				for i in dic:
					if i.upper() == upper_key:
						result = dic[i]
						break
				else:
					raise KeyError(error_message)
			else:
				raise KeyError(error_message)

		return result

def pluralizeRussian(number, nom_sing, gen_sing, gen_pl):
	s_last_digit = str(number)[-1]

	if int(str(number)[-2:]) in range(11,20):
		#11-19
		return gen_pl
	elif s_last_digit == '1':
		#1
		return nom_sing
	elif int(s_last_digit) in range(2,5):
		#2,3,4
		return gen_sing
	else:
		#5,6,7,8,9,0
		return gen_pl

def secondsToText(secs, lang="EN"):
	days = secs//86400
	hours = (secs - days*86400)//3600
	minutes = (secs - days*86400 - hours*3600)//60
	seconds = secs - days*86400 - hours*3600 - minutes*60

	if lang == "ES":
		days_text = "día{}".format("s" if days!=1 else "")
		hours_text = "hora{}".format("s" if hours!=1 else "")
		minutes_text = "minuto{}".format("s" if minutes!=1 else "")
		seconds_text = "segundo{}".format("s" if seconds!=1 else "")
	elif lang == "DE":
		days_text = "Tag{}".format("e" if days!=1 else "")
		hours_text = "Stunde{}".format("n" if hours!=1 else "")
		minutes_text = "Minute{}".format("n" if minutes!=1 else "")
		seconds_text = "Sekunde{}".format("n" if seconds!=1 else "")
	elif lang == "RU":
		days_text = pluralizeRussian(days, "день", "дня", "дней")
		hours_text = pluralizeRussian(hours, "час", "часа", "часов")
		minutes_text = pluralizeRussian(minutes, "минута", "минуты", "минут")
		seconds_text = pluralizeRussian(seconds, "секунда", "секунды", "секунд")
	else:
		#Default to English
		days_text = "day{}".format("s" if days!=1 else "")
		hours_text = "hour{}".format("s" if hours!=1 else "")
		minutes_text = "minute{}".format("s" if minutes!=1 else "")
		seconds_text = "second{}".format("s" if seconds!=1 else "")

	result = ", ".join(filter(lambda x: bool(x),[
	"{0} {1}".format(days, days_text) if days else "",
	"{0} {1}".format(hours, hours_text) if hours else "",
	"{0} {1}".format(minutes, minutes_text) if minutes else "",
	"{0} {1}".format(seconds, seconds_text) if seconds else ""
	]))
	return result