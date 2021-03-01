from tkinter import  * 
from tkinter import messagebox
root=Tk()

 # types of messageboxes available are : 
 # showinfo,showwarning,showerror,askquestion,askyesno,askokcancel
def popup():
    p=messagebox.askyesno("This is my Popup","Hello World !!")
    if p==1:
        label=Label(root,text="Yes").pack()
    else:
        label=Label(root,text="No").pack()

button=Button(root,text="Popup",padx=10,pady=10,bd=2,bg="red",fg="blue",command=popup).pack()


root.mainloop()