#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
from os import path
import sys

if getattr(sys, 'frozen', False):
	# frozen
	SCRIPT_FOLDER = path.dirname(sys.executable)
else:
	SCRIPT_FOLDER = path.dirname(path.realpath(__file__))

##############
# FILENAMES###
##############

#A filename of a file containing Telegram bot token.
BOT_TOKEN_FILENAME = 'tokens/token'

with open(path.join(SCRIPT_FOLDER, BOT_TOKEN_FILENAME),'r') as f:
	BOT_TOKEN = f.read().replace("\n","")

# Subscribers database
DATABASE_PATH = path.join(SCRIPT_FOLDER, "databases/main_DB.db")

#############
# TEXTS######
#############

START_MESSAGE = {"EN": "Welcome! Type /help to get help.",
"RU": "Добро пожаловать! Наберите /help для получения помощи."}
WORD_ADDED_MESSAGE = {"EN": "The word has been added!",
"RU": "Слово добавлено!"}
COURSE_ADDED_MESSAGE = {"EN": "The course has been created!",
"RU": "Курс создан!"}
COURSE_SET_MESSAGE = "The course is set to {0}"

UNKNOWN_COMMAND_MESSAGE = {"EN": "Unknown command!",
"RU":"Неизвестная команда"}

################
### BUTTONS#####
################

EN_LANG_BUTTON = "🇬🇧 EN"
RU_LANG_BUTTON = "🇷🇺 RU"

ABOUT_BUTTON = {"EN":"ℹ️ About", "RU": "ℹ️ О программе"}
OTHER_BOTS_BUTTON = {"EN":"👾 My other bots", "RU": "👾 Другие мои боты"}
HELP_BUTTON = {"EN":"⁉️" + "Help", "RU": "⁉️ Помощь"}

WORD_LIST_BUTTON = {"EN": "Word list", "RU": "Список слов"}

##################
# BIG TEXTS#######
##################

ABOUT_MESSAGE = """*Word Learner bot*
_Created by:_ Highstaker a.k.a. OmniSable.
Source: https://github.com/Highstaker/Language-learner-telegram-bot
Version: {0}
This bot uses the python-telegram-bot library.
https://github.com/leandrotoledo/python-telegram-bot
"""

OTHER_BOTS_MESSAGE = """*My other bots*:

@OmniCurrencyExchangeBot: a currency converter bot supporting past rates and graphs.

@multitran\_bot: a Russian-Whichever dictionary with support of 9 languages. Has transcriptions for English words.
"""

HELP_MESSAGE = """no help
"""