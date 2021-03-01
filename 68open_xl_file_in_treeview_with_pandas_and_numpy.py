from tkinter import *
from tkinter import ttk,filedialog
import pandas as pd
import numpy as np


def open_file():
    filename=filedialog.askopenfilename(title="Choose xlsx  file",filetypes=(("xlsx files","*.xlsx"),))
    
    if filename:
        
        print(filename)
       
        df=pd.read_excel(filename)
        

        clear_tree()

        #set up new treeview
        my_tree["column"]=df.columns
        my_tree["show"]="headings"

        #loop through the column list through headers

        for column in my_tree["column"]:
            my_tree.heading(column,text=column)
        #put data in treeview

        df_rows=df.to_numpy().tolist()
        for row in df_rows:
            my_tree.insert("","end",values=row)
            
        my_tree.pack()

def clear_tree():
    my_tree.delete(*my_tree.get_children())
root=Tk()
root.geometry("700x650")

#create a frame
my_frame=Frame(root)
my_frame.pack()

#create treeview

my_tree=ttk.Treeview(my_frame)
my_tree.pack()


#create menu
my_menu=Menu(root)
root.config(menu=my_menu)

#create file menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="Open",command=open_file)



root.mainloop()
