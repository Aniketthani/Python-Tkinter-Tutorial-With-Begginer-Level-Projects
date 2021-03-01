from tkinter import *
root=Tk()
root.title("List Box")
root.geometry("500x500")

def delete():
    listbox.delete(ANCHOR)
def select():
    label=Label(root,text=listbox.get(ANCHOR)).pack()
def delete_all():
    listbox.delete(0,END)
listbox=Listbox(root)
listbox.pack()

list=['one','two','three','four','five']
for i in list:
    listbox.insert(END,i)

delete_button=Button(root,text="delete",command=delete)
delete_button.pack(pady=10)

select_button=Button(root,text="select",command=select)
select_button.pack(pady=10)

delete_all_button=Button(root,text="delete all",command=delete_all)
delete_all_button.pack(pady=10)



root.mainloop()