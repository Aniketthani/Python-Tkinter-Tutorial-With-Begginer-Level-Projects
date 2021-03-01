from tkinter import  *

root=Tk()

height=500
width=700

x=(root.winfo_screenwidth()/2) - (width/2)
y=(root.winfo_screenheight()/2) - (height/2)

root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

root.mainloop()