#super function extends the functionality of the parent class
class shapes:
    def __init__(self,color,filled,radius):
            self.color=color
            self.filled=filled

    class circle(shapes):
        def __init__(self,color,filled,radius):
            super().__init__(self,color,filled)
            self.radius=radius

    class rectangle(shapes):
        def __init__(self,color,filled,width,breadth):
            super().__init__(self,color)
            self.width=width
            self.breadth=breadth
    
    class  triangle(shapes):
        def __init__(self,color,filled,hypotenuse,base):
            super().__init__(self,color,filled,hypotenuse,base)
            self.hypotenuse=hypotenuse
            self.base=base

circle1=circle("red",True,5)
print(cricle1.color)
csquare=rectangle("red",True,5,4)
print(csquare.color)



