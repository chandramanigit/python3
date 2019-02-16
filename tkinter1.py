from tkinter import *

window=Tk()

def converter():
    g=float(e2_value.get())*1000
    p=float(e2_value.get())*2.20462
    o=float(e2_value.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END,g)
    t2.delete("1.0", END)
    t2.insert(END,p)
    t3.delete("1.0", END)
    t3.insert(END,o)

l1=Label(window,text="Enter Kg")
l1.grid(row=0 , column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=2)

b1=Button(window,text="Convert to Grams,Pounds,Ounces",command=converter)
b1.grid(row=0,column=3)

t1=Text(window,height=1,width=10)
t1.grid(row=1,column=2)

t1_l=Label(window,text="Grams=")
t1_l.grid(row=1,column=1)

t2=Text(window,height=1,width=10)
t2.grid(row=1,column=4)

t2_l=Label(window,text="Punds=")
t2_l.grid(row=1,column=3)

t3=Text(window,height=1,width=10)
t3.grid(row=1,column=6)

t3_l=Label(window,text="Ounces=")
t3_l.grid(row=1,column=5)

window.mainloop()



"""
def km_to_mile():

    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)

window=Tk()
b1=Button(window,text="Kg",command=km_to_mile)
#b1.pack()
b1.grid(row=0 ,column=0)

e2=Label(window,text="mykg")
e2.grid(row=0,column=0)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=1,column=1)

t1=Text(window,height=1 , width=10)
t1.grid(row=1,column=2)
window.mainloop()
"""
