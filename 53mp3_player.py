from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import mutagen
import pygame
import time
from tkinter import ttk
from mutagen.mp3 import MP3
from pygame.mixer import fadeout, pause # for getting the length of music




#pause variable
global playing
playing=0

global paused

paused=False
global stopped
stopped=False

#functions
def add_song():
    
    song=filedialog.askopenfilename(initialdir='sounds/',title="Choose A Song",filetypes=(("mp3 Files",'*.mp3'),))
    song=song.replace("C:/Users/Aniket thani/Desktop/Tkinter tutorial/sounds/","")
    song=song.replace(".mp3","")
    song_box.insert(END,song.title())


def add_many_songs():
    songs=filedialog.askopenfilenames(initialdir="sounds/",title="Select songs",filetypes=(("mp3 Files","*.mp3"),))

    #loop throught the song list and insert them
    for song in songs:
        song=song.replace("C:/Users/Aniket thani/Desktop/Tkinter tutorial/sounds/","")
        song=song.replace(".mp3","")
        song_box.insert(END,song.title())


global song 
song=""





def play(is_playing,is_paused):
    global song
    
    if (song_box.get(ANCHOR)).lower()!=((song.split("/")[-1]).split(".")[0]).lower() :  # to change the current playing music
        play_btn.config(image=pause_img,command=lambda : play(1,0))
        song = song_box.get(ANCHOR)
        song="C:/Users/Aniket thani/Desktop/Tkinter tutorial/sounds/"+ song + ".mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        paused=False
        #play status
        length_of_song()
        play_status()
        #update the slider
        slider.config(to=length_song_copy, value=0)
        
        

    elif not(is_playing or is_paused ) and song_box.get(ANCHOR): # to play a music
        
        song=song_box.get(ACTIVE)
        song="C:/Users/Aniket thani/Desktop/Tkinter tutorial/sounds/"+ song + ".mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        #play status
        paused=False
        length_of_song()
        play_status()
        #update the slider
        slider.config(to=length_song_copy, value=0)
        
        play_btn.config(image=pause_img,command=lambda : play(1,0))
    elif  is_playing and not is_paused :  # to pause a music

        pygame.mixer.music.pause()
        paused=True
        play_btn.config(image=play_img,command=lambda : play(1,1))
        
        
    elif is_playing and  is_paused:   # to unpause a music
        pygame.mixer.music.unpause()
        paused=False
        play_btn.config(image=pause_img,command=lambda : play(1,0))
    
    

    
    


def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(0,END)
    
    #clear the status bar
    status_bar.config(text="")
    stopped=True
    slider.config(value=0)

    play_btn.config(image=play_img,command=lambda:play(0,0))

    
    

def next_song():
    #get current song selection index and increment it for getting next song
    next_song_index=song_box.curselection()[0] + 1

    # song to be played
    song=song_box.get(next_song_index)
    if(not song): # check if next song exists in the list or not  
        song=song_box.get(next_song_index-1)
        next_song_index=next_song_index-1
    song="C:/Users/Aniket thani/Desktop/Tkinter tutorial/sounds/"+ song.lower() + ".mp3"

    #load and play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # clear active bar in the playlist

    song_box.selection_clear(0,END)

    #activate the next song's bar for display
    song_box.activate(next_song_index)

    #set active bar to the next song
    song_box.selection_set(next_song_index,last=None)

    #determine length of song to be displayed on status bar
    length_of_song()
    # update the play button
    play_btn.config(image=pause_img, command=lambda: play(1, 0))
    

def previous_song():

    #get current song selection index and decrement it for getting previous song
    next_song_index=song_box.curselection()[0] -1
    # song to be played
    song = song_box.get(next_song_index)
    if(not song):  # check if next song exists in the list or not
        song = song_box.get(next_song_index+1)
        next_song_index = next_song_index+1
    song = "C:/Users/Aniket thani/Desktop/Tkinter tutorial/sounds/" + song.lower() + ".mp3"

    #load and play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # clear active bar in the playlist

    song_box.selection_clear(0, END)

    #activate the next song's bar for display
    song_box.activate(next_song_index)

    #set active bar to the next song
    song_box.selection_set(next_song_index, last=None)

    #determine length of song to be displayed on status bar
    length_of_song()

    # update the play button
    play_btn.config(image=pause_img, command=lambda: play(1, 0))

def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()
    
def delete_all_songs():
    song_box.delete(0,END)
    pygame.mixer.music.stop()

def play_status():
    global current_time
    current_time=pygame.mixer.music.get_pos() //1000  # in secs
    
    
   
    
    current_time+=1
    #update the slider position according to song
    
    if int(slider.get())==int(length_song_copy):
        status_bar.config(text=length_song + " off " + length_song)
    elif stopped:
        return
    elif paused:
        pass   
    elif int(current_time) == int(slider.get()):
        slider.config(value=current_time)
        #updating the status bar

        # arranging current_time in right format
        current_time_formatted = time.strftime("%H:%M:%S", time.gmtime(current_time))
        status_bar.config(text=current_time_formatted + " off " + length_song)
    else:
        
        slider.config(value=int(slider.get()))
        #updating the status bar
        slider_time = time.strftime("%H:%M:%S", time.gmtime(int(slider.get())))
        status_bar.config(text=slider_time + " off " + length_song)

        #increase the value of slider by one
        next_one=int(slider.get()) +1
        slider.config(value=next_one)

    
    
    

    

    status_bar.after(1000,play_status)

def length_of_song():
    global length_song
    #getting the current song from playlist
    try:

        # index of current song in playlist
        current_song = song_box.curselection()[0]
        current_song = song_box.get(current_song).lower()
        current_song = "C:/Users/Aniket Thani\Desktop\Tkinter tutorial/sounds/"+current_song+".mp3"

        # getting length of song with the help of  mutagen

        # first creating a mutagen object and loading a song in it
        song_mut = MP3(current_song)  # loading song

        #length of song
        length_song = song_mut.info.length  # in secs
        global length_song_copy
        length_song_copy=length_song
        #convert length to correct format
        length_song = time.strftime("%H:%M:%S", time.gmtime(length_song))
        


    except IndexError:
        pass

def slider_function(x):
    if not paused:

        song = song_box.get(ANCHOR)
        song = "C:/Users/Aniket thani/Desktop/Tkinter tutorial/sounds/" + song + ".mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0,start=int(slider.get()))
       

    #slider_label.config(text=f'{int(slider.get())} of {int(length_song_copy)}')

def volume(x):
    pygame.mixer.music.set_volume(1-volume_slider.get())




root=Tk()
root.title("Mp3 Player By Aniket Thani")
root.geometry("750x650")
root.config(bg="#03DAC5")

#initialize pygame mixer
pygame.mixer.init()

#create master  frame
master_frame = Frame(root, bg="#03DAC5")
master_frame.pack()

#create player control frame
control_frame = Frame(master_frame, bg="#03DAC5")
control_frame.grid(row=2,column=0,pady=5)

#create volume label frame
volume_frame=LabelFrame(master_frame,text="VOLUME")
volume_frame.grid(row=0,column=1,padx=10)

#create playlist box
song_box=Listbox(master_frame,width=60,bg="#282828",bd=5,fg="white",font=("Arial",14),selectbackground="white",selectforeground="black")
song_box.grid(row=0,column=0,pady=(20,2))

# define player control button images
back_img=ImageTk.PhotoImage(Image.open("button_image/backward.png").resize((50,50),Image.ANTIALIAS))
forward_img=ImageTk.PhotoImage(Image.open("button_image/forward.png").resize((50,50),Image.ANTIALIAS))
play_img=ImageTk.PhotoImage(Image.open("button_image/play.png").resize((50,50),Image.ANTIALIAS))
pause_img=ImageTk.PhotoImage(Image.open("button_image/pause.png").resize((50,50),Image.ANTIALIAS))
stop_img = ImageTk.PhotoImage(Image.open("button_image/stop.png").resize((50, 50), Image.ANTIALIAS))

#create slider

slider=ttk.Scale(master_frame,from_=0,to=100,orient=HORIZONTAL,length=600,command=slider_function,value=pygame.mixer.music.get_volume())
slider.grid(row=1,column=0,pady=(10,5))

#create temporary label for slider

#slider_label = Label(root, text="", bg="#03DAC5")
#slider_label.pack(pady=5)



#create player control buttons

back_btn=Button(control_frame,image=back_img,borderwidth=0,command=previous_song)
forward_btn=Button(control_frame,image=forward_img,borderwidth=0,command=next_song)
play_btn=Button(control_frame,image=play_img,borderwidth=0,command=lambda : play(0,0))

stop_btn = Button(control_frame, image=stop_img, borderwidth=0,command=stop)

back_btn.grid(row=0,column=0,padx=10)
forward_btn.grid(row=0,column=1,padx=10)
play_btn.grid(row=0,column=2,padx=10)
stop_btn.grid(row=0, column=3, padx=10)

#status bar
status_bar=Label(root,text="",anchor=E,bd=5,relief=GROOVE)
status_bar.pack(fill=X,side=BOTTOM)

#volume slider
volume_slider=ttk.Scale(volume_frame,from_=0,to=1,length=125,orient=VERTICAL,command=volume,value=1)
volume_slider.pack()

#create menu
my_menu=Menu(root)
root.config(menu=my_menu)

#add add_song menu item
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)

add_song_menu.add_command(label="Add one song to Playlist",command=add_song)
add_song_menu.add_command(label="Add many songs to Playlist",command=add_many_songs)

#create delete song menu
delete_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Delete Songs",menu=delete_song_menu)

delete_song_menu.add_command(label="Delete a Song from Playlist",command=delete_song)
delete_song_menu.add_command(label="Delete ALL Songs from Playlist",command=delete_all_songs)



root.mainloop()
