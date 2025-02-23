import random
n=random.randint(1,100)
count=0
a=-1
while a!=n:
    count+=1
    a=int(input("Enter your guess: "))
    if(a>n):
        print("Wrong ans!, lower number please.")
    elif(a<n):
        print("Wrong ans!, higher number please.")

print(f"You guessed it right in {count} attempts")