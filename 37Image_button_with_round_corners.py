from tkinter import*
from PIL import ImageTk,Image
root=Tk()
root.title("Create Image Button with round corner")
root.geometry("500x500")

global img
img = ImageTk.PhotoImage(Image.open("image/button.png"))
button=Button(root,image=img,borderwidth=0)
button.pack()



root.mainloop()
