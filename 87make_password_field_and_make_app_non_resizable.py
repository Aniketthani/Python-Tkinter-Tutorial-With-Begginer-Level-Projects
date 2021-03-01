from tkinter import  *
root=Tk()
root.title("Make Password field and Also Make our App non resizable")
root.geometry("500x500")

#make app non resizable 
root.resizable(width=False,height=False)

password_label=Label(root,text="Password",font=("Helvetica",20))
password_label.pack(pady=20)
password=Entry(root,show="*",font=("Helvetica",20))
password.insert(0,"password")
password.focus()
password.pack(pady=40)





root.mainloop()