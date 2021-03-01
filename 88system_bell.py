from tkinter import *
root=Tk()
root.geometry("400x400")

def bell():
    root.bell()


button=Button(root,text="Ring The Bell",command=bell)
button.pack(pady=20)

root.mainloop()