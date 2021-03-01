from tkinter import *
from tkinter.tix import *  #this widget is depreciated

root=Tk()
root.geometry("500x500")

#create tooltip
tip=Balloon(root)

'''
#Additonal formatting
tip.config(bg="red",bd=20)

#sub categories
tip.label.config(bg="blue",bd=20)  # configuration for arrow
tip.message.config(bg="orange",fg="white") # configuration for message'''


#create button
buttn=Button(root,text="Hover On Me")
buttn.pack(pady=20)

#bind tooltip to buttn
tip.bind_widget(buttn,balloonmsg="This is a balloon msg binded with this button")


root.mainloop()