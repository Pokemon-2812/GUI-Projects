from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
root=tb.Window(themename="darkly")
root.title("HCF and LCM")
root.geometry("450x400")
style=tb.Style()
var1=StringVar()
var2=StringVar()
var3=StringVar()
def HCF():
    num1=int(var1.get())
    num2=int(var2.get())
    numbers=[num1,num2]
    dividend=max(numbers)
    divisor=min(numbers)
    while True:
        if(dividend%divisor==0):
            hcf=divisor
            return hcf
            break
        temp=dividend
        dividend=divisor
        divisor=temp%divisor
def LCM():
    num1=int(var1.get())
    num2=int(var2.get())
    lcm=(num1*num2)/HCF()
    return lcm
def write_hcf():
    var3.set(str(HCF()))
def write_lcm():
    var3.set(str(LCM()))
tb.Label(text="Number1",font="arial 13").pack(anchor=W,pady=5)
tb.Entry(textvariable=var1,font="arial 12").pack(fill=X,ipady=5,pady=5)
tb.Label(text="Number2",font="arial 13").pack(anchor=W,pady=5)
tb.Entry(textvariable=var2,font="arial 12").pack(fill=X,ipady=5,pady=5)
tb.Label(text="Result",font="arial 13").pack(anchor=W,pady=5)
tb.Entry(textvariable=var3,font="arial 12").pack(fill=X,ipady=5,pady=5)
btn=tb.Button(text="HCF",bootstyle="success",command=write_hcf)
btn.pack(fill=X,ipady=5,pady=5)
btn2=tb.Button(text="LCM",bootstyle="primary",command=write_lcm)
btn2.pack(fill=X,ipady=5,pady=5)
style.configure('TButton',font="arial 12")
root.mainloop()
