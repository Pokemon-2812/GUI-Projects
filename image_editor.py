#Importing the modules
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image,ImageTk,ImageFilter,ImageEnhance
import ttkbootstrap as tb
from ttkbootstrap.constants import *
root=tb.Window(themename='superhero')
root.title("Image Editor")
root.geometry("1350x675")
style=tb.Style()
#These are the variables for CheckButton and Entries
var1=IntVar()
var2=StringVar()
var3=StringVar()
var2.set("1.0")
var3.set("0,0,0,0")
fil="apple.jpg"
img1=Image.open(fil)
#the width and height of the image
width,height=img1.size
img2=ImageTk.PhotoImage(img1)
f=Frame(root)
f.pack(anchor=NW,pady=10)
#Our image
lbl=tb.Label(f,image=img2)
lbl.pack(side=LEFT)
#A message
t="*The Image will remain in its original or applied size\nIt is resized to make it fit inside the window."
tb.Label(f,font="lucida 13 italic",text=t,bootstyle="info").pack(side=LEFT)
#Our labels for the different values
f1=tb.Frame(root)
f1.pack(anchor=NW,pady=10)
lbl2=tb.Label(f1,text="Width",font="lucida 13",bootstyle="light").pack(side=LEFT,padx=5)
slider1=tb.Scale(f1,from_=0,to=1500,orient=HORIZONTAL)
slider1.pack(side=LEFT)
f2=tb.Frame(root)
f2.pack(anchor=NW,pady=10)
lbl3=tb.Label(f2,text="Height",font="lucida 13",bootstyle="light").pack(side=LEFT,padx=5)
slider2=tb.Scale(f2,from_=0,to=1000,orient=HORIZONTAL)
slider2.pack(side=LEFT)
f3=tb.Frame(root)
f3.pack(anchor=NW,pady=10)
lbl4=tb.Label(f3,text="Rotate",font="lucida 13",bootstyle="light").pack(side=LEFT,padx=5)
slider3=tb.Scale(f3,from_=0,to=360,orient=HORIZONTAL)
slider3.pack(side=LEFT)
f4=tb.Frame(root)
f4.pack(anchor=NW,pady=10)
lbl5=tb.Label(f4,text="Blur",font="lucida 13",bootstyle="light").pack(side=LEFT,padx=5)
slider4=tb.Scale(f4,from_=0,to=40,orient=HORIZONTAL)
slider4.pack(side=LEFT)
f5=tb.Frame(root)
f5.pack(anchor=NW,pady=10)
lbl6=tb.Label(f5,text="Brightness",font="lucida 13",bootstyle="light").pack(side=LEFT,padx=5)
tb.Entry(f5,textvariable=var2).pack(side=LEFT)
f6=tb.Frame(root)
f6.pack(anchor=NW,pady=10)
lbl7=tb.Label(f6,text="Crop",font="lucida 13 ",bootstyle="light").pack(side=LEFT,padx=5)
tb.Entry(f6,textvariable=var3).pack(side=LEFT)
#Setting Default Value
slider1.set(width)
slider2.set(height)
#Entries
#Checkbutton for black and white
b_a=tb.Checkbutton(text="Want Black and White image?",variable=var1,bootstyle="light")
b_a.pack(pady=5,anchor=NW)
#Openfile method
def openfile():
    global fil,img1
    fil=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=[("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")])
    img1=Image.open(fil)
    width,height=img1.size
    if height>350 or width>1250:
        img1=img1.resize((int(width/17),int(height/17)))
        slider1.set(int(width/17))
        slider2.set(int(height/17))
    slider1.set(width)
    slider2.set(height)
    img2=ImageTk.PhotoImage(img1)
    lbl.configure(image=img2)
    lbl.image=img2
#Method for cropping
def crop():
    global img1
    width,height=img1.size
    try:
        directions=var3.get().split(",")
        top,bottom,left,right=int(directions[0]),int(directions[1]),int(directions[2]),int(directions[3])
    except Exception as e:
        pass
    else:
        img1=img1.crop((left,top,width-right,height-bottom))
#Our main apply method that applies the effects
def apply():
    global img1
    img1=Image.open(fil)
    width=int(slider1.get())
    height=int(slider2.get())
    rotation=int(slider3.get())
    blur=slider4.get()
    crop()
    try:
        bright=float(var2.get())
    except Exception as e:
        pass
    else:
        enhancer=ImageEnhance.Brightness(img1)
        img1=enhancer.enhance(bright)
    img1=img1.filter(ImageFilter.GaussianBlur(blur))
    img1=img1.rotate(rotation)
    if var1.get()==1:
        img1=img1.convert(mode='L')
    try:
        img1=img1.resize((width,height))
    except ValueError:
        img1=img1.resize((1,1))
    if width>1250 or height>350:
        pass
    if not(width>1250 or height>350):
        img2=ImageTk.PhotoImage(img1)
        lbl.configure(image=img2)
        lbl.image=img2
#Save methodz
def save():
    fil=filedialog.asksaveasfilename(initialfile="Untitled-1.jpg",defaultextension=".jpg",filetypes=[("JPG File","*.jpg*"),("PNG File","*.png")])
    try:
        rgb=img1.convert('RGB')
        rgb.save(fil)
    except Exception as e:
        pass
#Clear Effects method
def clear():
    img1=Image.open(fil)
    width,height=img1.size
    if height>600 or width>1250:
        img1=img1.resize((int(width/17),int(height/17)))
    img2=ImageTk.PhotoImage(img1)
    lbl.configure(image=img2)
    lbl.image=img2
    var1.set(0)
    var2.set("1.0")
    var3.set("0,0,0,0")
    slider1.set(width)
    slider2.set(height)
    slider3.set(0)
    slider4.set(0)
#Filemenu
menu=Menu(root)
filemenu=Menu(menu,tearoff=0)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Clear Effects",command=clear)
root.config(menu=menu)
menu.add_cascade(label="File",menu=filemenu)
#Apply button
tb.Button(root,text="Apply",bootstyle="info-outline",command=apply).pack(padx=5,pady=5,ipadx=5,ipady=5,anchor=NW)
style.configure('TButton',font="arial 12")
style.configure('TCheckbutton',font="arial 12")
root.mainloop()