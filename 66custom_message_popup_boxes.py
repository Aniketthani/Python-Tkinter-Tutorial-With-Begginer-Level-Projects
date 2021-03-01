from tkinter import * 
from PIL import ImageTk,Image

def clicked():
    global pop
    pop=Toplevel()
    pop.geometry("250x200")
    pop.title("Custom Pop Up Box")

    pop.config(bg="#780000")

    global img
    img = ImageTk.PhotoImage(Image.open("image/mario.png").resize((50,80)))
    img_label=Label(pop,image=img,borderwidth=0)
    img_label.grid(row=0,column=0,pady=10)

    message_label=Label(pop,text="You Liked this message ??",background="#780000",foreground="#11BC00",font=("Helvetica",10))
    message_label.grid(row=0,column=1,columnspan=2,padx=10)

    button_y=Button(pop,text="Yes",background="green",foreground="black",font=("Helvetica",10),command=lambda : choice(button_y))
    button_n=Button(pop,text="No",background="red",foreground="black",font=("Helvetica",10),command=lambda : choice(button_n))

    button_y.grid(row=1,column=1,pady=5)
    button_n.grid(row=1, column=2, pady=5)

def choice(b):
    label.config(text=b['text'])
    pop.destroy()



root=Tk()
root.geometry("500x500")

button=Button(root,text="Click Here",command=clicked)
button.pack(pady=20)

label=Label(root,text="")
label.pack(pady=20)


root.mainloop()
