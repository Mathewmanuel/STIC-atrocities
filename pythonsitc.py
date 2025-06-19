import sys
import random
from enum import Enum
class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3
print('hi')
playerchoice=input("Enter....\n 1 for rock\n 2 for paper \n 3 for Scissors \n\n")
player=int(playerchoice)
if player<1 or player>3:
    sys.exit("you must enter valid numbers da koomuttai")
computerchoice=random.choice("123")
compc=int(computerchoice)
print("you chose"+ str(RPS(player)).replace('RPS.',''))
print("Your opponent chose" + str(RPS(compc)).replace('RPS.',''))
if player == 3 and compc == 2:
    print("you win🥳")
elif player == 2 and compc == 1:
    print("you win🏆")
elif player == 1 and compc == 3:
    print("you win🏆")
elif player == compc:
    print(" you win da matti by default🍾")
else:
    print("☠️computer wins robo takes over the world and the fault is on you'☠️")

    