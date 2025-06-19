#writitng file
import csv
txt="hi bro"
filepath="test.txt"
employees=[["Mady",21],["praddy",21],["Aki",21],["Che",21]]
try:
    with open(filepath,"w")as file:
          writer=csv.writer(file)
          for row in employees:
               writer.writerow(row)
          print(f"csv file '{filepath}'was created")
except FileExistsError:
    print("That file already exists!")