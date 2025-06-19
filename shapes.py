from abc import ABC,abstractmethod
class shape(ABC):

    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height

circle1=circle(34)
#circle1 is a circle as well as a shape this is polymorphism in real life
square1=square(21)
triangle1=triangle(5,9)
class pizza:
    def __init__(self,topping,radius):
        self.radius=radius
        self.topping=topping
    def area(self):
        return 3.14*self.radius**2
shapes=[circle1,square1,triangle1]
pixxa=pizza("pepperoni",21)
print(f"the size of the{pixxa.topping} pizza is ")
print(pixxa.area())
for shape in shapes:
    print(shape.area())