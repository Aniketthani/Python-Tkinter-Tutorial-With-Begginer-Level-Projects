from tkinter import *
from tkcalendar import *
root=Tk()
root.title("Date Picker")
root.geometry("500x500")

calendar=Calendar(root)
calendar.pack()
def date():
    label.config(text=calendar.get_date())
    

button=Button(root,text="Pick Date",command=date)
button.pack()

label=Label(root,text="")
label.pack()

root.mainloop()