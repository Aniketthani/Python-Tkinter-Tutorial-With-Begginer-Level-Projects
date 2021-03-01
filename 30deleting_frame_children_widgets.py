from tkinter import *
root=Tk()
root.title("creating menu")
root.geometry("500x500")

def new():
    hide_all_frames()
    file_new_frame.pack(fill="both",expand=1)
    label=Label(file_new_frame,text="You selected new option from file menu").pack()
def cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both",expand=1)
    label=Label(edit_cut_frame,text="You selected cut option from edit menu").pack()
    
def copy():
    pass
def find():
    pass
def find_next():
    pass
def hide_all_frames():
    for widget in file_new_frame.winfo_children():
        widget.destroy()
    for widget in edit_cut_frame.winfo_children():
        widget.destroy()    

    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


my_menu=Menu(root)
root.config(menu=my_menu)

#create a menu item : file
file_menu=Menu(my_menu)

my_menu.add_cascade(menu=file_menu,label="File")
file_menu.add_command(label="New",command=new)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# create a edit menu item
edit_menu=Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)

# create a find menu item
find_menu = Menu(my_menu)
my_menu.add_cascade(label="Find", menu=find_menu)
find_menu.add_command(label="Find", command=find)
find_menu.add_command(label="Find Next", command=find_next)


#file new frame
file_new_frame=Frame(root,width=500,height=500,bg="red")
edit_cut_frame=Frame(root,width=500,height=500,bg="blue")
root.mainloop()
