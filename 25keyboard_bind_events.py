from tkinter import *
root=Tk()
root.title("Keyboard Event Binding")
root.geometry("500x500")

def clicker(event):
    label=Label(root,text="You clicked this button : "+ event.char ) #event.keysym
    label.pack()
button=Button(root,text="Click here")

button.bind("<Key>",clicker)
button.pack()
root.mainloop()