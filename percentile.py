from tkinter import *
from tkinter.messagebox import showinfo
root=Tk()
root.geometry("400x300")
root.title("Percentile Calculator")
var1=StringVar()
var2=StringVar()
var3=StringVar()
def calculate():
	try:
		percentile=round((int(var2.get())-int(var1.get()))/int(var2.get())*100,2)
		var3.set(f"{percentile}%")
	except Exception as e:
		showinfo("Error","Please enter numbers!")
Label(root,text="Rank",font="arial 16").pack(anchor=W)
Entry(root,textvariable=var1,font="arial 12").pack(ipady=5,fill=X,pady=5)
Label(root,text="Total Participants",font="arial 16").pack(anchor=W)
Entry(root,textvariable=var2,font="arial 12").pack(ipady=5,fill=X,pady=5)
Label(root,text="Percentile",font="arial 16").pack(anchor=W)
entry=Entry(root,textvariable=var3,font="arial 12")
entry.pack(ipady=5,fill=X,pady=5)
btn=Button(root,text="Calculate",font="arial 12 bold",bg="blue",fg="white",command=calculate)
btn.pack(fill=X,ipady=6,pady=5)
root.mainloop()