from tkinter import *
root=Tk()
root.geometry("500x800")

frame=LabelFrame(root,text="Right Justified")
frame.pack(pady=20)

message=Message(frame,text="Hello This is a very long text . Therefore Iam using Message widget of tkiner to resolve the problem caused by label widget when dealing with long texts",
font=("Helvetica",18),justify=RIGHT,aspect=150
)
message.pack()

frame=LabelFrame(root,text="Center Justified")
frame.pack(pady=20)

message=Message(frame,text="Hello This is a very long text . Therefore Iam using Message widget of tkiner to resolve the problem caused by label widget when dealing with long texts",
font=("Helvetica",18),justify=CENTER,aspect=100
)
message.pack()


frame = LabelFrame(root, text="Left Justified")
frame.pack(pady=20)

message = Message(frame, text="Hello This is a very long text . Therefore Iam using Message widget of tkiner to resolve the problem caused by label widget when dealing with long texts",
                  font=("Helvetica", 18), justify=LEFT, aspect=200
                  )
message.pack()


root.mainloop()
