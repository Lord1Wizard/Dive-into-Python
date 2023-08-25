# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.


class Rectangle:
    __slots__ = ('_a', '_b')

    def __init__(self, a, b=None):
        self._a = a
        if b is None:
            self._b = a
        else:
            self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError

    def get_area(self):
        return self._a * self._b

    def get_perimetr(self):
        return 2 * self._a * self._b

    def __repr__(self):
        return f'Rectangle({self._a}, {self._b})'

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self._a + other._a, self._b + other._b)
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self._a >= other._a and self._b >= other._b:
                return Rectangle(self._a - other._a, self._b - other._b)
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
print(r1.a)
r1.a = 10
print(r1.a)
print(r1.b)
r1.b = 20
print(r1.b)
print(r1)

print(Rectangle.__dict__)
print(r1.__slots__)
