from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("500x700")

new_wn = Toplevel()
new_wn.geometry("400x400")

def resize(e):
    ratio=slider.get()
    if ratio==0:
        ratio=0.3
    height=new_wn.winfo_screenheight()*ratio
    width=new_wn.winfo_screenwidth()*ratio
    new_wn.geometry(f'{int(width)}x{int(height)}')


slider=ttk.Scale(root,from_=0,to=1,length=300,command=resize)
slider.pack(pady=20)





root.mainloop()
