from tkinter import *


def clear_text():
    textbox.delete(1.0, END)    # indexing in Text box in Tkinter starts with 1.0

def print_text():
    label.config(text=textbox.get(1.0,END))

root=Tk()
root.title("TextBox Widget")
root.geometry("600x700")

#adding scrollbar for  Text box
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

#creating Text Widget
textbox=Text(root,height=30,width=40,font=("Helvetica"))
textbox.pack(pady=20)

#configuring Text Widget and Scrollbar
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)


button_frame=Frame(root)
button_frame.pack(pady=10)

clear_button=Button(button_frame,text="Clear Text",command=clear_text)
clear_button.grid(row=0,column=0)

print_text_button=Button(button_frame,text="Print Text",command=print_text)
print_text_button.grid(row=0,column=1,padx=20)



label=Label(root,text="")
label.pack(pady=10)
root.mainloop()
