from tkinter import *
from tkinter import messagebox

global clicked
global count
clicked=True   # True for X and False for O
count=0

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkifwon():
    global winner
    winner=False

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        messagebox.showinfo("Game Won","Congrations !! X is the Winner")
        winner=True
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Game Won", "Congrations !! X is the Winner")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! X is the Winner")
        disable_all_buttons()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Game Won", "Congrations !! X is the Winner")
        disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! X is the Winner")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Game Won", "Congrations !! X is the Winner")
        disable_all_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! X is the Winner")
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! X is the Winner")
        disable_all_buttons()




    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Game Won", "Congrations !! O is the Winner")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Game Won", "Congrations !! O is the Winner")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! O is the Winner")
        disable_all_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! O is the Winner")
        disable_all_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! O is the Winner")
        disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! O is the Winner")
        disable_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! O is the Winner")
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Won", "Congrations !! O is the Winner")
        disable_all_buttons()

    if count==9 and winner==False:
        messagebox.showinfo("Game Tied","It's a Tie , No one wins")
        disable_all_buttons()

def b_click(b):
    global clicked
    global count
    if b["text"]==" " and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        checkifwon()
    elif b["text"]==" " and clicked==False:
        b["text"]="O"
        clicked=True
        count += 1
        checkifwon()
    else : 
        messagebox.showerror("Wrong Option Selected","!!You have Selected a previously occupied Box")


def reset():
    b1.config(text=" ",state=NORMAL,bg="SystemButtonFace")
    b2.config(text=" ",state=NORMAL,bg="SystemButtonFace")
    b3.config(text=" ",state=NORMAL,bg="SystemButtonFace")
    b4.config(text=" ",state=NORMAL,bg="SystemButtonFace")
    b5.config(text=" ",state=NORMAL,bg="SystemButtonFace")
    b6.config(text=" ",state=NORMAL,bg="SystemButtonFace")
    b7.config(text=" ",state=NORMAL,bg="SystemButtonFace")
    b8.config(text=" ",state=NORMAL,bg="SystemButtonFace")
    b9.config(text=" ",state=NORMAL,bg="SystemButtonFace")

    global clicked
    global count
    clicked=True
    count=0



root=Tk()
root.title("Tic Tac Toe By : Aniket Thani")


#build our buttons
b1=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda :b_click(b1))
b2=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda :b_click(b2))
b3=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda :b_click(b3))
b4=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda :b_click(b4))
b5=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda :b_click(b5))
b6=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda :b_click(b6))
b7=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda :b_click(b7))
b8=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda :b_click(b8))
b9=Button(root, text=" ", font=("Helvetica", 20), height=3,width=6, bg="SystemButtonFace", command=lambda: b_click(b9))


b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

# create menu
my_menu=Menu(root)
root.config(menu=my_menu)

#create options menu
options_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Reset",command=reset)


root.mainloop()
