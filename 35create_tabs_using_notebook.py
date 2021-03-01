from tkinter import  *
from tkinter import ttk



def hide():
    my_notebook.hide(1)
    show_red.config(state=ACTIVE)
    delete_red.config(state=DISABLED)

def show():
    my_notebook.add(frame2,text="Red Tab")
    show_red.config(state=DISABLED)
    delete_red.config(state=ACTIVE)

def select():
    my_notebook.select(1)




root=Tk()
root.title("Create Tabs in GUI interface using Notebook widget")
root.geometry("500x500")


my_notebook=ttk.Notebook(root)
my_notebook.pack()

#creating frames
frame1=Frame(my_notebook,height=500,width=500,bg="blue")
frame2=Frame(my_notebook,height=500,width=500,bg="red")

frame1.pack(fill="both",expand=1)
frame2.pack(fill="both",expand=1)

#adding frame1 and frame 2 as tabs in notebook
my_notebook.add(frame1,text="BLue Tab")
my_notebook.add(frame2,text="Red Tab")

#creating buttons
delete_red=Button(frame1,text="delete red tab",command=hide)
delete_red.pack()

show_red=Button(frame1,text="show red tab",state=DISABLED,command=show)
show_red.pack(pady=10)

navigate_to_red=Button(frame1,text="navigate to red",command=select)
navigate_to_red.pack(pady=10)




root.mainloop()