from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()

root.title("Simple Currency Converter By Aniket Thani")
root.geometry("500x500")
root.config(bg="#db1651")

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("Warning!","You Didn't Filled All Fields")
    else:
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        my_notebook.tab(1,state="normal")

        #change tab fields
        amount_label.config(text=f"Amount of {home_entry.get()} To Convert To {conversion_entry.get()}")
        converted_label.config(text=f"Equals This Many{conversion_entry.get()}")
        convert_button.config(text=f"Convert from {home_entry.get()}")
def unlock():
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")

    my_notebook.tab(1,state="disabled")
def convert():
    
    #clear converted entry box
    converted_entry.config(state=NORMAL)
    converted_entry.delete(0,END)

    #convert
    conversion=float(rate_entry.get()) * float(amount_entry.get())
    #convert to two decimal places
    conversion=round(conversion,2)
    #add commas
    conversion="{:,}".format(conversion)


    #update entry box
    converted_entry.insert(0,conversion)
    converted_entry.config(state="readonly")


def clear():
    amount_entry.delete(0,END)
    converted_entry.config(state=NORMAL)
    converted_entry.delete(0,END)
    converted_entry.config(state="readonly")

#create Tabs
my_notebook=ttk.Notebook(root)

my_notebook.pack(pady=5)



#create Frames
currency_frame=Frame(my_notebook,width=480,height=480,bg="#db1651")
conversion_frame=Frame(my_notebook,width=480,height=480,bg="#db1651")

#currency_frame.pack(fill=BOTH,expand=1)
#conversion_frame.pack(fill=BOTH,expand=1)

#add Tabs
my_notebook.add(currency_frame,text="Currencies")
my_notebook.add(conversion_frame,text="Convert")

#disable second tab
my_notebook.tab(1,state="disabled")


##currency stuff
home=LabelFrame(currency_frame,text="Your Home Currency",bg="#db1651")
home.pack(pady=20)

#home currency entry box
home_entry=Entry(home,font=("Arial",25))
home_entry.pack(pady=10,padx=10)

#conversion currency frame
conversion=LabelFrame(currency_frame,text="Conversion Currency",bg="#db1651")
conversion.pack(pady=20)

#convert_to label
conversion_label=Label(conversion,text="Currency To Convert To")
conversion_label.pack(pady=10)

#conversion entry
conversion_entry=Entry(conversion,font=("Arial",25))
conversion_entry.pack(pady=10,padx=10)

#rate label
rate_label=Label(conversion,text="Currency Conversion Rate")
rate_label.pack(pady=10)

#rate entry
rate_entry=Entry(conversion,font=("Arial",25))
rate_entry.pack(pady=10,padx=10)

#Button Frame
button_frame=Frame(currency_frame,bg="#db1651")
button_frame.pack(pady=20)

#buttons

lock_button=Button(button_frame,text="Lock",command=lock)
lock_button.grid(row=0,column=0,padx=10)

unlock_button=Button(button_frame,text="Unlock",command=unlock)
unlock_button.grid(row=0,column=1,padx=10)

##Conversion Stuff

amount_label=LabelFrame(conversion_frame,text="Amount to Convert",bg="#db1651")
amount_label.pack(pady=20)

# entry box for Amount
amount_entry=Entry(amount_label,font=("Arial",25))
amount_entry.pack(pady=10,padx=10)

#Convert Button
convert_button=Button(amount_label,text="Convert",command=convert)
convert_button.pack(pady=20)

#Equals Frame
converted_label=LabelFrame(conversion_frame,text="Converted Currency",bg="#db1651")
converted_label.pack(pady=20)

#converted entry
converted_entry=Entry(converted_label,font=("Helvetica",24),bd=0,state="readonly")
converted_entry.pack(pady=10,padx=10)

#clear button
clear_button=Button(conversion_frame,text="Clear",command=clear)
clear_button.pack(pady=20)

#fake label for spacing
spacer=Label(conversion_frame,text="",width=70,bg="#db1651")
spacer.pack()

root.mainloop()