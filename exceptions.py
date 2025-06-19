#exception is an event that interrupts normal flow of a program
try:
    num=int(input("enter a number"))
    print(1/num)
except ZeroDivisionError:
    print("you cannot dived by zero")
except ValueError:
    print("enter only integers pls")
except Exception:
    print("something went wrong")
finally:
    print("somebody clean this shit pls")