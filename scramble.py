from random import randint
notations=["R","F","L","U","D","B","R'","F'","U'","D'","B'"]
text=""
for i in range(50):
	text+=notations[randint(0,len(notations)-1)]+" "
print(text)