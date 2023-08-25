# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Range:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')
class Rectangle:
    a = Range(1, 100)
    b = Range(1, 100)
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
                return Rectangle(self.a - other.a, self._b - other.b)
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


r1 = Rectangle(3, 40)
r2 = Rectangle(5, 6)
r3 = r1 + r2
print(r1, r2, r3)

print(r1)


