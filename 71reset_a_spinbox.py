from tkinter import * 

def reset():
    var=IntVar(root)
    var.set(0)
    s.config(textvariable=var)

root=Tk()
root.geometry("400x400")

s=Spinbox(root,from_=0,to=100,font=("Helvetica",20))
s.pack(pady=20)

button=Button(root,text="reset",command=reset)
button.pack(pady=20)


root.mainloop()