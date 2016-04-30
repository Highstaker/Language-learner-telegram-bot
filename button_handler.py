#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

from textual_data import *

def getMainMenu():
	"""
	Returns a representation of custom keyboard to be passed to message-sending functions
	:param subscribed: is the user subscribed?
	Affects which button shall be displayed, subscribe or unsubscribe
	:return: list of lists
	"""

	MAIN_MENU_KEY_MARKUP = [
	[REFRESH_BUTTON],
	[WORD_LIST_BUTTON,COURSES_LIST_BUTTON],
	[HELP_BUTTON, ABOUT_BUTTON, OTHER_BOTS_BUTTON],
	[EN_LANG_BUTTON, RU_LANG_BUTTON]
	]

	return MAIN_MENU_KEY_MARKUP