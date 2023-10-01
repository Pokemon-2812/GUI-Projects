import random
values={"A":8,"B":6,"C":4,"D":2}
letters=list(values.keys())
def deposit():
    global deposited_money
    try:
        deposited_money=int(input("How much money do you want to deposit?\n"))
    except Exception as e:
        print("Please enter a number.")
    runGame()
def runGame():
    global deposited_money,letters
    try:
        bet=int(input("How much money do you want to bet on each line?\n"))
    except Exception as e:
        print("Please enter a number.")
    else:
        if bet*3>deposited_money or deposited_money<3:
            print("Sorry,you don't have enough money deposited.")
        else:
            game_letters=""
            text=""
            won=0
            slot_values=[[],[],[]]
            for i in range(3):
                index=random.randint(0,len(letters)-1)
                game_letters+=letters[index]
                letters.pop(index)
            letters=list(values.keys())
            for i in range(3):
                for j in range(3):
                    random_letter=random.choice(game_letters)
                    text+=random_letter
                    slot_values[i].append(random_letter)
                    if j!=2:
                        text+="|"
                text+="\n"
            for line in slot_values:
                if line[0]==line[1]==line[2]:
                    won+=bet*values[line[0]]
            print(text)
            if won>0:
                deposited_money+=won
            else:
                deposited_money-=bet*3
            print(f"You won {won}$.You have currently {deposited_money}$.")
            choice=input("Do you want to continue(y/n)?\n")
            if choice.lower()=="y":
                if deposited_money>=3:
                    runGame()
            else:
                print(f"Withdrawing {deposited_money}$")
deposit()
