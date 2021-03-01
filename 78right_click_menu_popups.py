from tkinter import *
root=Tk()
root.geometry("500x500")

def hello():
    pass
def how():
    pass
def popup(e):
    my_menu.tk_popup(e.x_root,e.y_root)
#create menu
my_menu=Menu(root,tearoff=False)
my_menu.add_command(label="Hello World",command=hello)
my_menu.add_command(label="How Are You",command=how)
my_menu.add_separator()
my_menu.add_command(label="Exit",command=root.quit)


root.bind("<Button-3>",popup)


root.mainloop()