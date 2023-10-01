#Program to make a quiz application with tkinter
from tkinter import *
import json
import ttkbootstrap as tb
from ttkbootstrap.constants import *
root=tb.Window(themename='superhero')
root.geometry("500x400")
root.title("Quiz")
user_answers={}
score=0
style=tb.Style()
with open('data.json') as f:
	data=json.load(f)
	questions=data[0]
	answers=data[1]
	options=data[2]
for i in range(len(questions)):
	user_answers[i]=None
label=tb.Label(root,text="Quiz",font="arial 20 bold").pack(pady=5)
index=0
radiobuttons=[]
var1=StringVar()
var1.set(" ")
question_label=tb.Label(root,text="1."+questions[index],bootstyle='info',font="arial 14")
question_label.pack(anchor=W,pady=10)
for option in options[index]:
    radiobutton=tb.Radiobutton(root, text = option, variable = var1,value = option,bootstyle='success')
    radiobutton.pack(anchor=W,pady=10)
    radiobuttons.append(radiobutton)
def next_option():
	global index,score
	if(button.cget("text")=="Next"):
		if(index<len(questions)-1):
			user_answers[index]=var1.get()
			index+=1
			if(user_answers[index]==None):
				var1.set(" ")
			else:
				var1.set(user_answers[index])
			question_label.config(text=f"{index+1}.{questions[index]}")
			for i in range(4):
				radiobuttons[i].config(text=options[index][i],value=options[index][i])
			if(index==len(questions)-1):
				button.config(text="Submit")
	else:
		user_answers[index]=var1.get()
		for i in range(len(answers)):
			if(answers[i]==user_answers[i]):
				score+=1
		score_text.config(text=f"Score:{score}/{len(questions)}")
		button.config(state=DISABLED)
		button2.config(state=DISABLED)
def previous_option():
	global index
	if(index>0):
		index-=1
		for i in range(4):
			radiobuttons[i].config(text=options[index][i],value=options[index][i])
		var1.set(user_answers[index])
		button.config(text="Next")
		question_label.config(text=f"{index+1}.{questions[index]}")
f=tb.Frame(root)
f.pack(anchor=W)
score_text=tb.Label(root,font="arial 14")
score_text.pack(anchor=W)
button=tb.Button(f,text="Next",command=next_option,bootstyle='primary')
button.pack(side=RIGHT,padx=5,ipadx=5,ipady=5,pady=5)
button2=tb.Button(f,text="Previous",command=previous_option,bootstyle='danger')
button2.pack(side=RIGHT,padx=5,ipadx=5,ipady=5,pady=5)
style.configure('TButton',width=9,height=3,font='arial 12')
style.configure('success.TRadiobutton',font='arial 12')
root.mainloop()