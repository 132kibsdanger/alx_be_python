import math
class Shape:

    @property
    def area(self):
        raise NotImplementedError("Derived classes need to override this method")
    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"length: {self.length} and width: {self.width}"

    @property
    def area(self):
        area = self.length*self.width
        return area
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        area = math.pi*self.radius*self.radius
        return area


