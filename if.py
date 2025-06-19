age=int(input("enter your age"))
if age>18:
    print("you may vote")
elif age==18:
    print(" congratulations you may vote beginnig this election")
if age>=100:
    print("you are eligible to apply for ballot voting rights")
else:
    print("you may not vote")

reponse=input(" iff you have voted already enter y, else n:\n")
if reponse == 'y':
    print(" congrats on exercising your rights")
else:
    print("go vote loser")

