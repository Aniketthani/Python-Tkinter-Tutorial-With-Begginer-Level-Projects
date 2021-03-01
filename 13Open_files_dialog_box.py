from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()

def openfile():
    root.filename=filedialog.askopenfilename(initialdir="image",title="select image file",filetypes=(("png file","*.png"),("jpeg file","*.jpeg"),("all files","*.*")))
    label=Label(root,text=root.filename).pack()
    global img
    img=ImageTk.PhotoImage(Image.open(root.filename))
    img_label=Label(root,image=img).pack()

btn=Button(root,text="Open File",command=openfile).pack()




root.mainloop()