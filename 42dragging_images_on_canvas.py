from tkinter import *
from PIL import ImageTk,Image


def drag(event):
    global img
    img = ImageTk.PhotoImage(Image.open("image/mario.png"))
    mario = canvas.create_image(event.x, event.y, image=img)



root=Tk()
root.title("Adding Image on Canvas")
root.geometry("2500x2500")

img=ImageTk.PhotoImage(Image.open("image/mario.png"))

canvas=Canvas(root,height=2500,width=2500,bg="yellow")
canvas.pack()

mario=canvas.create_image(260,125,anchor=NW,image=img)


'''root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.bind("<Key>", press)'''

root.bind("<B1-Motion>",drag)

root.mainloop()
