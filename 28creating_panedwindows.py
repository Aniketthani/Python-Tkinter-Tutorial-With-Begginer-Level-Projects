from tkinter import *
root=Tk()
root.title("creating panels or panedwindows")
root.geometry("500x500")
#panels
panel_1=PanedWindow(bd=4,relief=RAISED,bg="red")
panel_1.pack(fill=BOTH,expand=1)

left_label=Label(panel_1,text="Left Panel")
panel_1.add(left_label)

#creating second panel
panel_2=PanedWindow(panel_1,orient=VERTICAL,bd=4,relief=RAISED,bg="blue")
panel_1.add(panel_2)

top=Label(panel_2,text="Top Panel")
panel_2.add(top)

bottom=Label(panel_2,text="Bottom Panel")
panel_2.add(bottom)

root.mainloop()
