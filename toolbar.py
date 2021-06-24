

import tkinter
import sys
import os
import ctypes
from programs import *

def main_window():
	window = tkinter.Tk()
	window.wm_attributes("-topmost", 1)
	window.title("ToolBar")
	window.geometry("300x200")
	window.configure(bg='black')
	cmd = tkinter.Button(window,text = "Open CMD", command = open_cmd).place(x=20,y=20)
	chrome = tkinter.Button(window,text = "Open Chrome", command = open_chrome).place(x=20,y=50)
	notepad = tkinter.Button(window,text = "Open Notepad", command = open_notepad).place(x=20,y=80)
	word = tkinter.Button(window,text = "Open Word", command = open_word).place(x=20,y=110)
	shutdown = tkinter.Button(window,text = "Shutdown", command = open_shutdown).place(x=200, y=20)
	restart = tkinter.Button(window, text = "Restart", command = open_restart).place(x=200, y=50)
	exit = tkinter.Button(window,text = "Exit", command = open_exit).place(x=200,y=80)
	ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
	window.mainloop()

main_window()