menu={"popcorn":6.00,
      "Chips":7.00,
      "Nachos":8.00}
cart=[]
total=0
print(".*.*.*.*MENU*.*.*.*.")
for key, value in menu.items():
    print(f"{key:15}:${value:.2f}")

while True:
    food=input("enna venum unakku")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total = total + menu.get(food)
    print(food)
print(total)