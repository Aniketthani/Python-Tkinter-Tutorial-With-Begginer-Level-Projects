from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Binding dropdown and combobox with events")
root.geometry("700x700")

def change_ddown(event):
    label=Label(root,text=var.get()).pack()

def combo_change(event):
    label=Label(root,text=combo.get()).pack()
options=["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
var=StringVar(root)
var.set(options[0])
dropdown=OptionMenu(root,var,*options,command=change_ddown)
dropdown.pack()

combo=ttk.Combobox(root,values=options)


combo.current(0)
combo.bind("<<ComboboxSelected>>", combo_change)
combo.pack()

root.mainloop()
