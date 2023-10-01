from tkinter import *
from random import randint
root=Tk()
root.title("Probability tester")
root.geometry("400x300")
Label(root,text="No.of rolls",font="arial 14").pack(anchor=W)
var1=StringVar()
Entry(root,textvariable=var1,font="arial 12").pack(anchor=W,pady=5,fill=X)
def roll():
  numbers=[]
  for i in range(int(var1.get())):
    numbers.append(randint(1,6))
  text=""
  for i in range(1,7):
    text+=f"No.of {i}'s' = {numbers.count(i)} ({round(numbers.count(i)/len(numbers)*100,2)}%)\n\n"
  top=Toplevel()
  top.title("Results")
  top.geometry("350x250")
  text_area=Text(top,font="arial 12")
  text_area.pack(fill=BOTH)
  text_area.insert(1.0,text)
  text_area.config(state=DISABLED)
  top.mainloop()
btn=Button(root,text="Roll",bg="blue",fg="white",font="arial 12 bold",command=roll)
btn.pack(fill=X,ipady=5,pady=5)
root.mainloop()