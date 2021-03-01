from tkinter import *
root=Tk()
root.geometry("500x500")

def change_tab_order():
    blue.focus()   # Now tab order will be blue,white,red 
    for w in widgets:
        w.lift()

red=Entry(root,bg="red",font=("Arial",20),fg="yellow",insertbackground="yellow")
red.pack(pady=20)

white = Entry(root,font=("Arial", 20))
white.pack(pady=20)

blue = Entry(root,  bg="blue", font=("Arial", 20),
             fg="yellow", insertbackground="yellow")
blue.pack(pady=20)

#set focus
red.focus()

#widget list
widgets = [blue, white, red ]

#change tab order button
change_tab_order_button=Button(root,text="change tab order",command=change_tab_order)
change_tab_order_button.pack(pady=20)


root.mainloop()
