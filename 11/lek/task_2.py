class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vektor({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vektor(x, y)


a = Vektor(2, 4)
b = Vektor(3, 7)
c = a + b
print(f'{a = }\t{b = }\t{c = }')