from tkinter import *
root=Tk()
root.title("drawing canvas ")
root.geometry("500x500")

canvas=Canvas(root,height=400,width=400,bg="yellow")
canvas.pack()

#create Rectangle
#canvas.create_rectangle(x1,y1,x2,y2,fill="color")
# x1,y1 :Top Left
# x2,y2 : Bottom Right
canvas.create_rectangle(50,100,350,300,fill="cyan")

#create oval
#canvas.create_oval(x1,y1,x2,y2,fill="color")
# x1,y1 :Top Left
# x2,y2 : Bottom Right
canvas.create_oval(50,100,350,300,fill="black")


#create line
#canvas.create_line(x1,y1,x2,y2,fill="color")
canvas.create_line(0,200,400,200,fill="red")
canvas.create_line(200,0,200,400,fill="red")



root.mainloop()