from tkinter import *
from tkinter import ttk

def pick_color(e):
    size=dropdown.get()
    if size=="large":
        color_dropdown['values']=large_size_colors
    elif size=="medium":
        color_dropdown['values']=medium_size_colors
    else:
        color_dropdown['values']=small_size_colors
root=Tk()
root.geometry("500x800")

size=["large","medium","small"]
large_size_colors=["Red","Blue","Green","White"]
medium_size_colors = ["Red", "Blue","Black","Maroon","orange"]
small_size_colors=["White","Black","Blue"]

dropdown=ttk.Combobox(root,width=30,values=("large","medium","small"))
dropdown.current(0)
dropdown.pack(pady=20)

color_dropdown=ttk.Combobox(root,width=30,values=large_size_colors)
color_dropdown.current(0)
color_dropdown.pack(pady=20)

#bind dropdown
dropdown.bind("<<ComboboxSelected>>",pick_color)

#frame
frame=Frame(root)
frame.pack(pady=20)
#listbox
list1=Listbox(frame)
list1.grid(row=0, column=0)


def list_color(e):
    list2.delete(0,END)
    size=list1.get(ANCHOR)
    if size == "large":
        for i in large_size_colors:
            list2.insert(END,i)
    elif size == "medium":
       for i in medium_size_colors:
           list2.insert(END, i)
    else:
       for i in small_size_colors:
           list2.insert(END, i)



for i in size:
    list1.insert(0,i)
list2=Listbox(frame)
list2.grid(row=0, column=1,padx=10)

#bind list1
list1.bind("<<ListboxSelect>>",list_color)

root.mainloop()
