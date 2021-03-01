from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Multiple Entry boxes and their management")

my_inputs=[]
def something():
    string=""
    for entry in my_inputs:
        string=string+entry.get()+"\n"
    label=Label(root,text=string)
    label.grid(row=3,column=2)
        





for i in range(5):
    input=Entry(root)
    input.grid(row=0,column=i)
    my_inputs.append(input)

button=Button(root,text="submit",command=something)
button.grid(row=2,column=2)



root.mainloop()