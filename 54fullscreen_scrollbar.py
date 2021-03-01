from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Adding Scroll Bar to Screen")
root.geometry("500x500")

#create a main frame
main_frame=Frame(root,bg="white")
main_frame.pack(fill=BOTH,expand=1)

#create a canvas
my_canvas=Canvas(main_frame,bg="red")
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
#add a scrollbar to the canvas
my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

#configure the canvas
my_canvas.config(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

#create another frame to a window in the canvas
second_frame=Frame(my_canvas,bg="cyan")


#add that new frame to a window in the canvas
my_canvas.create_window((0,0),window=second_frame,anchor=NW)



# creating 100 buttons
for i in range(100):
    button=Button(second_frame,text="button " + str(i))
    button.pack(pady=5)


root.mainloop()