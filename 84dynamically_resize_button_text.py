from tkinter import *
root=Tk()

root.geometry("400x400")

def resize(e):
    size=int((e.height + e.width)/20)
    button.config(font=("Helvetica",size))

Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)

button=Button(root,text="Button 1")
button.grid(row=0,column=0,sticky="nsew")

root.bind("<Configure>",resize)


root.mainloop()