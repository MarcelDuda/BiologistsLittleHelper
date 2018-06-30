#!/usr/bin/env python

from tkinter import *
import functions

def cvc():
    cvc = Tk()
    cvc.geometry("600x600")
    cvc.title("Concentration-Volume-Calculation")
    label = Label(cvc, text="tdb")
    label.grid()
    Label(cvc, text="c1=").grid(row=0)
    Label(cvc, text="v1=").grid(row=1)
    Label(cvc, text="c2=").grid(row=2)
    Label(cvc, text="v2=").grid(row=3)
    
    c1 = Entry(cvc)
    v1 = Entry(cvc)
    c2 = Entry(cvc)
    v2 = Entry(cvc)
    
    c1.grid(row=0, column=1)
    v1.grid(row=1, column=1)
    c2.grid(row=2, column=1)
    v2.grid(row=3, column=1)
    
    Label(cvc, text="Result:").grid(row=6, column=0)
    result = Entry(cvc,width=50)
    result.grid(row=6,column=1)
    
    def fillresult(a):
        a.delete(0,END)
        y=functions.cvc_calc(c1.get(),v1.get(),c2.get(),v2.get())
        a.insert(INSERT,y)
    
    
    showresult = Button(cvc, text="Show", command=lambda:fillresult(result))
    showresult.grid(row=4, column=1)

    cvc.mainloop()
    
    
def uc():
    uc = Tk()
    uc.geometry("600x600")
    uc.title("Unit-Conversion")
    label = Label(uc, text="tdb")
    label.grid()
    
    si = Entry(uc)
    milli = Entry(uc)
    micro = Entry(uc)
    nano = Entry(uc)
    
    Label(uc, text="Convert from grams/litres/Molar:").grid(row=0)
    si.grid(row=1)
    Label(uc, text="Convert from  milli-grams/litres/Molar:").grid(row=2)
    milli.grid(row=3)
    Label(uc, text="Convert from micro-grams/litres/Molar:").grid(row=4)
    micro.grid(row=5)
    Label(uc, text="Convert from nano-grams/litres/Molar:").grid(row=6)
    nano.grid(row=7)
    
    def fillresult(a,b,c,d):
        if a!='':
            a1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[0]
            b1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[1]
            c1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[2]
            d1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[3]
            a.delete(0,END)
            b.delete(0,END)
            c.delete(0,END)
            d.delete(0,END)
            a.insert(INSERT,a1)
            b.insert(INSERT,b1)
            c.insert(INSERT,c1)
            d.insert(INSERT,d1)
            
        elif b!='':
            a1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[0]
            b1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[1]
            c1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[2]
            d1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[3]
            a.delete(0,END)
            c.delete(0,END)
            d.delete(0,END)
            b.delete(0,END)
            a.insert(INSERT,a1)
            b.insert(INSERT,b1)
            c.insert(INSERT,c1)
            d.insert(INSERT,d1)
            
        elif c!='':
            a1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[0]
            b1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[1]
            c1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[2]
            d1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[3]
            a.delete(0,END)
            c.delete(0,END)
            d.delete(0,END)
            b.delete(0,END)
            a.insert(INSERT,a1)
            b.insert(INSERT,b1)
            c.insert(INSERT,c1)
            d.insert(INSERT,d1)
            
        elif d!='':
            a1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[0]
            b1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[1]
            c1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[2]
            d1=functions.uc_calc(si.get(),milli.get(),micro.get(),nano.get())[3]
            a.delete(0,END)
            c.delete(0,END)
            d.delete(0,END)
            b.delete(0,END)
            a.insert(INSERT,a1)
            b.insert(INSERT,b1)
            c.insert(INSERT,c1)
            d.insert(INSERT,d1)
            
    def delete(a,b,c,d):
            a.delete(0,END)
            c.delete(0,END)
            d.delete(0,END)
            b.delete(0,END)
        

    result = Button(uc, text="Show", command=lambda:fillresult(si,milli,micro,nano))
    result.grid(row=5, column=1)
    
    clear=Button(uc, text="Clear",command=lambda:delete(si,milli,micro,nano))
    clear.grid(row=5, column=2)
    

    


    uc.mainloop()