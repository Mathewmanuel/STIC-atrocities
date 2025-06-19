wt=float(input("enter your weight"))
unit=input("enter k if weight is in kg and l if weight is in pounds")
if unit=='k':
    print(wt*2.205)
elif unit=='l':
    print(wt/2.205)