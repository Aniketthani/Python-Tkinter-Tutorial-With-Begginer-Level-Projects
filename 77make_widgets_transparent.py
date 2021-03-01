from tkinter import *  
root=Tk()
root.geometry("500x500")

root.wm_attributes("-transparentcolor","red") # here wm stands fro windows manager and transparentcolor attribute will make the things transparent that has the same color
    # we can also use root['bg'] as color to make the entire root window transparent
frame=Frame(root,height=200,width=200,bg="red")   
frame.pack(pady=20,ipadx=100,ipady=100)

label=Label(frame,text="Hey",font=("Arial",15),width=20,height=20,bd=7,bg="red",foreground="yellowgreen")
label.pack()

root.mainloop()