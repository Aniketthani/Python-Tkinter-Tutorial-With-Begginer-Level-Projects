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

c.execute("CREATE TABLE address (first_name text , last_name text, address text , city text ,state text , zip integer)")

#commit changes

conn.commit()

#close connection

conn.close()

root.mainloop()