from tkinter import *

root=Tk()
root.title("Resize buttons dynamically when resizing window")
root.geometry("500x500")

#for the buttons to be resized upon resizing the windows

#for rows
Grid.rowconfigure(root,0,weight=1)  # more the weight more the size of button
Grid.rowconfigure(root,1,weight=1)

#for cols
Grid.columnconfigure(root,0,weight=1)

b1=Button(root,text="button 1")

b2=Button(root,text="button 2")

b1.grid(row=0,column=0,sticky="nsew")
b2.grid(row=1,column=0,sticky="nsew")

root.mainloop()