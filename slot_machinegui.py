from tkinter import *
import random
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror,showinfo,askyesno
root=Tk()

values={"A":8,"B":6,"C":4,"D":2}
letters=list(values.keys())
def deposit():
    global deposited_money
    try:
        deposited_money=int(askstring("Deposit","How much money do you want to deposit(in dollars)?\n"))
    except Exception as e:
        showerror("Error","Please enter a number")
    runGame()
def runGame():
    global deposited_money,letters
    try:
        bet=int(askstring("Bet","How much money do you want to bet on each line?\n"))
    except Exception as e:
        showerror("Error","Please enter a number")
    else:
        if bet*3>deposited_money or deposited_money<3:
            showerror("Error","Sorry,you don't have enough money deposited.")
        else:
            game_letters=""
            won=0
            slot_values=[[],[],[]]
            btn_index=0
            for i in range(3):
                index=random.randint(0,len(letters)-1)
                game_letters+=letters[index]
                letters.pop(index)
            letters=list(values.keys())
            for i in range(3):
                for j in range(3):
                    random_letter=random.choice(game_letters)
                    slot_values[i].append(random_letter)
                    buttons[btn_index].config(text=random_letter)
                    btn_index+=1
            for line in slot_values:
                if line[0]==line[1]==line[2]:
                    won+=bet*values[line[0]]
            if won>0:
                deposited_money+=won
                showinfo("Won",f"You won {won}$.You have currently {deposited_money}$.")
            else:
                deposited_money-=bet*3
                showinfo("Lost",f"You lost {bet*3}$.You have currently {deposited_money}$.")
            choice=askyesno("Continue","Do you want to continue?")
            if choice==True:
                if deposited_money>=3:
                    runGame()
                else:
                    showerror("Error","You don't have enough money deposited.")
            else:
                showinfo("Withdraw",f"Withdrawing {deposited_money}$")
root.title("Slot Machine")
b1=Button(root,width=6,height=3,font="helvetica 18")
b1.grid(row=0,column=0)

b2=Button(root,width=6,height=3,font="helvetica 18")
b2.grid(row=0,column=1)

b3=Button(root,width=6,height=3,font="helvetica 18")
b3.grid(row=0,column=2)

b4=Button(root,width=6,height=3,font="helvetica 18")
b4.grid(row=1,column=0)

b5=Button(root,width=6,height=3,font="helvetica 18")
b5.grid(row=1,column=1)

b6=Button(root,width=6,height=3,font="helvetica 18")
b6.grid(row=1,column=2)

b7=Button(root,width=6,height=3,font="helvetica 18")
b7.grid(row=2,column=0)

b8=Button(root,width=6,height=3,font="helvetica 18")
b8.grid(row=2,column=1)

b9=Button(root,width=6,height=3,font="helvetica 18")
b9.grid(row=2,column=2)
buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
menubar=Menu(root)
option_menu=Menu(menubar,tearoff=False)
option_menu.add_command(label="Deposit",command=deposit)
menubar.add_cascade(label="Options",menu=option_menu)
root.config(menu=menubar)
root.mainloop()