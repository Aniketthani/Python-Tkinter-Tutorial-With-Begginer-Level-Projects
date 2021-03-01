from tkinter import  *


def new():
    pass
def open_():
    pass
def disable_new():
    file_menu.entryconfig("New",state=DISABLED)
def enable_new():
    file_menu.entryconfig("New",state=NORMAL)

def delete_new():
    file_menu.delete("New")

root=Tk()
root.geometry("500x500")

my_menu=Menu(root)
root.config(menu=my_menu)
root.iconbitmap("image/logo.ico")

file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new)
file_menu.add_command(label="Open",command=open_)


disable=Button(root,text="disble new",command=disable_new)
disable.pack(pady=10)

enable=Button(root,text="enable new",command=enable_new)
enable.pack(pady=10)

delete=Button(root,text="delete new",command=delete_new)
delete.pack(pady=10)
root.mainloop()
