from tkinter import *
import random
root=Tk()
root.geometry("400x250")
root.title("Click Color")
time_left=61
score=0
game_running=True
def change():
	if(game_running):
		btn.config(bg=colors[random.randint(0,len(colors)-1)])
	root.after(800,change)
def change_time():
	global time_left,game_running
	if(time_left>0):
		time_left-=1
		time_text.config(text=f"Time Left:{time_left}")
		root.after(1000,change_time)
	else:
		btn.config(state=DISABLED)
		lbl2.config(text="Game Over",font="arial 13")
		game_running=False
def check():
	global mistakes,score
	if(btn.cget("bg")==root.cget("bg")):
		root.config(bg=colors[random.randint(0,len(colors)-1)])
		lbl1.config(bg=root.cget("bg"))
		lbl2.config(bg=root.cget("bg"))
		score_text.config(bg=root.cget("bg"))
		time_text.config(bg=root.cget("bg"))
		score+=1
		score_text.config(text=f"Score:{score}")
	else:
		score-=1
		score_text.config(text=f"Score:{score}")
		root.config(bg=colors[random.randint(0,len(colors)-1)])
		lbl1.config(bg=root.cget("bg"))
		lbl2.config(bg=root.cget("bg"))
		score_text.config(bg=root.cget("bg"))
		time_text.config(bg=root.cget("bg"))
lbl1=Label(root,text="Click Color",font="arial 18")
lbl1.pack(anchor=CENTER,ipady=5)
lbl2=Label(root,text="Click the button when it shows the color of the background",font="arial 11")
lbl2.pack(anchor=CENTER,ipady=5)
score_text=Label(root,text="Score:0",font="arial 14")
score_text.pack(anchor="center")
time_text=Label(root,text="Time Left:60",font="arial 14")
time_text.pack(anchor="center")
btn=Button(root,font="arial 12",command=check)
btn.pack(anchor=CENTER,fill=X,ipady=5)
colors=["red","blue","green","yellow","orange","purple","brown","grey","white","gold","pink"]
root.config(bg=colors[random.randint(0,len(colors)-1)])
lbl1.config(bg=root.cget("bg"))
lbl2.config(bg=root.cget("bg"))
score_text.config(bg=root.cget("bg"))
time_text.config(bg=root.cget("bg"))
change()
change_time()
root.mainloop()
