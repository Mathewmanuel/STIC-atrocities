'''
import time
utime=int(input("enter the sleep time"))

for x in range(utime,0,-1):
    seconds=x%60
    minutes=x//60
    hour=int(x/3600)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    print("sorry thoongiten")
    '''
'''''
rows=int(input("enter row"))
column=int(input("enter columns"))
symbol=input("enter the symbol")
for x in range(rows):
    for y in range (column):
        print(symbol,end="")
    print()
    '''''
#collections
'''''''''
foods=[]
prices=[]
total=0
while True:
    food=input("enter your choice, oress q to quit")
    if food.lower()=='q':
        break
    else:
        price=int(input(f"enter the cost of {food}"))
        foods.append(food)
        prices.append(price)
        
print("*******your cart*******")
for food in foods:
    print(food, end=" ")
print(" ")
for price in prices:
    total += price
    print(price,end=" ")

print(total)
'''
#2d tuple numpad

numb=((1,2,3),
      (4,5,6),
      (7,8,9),
      ("*",0,"#"))

for num in numb:
    for digi in num:
        print(digi,end=" ")
    print("")