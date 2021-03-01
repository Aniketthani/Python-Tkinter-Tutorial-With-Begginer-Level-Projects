from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer App By Aniket Thani")

def forward(image_number):
    global label
    global button_back
    global button_forward

    label.grid_forget()
    label=Label(root,image=image_list[image_number-1])
    label.grid(row=0,column=0,columnspan=3)
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))

    if image_number==5:
        button_forward=Button(root,text=">>",state=DISABLED)

    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)


def back(image_number):
    global label
    global button_back
    global button_forward

    label.grid_forget()
    label=Label(root,image=image_list[image_number-1])
    label.grid(row=0,column=0,columnspan=3)
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))

    if image_number==1:
        button_back=Button(root,text=">>",state=DISABLED)

    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)




my_img1=ImageTk.PhotoImage(Image.open("image/parrot.jpeg"))
my_img2=ImageTk.PhotoImage(Image.open("image/img2.jpeg"))
my_img3=ImageTk.PhotoImage(Image.open("image/img3.jpeg"))
my_img4=ImageTk.PhotoImage(Image.open("image/img4.jpeg"))
my_img5=ImageTk.PhotoImage(Image.open("image/img5.jpeg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

label=Label(root,image=image_list[0])
label.grid(row=0,column=0,columnspan=3)

button_back=Button(root,text="<<",state=DISABLED)
button_exit=Button(root,text="Exit",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:forward(2))


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)






root.mainloop()