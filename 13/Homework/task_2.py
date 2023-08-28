# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class LenError(ValueError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Ошибка размеров {self.value = } должно быть > 0 '

class TypeError(ValueError):
    def __init__(self, other, Matrix):
        self.other = other
        self.Matrix = Matrix
        print(other)

    def __str__(self):
        return f'Ошибка. Ожидается тип  {self.Matrix} а получен тип {type(self.other)} '


class Rectangle:

    def __init__(self, a, b=None):
        if a > 0:
            self.a = a
        else:
            LenError(a)
        if b is None:
            self.b = a
        else:
            if b > 0:
                self.b = b
            else:
                LenError(b)

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
            raise TypeError(other, Rectangle)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.a > other.a and self.b > other.b:
                return Rectangle(self.a - other.a, self.b - other.b)
            else:
                if not self.a > other.a:
                    raise LenError(self.a-other.a)
                else:
                    raise LenError(self.b-other.b)
        else:
            raise TypeError(other, Rectangle)
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() == other.get_area()
        else:
            raise TypeError(other, Rectangle)

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() > other.get_area()
        else:
            raise TypeError(other, Rectangle)

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() >= other.get_area()
        else:
            raise TypeError(other, Rectangle)

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
# r4 -= r2 #LenError: Ошибка размеров self.value = 0 должно быть > 0
# r4 = r3 - 1 #TypeError: Ошибка. Ожидается тип  <class '__main__.Rectangle'> а получен тип <class 'int'>
print(r2 == r4)
print(r1 > r2)
print(r1 < r2)
print(r1, r4)
print(r1 <= r4)
print(r1 >= r4)
