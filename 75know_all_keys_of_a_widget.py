from tkinter import * 
root=Tk()

root.geometry("500x500")

label=Label(root,text="See the keys of Label Widget on the command prompt ")
label.pack()

for key in label.keys():
    print(key)

root.mainloop()