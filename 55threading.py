from tkinter import *
import threading
from random import randint
import time

def wait_five_seconds():
    time.sleep(5)
    label.config(text="5 Seconds Up")

def random_no_generator():
    label1.config(text=f'Random no : {randint(0,100)}')



root=Tk()
root.title("Threading in Tkinter")
root.geometry("500x500")

label=Label(root,text="")
label.pack()

button=Button(root,text="wait 5 second",command=threading.Thread(target=wait_five_seconds).start())
button.pack(pady=20)

button1=Button(root,text="Generate a random number",command=random_no_generator)
button1.pack()

label1=Label(root,text="")
label1.pack()

root.mainloop()