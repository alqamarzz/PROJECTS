import random

computer = random.choice([1,-1,0])
user=input("Enter your choice: ")
userDict={"s": 1, "w":-1, "g":0}
you=userDict[user]
compDict={1:"snake", -1:"water", 0:"gun"}
print(f"You Chose {compDict[you]}\nComputer Chose {compDict[computer]}")
if(computer==you):
    print("It's a Draw!")
else:
    if(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Win!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==1 and you==-1):
        print("You Loose!")
    elif(computer==0 and you==1):
        print("You Loose!")
    elif(computer==0 and you==-1):
        print("You Loose!")