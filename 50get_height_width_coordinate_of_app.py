from tkinter import *
root=Tk()
root.geometry("600x700+400+200")

def update():
    label.config(text="Height : "+str(root.winfo_height()) + " Width : "+str(root.winfo_width()) + " Geometry : " + str(root.winfo_geometry())+ " X : "+str(root.winfo_x()) + " Y : " + str(root.winfo_y()))
    label.after(100,update)


label=Label(root,text="")
label.pack()

button=Button(root,text="Get Height , width , X and Y coordinate of window",command=update)
button.pack(pady=10)






root.mainloop()
