#decorator-a function that extends the behaviour of a another function. w/o modifying the base function,we pass the  base function as an argument to the decorator
def addsprinkles(func):
    def wrapper(*args,**kwargs):
        print("YOU May Add Sprinkles🎊🎊")
        func(*args,**kwargs)
    return wrapper

def addwaffles(func):
    def wrapper(*args,**kwargs):
        print("You May Add Waffles🧇🧇")
        func(*args,**kwargs)
    return wrapper

@addsprinkles
@addwaffles
def geticecream(flavour):
    print(f"here is your {flavour} icecream🍦🍦")

geticecream("vanilla")
