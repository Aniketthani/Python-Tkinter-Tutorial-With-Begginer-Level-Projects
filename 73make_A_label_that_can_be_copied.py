#generally labels cannot be copied and therefore we will use entry boxes with zero border and readonly mode for this 
#  as Text in Entry Boxes can be copied easily

from tkinter import *

root=Tk()
root.geometry("500x500")

label=Label(root,text="You can't copy me",font=("Arial",20))
label.pack(pady=20)

#Two ways of designing our Entry box for this purpose 

# first way:
'''
var=StringVar(root)
var.set("You Can Copy Me Easily")

entry = Entry(root,bd=0, font=("Arial", 20),textvariable=var,state="readonly",width=25)
entry.pack(pady=20)'''

#secoond way :

entry = Entry(root,bd=0, font=("Arial", 20),width=25)
entry.insert(0, "You Can Copy Me Easily")
entry.config(state="readonly")
entry.pack(pady=20)



root.mainloop()
