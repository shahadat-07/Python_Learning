from math import pi

class Shape:
    def __init__(self, name) -> None:
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

        def area(self):
            print(self.length * self.width)
        
class Circle(Shape):
    def __init__(self, name, radious) -> None:
        self.radious = radious
        super().__init__(name)

    def area(self):
            print(pi * self.radious * self.radious)
        
big_circle = Circle('circle', 2)
big_circle.area()
