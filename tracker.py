from ttkbootstrap.constants import *
from tkinter import *
import ttkbootstrap as tb
import sqlite3
from tkinter.messagebox import showerror
root=tb.Window(themename='darkly')
root.title("Expense Tracker GUI")
root.geometry("600x400")
itemVar=StringVar()
quantVar=IntVar()
costVar=IntVar()
quantVar.set(1)
comboVar=StringVar()
conn=sqlite3.connect('expense_book.db')
c=conn.cursor()
def deleteItem():
	comboValue=comboVar.get()
	try:
		c.execute(f"DELETE FROM expenses WHERE itemName='{comboValue}'")
		conn.commit()
	except Exception as e:
		showerror("Error","Enter correct value!")
	else:
		comboVar.set("")
		setBox()
		showTotal()
def setBox():
	values=[]
	d=c.execute("SELECT * FROM expenses")
	for row in d:
		values.append(row[0])
		combo['values']=values
def showItems():
	global combo
	top=Toplevel(root)
	top.geometry("500x350")
	top.title("All Items")
	tb.Label(top,text="All Items",font="arial 16 bold",bootstyle="light").pack()
	combo=tb.Combobox(top,textvariable=comboVar)
	combo.pack(padx=5,pady=5,ipadx=5,ipady=5)
	deleteBtn=tb.Button(top,text="Delete",bootstyle="danger",command=deleteItem)
	deleteBtn.pack(padx=5,pady=5,ipadx=5,ipady=5)
	setBox()
	top.mainloop()
def checkItem(item):
	d=c.execute("SELECT * FROM expenses")
	for row in d:
		if row[0]==item:
			return True
	return False
def showTotal():
	data=c.execute("SELECT * FROM expenses")
	cost=0
	for row in data:
		cost+=row[1]*row[2]
	label.config(text=f"Total Cost : ₹{cost}")
def addItem():
	try:
		item=itemVar.get()
		cost=costVar.get()
		quant=quantVar.get()
	except Exception as e:
		pass
	else:
		if(checkItem(item)==False):
			c.execute("INSERT INTO expenses VALUES (:itemName,:cost,:quantity)",
				{
				'itemName':item,
				'cost':cost,
				'quantity':quant

				})
		else:
			showerror("Error","Item Already in List!")
		showTotal()
		conn.commit()
	itemVar.set("")
	costVar.set("")
	quantVar.set("")
tb.Label(root,text="Item",font="arial 14",bootstyle="light").pack(pady=5,padx=5,anchor=NW)
tb.Entry(root,textvariable=itemVar,bootstyle="primary").pack(pady=5,anchor=NW,fill=X)
tb.Label(root,text="Cost",font="arial 14",bootstyle="light").pack(pady=5,padx=5,anchor=NW)
tb.Entry(root,textvariable=costVar,bootstyle="primary").pack(pady=5,anchor=NW,fill=X)
tb.Label(root,text="Quantity",font="arial 14",bootstyle="light").pack(pady=5,padx=5,anchor=NW)
tb.Entry(root,textvariable=quantVar,bootstyle="primary").pack(pady=5,anchor=NW,fill=X)
button=tb.Button(root,text="Add Item",bootstyle="info",command=addItem)
button.pack(anchor=NW,padx=5,pady=10,ipadx=5)
label=tb.Label(root,text="Total Cost : ",font="arial 14",bootstyle="light")
showTotal()
label.pack(pady=5,padx=5,anchor=NW)
menu=Menu(root)
menubar=Menu(menu,tearoff=False)
menubar.add_command(label="Show Items",command=showItems)
menu.add_cascade(label="File",menu=menubar)
root.config(menu=menu)
root.mainloop()
conn.close()