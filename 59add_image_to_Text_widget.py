from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image


def open_txt():
    file = filedialog.askopenfilename(filetypes=(("txt File", '*.txt'),))
    txt_file = open(file, "r")
    stuff = txt_file.read()
    textbox.insert(END, stuff)
    txt_file.close()


def save_txt():
    file = filedialog.asksaveasfilename()
    txt_file = open(file, "w")
    txt_file.write(textbox.get(1.0, END))
    txt_file.close()


def insert_image():
    # ,filetypes=(("jpg File","*.jpg"),("png File","*.png"),("jpeg File",'*.jpeg')))
    # initialdir="C:/Users/Aniket thani/Desktop/Tkinter tutorial/"
    global img_file
    img_file = filedialog.askopenfilename()
    global img
    img=ImageTk.PhotoImage(Image.open(img_file))
    cursor_position=textbox.index(INSERT)  # gettin current position of cursor to insert image at that position

    textbox.image_create(cursor_position,image=img)
    


root = Tk()
root.geometry("600x700")

yscrollbar = Scrollbar(root, orient=VERTICAL)
yscrollbar.pack(fill=Y, side=RIGHT)


textbox = Text(root, width=40, height=20, font=("Helvetica", 15),selectbackground="orange", selectforeground="black")
textbox.pack()

#configure Text box and Scrollbar
yscrollbar.config(command=textbox.yview)

textbox.config(yscrollcommand=yscrollbar.set)


#button_frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#open file button

open_file_button = Button(
    button_frame, text="Open text file", command=open_txt)
open_file_button.grid(row=0, column=0)

save_file_button = Button(button_frame, text="Save File", command=save_txt)
save_file_button.grid(row=0, column=1, padx=10)

add_image_button=Button(button_frame,text="Insert Image",command=insert_image)
add_image_button.grid(row=1,column=0,columnspan=2)


root.mainloop()
