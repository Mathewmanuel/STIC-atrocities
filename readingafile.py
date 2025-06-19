import csv
filepath="C:/Users/Dell/OneDrive/Documents/SITC internship/test.csv"
try:
    with open(filepath,"r") as file:
        content=csv.reader(file)
        for line in content:
            print(line)
        print(content)
except FileNotFoundError:
    print("this shit illa pa")
except PermissionError:
    print("You cannot access asaid fiel")