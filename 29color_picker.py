from tkinter import *
from tkinter import colorchooser

root=Tk()
root.title("Color Picker")
root.geometry("500x500")

def color():
    mycolor=colorchooser.askcolor()[1]
    my_label=Label(root,text="You choose this color",font=("Helvetica",30),bg=mycolor).pack()

my_button=Button(root,text="Pick a Color",command=color).pack()
root.mainloop()