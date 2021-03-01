from tkinter import *
root=Tk()
root.title("Unicode and special characters with Tkinter")
root.geometry("400x400")

label=Label(root,text="41" + u'\u00B0',font=('Helvetica',32)).pack()

root.mainloop()