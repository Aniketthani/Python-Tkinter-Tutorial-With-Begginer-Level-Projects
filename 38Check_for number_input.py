from tkinter import *
root=Tk()
root.title("Checking input is a number or not")
root.geometry("500x500")

def check():
    try:
        float(input.get())
        answer = Label(root, text="Input is a number").pack()
    except ValueError:
        answer=Label(root,text="Input is not a number").pack()

input=Entry(root)
input.pack()

button=Button(root,text="submit",command=check)
button.pack()


root.mainloop()
