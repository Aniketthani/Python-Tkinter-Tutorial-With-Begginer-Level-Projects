from tkinter import* 
import time

root=Tk()
root.title("Live Clock")
root.geometry("500x500")

def clock():
    hour=time.strftime('%I') #for 12 hours format
    minute=time.strftime("%M") # for minutes
    seconds=time.strftime("%S") # for seconds
    am_or_pm=time.strftime("%p") # for am or pm
    day=time.strftime("%A") # for day

    label.config(text=hour+":"+minute+":"+seconds+" "+am_or_pm+" "+day)
    label.after(1000,clock)



label=Label(root,text="",font=("Helvetica",20),bg="black",fg="yellow")
label.pack(pady=30)

clock()



root.mainloop()