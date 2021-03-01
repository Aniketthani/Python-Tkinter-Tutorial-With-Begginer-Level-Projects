from tkinter import *
root=Tk()
root.title("List Box")
root.geometry("500x500")

#create frame and scrollbar
myframe=Frame(root)

myscrollbar=Scrollbar(myframe,orient=VERTICAL)


#create functions

def delete():
    listbox.delete(ANCHOR)
def select():
    label=Label(root,text=listbox.get(ANCHOR)).pack()
def delete_all():
    listbox.delete(0,END)

def select_all():
    result=""
    for i in listbox.curselection():
        result=result+listbox.get(i)+"\n"
    label=Label(root,text=result)
    label.pack(pady=5)

def multiple_delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

# selectmode parameter of listbox : (SINGLE(default),MULTIPLE,EXTENDED,BROWSE)
listbox=Listbox(myframe,yscrollcommand=myscrollbar.set,selectmode=MULTIPLE)

#configure myscrollbar

myscrollbar.config(command=listbox.yview)
myscrollbar.pack(fill=Y,side=RIGHT)
myframe.pack()

listbox.pack()

list = ['one', 'two', 'three', 'four', 'five', 'one', 'two',
        'three', 'four', 'five', 'one', 'two', 'three', 'four', 'five', 'one', 'two', 'three', 'four', 'five', 'one', 'two', 'three', 'four', 'five', 'one', 'two', 'three', 'four', 'five']
for i in list:
    listbox.insert(END,i)

delete_button=Button(root,text="delete",command=delete)
delete_button.pack(pady=10)

select_button=Button(root,text="select",command=select)
select_button.pack(pady=10)

delete_all_button=Button(root,text="delete all",command=delete_all)
delete_all_button.pack(pady=10)

select_all_button=Button(root,text="select all",command=select_all)
select_all_button.pack(pady=10)

multiple_delete_button=Button(root,text="multiple delete",command=multiple_delete)
multiple_delete_button.pack(pady=5)


root.mainloop()
