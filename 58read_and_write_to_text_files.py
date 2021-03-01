from tkinter import * 
from tkinter import filedialog



def open_txt():
    file=filedialog.askopenfilename(filetypes=(("txt File",'*.txt'),))
    txt_file=open(file,"r")
    stuff=txt_file.read()
    textbox.insert(END,stuff)
    txt_file.close()

def save_txt():
    file=filedialog.asksaveasfilename()
    txt_file=open(file,"w")
    txt_file.write(textbox.get(1.0,END))
    txt_file.close()



root=Tk()
root.geometry("600x700")

yscrollbar=Scrollbar(root,orient=VERTICAL)
yscrollbar.pack(fill=Y,side=RIGHT)


textbox=Text(root,width=40,height=20,font=("Helvetica",15),selectbackground="orange",selectforeground="black")
textbox.pack()

#configure Text box and Scrollbar
yscrollbar.config(command=textbox.yview)

textbox.config(yscrollcommand=yscrollbar.set)


#button_frame
button_frame=Frame(root)
button_frame.pack(pady=20)

#open file button

open_file_button=Button(button_frame,text="Open text file",command=open_txt)
open_file_button.grid(row=0,column=0)

save_file_button=Button(button_frame,text="Save File",command=save_txt)
save_file_button.grid(row=0,column=1,padx=10)





root.mainloop()