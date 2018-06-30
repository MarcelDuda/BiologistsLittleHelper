#!/usr/bin/env python

# Open a new Window with a button Tkinter
# You may use this for any type of coding, including for professional use
 

from tkinter import *
import functions
import children

welcomestring="Welcome to BiologistsLittleHelper"
welcomestring1="This program performs calculations you might be confronted with in the lab"


  


master = Tk()
master.geometry("800x500")
master.title("BiologistsLittleHelper")

w = Label(master, text=welcomestring)
w.place(relx=0.4, rely=0)

w = Label(master, text=welcomestring1)
w.place(relx=0.25, rely=0.1)


     
newwindow = Button(master, text="Concentration-\nVolume-\nCalculation", command=children.cvc,height = 5, width = 10)
newwindow.place(relx=0.4, rely=0.2)

newwindow = Button(master, text="Unit-\nConversion", command=children.uc,height = 5, width = 10)
newwindow.place(relx=0.6, rely=0.2)


master.mainloop()