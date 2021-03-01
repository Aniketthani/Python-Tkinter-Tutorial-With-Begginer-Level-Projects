from tkinter import *
from tkinter import ttk
import time

def progress():
    #progress_bar['value']+=20
    #progress_bar.start(10)
    for i in range(5):
        progress_bar['value']+=20
        root.update_idletasks() # to slow down the updates so that we can notice the change on screen   
        time.sleep(1) #waiting 

def stop():
    progress_bar.stop()
root=Tk()
root.title("Progress bar")
root.geometry("500x500")

progress_bar=ttk.Progressbar(root,orient=HORIZONTAL,length=400,mode="determinate") #mode=determinate or indeterminate
progress_bar.pack(pady=100)

button=Button(root,text="progress",command=progress)
button.pack()

stop_button=Button(root,text="stop",command=stop)
stop_button.pack()

root.mainloop()