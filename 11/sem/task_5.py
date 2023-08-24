# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle:

    # def __new__(cls, *args, **kwargs):
    def __init__(self, a, b=None):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimetr(self):
        return 2 * self.a * self.b

    def __repr__(self):
        return f'Rectangle({self.a}, {self.b})'

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.a + other.a, self.b + other.b)
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.a >= other.a and self.b >= other.b:
                return Rectangle(self.a - other.a, self.b - other.b)
            else:
                raise ValueError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() == other.get_area()
        else:
            raise ValueError

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() > other.get_area()
        else:
            raise ValueError

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() >= other.get_area()
        else:
            raise ValueError

    # def __le__(self, other):
    #     if isinstance(other, Rectangle):
    #         return self.get_area() <= other.get_area()
    #     else:
    #         raise ValueError


r1 = Rectangle(3, 4)
r2 = Rectangle(5, 6)
r3 = r1 + r2
print(r1, r2, r3)
r4 = r3 - r1
print(r4)

print(r2 == r4)
print(r1 > r2)
print(r1 < r2)
print(r1, r4)
print(r1 <= r4)
print(r1 >= r4)

