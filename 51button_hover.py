from tkinter import *
root=Tk()
root.geometry("400x400")

def hover(event):
    button.config(bg="black",fg="green")
    label.config(text="You Hovered on the button")
    
def leave(event):
    button.config(bg="white",fg="red")
    label.config(text="")
button=Button(root,text="Hover Over Me to See The Change",font=("Arial",15),bg="white",fg="red")
button.pack(pady=40)
button.bind("<Enter>",hover)
button.bind("<Leave>",leave)

label=Label(root,text="",bd=5,relief=SUNKEN,anchor=E)
label.pack(fill=X,side=BOTTOM,ipady=5)


root.mainloop()
