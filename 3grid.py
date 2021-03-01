from tkinter import *
root=Tk()

#Creating a Label Widget
mylabel1=Label(root,text="Hello World")
mylabel2=Label(root,text="Hi This is Tkinter")

#showing it on screen
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=3,column=3)

root.mainloop()