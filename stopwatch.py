from tkinter import *
root=Tk()
root.title("StopWatch")
root.geometry("300x200")
start=False
time=0
def startgame():
	global start,time
	if(start==False):
		start=True
		btn.config(text="Stop")
	else:
		start=False
		time=0
		btn.config(text="Start")
	run()
def run():
	global time,start
	if(start):
		time+=1
		if(time<60):
			label.config(text=time)
		if(time>=60):
			seconds=time%60
			if(seconds<10):
				seconds="0"+str(seconds)
			label.config(text=f"{time//60}:{seconds}")
		root.after(1000,run)
label=Label(root,text="",font="arial 16 bold")
label.pack()
btn=Button(root,text="Start",bg="red",font="arial 12",command=startgame)
btn.pack(fill=X)
root.mainloop()