from tkinter import *
root=Tk()

# function for button onclick

def click():
    label=Label(root,text="You clicked Me")
    label.pack()
#Creating a Button
mybutton=Button(root,text="Click Me" , pady="50", padx="100" , command=click,fg="blue", bg="orange")

# for disabling a button
disabled_button=Button(root,text="This is a Disabled Button",state="disabled")

#showing it on screen
mybutton.pack()
disabled_button.pack()

root.mainloop()