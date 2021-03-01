from tkinter import *
root=Tk()
root.title("Class wit Tkinter")
root.geometry("400x400")

class test:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()

        
        self.mybutton=Button(master,text="Click me !!",command=self.clicker)
        self.mybutton.pack()
    def clicker(self):
        print("Look at you ... You clicked a Button")


e=test(root)

root.mainloop()
