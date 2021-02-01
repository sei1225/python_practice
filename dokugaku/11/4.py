class Hexagon:
    def __init__(self,l):
        self.length = l

    def calculate_perimeter(self):
        return self.length * 6

hexagon1 = Hexagon(6)
print(hexagon1.calculate_perimeter())
hexagon2 = Hexagon(10)
print(hexagon2.calculate_perimeter())