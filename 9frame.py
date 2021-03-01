from tkinter import *
root=Tk()
frame=LabelFrame(root,text="This is my Frame",padx=10,pady=10)

frame.pack(padx=50,pady=50)

button=Button(frame,text="Button inside frame")
button.pack()
# we can also use grid with this
#button.grid(row=1,column=2)
root.mainloop()