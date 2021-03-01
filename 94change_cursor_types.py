# twenty cursor types
from tkinter import *
root=Tk()
root.geometry("500x800")
root.config(cursor="mouse")

list=["arrow","circle","cross","clock","dotbox","fleur","heart","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek"]


for i in list:
    button=Button(root,text=i,cursor=i)
    button.pack(pady=5)
root.mainloop()