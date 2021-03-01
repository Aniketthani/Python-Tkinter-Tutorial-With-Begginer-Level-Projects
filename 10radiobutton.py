from tkinter import *

root=Tk()

Modes=[
    ('Laptop',1,50000),
    ('Desktop',2,30000),
    ('Keyboard',3,1000),
    ('Mouse',4,500),
    ('Webcam',5,5000)
]

def action(value):
    output="Selected Device is "+str(Modes[value-1][0]) + " and it's Price is "+ str(Modes[value-1][2])
    label=Label(root,text=output).pack()
radio=IntVar(root)
radio.set(50000)
for text,value,price in Modes:
    Radiobutton(root,text=text,value=value,variable=radio).pack()

submit=Button(root,text="submit",padx=5,pady=5,command=lambda : action(radio.get())).pack()
label=Label(root,text="")
root.mainloop()