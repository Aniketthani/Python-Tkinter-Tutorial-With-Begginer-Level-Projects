from tkinter import *
from tkinter import ttk
from typing import ValuesView

global count_iid
count_iid=4 # no. of entries already present from 0 to 4

def add_record():

    #create striped row tags
    my_tree.tag_configure("oddrow", background="yellow")
    my_tree.tag_configure("evenrow", background="cyan")
    if str(name_entry.get()) and str(id_entry.get()) and str(city_entry.get()):
         global count_iid
         name=name_entry.get()
         id=id_entry.get()
         city=city_entry.get()
         if count_iid%2==0:
            my_tree.insert(parent='',index='end',iid=count_iid+1,text="Parent",values=(name,id,city),tags=('evenrow',))
         else:
            my_tree.insert(parent='',index='end',iid=count_iid+1,text="Parent",values=(name,id,city),tags=('oddrow',))
         my_tree.pack(pady=10)

         # empty the input or entry boxes
         name_entry.delete(0,END)
         id_entry.delete(0,END)
         city_entry.delete(0,END)
         
         count_iid+=1

def remove_record():
    global count_iid
    selected_indices=my_tree.selection()
    for index in selected_indices:
        my_tree.delete(index)
    my_tree.pack(pady=10)

def remove_all_records():
    my_tree.delete(*my_tree.get_children())
    count_iid=0
    my_tree.pack(pady=10)


def select_record():
    global index
    name_entry.delete(0,END)
    id_entry.delete(0,END)
    city_entry.delete(0,END)
    index=my_tree.focus()
    values=my_tree.item(index,"values")
    name_entry.insert(0,values[0])
    id_entry.insert(0, values[1])
    city_entry.insert(0, values[2])

def update_record():
    global index
    my_tree.item(index,values=(name_entry.get(),id_entry.get(),city_entry.get()))


def move_up():
    records=my_tree.selection()
    for row in records:
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)-1)
def move_down():
    records = my_tree.selection()
    for row in reversed(records):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)
root=Tk()
root.title("Treeview")
root.geometry("500x500")

#add some style

style=ttk.Style(root)

#pick a theme
style.theme_use("clam") # other options are alt,default
#configure Treeview colors
style.configure("Treeview",background="silver",foreground="black",rowheight=25,fieldbackground="silver")

#change selection color
style.map("Treeview",background=[('selected','green')])



#create frame
main_frame=Frame(root)
main_frame.pack()


#scrollbar
scrollbar=Scrollbar(main_frame)
scrollbar.pack(fill=Y,side=RIGHT)
#create tree
my_tree=ttk.Treeview(main_frame)
my_tree.config(yscrollcommand=scrollbar.set)

#config scrollbar
scrollbar.config(command=my_tree.yview)



#define tree columns
my_tree["columns"]=("Name","ID","City")

# format tree columns
my_tree.column("#0",width=120,minwidth=25)  #  (#0) is the phantom column added by treeview itself
my_tree.column("Name",width=120,anchor=W)
my_tree.column("ID",width=120,anchor=CENTER)
my_tree.column("City",width=120,anchor=W)

# to get rid of the phantom column 

#my_tree.column("#0",width=0,stretch=NO)

# and also remove any heading text of this column if any given


#create Headings

my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Name",text="Name",anchor=W)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("City", text="City", anchor=W)

#create striped row tags
my_tree.tag_configure("oddrow",background="yellow")
my_tree.tag_configure("evenrow",background="cyan")



#add data
# my_tree.insert(parent='', index='end', iid=0, text="Label", values=("Hello", "Second Col", "Third Col"))
#Here, we insert the node to parent. If you want the parent widget as the master(root) node, we can set this to the empty string(”). Otherwise, we must mention the iid of an existing parent node.
#index is the position at which you want to add data
#text is the text you want to display in the phantom's column 
#idd is the id of the record 
# values are the values to be inserted in the record

my_tree.insert(parent='',index='end',iid=0,text="Parent",values=("Aniket","1","Ujjain"),tags=("oddrow",))
my_tree.insert(parent='',index='end',iid=1,text="Parent",values=("Jaya","2","Ujjain"),tags=("evenrow",))
my_tree.insert(parent='',index='end',iid=2,text="Parent",values=("Manisha","3","Ujjain"),tags=("oddrow",))
my_tree.insert(parent='',index='end',iid=3,text="Parent",values=("Kamal","4","Ujjain"),tags=("evenrow",))
my_tree.insert(parent='',index='end',iid=4,text="Parent",values=("Thani","5","Ujjain"),tags=("oddrow",))

#add a child

# two ways to add child

# one way

#my_tree.insert(parent='',index='end',iid=5,text="Child",values=("Software Developer","6","Indore"))
#my_tree.move(item=5,parent=0,index="end")

#  two way

#my_tree.insert(parent='0',index='end',iid=5,text="Child",values=("Software Developer","6","Indore"))



my_tree.pack(pady=20)

insert_frame=Frame(root)
insert_frame.pack(pady=10)

name_label=Label(insert_frame,text="Name")
name_label.grid(row=0,column=0)

id_label = Label(insert_frame, text="ID")
id_label.grid(row=0, column=1)

city_label = Label(insert_frame, text="City")
city_label.grid(row=0, column=2)

name_entry=Entry(insert_frame)
name_entry.grid(row=1,column=0)

id_entry=Entry(insert_frame)
id_entry.grid(row=1,column=1,padx=5)

city_entry=Entry(insert_frame)
city_entry.grid(row=1, column=2, padx=5)

add_button=Button(insert_frame,text="Add record",command=add_record)
add_button.grid(row=2,column=0,pady=10)

remove_button=Button(insert_frame,text="Remove Selected records",command=remove_record)
remove_button.grid(row=2,column=1,padx=10)

remove_all_button=Button(insert_frame,text="Remove ALL Records",command=remove_all_records)
remove_all_button.grid(row=2,column=2,padx=10)

select_button=Button(insert_frame,text="Select Record",command=select_record)
select_button.grid(row=3,column=0)

update_button=Button(insert_frame,text="Update Record",command=update_record)
update_button.grid(row=3,column=2)

move_up_button=Button(insert_frame,text="Move Up",command=move_up)
move_up_button.grid(row=3,column=1)

move_down_button=Button(insert_frame,text="Move Down",command=move_down)
move_down_button.grid(row=4,column=1,pady=5)


root.mainloop()
