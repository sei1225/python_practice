class Rectangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h

    def calculate_parameter(self):
        return 2*self.bottom + 2*self.height


class Square:
    def __init__(self, l):
        self.length = l

    def calculate_parameter(self):
        return 4*self.length

    def change_size(self,l):
        self.length += l
        
rec_1 = Rectangle(10,12)
print(rec_1.calculate_parameter())
squ_1 = Square(10)
print(squ_1.calculate_parameter())
squ_1.change_size(-5)
print(squ_1.calculate_parameter())
