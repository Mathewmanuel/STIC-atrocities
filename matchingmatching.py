#match case 
def weekendah(day):
    match day:
        case "saturday" | "sunday":
            return True
        case _:
            return False
        
day=input("enter day")
print(weekendah(day))