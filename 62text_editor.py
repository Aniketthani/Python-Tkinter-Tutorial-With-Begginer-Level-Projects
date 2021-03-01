from os import name
from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import colorchooser
import os,sys
import win32print
import win32api


global name_of_file_open
name_of_file_open=False

global selected_text
selected_text=False

def new_file():
    textbox.delete(1.0,END)
    root.title("Text Editor By Aniket Thani : Untitled.txt ")
    status_bar.config(text="Untitled.txt")
    global name_of_file_open
    name_of_file_open=False

def open_file():
    textbox.delete(1.0,END)
    file=filedialog.askopenfilename(filetypes=(("Text File","*.txt"),("HTML File","*.html"),("Python File","*.py"),("All Files","*.*")))
    global name_of_file_open
    if file:
        name_of_file_open=file

    #update title and status bar
    name=file
    status_bar.config(text=file)
    name=name.split("/")[-1]
    root.title(f'Text Editor By Aniket Thani : {name}')

    #open file
    file=open(file,"r")
    stuff=file.read()
    textbox.insert(END,stuff)
    file.close()

def save_as():
    file_name = filedialog.asksaveasfilename(defaultextension="*.txt", initialdir="C:/Users/Aniket thani/Desktop/Tkinter tutorial/", title="Save File", filetypes=(("Text File", "*.txt"), ("HTML File", "*.html"), ("Python File", "*.py"), ("All Files", "*.*")))

    if file_name:
        #update the title and status bar
        name = file_name
        status_bar.config(text="Saved : " + file_name)
        name = name.split("/")[-1]
        root.title(f'Text Editor By Aniket Thani : {name}')

        #save file
        f=open(file_name,"w")
        f.write(textbox.get(1.0,END))
        f.close()
        global name_of_file_open
        name_of_file_open=file_name

def save_file(e):
    global name_of_file_open
    if name_of_file_open:
        f=open(name_of_file_open,"w")
        f.write(textbox.get(1.0,END))
        f.close()
        #update status bar
        status_bar.config(text="Saved : " + name_of_file_open)
    else:
        save_as()


# when we cut or copy or paste something using keyboard shortcuts then windows clipboard will also perform that action along 
# with our code written for  that thing
# therefore we will not do anything if keyboard shortcuts are used
# and will rely on windows clipboard to do these jobs for us


def cut_text(e):
    global selected_text
    if e:  # check if keyboard shortcuts are pressed or not
        # if events are supplied then we will get text from windows clipboard and assign it to selected_text
        # then we delete the selected text from textbox
        selected_text=root.clipboard_get()
        # delete the selected text from textbox
        textbox.delete("sel.first", "sel.last")
    else: # keyboard shortcuts are not used
        #we will get the selected text and assign it to selected_text
        #delete selected text from textbox
        
        # after that if any body uses any keyboard shortcut for paste then we will not insert that text into textbox
        # but will make sure windows clipboard do that itself
        # for that we first clear the clipboard
        # and then append selected_text to clipboard
        # now when some body press Ctrl+v then windows clipboard will do the paste job

        if textbox.selection_get():
            selected_text=textbox.selection_get()

            # delete the selected text from textbox
            textbox.delete("sel.first","sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected_text)

def paste_text(e):
    global selected_text
    #check if keyboard shortcuts are pressed or not
    if e:
        selected_text=root.clipboard_get()
        # we will not do anything since keyboard shortcut is used
        # windows clipboard will do the job for us
    else:
        if selected_text:
            #position to paste at
            position=textbox.index(INSERT)

            # paste text at position
            textbox.insert(position,selected_text)

def copy_text(e):
    global selected_text
    #check if keyboard shortcuts are pressed or not
    if e: # if keyboard shortcuts are pressed then an event will be passed in e
        selected_text=root.clipboard_get()
    else:
        if textbox.selection_get():
            selected_text=textbox.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected_text)

def bold_text():
    bold_font=font.Font(textbox,textbox.cget("font"))
    bold_font.configure(weight="bold")

    #add bold tag to textbox
    textbox.tag_configure("bold",font=bold_font)

    # retrieve tags from textbox
    current_tags=textbox.tag_names("sel.first")
    if "bold" in current_tags:
        # remove bold tag from textbox from selected text to unbold it 
        textbox.tag_remove("bold","sel.first","sel.last")
    else : 
        # add bold tag to textbox to only selected text to make it bold
        textbox.tag_add("bold","sel.first","sel.last")


def italic_text():
    italic_font=font.Font(textbox,textbox.cget("font"))

    italic_font.config(slant="italic")

    textbox.tag_configure("italic",font=italic_font)

    current_tags=textbox.tag_names("sel.first")

    if "italic" in current_tags:
        textbox.tag_remove("italic","sel.first","sel.last")
    else:
        textbox.tag_add("italic","sel.first","sel.last")

def color_text():
    my_color=colorchooser.askcolor()[1]
    if my_color:


        color_font = font.Font(textbox, textbox.cget("font"))


        textbox.tag_configure("colored", font=color_font,foreground=my_color)

        current_tags = textbox.tag_names("sel.first")

        if "colored" in current_tags:
            textbox.tag_remove("colored", "sel.first", "sel.last")
        else:
            textbox.tag_add("colored", "sel.first", "sel.last")


def color_all_text():

    color=colorchooser.askcolor()[1]
    if color:
        textbox.config(foreground=color,insertbackground=color) # insertbackground is used to set color of cursor

def color_background():
    color = colorchooser.askcolor()[1]
    if color:
        textbox.config(background=color)

def select_all():

    textbox.tag_add("sel","1.0","end")

def clear_all():

    textbox.delete(1.0,END)
def print_file():
    #printter_name=win32print.GetDefaultPrinter()
    #print(printter_name)

    file_to_print=filedialog.askopenfilename(defaultextension="*.txt", initialdir="C:/Users/Aniket thani/Desktop/Tkinter tutorial/", title="Save File", filetypes=(("Text File", "*.txt"), ("HTML File", "*.html"), ("Python File", "*.py"), ("All Files", "*.*")))

    if file_to_print:
        win32api.ShellExecute(0,"print",file_to_print,None,".",0)

def night_mode_on():
    main_color="#121212"
    textbox_color="#505050"
    textbox_text_color="#00FF33"
    toolbar_frame_color="#9966FF"
    toolbar_button_text_color="white"
    toolbar_button_color="#9900FF"
    status_bar_text_color="#33FFFF"
    menu_items_bg_color = "#C8C8C8"
    menu_items_text_color = "black"

    root.config(bg=main_color)
    textbox.config(background=textbox_color,foreground=textbox_text_color,insertbackground=textbox_text_color)
    toolbar_frame.config(bg=toolbar_frame_color)
    bold_button.config(fg=toolbar_button_text_color,bg=toolbar_button_color,font=("Arial",12))
    italic_button.config(fg=toolbar_button_text_color,bg=toolbar_button_color,font=("Arial",12))
    undo_button.config(fg=toolbar_button_text_color,bg=toolbar_button_color,font=("Arial",12))
    redo_button.config(fg=toolbar_button_text_color,bg=toolbar_button_color,font=("Arial",12))
    color_text_button.config(fg=toolbar_button_text_color, bg=toolbar_button_color,font=("Arial",12))
    status_bar.config(bg=main_color,fg=status_bar_text_color)
    
    file_menu.config(bg=menu_items_bg_color,fg=menu_items_text_color)
    edit_menu.config(bg=menu_items_bg_color,fg=menu_items_text_color)
    color_menu.config(bg=menu_items_bg_color,fg=menu_items_text_color)
    options_menu.config(bg=menu_items_bg_color, fg=menu_items_text_color)


def night_mode_off():
    main_color="SystemButtonFace"
    textbox_color = "white"
    textbox_text_color="black"
    toolbar_frame_color="SystemButtonFace"
    toolbar_button_text_color="black"
    toolbar_button_color="SystemButtonFace"
    status_bar_text_color="black"
    menu_items_bg_color = "SystemButtonFace"
    menu_items_text_color = "black"

    root.config(bg=main_color)
    textbox.config(background=textbox_color,foreground=textbox_text_color,insertbackground=textbox_text_color)
    toolbar_frame.config(bg=toolbar_frame_color)
    bold_button.config(fg=toolbar_button_text_color,bg=toolbar_button_color,font=("Arial",12))
    italic_button.config(fg=toolbar_button_text_color,bg=toolbar_button_color,font=("Arial",12))
    undo_button.config(fg=toolbar_button_text_color,bg=toolbar_button_color,font=("Arial",12))
    redo_button.config(fg=toolbar_button_text_color,bg=toolbar_button_color,font=("Arial",12))
    color_text_button.config(fg=toolbar_button_text_color, bg=toolbar_button_color,font=("Arial",12))
    status_bar.config(bg=main_color,fg=status_bar_text_color)
    
    file_menu.config(bg=menu_items_bg_color,fg=menu_items_text_color)
    edit_menu.config(bg=menu_items_bg_color,fg=menu_items_text_color)
    color_menu.config(bg=menu_items_bg_color,fg=menu_items_text_color)
    options_menu.config(bg=menu_items_bg_color, fg=menu_items_text_color)


root=Tk()
root.title("Text Editor By Aniket Thani  ")
root.geometry("1200x700")
root.maxsize(1200,700)
root.minsize(1200,700)

#create toolbar frame
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)

#create main frame
main_frame=Frame(root)
main_frame.pack(pady=5)



#scrollbar
text_scroll_y=Scrollbar(main_frame)
text_scroll_y.pack(fill=Y,side=RIGHT)

text_scroll_x=Scrollbar(main_frame,orient=HORIZONTAL)
text_scroll_x.pack(fill=X,side=BOTTOM)


# create Text box
# make sure to make wrap attribute of Text Widget to "none" like that wrap="none"
# otherwise horizontal scrollbar will not work as text will be wrapped by tkinter
textbox=Text(main_frame,height=25,width=97,undo=True,font=("Helvetica",16),wrap="none",yscrollcommand=text_scroll_y.set,xscrollcommand=text_scroll_x.set, selectbackground="orange",selectforeground="black")
textbox.pack()

#configure the scroll bar
text_scroll_y.config(command=textbox.yview)
text_scroll_x.config(command=textbox.xview)
#create menu
my_menu=Menu(root)
root.config(menu=my_menu)

#create file menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=lambda : save_file(0))
file_menu.add_command(label="Save As",command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Print File", command=print_file)

file_menu.add_separator()

file_menu.add_command(label="Exit",command=root.quit)

#create edit menu
edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut            (Ctrl+x)",command=lambda : cut_text(0))
edit_menu.add_command(label="Copy           (Ctrl+c)",command=lambda : copy_text(0))
edit_menu.add_command(label="Paste          (Ctrl+v)", command=lambda: paste_text(0))
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command=textbox.edit_undo,accelerator="(Ctrl+z)")

edit_menu.add_command(label="Redo",command=textbox.edit_redo,accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label="Select All",command=select_all ,accelerator="(Ctrl+a)")
edit_menu.add_command(label="Clear All", command=clear_all)

#create color menu
color_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Color", menu=color_menu)

color_menu.add_command(label="Selected Text",command=color_text)
color_menu.add_command(label="All Text",command=color_all_text)
color_menu.add_command(label="Background", command=color_background)

#create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)

options_menu.add_command(label="Turn On Night Mode", command=night_mode_on)
options_menu.add_command(label="Turn Off Night Mode", command=night_mode_off)



#add status bar to the bottom
status_bar=Label(root,text="Ready ",anchor=E,border=4)
status_bar.pack(fill=X,side=BOTTOM)

# toolbar buttons
bold_button=Button(toolbar_frame,text="Bold",command=bold_text,font=("Arial",12))
bold_button.grid(row=0,column=0)

italic_button=Button(toolbar_frame,text="Italic",command=italic_text,font=("Arial",12))
italic_button.grid(row=0,column=1,padx=10)

undo_button=Button(toolbar_frame,text="Undo",command=textbox.edit_undo,font=("Arial",12))
undo_button.grid(row=0,column=2,padx=10)

redo_button = Button(toolbar_frame, text="Redo", command=textbox.edit_redo,font=("Arial",12))
redo_button.grid(row=0, column=3, padx=10)

color_text_button=Button(toolbar_frame,text="Color Text",command=color_text,font=("Arial",12))
color_text_button.grid(row=0,column=4,pady=10)



#bind keys for cut ,copy ,paste,save,etc
root.bind("<Control-Key-x>",cut_text)
root.bind("<Control-Key-c>",copy_text)
root.bind("<Control-Key-v>", paste_text)

root.bind("<Control-Key-s>",save_file)



root.mainloop()
