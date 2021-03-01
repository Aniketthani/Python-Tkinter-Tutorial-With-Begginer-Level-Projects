from tkinter import *
from tkinter import ttk
def new_window():
    
    def solid(e):
        w.attributes("-alpha",1.0)
    
    
    w=Toplevel()
    w.attributes('-alpha',0.5)

    w.bind("<Button-1>",solid)





def slider(e):
    root.attributes("-alpha",my_slider.get())
    label.config(text=round(my_slider.get(),2))

root=Tk()
root.geometry("500x500")


root.attributes("-alpha",0.7)  # value of alpha ranges from 0 to 1

#slider for adjusting transparency of window
my_slider=ttk.Scale(root,from_=0.1,to=1.0,value=0.7,command=slider,orient=HORIZONTAL)
my_slider.pack(pady=20)

label=Label(root,text="")
label.pack(pady=20)

button=Button(root,text="click me",command=new_window)
button.pack(pady=20)


root.mainloop()