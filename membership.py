grades={ "maddy":"A","Sujan":"B","Akilesh":"C"}
student="Sujan"
if student in grades:
    print(f"{student}:{grades[student]}")

#list comprehension
fruits=["apples","Oranges","Grapes"]
fruits=[x[0].upper() for x in fruits]
print(fruits)

#list comprehension 2

grades=[34,65,65,87,43,54,9,65,32]
passinggrades=[grade for grade in grades if grade>40]
print(passinggrades)