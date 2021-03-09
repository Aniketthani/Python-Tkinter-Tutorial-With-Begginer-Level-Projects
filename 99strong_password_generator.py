from tkinter import *
from random import randint

root=Tk()
root.title("Strong Password Generator App")
root.geometry("600x400")
root.minsize(600,400)
root.maxsize(600,400)


def new_random_char():
    passwd_box.config(state=NORMAL)
    passwd_box.delete(0,END)

    
    try:
        length_of_pass=int(no_of_chars.get())
    except:
        return
    passwd=""

    for i in range(length_of_pass):
        passwd+=str(chr(randint(33,126)))  
    
    passwd_box.insert(0,passwd)
    passwd_box.config(state="readonly")
    no_of_chars.delete(0,END)

def copy_to_clipbd():
    #clear the clipboard
    root.clipboard_clear()
    #copy to clipboard
    root.clipboard_append(passwd_box.get())



#Label Frame
lf=LabelFrame(root,text="How Many Characters?")
lf.pack(pady=20)

#Entry Box for getting no of characters
no_of_chars=Entry(lf,font=("Helvetica",25))
no_of_chars.pack(pady=20)

#create Entry box to display password
passwd_box=Entry(lf,font=("Helvetica",35),text="",bd=0,bg=root.cget('bg'))
passwd_box.pack(pady=20)

#create a frame for buttons
btnframe=Frame(root)
btnframe.pack(pady=20)

#generate passwd button
generate_pass_btn=Button(btnframe,text="Generate Strong Password",command=new_random_char,bg="#0000FF",fg="white",font=("Arial",15,"bold"))

generate_pass_btn.grid(row=0,column=0,padx=10)


copy_btn=Button(btnframe,text="Copy To Clipboard",command=copy_to_clipbd,bg="#0000FF",fg="white",font=("Arial",15,"bold"))
copy_btn.grid(row=0,column=1,padx=10)



root.mainloop()