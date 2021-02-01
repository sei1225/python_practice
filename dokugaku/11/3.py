class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h

    def area(self):
        return self.bottom * self.height / 2

triangle1 = Triangle(2,3)
print(triangle1.area())
triangle2 = Triangle(3,4)
print(triangle2.area())
