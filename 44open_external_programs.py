from tkinter import *
from tkinter import filedialog
import os

def open_file():
    file=filedialog.askopenfilename()
    os.system('"%s"' % file)

def open_notepad():
    os.system('"%s"' % "C:/Windows/System32/notepad.exe")
root=Tk()
root.title("open external files and programs")
root.geometry("500x500")


open_button=Button(root,text="open file",command=open_file)
open_button.pack()

open_notepad_button=Button(root,text="Open Notepad",command=open_notepad)
open_notepad_button.pack()

root.mainloop()
