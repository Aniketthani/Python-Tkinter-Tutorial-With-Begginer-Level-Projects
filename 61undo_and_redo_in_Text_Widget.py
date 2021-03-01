

#Read this first

#firstly we have to give our allowance of doing undo operations to Text widget
# example :-   textbox = Text(root,undo=True, width=40, height=20, font=("Helvetica", 15),selectbackground = "orange", selectforeground = "black")
# and then we have to make buttons for undo and redo 
# give command = textbox.edit_undo in undo_button
# and give command = textbox.edit_redo in redo_button





from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import font


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
    img = ImageTk.PhotoImage(Image.open(img_file))
    # gettin current position of cursor to insert image at that position
    cursor_position = textbox.index(INSERT)

    textbox.image_create(cursor_position, image=img)


def bolder():
    #make or define bold_font
    bold_font = font.Font(textbox, textbox.cget("font"))
    bold_font.config(weight="bold")

    #adding bold tag in our Text Widget

    textbox.tag_configure("bold", font=bold_font)

    #retrieving all current tags
    current_tags = textbox.tag_names("sel.first")
    if "bold" in current_tags:
        #unbold the selected text
        textbox.tag_remove("bold", "sel.first", "sel.last")
    else:
        #bold the selected text
        textbox.tag_add("bold", "sel.first", "sel.last")


def italic():
    #make or define itaclic_font
    italic_font = font.Font(textbox, textbox.cget("font"))
    italic_font.config(slant="italic")

    #adding italic tag in our Text Widget

    textbox.tag_configure("italic", font=italic_font)

    #retrieving all current tags
    current_tags = textbox.tag_names("sel.first")
    if "italic" in current_tags:
        #remove italic from selected text
        textbox.tag_remove("italic", "sel.first", "sel.last")
    else:
        #make  the selected text italic
        textbox.tag_add("italic", "sel.first", "sel.last")


root = Tk()
root.geometry("600x700")

yscrollbar = Scrollbar(root, orient=VERTICAL)
yscrollbar.pack(fill=Y, side=RIGHT)


textbox = Text(root,undo=True, width=40, height=20, font=("Helvetica", 15),selectbackground="orange", selectforeground="black")
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

add_image_button = Button(
    button_frame, text="Insert Image", command=insert_image)
add_image_button.grid(row=1, column=0, columnspan=2)

bold_button = Button(button_frame, text="BOLD", command=bolder)
bold_button.grid(row=2, column=0)

italic_button = Button(button_frame, text="Italic", command=italic)
italic_button.grid(row=2, column=1, padx=10)

undo_button = Button(button_frame, text="Undo", command=textbox.edit_undo)
undo_button.grid(row=3, column=0)

redo_button = Button(button_frame, text="Redo", command=textbox.edit_redo)
redo_button.grid(row=3, column=1, padx=10)

root.mainloop()
