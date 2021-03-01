# there are 9 bitmaps provided by tkinter
from tkinter import *
root=Tk()
root.geometry("500x800")

list=["error","gray75","gray50","gray12","hourglass","info","questhead","question","warning"]

for i in list:
    button=Button(root,bitmap=i,fg="red")
    button.pack(pady=20)

root.mainloop()