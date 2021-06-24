

import os
import sys

def open_cmd():
	os.system('start cmd')

def open_chrome():
	os.system('start chrome.exe')

def open_notepad():
	os.system('start notepad.exe')

def open_shutdown():
	os.system('cmd /k shutdown /s')

def open_restart():
	os.system('cmd /k shutdown /r')

def open_exit():
	sys.exit()

def open_word():
	os.system('start WINWORD.EXE')