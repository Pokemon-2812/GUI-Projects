from tkinter import *
from tkinter.simpledialog import askstring
import random
from datetime import date
from tkinter.filedialog import asksaveasfilename
from pathlib import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
root=tb.Window(themename="superhero")
order_no=0
name=""
def check_change():
	for key,value in item_checked.items():
		if value==1:
			if item_quantity[key].get()==0:
				quant_obj[key].set(1)
		elif value==0:
			quant_obj[key].set(0)
def add():
	global order_no,name
	order_no=random.randint(1000,9000)
	if name=="":
		name=askstring("Name","What is your name?")
	if name!=None:
		today=date.today()
		text="Order Number-"+str(order_no)+"\n"
		text+=f"Name-{name}\nDate-{today}\n"
		text+="-"*80+"\n"
		total=0
		for key,value in item_checked.items():
			if value.get()==1:
				if isinstance(item_quantity[key].get(), str):
					item_quantity[key].set(1)
				item_cost=int(cost[key])*int(item_quantity[key].get())
				text+=f"Food: {key},Quantity: {item_quantity[key].get()},Cost: {item_cost}\n"
				total+=item_cost
		text+="-"*80+"\n"
		text+=f"Total Cost:{total}\n"
		text+=f"Total Cost(GST Included):{total * 105/100}"
		text_area.config(state=NORMAL)
		text_area.delete(1.0,END)
		text_area.insert(1.0,text)
		text_area.config(state=DISABLED)

def save():
	file = asksaveasfilename(initialfile = f'bill{order_no}.txt',defaultextension=".txt",filetypes=[("Text Documents","*.txt")])
	if file!="":
		with open(file,'w') as f:
			f.write(text_area.get(1.0,END))
def reset():
	global name
	text_area.config(state=NORMAL)
	text_area.delete(1.0,END)
	text_area.config(state=DISABLED)
	for key,value in item_checked.items():
		value.set(0)
		item_quantity[key].set(0)
	name=""
def check_click(food):
	print(item_checked)
	if(item_checked[food]==0):
	    foods_obj[food].set(1)
root.geometry("1000x650")
root.title("Restaurant Management System")
foods=["Dosa","Idli","Pav","Aloo Parantha","Burger","Pizza"]
drinks=["Lassi","Shikanji","Pepsi","Coca-Cola","Red Bulls","Fanta"]
sweets=["Rasmalai","Rasgulla","Rasmulla","Jalebi","Gulab Jamun","Kheer"]
cost={}
foods_obj={}
quant_obj={}
drinks_obj={}
sweets_obj={}
for drink in drinks:
	cost[drink]=50
for sweet in sweets:
	cost[sweet]=75
for food in foods:
	cost[food]=120
tb.Label(root,text="Restaurant Management System",font="arial 22 bold",bootstyle="light").pack(fill=X)
#Food frame
left_frame=tb.Frame(root,bootstyle="primary")
left_frame.pack(side="left", fill="both", expand=True)
food_frame=tb.Frame(left_frame,bootstyle="secondary")
food_frame.pack(side=LEFT)
item_quantity={}
item_checked={}
tb.Label(food_frame,text="Meals",font="arial 18 bold",bootstyle="light").pack()
for food in foods:
    var=IntVar()
    var2=IntVar()
    checkbox=tb.Checkbutton(food_frame,text=food,variable=var,command=lambda:check_change())
    checkbox.pack(padx=14)
    entry=tb.Entry(food_frame,textvariable=var2)
    entry.pack()
    entry.bind('<Button-1>',lambda food:check_click(food))
    item_quantity[food]=var2.get()
    item_checked[food]=var.get()
    foods_obj[food]=var
    quant_obj[food]=var2
#Drinks Frame
drinks_frame=tb.Frame(left_frame,bootstyle="secondary")
drinks_frame.pack(side=LEFT)
tb.Label(drinks_frame,text="Drinks",font="arial 18 bold",bootstyle="light").pack()
for drink in drinks:
    var=IntVar()
    var2=IntVar()
    checkbox=tb.Checkbutton(drinks_frame,text=drink,variable=var,command=lambda:check_change())
    checkbox.pack(padx=14)
    entry=tb.Entry(drinks_frame,textvariable=var2)
    entry.pack()
    entry.bind('<Button-1>',lambda drink:check_click(drink))
    item_quantity[drink]=var2.get()
    item_checked[drink]=var.get()
    foods_obj[drink]=var
    quant_obj[drink]=var2
#Sweets Frame
sweets_frame=tb.Frame(left_frame,bootstyle="secondary")
sweets_frame.pack(side=LEFT)
tb.Label(sweets_frame,text="Sweets",font="arial 18 bold",bootstyle="light").pack()
for sweet in sweets:
    var=IntVar()
    var2=IntVar()
    checkbox=tb.Checkbutton(sweets_frame,text=sweet,variable=var,command=lambda:check_change())
    checkbox.pack(padx=14)
    entry=tb.Entry(sweets_frame,textvariable=var2)
    entry.pack()
    entry.bind('<Button-1>',lambda sweet:check_click(sweet))
    item_quantity[sweet]=var2.get()
    item_checked[sweet]=var.get()
    foods_obj[sweet]=var
    quant_obj[sweet]=var2
# #Right Frame
bill_frame=tb.Frame(root,bootstyle="primary")
bill_frame.pack(side="right",fill="both",expand=True)
scrollbar=tb.Scrollbar(bill_frame)
scrollbar.pack(fill=Y,side=RIGHT)
text_area=Text(bill_frame,yscrollcommand=scrollbar.set)
text_area.pack(fill=Y)
scrollbar.config(command=text_area.yview)
text_area.config(state=DISABLED)
btn_frame=tb.Frame(root,bootstyle="primary")
btn_frame.pack(side=BOTTOM)
reset_btn=tb.Button(btn_frame,text="Reset",command=reset)
reset_btn.pack(side="left")
add_btn=tb.Button(btn_frame,text="Add",command=add)
add_btn.pack(side="left")
save_btn=tb.Button(btn_frame,text="Save",command=save)
save_btn.pack(side="left")
root.mainloop()