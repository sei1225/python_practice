from math import pi


class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return pi * self.radius**2

circle1 = Circle(10)
print(circle1.area())
circle2 = Circle(100)
print(circle2.area())
