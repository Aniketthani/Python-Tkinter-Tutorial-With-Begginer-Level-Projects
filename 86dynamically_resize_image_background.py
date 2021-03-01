from tkinter import *
from PIL import ImageTk, Image

def resize(e):
    global img,my_canvas # make sure to use global else image resize will not happen
    img = ImageTk.PhotoImage(Image.open("image/mountain.jpg").resize((e.width,e.height)))
    my_canvas.config(height=e.height,width=e.width)
    my_canvas.create_image(0, 0, image=img, anchor="nw")
    my_canvas.create_text(350, 200, text="Hey this is me",fill="red", font=("Arial", 20))

root = Tk()
root.geometry("800x500")
#root.maxsize(800, 500)
#root.minsize(800, 500)

img = ImageTk.PhotoImage(Image.open("image/mountain.jpg").resize((800, 500)))

#there are two methods to do this job
# in the first method we can easily put the image as background but our widgets will not be transparent relative to that background perfectly
#and in second method we will use canvas and put that image on canvas and then create window on that image and then we will add those widgets in those windows

# first method
'''
label=Label(root,image=img)

#now we  will place  this label on root
label.place(relx=0,rely=0,relheight=1,relwidth=1)

#extra widgets
button=Button(root,text="button")
button.pack(pady=10)

text_label=Label(root,text="Hey this is me",font=("Helvetica"))
text_label.pack(pady=20)

'''

# second method of using canvas


#creating canvas
my_canvas = Canvas(root,width=800,height=500)
my_canvas.pack()

#create widgets for putting on window
button1 = Button(my_canvas, text="Button 1")
button2 = Button(my_canvas, text="Button 2")
button3 = Button(my_canvas, text="Button 3")


#putting image on canvas
my_canvas.create_image(0, 0, image=img, anchor="nw")

# making windows on canvas and storing widgets in them
my_canvas.create_window(100, 100, window=button1)
my_canvas.create_window(200, 100, window=button2)
my_canvas.create_window(300, 100, window=button3)

my_canvas.create_text(350, 200, text="Hey this is me",fill="red", font=("Arial", 20))



root.bind("<Configure>",resize)
root.mainloop()
