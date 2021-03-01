from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Tkinter By Aniket Thani")
#root.iconbitmap("heart.ico") for adding icon

#adding image as a label
my_img=ImageTk.PhotoImage(Image.open("image/parrot.jpeg"))
my_label=Label(image=my_img)
my_label.pack()








button_quit=Button(root,text="Exit",command=root.quit)
button_quit.pack()

root.mainloop()