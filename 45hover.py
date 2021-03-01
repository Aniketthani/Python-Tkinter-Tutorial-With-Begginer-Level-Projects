from tkinter import *
from PIL import ImageTk,Image



def hover(event):
    img_label.config(image=img2)
    
def leave(event):
    img_label.config(image=img1)

root=Tk()
root.title("changing image on hover event")
root.geometry("2000x2000")

img1=ImageTk.PhotoImage(Image.open("image/img4.jpeg"))
img2=ImageTk.PhotoImage(Image.open("image/img3.jpeg"))

img_label=Label(root,image=img1)
img_label.pack(pady=10)

img_label.bind("<Enter>",hover)
img_label.bind("<Leave>",leave)

root.mainloop()