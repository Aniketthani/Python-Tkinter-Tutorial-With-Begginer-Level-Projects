from tkinter import *
root=Tk()
root.geometry("700x700")

count=0
size=20
def contract():
    global count,size

    if count>=0 and count<=11:
        count-=1
        size-=1
        button.config(font=("Helvetica",size))
        button.after(10,contract)

def expand():
    global count,size

    if count<=10:

        size+=1
        count+=1

        button.config(font=("Helvetica",size))
        button.after(10,expand)
    else :
        contract()

button=Button(root,text="click me",font=("Helvetica",20),command=expand)
button.pack(pady=20)

root.mainloop()