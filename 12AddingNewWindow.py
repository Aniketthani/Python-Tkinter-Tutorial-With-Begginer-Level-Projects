from tkinter import * 
from PIL import ImageTk,Image

root=Tk()
root.title("This is First window")

def newwindow():
    global img
    nw=Toplevel()
    nw.title("This is Second Window")
    img=ImageTk.PhotoImage(Image.open("image/img4.jpeg"))
    label=Label(nw,image=img).pack()
    exitbutton=Button(nw,text="Close Window",command=nw.destroy).pack()

    
button=Button(root,text="Generate New Window",command=newwindow).pack()




root.mainloop()