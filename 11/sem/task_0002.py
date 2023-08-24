class NumStr:
    """Клас состоящий из двух элементов: строки и числа"""
    def __init__(self, string, number):
        self.number = number
        self.string = string

    def __str__(self):
        """Переопределение метода str"""
        return f'{self.string, self.number}'


class Archiv:
    """Класс архив."""
    __arch = []

    def __init__(self, string, number):
        """Создание экземпляра архив"""
        Archiv.__arch.append(NumStr(string, number))

    def print_arch(self):
        """Переопределение метода str"""
        rez = ''
        for num in self.__arch:
            rez += f'{num} '
        return f'{rez}'


class MyClass(NumStr, Archiv):
    """Класс содержащий значение и архив значений"""
    def __new__(cls, *args, **kwargs):
        """Создание класса"""
        instance = NumStr.__new__(cls)
        return instance


    def __init__(self, string, number):
        """Создание экземпляра класса"""
        NumStr.__init__(self, string, number)
        Archiv.__init__(self, string, number)

    def __repr__(self):
        """Данные для программиста"""
        return f'MyClass{self}'


first = MyClass('a', 1)
print(first)
first = MyClass('b', 2)
print(first)
second = MyClass('c', 3)
print(second)
print(first.print_arch())
print(second.print_arch())
print(id(first), id(second))
print(id(first.print_arch()), id(second.print_arch()))
print(first.__repr__())
