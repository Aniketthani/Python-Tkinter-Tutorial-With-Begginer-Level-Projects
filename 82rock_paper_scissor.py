from tkinter import *  
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
from random import choice

def play():
    user_label.config(text="Select Your Next Choice")
    computer_choice.config(text="Computer's Choice Was ")
    computer_player()
    global response
    input=var.get().lower()
    if obj_choosen==rock and input=="rock":
        response="It's a Tie"
    elif obj_choosen==rock and input=="paper":
        response="Congratulations You Won"
    elif obj_choosen == rock and input == "scissor":
        response = "Oops ! ! You lost"
    
    elif obj_choosen == paper and input == "rock":
        response = "Oops ! ! You lost"
    elif obj_choosen == paper and input == "paper":
        response = "It's a Tie"
    elif obj_choosen == paper and input == "scissor":
        response =  "Congratulations You Won"
    
    elif obj_choosen == scissor and input == "rock":
        response = "Congratulations You Won"
    elif obj_choosen == scissor and input == "paper":
        response = "Oops ! ! You lost"
    elif obj_choosen == scissor and input == "scissor":
        response = "It's a Tie"
    
    response_label.config(text=response, bg="#00FF33")
    
        

def computer_player():
    global obj_choosen
    obj_choosen=choice(obj)
    image_label.config(image=obj_choosen)
    
    

root=Tk()
root.title("Rock Paper Scissor By Aniket Thani")
root.geometry("500x650+450+100")
root.config(bg="#C00000")


#images
rock=ImageTk.PhotoImage(Image.open("image/rock.jpg").resize((250,250)))
paper=ImageTk.PhotoImage(Image.open("image/paper.jpg").resize((250,250)))
scissor=ImageTk.PhotoImage(Image.open("image/scissor.jpg").resize((250, 250)))

#list of objects
obj=[rock,paper,scissor]

#computer label
computer_choice = Label(root, text="", bg="#C00000",font=("Helvetica",20),fg="yellow")
computer_choice.pack(pady=10)

image_label = Label(root, bg="#C00000")
image_label.pack(pady=10)

user_label=Label(root,text="Select Your Choice ",bg="#C00000",font=("Helvetica",20),fg="white")
user_label.pack(pady=10)

var=StringVar()
dropdown=Combobox(root,values=('Rock','Paper','Scissor'),textvariable=var,font=("Helvetica",20))
dropdown.current(0)
dropdown.pack(pady=50)

play_button=Button(root,text="Play",command=play,font=("Arial",15))
play_button.pack()

response_label=Label(root,text="",font=("Helvetica",20),bg="#C00000",fg="#330099")
response_label.pack(pady=10)



root.mainloop()
