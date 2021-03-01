from tkinter import *
import numpy as np
import random
import matplotlib.pyplot as plt

root=Tk()
root.title("Plots")
root.geometry("400x400")

def graph():
    house_prices=np.random.normal(200000,25000,5000)
    plt.hist(house_prices)
    plt.show()

button=Button(root,text="Plot Graph",command=graph)
button.pack()
root.mainloop()