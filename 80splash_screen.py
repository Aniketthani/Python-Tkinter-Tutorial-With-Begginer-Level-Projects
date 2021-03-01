from tkinter import * 

splash_screen=Tk()
splash_screen.geometry("300x300+500+225")
splash_screen.title("Splash Screen")

x=3
label = Label(splash_screen, text=f'Wait for {x} seconds')
label.pack(pady=20)

def main_screen():
    splash_screen.destroy()
    root=Tk()
    root.geometry("500x500+500+200")

    label=Label(root,text="Hey Welcome, This is the main screen")

    label.pack(pady=20)



        
splash_screen.after(3000,main_screen)


   


mainloop()
