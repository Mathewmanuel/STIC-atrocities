import random
lnum=1
hnum=100
ans=random.randint(lnum,hnum)
guesses=0
runngin= True
print("Welcome")
print(f"enter number between {lnum} and {hnum}")
while runngin:
    guess=input("Enter your number")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        
        if guess < lnum or guess> hnum:
            print("the number is out of range please selesct a number between lowest anfd highest num")
    else:
        print("enter a valid num")

