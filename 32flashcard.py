from tkinter import *
from PIL import ImageTk,Image
from random import randint, shuffle


root=Tk()
root.title("Flashcard App By Aniket Thani")
root.geometry("700x700")
root.config(bg="orange")

#functions

def random_image():
    #list of state names
    global our_states
    our_states = ['chhattisgarh', 'madhya_pradesh', 'karnataka', 'tamil_nadu',
                  'gujarat', 'harayana', 'rajasthan', 'delhi', 'maharashtra', 'bihar']
    #generate random integer
    global rnum
    rnum = randint(0, len(our_states)-1)

    global state
    state = "states/"+our_states[rnum]+".jpg"

    #display image of state
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(state))
    global img_label
    img_label = Label(states_frame, image=state_img)
    img_label.pack()

def check_answer():
    value=answer.get().lower()
    value=value.replace(" ","_")
    if our_states[rnum]==value:
        response.config(text="Correct!! " + our_states[rnum].replace("_"," ").title())
    else:
        response.config(text="Incorrect!! " + our_states[rnum].replace("_"," ").title())
    answer.delete(0,"end")
    img_label.destroy()
    random_image()
    

def states():
    hide_all_frames()
    states_frame.pack()
    states_frame.focus_set()

    #create next state button
    next_button=Button(states_frame,text=" >> ",padx=10,pady=7,command=states)
    next_button.pack(pady=5)

    #create answer input box
    global answer
    answer=Entry(states_frame,font=("Helvetica",20),bd=3)
    answer.pack(pady=5)

    #create submit button
    submit=Button(states_frame,text="Submit",pady=5,command=check_answer)
    submit.pack()

    #create response label
    global response
    response=Label(states_frame,text="",font=("Helvetica",16),bg="orange")
    response.pack()

    random_image()

    
    
    

    
    
    

def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill=BOTH,expand=1)
    label=Label(state_capitals_frame,text="Capitals").pack(pady=5)

    #selecting random states and capitals
    count =1
    global answer_list
    answer_list=[]
    global ranum
    global state_list
    state_list = ['chhattisgarh', 'madhya_pradesh', 'karnataka', 'tamil_nadu','gujarat', 'harayana', 'rajasthan', 'delhi', 'maharashtra', 'bihar']

    global capitals
    capitals=['raipur','bhopal','bangalore','chennai','gandhinagar','chandigarh','jaipur','delhi','mumbai','patna']
    while count<4:
        if count==1:
            ranum=randint(0,len(state_list)-1)
            global answer_state
            answer_state=state_list[ranum]
            global answer_capital

            answer_capital=capitals[ranum]

        else:
            ranum=randint(0,len(state_list)-1)
        
        answer_list.append(capitals[ranum])

        state_list.remove(state_list[ranum])
        capitals.remove(capitals[ranum])

        count+=1
    #shuffle the answer list
    shuffle(answer_list)

    #var for radio button
    global user_selection
    user_selection=StringVar()
    user_selection.set("0")
    
    #create a pass button
    pass_button=Button(state_capitals_frame,text=" >> " , font=("Helvetica",14),command=state_capitals).pack(pady=5)

    #create radio buttons

    radio1=Radiobutton(state_capitals_frame,text=answer_list[0],variable=user_selection,value='0',tristatevalue=4,bg="orange")
    radio2=Radiobutton(state_capitals_frame,text=answer_list[1],variable=user_selection,value='1',tristatevalue=4,bg="orange")
    radio3 = Radiobutton(state_capitals_frame, text=answer_list[2], variable=user_selection, value='2',tristatevalue=4,bg="orange")
    
    radio1.pack(pady=5)
    radio2.pack(pady=5)
    radio3.pack(pady=5)

    submit=Button(state_capitals_frame,text="Submit",command=capital_check).pack(pady=5)

    #response label
    global response_label
    response_label=Label(state_capitals_frame,text="",font=("Helvetica",15),bg="orange")
    response_label.pack(pady=5)
    # putting image on screen
    global state_path
    global img
    global label_img
    state_path="states/"+answer_state+".jpg"
    img=ImageTk.PhotoImage(Image.open(state_path))
    label_img=Label(state_capitals_frame,image=img).pack()

    
def capital_check():
    if answer_list[int(user_selection.get())]==answer_capital:
        response="Correct !! "
    else:
        response="Incorrect !! "
    answer_capital_copy=answer_capital
    state_capitals()
    response_label.config(text=response + answer_capital_copy + " was the right answer")

def hide_all_frames():
    #loop through and destroy children widgets in frames
    for widget in states_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    for widget in math_addition_frame.winfo_children():
        widget.destroy()

    # hiding frames
    states_frame.pack_forget()
    state_capitals_frame.pack_forget()
    math_addition_frame.pack_forget()

#creating math addition function
def add():
    hide_all_frames()
    math_addition_frame.pack(fill="both",expand=1)
    math_addition_label=Label(math_addition_frame,text="Additon Flashcard",font=("Helvetica",15)).pack(pady=10)

    #frame for displaying images
    pic_frame=Frame(math_addition_frame,height=500,width=500,bg="orange")
    pic_frame.pack()

    global num_1
    global num_2

    num_1=randint(1,10)
    num_2=randint(1,10)

    #path to image
    global path1
    global path2
    path1="numbers/"+str(num_1) + ".jpg"
    path2="numbers/"+str(num_2) + ".jpg"
    
    #images
    global img_1
    global img_2
    img_1=ImageTk.PhotoImage(Image.open(path1))
    img_2=ImageTk.PhotoImage(Image.open(path2))
    
    #labels
    global num_1_label
    global num_2_label
    num_1_label=Label(pic_frame,image=img_1,height=300,width=250).grid(row=0,column=0)
    num_2_label=Label(pic_frame,image=img_2,height=300,width=250).grid(row=0,column=2)
    sign_label = Label(pic_frame, text=" + ",font=("Helvetica",30),bg="orange").grid(row=0, column=1)

    #answer input box
    global answer_box
    answer_box=Entry(math_addition_frame,font=("Helvetica",20),bd=3)
    answer_box.pack(pady=30)

    submit_button=Button(math_addition_frame,text="submit",command=addition_check).pack(pady=15)
    global output_label
    output_label=Label(math_addition_frame,text="",font=("Helvetica",16),bg="orange")
    output_label.pack(pady=10)

    answer_box.focus_set()


def addition_check():
    ans=num_1+num_2
    if(str(ans)==str(answer_box.get())):
        response="Correct!! The Value of Sum was "+str(ans)
    else:
        response="Incorrect!! The Value of Sum was "+str(ans)
    
    add()
    output_label.config(text=response)




def event_bind(event):
    #checking if states_frame is packed on screen or not
    if  states_frame.winfo_manager():
        # calling the check answer function
        check_answer()
    if state_capitals_frame.winfo_manager():
        capital_check()
    if math_addition_frame.winfo_manager():
        addition_check()
    


#binding return key for submit
root.bind("<Return>", event_bind)

#creating menu
my_menu=Menu(root)
root.config(menu=my_menu)

#create geography menu items
states_menu=Menu(my_menu)
my_menu.add_cascade(label="Geography",menu=states_menu)
states_menu.add_command(label="States",command=states)
states_menu.add_separator()
states_menu.add_command(label="State Capitals",command=state_capitals)
states_menu.add_command(label="Exit",command=root.quit)

#creating math menu
math_menu=Menu(my_menu)
my_menu.add_cascade(label="Math",menu=math_menu)
math_menu.add_command(label="Addition",command=add)

#creating Frames
states_frame=Frame(root,height=700,width=700,bg="orange")
state_capitals_frame=Frame(root,height=700,width=700,bg="orange")
math_addition_frame=Frame(root,height=700,width=700,bg="orange")



root.mainloop()
