#Static method-belongs to the clas
#instance method- belong to a partciular instance of the class
class employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    #instance method
    def putinfo(self):
        return f"{self.name} : {self.position}"
    
    @staticmethod
#dont need self keyword no need for object
    def isvalidposition(position):
        validposition=["manager","Cashier","Cook","Janitor"]
        return position in validposition
    
emp1=employee("Eugene","manager")
emp2=employee("Sujan","Janitor")
emp3=employee("Mathew","Senior Janitor")
print(employee.isvalidposition("Cook"))

print(emp1.putinfo())
print(emp2.putinfo())
print(emp3.putinfo())
