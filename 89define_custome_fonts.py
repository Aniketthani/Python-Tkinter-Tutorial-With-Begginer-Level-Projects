from tkinter import *
from tkinter.font import Font


root=Tk()
root.title("Define Our Own Customs")
root.geometry("700x700")

bigFont=Font(family="Times",size=42,weight="bold",slant="roman",underline=0,overstrike=0)

mediumFont=Font(family="Helvetica",size=28,slant="italic",underline=1,overstrike=0)

strikeFont=Font(family="Arial",size=25,slant="italic",underline=0,overstrike=1)

button=Button(root,text="Big Font",font=bigFont)
button.pack(pady=20)

button=Button(root,text="medium Font",font=mediumFont)
button.pack(pady=20)

button = Button(root, text="Hello World", font=strikeFont)
button.pack(pady=20)



root.mainloop()
