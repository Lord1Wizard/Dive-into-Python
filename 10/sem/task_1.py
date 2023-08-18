# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def square(self):
        return self.radius ** 2 * 3.14159

    def length(self):
        return self.radius * 2 * 3.14159


c1 = Circle(10)
print(c1.square())
print(c1.length())
