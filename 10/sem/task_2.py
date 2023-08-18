# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат

class Rectangle:
    def __init__(self, height=1, width=None):
        self.height = height
        self.width = width or height

    def square(self):
        return self.height * self.width

    def length(self):
        return (self.height + self.width) * 2


r1 = Rectangle(10, 5)
print(r1.square())
print(r1.length())
