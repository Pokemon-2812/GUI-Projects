from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
root=tb.Window(themename='darkly')
root.iconbitmap('cal_ico.ico')
style=tb.Style()
def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=='=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())
            scvalue.set(value)
        else:
            try:
                value=eval(screen.get())
            except Exception as e :
                print("Entered a wrong expression.")
            else:
                scvalue.set(value)
    elif text=='C':
        scvalue.set("")
    else:
        scvalue.set(scvalue.get()+str(text))
        screen.update()
root.geometry("550x700")
root.title("Calculator")
scvalue=StringVar()
scvalue.set("")
screen=tb.Entry(root,textvariable=scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx=8,pady=12)
num=1
def create_frame():
    global f
    f=tb.Frame(root)
    f.pack()
def create_button(text):
    b=tb.Button(f,text=text,bootstyle='primary')
    b.pack(side=LEFT,ipadx=5,ipady=5,padx=5,pady=5)
    b.bind("<Button-1>",click)
for i in range(3):
    create_frame()
    for i in range(3):
        create_button(num)
        num+=1
create_frame()
buttons=['0','=','*']
for text in buttons:
    create_button(text)
create_frame()
buttons=['+','-','/']
for text in buttons:
    create_button(text)
create_frame()
buttons=['%','.','C']
for text in buttons:
    create_button(text)
create_frame()
buttons=['(',')','00']
for text in buttons:
    create_button(text)
style.configure('primary.TButton', font='-size 15',width=8,height=4)
root.mainloop()

