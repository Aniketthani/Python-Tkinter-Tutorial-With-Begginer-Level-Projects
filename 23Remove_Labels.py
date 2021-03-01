from tkinter import *
root=Tk()
root.title("Removing existing labels")
root.geometry("400x400")

def output():
    global mylabel
    mylabel=Label(root,text=text.get())
    mylabel.pack()
    submit['state']=DISABLED

def delete():
   mylabel.pack_forget() 
   submit['state']=NORMAL

   # one more way is there
   ''' mylabel.destroy()'''
   # for grid system
   ''' mylabel.grid_forget() '''


text=Entry(root,width=30,font=("Helvetica",20))
text.pack()

submit=Button(root,text="submit",command=output)
submit.pack()

delete_text=Button(root,text="Delete Text",command=delete).pack()


root.mainloop()

