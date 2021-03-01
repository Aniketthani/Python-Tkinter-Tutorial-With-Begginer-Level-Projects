from tkinter import *
from bs4 import BeautifulSoup
import urllib
from urllib import request
from datetime import datetime


def update():
    global previous

    page=urllib.request.urlopen("https://www.coindesk.com/price/bitcoin")
    html=BeautifulSoup(page,"html.parser")
    price_large=html.find(class_="price-large")
    price_large=str(price_large)
    price_large=price_large[54:63]
    
    label.config(text=f'${price_large}')

    date=datetime.now()
    date=date.strftime("%H:%M:%S %p")

    updated_label.config(text=f'Last Updated at {date}')

    root.after(10000,update)


root=Tk()
root.geometry("300x150")
root.config(bg="black")

label=Label(root,text="Test",font=("Arial",40),fg="green",bg="black")
label.pack(pady=10)
updated_label=Label(root,text="test",font=("Helvetica",15),bg="black",fg="green")
updated_label.pack(anchor="se")

update()

root.mainloop()