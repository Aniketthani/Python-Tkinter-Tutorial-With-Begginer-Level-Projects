from tkinter import *
from PIL import ImageTk,Image


def left(event):
    x = -10
    y = 0
    canvas.move(mario, x, y)


def right(event):
    x = 10
    y = 0
    canvas.move(mario, x, y)


def up(event):
    x = 0
    y = -10
    canvas.move(mario, x, y)


def down(event):
    x = 0
    y = 10
    canvas.move(mario, x, y)


def press(event):
    if event.char == "a":
        x = -10
        y = 0
        canvas.move(mario, x, y)
    elif event.char == "d":
        x = 10
        y = 0
        canvas.move(mario, x, y)
    elif event.char == "w":
        x = 0
        y = -10
        canvas.move(mario, x, y)
    elif event.char == "s":
        x = 0
        y = 10
        canvas.move(mario, x, y)

root=Tk()
root.title("Adding Image on Canvas")
root.geometry("2500x2500")

img=ImageTk.PhotoImage(Image.open("image/mario.png"))

canvas=Canvas(root,height=2500,width=2500,bg="yellow")
canvas.pack()

mario=canvas.create_image(260,125,anchor=NW,image=img)


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.bind("<Key>", press)

root.mainloop()
