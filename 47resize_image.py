from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Resize Image")
root.geometry("1000x1000")

img=ImageTk.PhotoImage(Image.open("image/img4.jpeg").resize((300,300),Image.ANTIALIAS))


label=Label(root,image=img).pack()



root.mainloop()
