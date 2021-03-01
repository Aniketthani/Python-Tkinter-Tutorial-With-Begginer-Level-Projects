from tkinter import * 
import sqlite3

root=Tk()
root.title("Databases")
root.geometry("500x500")

#Databases

#create a database or connect to one

conn=sqlite3.connect("address_book.db")


#create a cursor, it will be used to give sql commands in the database

c=conn.cursor()

#create table

#c.execute("CREATE TABLE address (first_name text , last_name text, address text , city text ,state text , zip integer)")

def action():
    #connect to database
    conn=sqlite3.connect("address_book.db")

    #create a cursor
    c=conn.cursor()

    #execute command
    c.execute("INSERT INTO address VALUES(:fname,:lname,:address,:city,:state,:zipcode)",
    
    {
        'fname':f_name.get(),'lname':l_name.get(),'address':address.get(),'city':city.get(),'state':state.get(),'zipcode':zipcode.get()
    } )

    #commit change
    conn.commit()

    #close connection
    conn.close()

    #empty the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def show_records():
    #connect to database
    conn=sqlite3.connect("address_book.db")

    #create a cursor
    c=conn.cursor()

    #execute command
    c.execute("SELECT *,oid FROM address")
    records=c.fetchall()
    #print(records)
    print_records=""
    for record in records:
        print_records+=str(record) + "\n"
    label=Label(root,text=print_records)
    label.grid(row=11,column=0,columnspan=2)

    #commit change
    conn.commit()

    #close connection
    conn.close()


# delete record function
def delete():
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor()
    c.execute("DELETE FROM address WHERE oid="+ select_record_box.get())
    select_record_box.delete(0,END)
    
    conn.commit()
    conn.close()
#edit function 

def edit():
    global editor
    editor=Tk()
    editor.title("Update Record")
    editor.geometry("400x300")

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #create text boxes
    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=30,pady=(20,0))
    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1)
    city_editor=Entry(editor,width=30)
    city_editor.grid(row=3,column=1)
    state_editor=Entry(editor,width=30)
    state_editor.grid(row=4,column=1)
    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1)

    # create label for text boxes

    f_name_label_editor=Label(editor,text="First Name :")
    f_name_label_editor.grid(row=0,column=0,pady=(20,0))
    l_name_label_editor=Label(editor,text="Last Name :")
    l_name_label_editor.grid(row=1,column=0)
    address_label_editor=Label(editor,text="Address :")
    address_label_editor.grid(row=2,column=0)
    city_label_editor=Label(editor,text="City :")
    city_label_editor.grid(row=3,column=0)
    state_label_editor=Label(editor,text="State :")
    state_label_editor.grid(row=4,column=0)
    zipcode_label_editor=Label(editor,text="Zipcode :")
    zipcode_label_editor.grid(row=5,column=0)

    #save button for saving edited record
    save=Button(editor,text="Save",command=update)
    save.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=125)

    #connect to database
    conn=sqlite3.connect("address_book.db")

    #create a cursor
    c=conn.cursor()

    #execute command
    record_id=select_record_box.get()
    c.execute("SELECT * FROM address WHERE oid= "+ record_id)
    records=c.fetchall()

    f_name_editor.insert(0,records[0][0])
    l_name_editor.insert(0,records[0][1])
    address_editor.insert(0,records[0][2])
    city_editor.insert(0,records[0][3])
    state_editor.insert(0,records[0][4])
    zipcode_editor.insert(0,records[0][5])

    conn.commit()
    conn.close()
    



def update():
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor()
    c.execute("UPDATE address SET first_name=:first, last_name=:last,address=:address,city=:city,state=:state,zip=:zipcode WHERE oid=:oid",
    {
        "first":f_name_editor.get(),
        "last":l_name_editor.get(),
        "address":address_editor.get(),
        "city":city_editor.get(),
        "state":state_editor.get(),
        "zipcode":zipcode_editor.get(),
        'oid':select_record_box.get()
    }
    )


    conn.commit()
    conn.close()

    editor.destroy()

    


#create text boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=30,pady=(20,0))
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)
address=Entry(root,width=30)
address.grid(row=2,column=1)
city=Entry(root,width=30)
city.grid(row=3,column=1)
state=Entry(root,width=30)
state.grid(row=4,column=1)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

select_record_box=Entry(root,width=30)
select_record_box.grid(row=8,column=1)

# create label for text boxes

f_name_label=Label(root,text="First Name :")
f_name_label.grid(row=0,column=0,pady=(20,0))
l_name_label=Label(root,text="Last Name :")
l_name_label.grid(row=1,column=0)
address_label=Label(root,text="Address :")
address_label.grid(row=2,column=0)
city_label=Label(root,text="City :")
city_label.grid(row=3,column=0)
state_label=Label(root,text="State :")
state_label.grid(row=4,column=0)
zipcode_label=Label(root,text="Zipcode :")
zipcode_label.grid(row=5,column=0)
select_record_label=Label(root,text="Select Record With OID :")
select_record_label.grid(row=8,column=0)
#submit button
submit=Button(root,text="Submit",command=action)
submit.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=125)

#show records button
show_records_button=Button(root,text="Show Records",command=show_records)
show_records_button.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#delete record button
delete_record=Button(root,text="Delete Record",command=delete)
delete_record.grid(row=9,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

#Edit record button
edit_record=Button(root,text="Edit Record",command=edit)
edit_record.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=108)

#commit changes

conn.commit()

#close connection

conn.close()

root.mainloop()