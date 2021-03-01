from tkinter import *
root=Tk()
root.title("dropdown menu")
root.geometry("500x500")

def show():
    label=Label(root,text=var.get()).pack()


var=StringVar()
options=["Jan","Feb","Mar","Apr","May"]
dropdown=OptionMenu(root,var,*options)
#dropdown=OptionMenu(root,var,"Jan","Feb","Mar","Apr","May")
var.set("Jan")
dropdown.pack()

submit=Button(root,text="submit",command=show).pack()

root.mainloop()