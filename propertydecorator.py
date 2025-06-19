#@property = decorator used to define a method as a property helps add additioinal logic to the program when reading or writing values
class rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
#additional steps to print the heigh and width to keep the original int as private
    @property
    def width(self):
        return  f"{self._width:.2f}cm"
    @property
    def height(self):
        return f"{self._height:.2f}cm"
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("width must be greater than zero")
    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height=new_height
        else:
            print("width must be greater than zero")
    @width.deleter
    def witdth(self):
        del self._width
        print("Width has been deleted")
rectangle.width=5
rectangle.height=4
print(rectangle.width)
print(rectangle.height)
del rectangle.width