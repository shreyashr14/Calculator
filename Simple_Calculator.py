import math
from tkinter import *
import os
os.system('clear')
root = Tk()
root.title('Simple Calculator')

e=Entry(root, width= 35,borderwidth=5 )
e.grid(row=0,column=0,columnspan=5, padx=10,pady=30)

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    global math
    math = "Addition"
    f_num = float(first_number)
    e.delete(0,END)

def button_subtract():
    first_number=e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = float(first_number)
    e.delete(0,END)

def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = float(first_number)
    e.delete(0,END)

def button_divide():
    first_number=e.get()
    global f_num
    global math
    math = "Division"
    f_num = float(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if math=="Addition":
        e.insert(0,f_num + float(second_number))
    if math=="Subtraction":
        e.insert(0,f_num - float(second_number))
    if math=="Multiplication":
        e.insert(0,f_num * float(second_number))
    if math=="Division":
        infi = float(second_number)
        if infi==0:
            e.insert(0, "Not possible to divide by zero")
        else:
            e.insert(0,f_num / int(second_number))
    

mylabel1 = Button(root, text ="1",width=5, command=lambda : button_click(1))
mylabel1.grid(row=1,column=0,padx=10,pady=10)

mylabel2 = Button(root, text ="2",width=5, command=lambda : button_click(2))
mylabel2.grid(row=1,column=1,padx=10,pady=10)

mylabel3 = Button(root, text ="3",width=5, command=lambda : button_click(3))
mylabel3.grid(row=1,column=2,padx=10,pady=10)

mylabel_1= Button(root, text ="-",width=5, command=button_subtract)
mylabel_1.grid(row=1,column=3,padx=10,pady=10)

mylabel4 = Button(root, text ="4",width=5, command=lambda : button_click(4))
mylabel4.grid(row=2,column=0,padx=10,pady=10)

mylabel5= Button(root, text ="5",width=5, command=lambda : button_click(5))
mylabel5.grid(row=2,column=1,padx=10,pady=10)

mylabel6= Button(root, text ="6",width=5, command=lambda : button_click(6))
mylabel6.grid(row=2,column=2,padx=10,pady=10)

mylabel_add= Button(root, text ="+",width=5, command=button_add)
mylabel_add.grid(row=2,column=3,padx=10,pady=10)

mylabel7= Button(root, text ="7",width=5, command=lambda : button_click(7))
mylabel7.grid(row=3,column=0,padx=10,pady=10)

mylabel8= Button(root, text ="8",width=5, command=lambda : button_click(8))
mylabel8.grid(row=3,column=1,padx=10,pady=10)

mylabel9= Button(root, text ="9",width=5, command=lambda : button_click(9))
mylabel9.grid(row=3,column=2,padx=10,pady=10)

mylabel_mul= Button(root, text ="x",width=5, command=button_multiply)
mylabel_mul.grid(row=3,column=3,padx=10,pady=10)

mylabel_dec= Button(root, text =".",width=5, command=lambda : button_click("."))
mylabel_dec.grid(row=4,column=0,padx=10,pady=10)

mylabel0= Button(root, text ="0",width=5, command=lambda : button_click(0))
mylabel0.grid(row=4,column=1,padx=10,pady=10)

mylabel_equal= Button(root, text ="=",width=5, command=button_equal)
mylabel_equal.grid(row=4,column=2,padx=10,pady=10)

mylabel_divide= Button(root, text ="/",width=5, command=button_divide)
mylabel_divide.grid(row=4,column=3,padx=10,pady=10)

mylabel_clear= Button(root, text ="Clear",width=5, command=button_clear)
mylabel_clear.grid(row=5,column=0,padx=10,pady=10)



root.mainloop()