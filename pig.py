from tkinter import *
import random
from tkinter.messagebox import showinfo
import ttkbootstrap as tb
from ttkbootstrap.constants import *
root=tb.Window(themename='darkly')
root.title("Pig")
root.geometry("600x400")
player1_chance=True
player1_score=0
player2_score=0
def restart():
    global player1_chance,player1_score,player2_score
    b1.config(state=ACTIVE)
    b2.config(state=ACTIVE)
    player1_chance=True
    player1_score=0
    player2_score=0
    score_label1.config(text=f"Score:{player1_score}")
    score_label2.config(text=f"Score:{player2_score}")
    showinfo("Game Restarted!","Game is restarted.")
def roll_dice(score):
    num=random.randint(1,6)
    if num==1:
        score=0
        showinfo("One","Oh No! You got a one.")
        change_chance()
    else:
        score+=num 
    return score
def roll():
    global player1_chance,player1_score,player2_score
    if(player1_chance):
        player1_score=roll_dice(player1_score)
        score_label1.config(text=f"Score:{player1_score}")
        if player1_score>=50:
            showinfo("Hurray!","Player 1 wins!")
            b1.config(state=DISABLED)
            b2.config(state=DISABLED)
    else:
        player2_score=roll_dice(player2_score)
        score_label2.config(text=f"Score:{player2_score}")
        if player2_score>=50:
            showinfo("Hurray!","Player 2 wins!")
            b1.config(state=DISABLED)
            b2.config(state=DISABLED)


def change_chance():
    global player1_chance
    player1_chance=not(player1_chance)
    if(player1_chance):
        showinfo("Chance changed","Chance changed to player 1.")
    else:
        showinfo("Chance changed","Chance changed to player 2.")
tb.Label(root,text="Pig",font="arial 18 bold",bootstyle='success').pack(side=TOP,padx=5,pady=5)
f1=tb.Frame(root)
f1.pack(side=LEFT)
tb.Label(f1,text="Player 1",font="arial 14 bold",bootstyle='light').pack(pady=5,ipady=5)
score_label1=tb.Label(f1,text="Score:0",font="arial 12 bold",bootstyle='warning')
score_label1.pack()
f2=tb.Frame(root)
f2.pack(side=RIGHT)
tb.Label(f2,text="Player 2",font="arial 14 bold",bootstyle='light').pack(pady=5,ipady=5)
score_label2=tb.Label(f2,text="Score:0",font="arial 12 bold",bootstyle='warning')
score_label2.pack()
b1=tb.Button(root,text="Roll Dice",command=roll,bootstyle='info-outline')
b1.pack(pady=5,ipady=5,ipadx=20,side=BOTTOM)
b2=tb.Button(root,text="Change Chance",command=change_chance,bootstyle='info-outline')
b2.pack(pady=5,ipady=5,side=BOTTOM)
menu=Menu(root)
optionMenu=Menu(menu,tearoff=0)
optionMenu.add_command(label="Restart",command=restart)
root.config(menu=menu)
menu.add_cascade(label="File",menu=optionMenu)
root.mainloop()