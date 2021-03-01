from tkinter import *
root=Tk()
root.title("Spniboxes in tkinter")
root.geometry("500x500")


def spin_values():
    label.config(text=str(sbox1.get())  + " " + str(sbox2.get())) 


sbox1=Spinbox(root,from_=0,to=10,increment=0.5,font=("Helvetica",20))
sbox1.pack(pady=20)

names=("aniket",'thani','abcd','efgh','ijkl')

sbox2=Spinbox(root,values=names,font=("Helvetica",20))
sbox2.pack(pady=20)

button=Button(root,text="get values",command=spin_values)
button.pack(pady=20)

label=Label(root,text="")
label.pack()

root.mainloop()