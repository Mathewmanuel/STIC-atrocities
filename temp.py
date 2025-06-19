userval=input("enter the value")
len=len(userval)
if userval.isdigit()==False and len<=12 and userval.count(" ")==0:
    print("valid")