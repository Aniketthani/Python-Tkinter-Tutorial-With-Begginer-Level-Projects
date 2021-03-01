from tkinter import *
root=Tk()

#input box

#e=Entry(root,width="100",fg="blue",bg="orange", borderwidth="10")
#e.pack()

# to get data from input field
# e.get()

# to insert some text in input field or box

# e.insert()

# function for button onclick

def click():
    label=Label(root,text="Hello " + e.get())
    label.pack()

# input box 

e=Entry(root,width="50",borderwidth="8")
e.insert(0,"Enter your name : ")
e.pack()

#Creating a Button
mybutton=Button(root,text="submit" , pady="50", padx="100" , command=click,fg="brown", bg="cyan")



mybutton.pack()

root.mainloop()