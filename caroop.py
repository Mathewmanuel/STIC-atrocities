class car:
    wheels=4
    noofcars=0
    def __init__(self,model,year,color,forsale):
        self.model=model
        self.year=year
        self.color=color
        self.forsale=forsale
        car.noofcars+=1

    def drive(self):
        print(f"you are driving a {self.color} {self.model} ")
        print(f"it has {car.wheels} wheels")

    def stop(self):
        print(f"you stopped driving a {self.color} {self.model}")

    def describe(self):
        print(f"this smexy car is a {self.color} {self.model} {self.year} and is {self.forsale}")