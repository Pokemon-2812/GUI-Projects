from tkinter import *
import json
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter.messagebox import showerror
values=[]
def reset():
    with open('addresses.json','r+') as f:
        f.seek(0)
        f.truncate()
    cb['values']=[]
    set_empty()
def set_empty():
    var1.set("")
    var2.set("")
    var3.set("")
def add():
    global values,addresses
    if var1.get() not in values:
        if var1.get()!="" and len(var2.get())==10 and var3.get()!="":
            address_obj={"name":var1.get(),"phone number":var2.get(),"address":var3.get()}
            addresses.append(address_obj)
            with open('addresses.json','w') as f:
                json.dump(addresses,f)
            values=[]
            for addr in addresses:
                values.append(addr['name'])
            cb['values']=values
            set_empty()
    else:
        showerror("Error","Enter correct details!")
def delete():
    global values,addresses
    name=var4.get()
    for ad in addresses:
        if name==ad['name']:
            addresses.remove(ad)
    with open('addresses.json','w') as f:
        json.dump(addresses,f)
    values=[]
    for addr in addresses:
        values.append(addr['name'])
    cb['values']=values
    var4.set("")
def view():
    global addresses
    name=var4.get()
    for ad in addresses:
        if name==ad['name']:
            view_ad=ad
    try:
        var1.set(name)
        var2.set(view_ad['phone number'])
        var3.set(view_ad['address'])
    except Exception as e:
        pass
root=tb.Window(themename='superhero')
root.title('Address Book')
root.geometry("700x500")
style=tb.Style()
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
lbl1=tb.Label(root,text="Name",font="arial 14 bold",bootstyle='light')
lbl1.pack(pady=5,padx=10,anchor=NW)
entry1=tb.Entry(root,textvariable=var1)
entry1.pack(pady=5,fill=X)
lbl2=tb.Label(root,text="Phone Number",font="arial 14 bold",bootstyle='light')
lbl2.pack(pady=5,padx=10,anchor=NW)
entry2=tb.Entry(root,textvariable=var2)
entry2.pack(pady=5,fill=X)
lbl3=tb.Label(root,text="Address",font="arial 14 bold",bootstyle='light')
lbl3.pack(pady=5,padx=10,anchor=NW)
entry3=tb.Entry(root,textvariable=var3)
entry3.pack(pady=5,fill=X)
lbl4=tb.Label(root,text="All Address",font="arial 14 bold")
lbl4.pack(pady=5,padx=10,anchor=NW)
cb=tb.Combobox(root,state="readonly",textvariable=var4)
cb.pack(pady=5,fill=X)
try:
    with open('addresses.json','r') as f:
        addresses=json.load(f)
except Exception as e:
    with open('addresses.json','w') as f:
        json.dump([],f)
    addresses=[]
for address in addresses:
    values.append(address['name'])
cb['values']=values
b1=tb.Button(root,text="Add",bootstyle="primary",command=add)
b1.pack(side=LEFT,padx=5,ipadx=5,ipady=5)
b2=tb.Button(root,text="Delete",bootstyle="success",command=delete)
b2.pack(side=LEFT,padx=5,ipadx=5,ipady=5)
b3=tb.Button(root,text="Reset",bootstyle="warning",command=reset)
b3.pack(side=LEFT,padx=5,ipadx=5,ipady=5)
b4=tb.Button(root,text="View",bootstyle="danger",command=view)
b4.pack(side=LEFT,padx=5,ipadx=5,ipady=5)
style.configure('TButton', font='-size 12',width=4,height=2)
root.mainloop()