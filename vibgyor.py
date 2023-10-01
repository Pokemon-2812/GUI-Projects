from tkinter import *
root=Tk()
root.title("Rainbow")
root.geometry("600x400")
root.config(bg="pink")
index=0
running=False
colors=["purple","indigo","blue","green","yellow","orange","red"]
def change():
	global running
	running=not(running)
	if(btn.cget("text")=="start"):
		btn.config(text="stop")
	else:
		btn.config(text="start")
	root.after(10,change_color)
def change_color():
	global index
	if(running):
		if(index<len(colors)-1):
			index+=1
		else:
			index=0
		root.config(bg=colors[index])
		root.after(10,change_color)
	else:
		index=0
		root.config(bg="pink")
btn=Button(root,bg="red",fg="white",text="start",font="arial 14",command=change)
btn.pack(fill=X,ipady=5)
root.mainloop()