#!/usr/bin/env p+----ython3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 16:37:22 2019

@author: kiran
"""

from tkinter import *
from math import *

x = []
final=[]

def click_1():
    a = '1'
    x.append(a)
    print(x)
def click_2():
    a = '2'
    x.append(a)
    print(x)
def click_3():
    a = '3'
    x.append(a)
    print(x)
def click_4():
    a = '4'
    x.append(a)
    print(x)
def click_5():
    a = '5'
    x.append(a)
    print(x)
def click_6():
    a = '6'
    x.append(a)
    print(x)
def click_7():
    a = '7'
    x.append(a)
    print(x)
def click_8():
    a = '8'
    x.append(a)
    print(x)
def click_9():
    a = '8'
    x.append(a)
    print(x)
def click_0():
    
    a = '0'
    x.append(a)
def click_Plus():
    if len(x) == 0:
        if len(final) == 0:
            print("invalid entry")
    else:
        str1 = ''.join(str(e) for e in x)
        first = int(str1)
        x.clear()
        final.append(first)
        sy = "+"
        final.append(sy)
def click_Minus():
    if len(x) == 0:
        if len(final) == 0:
            print("invalid entry")  
    else:
        str1 = ''.join(str(e) for e in x)
        first = int(str1)
        x.clear()
        final.append(first)
def click_Mul():
    if len(x) == 0:
        if len(final) == 0:
            print("invalid entry")  
    else:
        str1 = ''.join(str(e) for e in x)
        first = int(str1)
        x.clear()
        final.append(first)
        sy = "*"
        final.append(sy)
def click_Div():
    if len(x) == 0:
        if len(final) == 0:
            print("invalid entry")  
    else:
        str1 = ''.join(str(e) for e in x)
        first = int(str1)
        x.clear()
        final.append(first)
        sy = "/"
        final.append(sy)
def click_Percent():

    if len(x) == 0:
        if len(final) == 0:
            print("invalid entry")  
    else:
        str1 = ''.join(str(e) for e in x)
        first = int(str1)
        x.clear()
        final.append(first)
        sy ="%"
        final.append(sy)
    print(x)
def click_Dot():
        str1 = ''.join(str(e) for e in x)
        first = str1 + '.'
        x.append(first)
def click_Square_R():
    if len(x) != 0:
        print("Invalid Operation")
    else:
        if len(x) == 0:
            if len(final) == 0:
                r = '√'
                final.append(r)
def click_Square():
    if len(x) == 0:
        if len(final) == 0:
            print("invalid entry")  
    else:
        str1 = ''.join(str(e) for e in x)
        first = int(str1)
        x.clear()
        final.append(first)
        sy ="x²"
        final.append(sy)
    print(x)
def click_Pi():
    a = '3.14'
    final.append(a)
    print(x)
def click_Open():
    if len(x) == 0:
            ob = "("
            final.append(ob)
    else:
        str1 = ''.join(str(e) for e in x)
        first = int(str1)
        x.clear()
        final.append(first)

    print(x)
def click_close():
    if len(x) == 0:
            ob = ")"
            final.append(ob)
    else:
        str1 = ''.join(str(e) for e in x)
        first = int(str1)
        x.clear()
        final.append(first)
    print(x)
def clear():
    final.clear()
    print(final)
def delete():
    if len(final) == 0:
        print("No more value to Delete")
    else:
        final.pop()
    print(final)
def equal():
    if len(x) == 0:
        if len(final) == 0:
            print("invalid entry")  
    else:
        str1 = ''.join(str(e) for e in x)
        first = int(str1)
        x.clear()
        final.append(first)
    while len(final) >= 2:
            if final[1] == "+":
                add = int(final [0]) + int(final[2])
                final.clear()
                final.append(add)
            elif final[1] == "-":
                sub = int(final [0]) - int(final[2])
                final.clear()
                final.append(sub)
            elif final[1] == "*":
                mul = int(final [0]) * int(final[2])
                final.clear()
                final.append(sub)
            elif final[1] == "/":
                div = int(final [0]) / int(final[2])
                final.clear()
                final.append(div)
            elif final[1] == "(":
                mul = int(final [0]) * int(final[2])
                final.clear()
                final.append(sub)
            elif final[1] == ")":
                mul = int(final [0]) * int(final[2])
                final.clear()
                final.append(sub)
            elif final[1] == "x²":
                mul = int(final [0]) * int(final[0])
                final.clear()
                final.append(sub)
    print(x)
    print(final)
root = Tk()
menu = Menu(root, fg="white", bg="black")
root.config(menu=menu)
FileMenu = Menu(menu,fg="white", bg="black")
menu.add_command(label="Exit",command=root.destroy)
fnt=("Arial",'10')
header = Label(root, text="Kiran Calculator",bg="White",fg="black",font=fnt)
header.grid(row=0,column=0)
inputs = Entry(root)
inputs.grid(row=1,column=0)
Label2 = Label(root, text="")
Label3 = Label(root, text="")
Label4 = Label(root, text="")
button1 = Button(root, text= "+", bg = "AliceBlue",command=click_Plus)
button1.grid(row=5,column=4)
button2 = Button(root, text= "-", bg = "AliceBlue",command=click_Minus)
button2.grid(row=4,column=4)
button3 = Button(root, text= "*", bg = "AliceBlue",command=click_Mul)
button3.grid(row=3,column=4)
button4 = Button(root, text= "/", bg = "AliceBlue",command=click_Div)
button4.grid(row=2,column=4)
button5 = Button(root, text= "%", bg = "AliceBlue",command=click_Percent)
button5.grid(row=5,column=3)
button6 = Button(root, text= "(", bg = "AliceBlue",command=click_Open)
button6.grid(row=3,column=5)
button7 = Button(root, text= ")", bg = "AliceBlue",command=click_close)
button7.grid(row=3,column=6)
button8 = Button(root, text= "=", bg = "AliceBlue",command=equal)
button8.grid(row=5,column=6)
button9 = Button(root, text= "√", bg = "AliceBlue",command=click_Square_R)
button9.grid(row=4,column=6)
button10 = Button(root, text= "Clr", bg = "AliceBlue",command=clear)
button10.grid(row=2,column=6)
button12 = Button(root, text= "Del", bg = "AliceBlue",command=delete)
button12.grid(row=2,column=5)
button13 = Button(root, text= "1", bg = "AliceBlue",command=click_1)
button13.grid(row=4,column=1)
button14 = Button(root, text= "2", bg = "AliceBlue",command=click_2)
button14.grid(row=4,column=2)
button15 = Button(root, text= "3", bg = "AliceBlue",command=click_3)
button15.grid(row=4,column=3)
button16 = Button(root, text= "4", bg = "AliceBlue",command=click_4)
button16.grid(row=3,column=1)
button17 = Button(root, text= "5", bg = "AliceBlue",command=click_5)
button17.grid(row=3,column=2)
button18 = Button(root, text= "6", bg = "AliceBlue",command=click_6)
button18.grid(row=3,column=3)
button19 = Button(root, text= "7", bg = "AliceBlue",command=click_7)
button19.grid(row=2,column=1)
button20 = Button(root, text= "8", bg = "AliceBlue",command=click_8)
button20.grid(row=2,column=2)
button21 = Button(root, text= "9", bg = "AliceBlue",command=click_9)
button21.grid(row=2,column=3)
button22 = Button(root, text= "0", bg = "AliceBlue",command=click_0)
button22.grid(row=5,column=1)
button23 = Button(root, text= "x²", bg = "AliceBlue",command=click_Square)
button23.grid(row=4,column=5)
button24 = Button(root, text= ".", bg = "AliceBlue",command=click_Dot)
button24.grid(row=5,column=2)
button25 = Button(root, text= "Pi", bg = "AliceBlue",command=click_Pi)
button25.grid(row=5,column=5)

root.mainloop()


