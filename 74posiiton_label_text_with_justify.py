from tkinter import * 


root=Tk()
root.geometry("700x700")

label1=Label(root,text="Stuff\nStuff Stuff\nStuff Stuff Stuff",bd=10,relief=SUNKEN,font=("Arial",20))  #justify=center (by default)
label1.pack(pady=20)

label2=Label(root,text="Stuff\nStuff Stuff\nStuff Stuff Stuff",justify="left",bd=10,relief=SUNKEN,font=("Arial",20))  #justify=left
label2.pack(pady=20)

# justify=right 
label3 = Label(root, text="Stuff\nStuff Stuff\nStuff Stuff Stuff", justify="right",bd=10, relief=SUNKEN, font=("Arial", 20))
label3.pack(pady=20)


root.mainloop()
