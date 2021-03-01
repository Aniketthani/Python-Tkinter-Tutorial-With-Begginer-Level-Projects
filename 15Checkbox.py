from tkinter import *
root=Tk()
root.title("Checkbox")
root.geometry("500x500")

def show():
    label=Label(root,text=var.get()).pack()



var=StringVar()
cbox=Checkbutton(root,text="This is Check Box",variable=var,onvalue="on",offvalue="off")
cbox.deselect() #to deselect the cbox at initialization. 
cbox.pack()

submit=Button(root,text="submit",command=show).pack()


root.mainloop()