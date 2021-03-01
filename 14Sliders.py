from tkinter import *

root=Tk()
root.title("Slide bar in Tkinter")
root.geometry("600x600")

def setdim():
    h=vertical.get()
    w=horizontal.get()
    root.geometry(str(w)+"x"+str(h))

vertical =Scale(root,from_=0,to=600)
vertical.set(600)
vertical.pack()

horizontal=Scale(root,from_=0,to=600,orient=HORIZONTAL)
horizontal.set(600)
horizontal.pack()

button=Button(root,text="set dimensions",command=setdim).pack()

root.mainloop()