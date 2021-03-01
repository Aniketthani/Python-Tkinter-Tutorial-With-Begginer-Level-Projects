from tkinter import *
import pyttsx3

root=Tk()

root.title("Text to Speech")
root.geometry("500x500")

def speak():
    engine = pyttsx3.init()
    #engine.setProperty('rate',500)

    #changing voice from male to female
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    engine.say(entry.get())
    engine.runAndWait()
    entry.delete(0,END)



entry=Entry(root)
entry.pack()
button=Button(root,text="speak",command=speak)
button.pack()

root.mainloop()
