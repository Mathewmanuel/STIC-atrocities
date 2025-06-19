#class method is a method that works on a class as a whole

class student:
    count=0
    total=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        student.count+=1
        student.total+=gpa

    def getinfo(self):
        return f"{self.name}{self.gpa}"
    @classmethod 
    def getcount(cls):
        return f"total is {cls.count}"
    @classmethod
    def avggpa(cls):
        return f"{cls.total/cls.count}"
st1=student("Amy",7.9)
st2=student("Sujan",8.65)
st2=student("Reshma",8.9)
print(student.getcount())
print(student.avggpa())