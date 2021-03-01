from tkinter import *
import pickle
root=Tk()
root.geometry("500x700")

def save():
    stuff=textbox.get(1.0,END)
    filename="dat_file"
    file=open(filename,"wb")
    pickle.dump(stuff,file)
    file.close()

def open_file():
    filename="dat_file"
    file=open(filename,"rb")
    stuff=pickle.load(file)
    textbox.insert(1.0,stuff)
    
textbox=Text(root,width=50,height=35)
textbox.pack(pady=20)

save_button=Button(root,text="save",command=save)
save_button.pack()

open_button=Button(root,text="open",command=open_file)
open_button.pack(pady=10)

root.mainloop()