import math 

balance=0
isrunning=True
def showbal():
    print(f"the account balance is:{balance}")
def withdraw():
    draw=int(input("Enter the amount you want to witdraw"))
    if draw>balance:
        print("Cannot Overdraw from a Savings account")
    else:
        balance-=draw
        print(f"the Remaining balance is{balance}")
def deposit():
    depos=int(input("Enter the amount you want to deposit"))
    balance+=depos
    print(f"the updated balance is {balance}")
while isrunning:

    print("Welcome to the State Bank of Tamil Nadu")
    print("Choose your action to be performed\n 1.View Balance \n 2.Withdraw \n 3.Deposit \n 4.Exit")
    choice=int(input("Enter your Choice"))
    match choice:
        case 1:
            showbal()
        case 2:
            withdraw()
        case 3:
            deposit()
        case 4:
           print("Thank you for using State Bank of Tamil Nadu")
           isrunning=False
        case _:
           print("Kindly make a valid choice")





    