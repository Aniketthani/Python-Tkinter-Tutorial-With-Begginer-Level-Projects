from tkinter import *
root=Tk()
root.title("Move canvas objects")
root.geometry("500x500")

def left(event):
    x=-10
    y=0
    canvas.move(circle,x,y)

def right(event):
    x=10
    y=0
    canvas.move(circle,x,y)


def up(event):
    x = 0
    y = -10
    canvas.move(circle, x, y)


def down(event):
    x = 0
    y = 10
    canvas.move(circle, x, y)

def press(event):
    if event.char=="a":
        x=-10
        y=0
        canvas.move(circle,x,y)
    elif event.char == "d":
        x = 10
        y = 0
        canvas.move(circle, x, y)
    elif event.char == "w":
        x = 0
        y = -10
        canvas.move(circle, x, y)
    elif event.char == "s":
        x = 0
        y = 10
        canvas.move(circle, x, y)

canvas=Canvas(root,height=500,width=500,bg="red",bd=10)
canvas.pack()

circle=canvas.create_oval(100,100,150,150,fill="blue")

root.bind("<Left>",left)
root.bind("<Right>",right)
root.bind("<Up>",up)
root.bind("<Down>",down)

root.bind("<Key>",press)




root.mainloop()
