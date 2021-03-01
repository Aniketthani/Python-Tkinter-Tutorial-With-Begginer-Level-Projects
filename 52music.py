from tkinter import *
import pygame

root=Tk()
root.geometry("500x500")

pygame.mixer.init()

def play():
    pygame.mixer.music.load("sounds/sound1.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

play_button=Button(root,text="Play Music",command=play)
play_button.pack()


stop_button=Button(root,text="stop",command=stop)
stop_button.pack(pady=20)

root.mainloop()