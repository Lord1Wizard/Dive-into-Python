# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра
class NumStr:
    def __init__(self, string, number):
        self.number = number
        self.string = string

    def __str__(self):
        return f'{self.string, self.number}'

class Archive:
    __arch = []
    # ns = None

    def __init__(self, string, number):
        self.ns = NumStr(string, number)
        Archive.__arch.append(NumStr(self.ns.string, self.ns.number))
    def print_arch(self):
        rez = ''
        for num in self.__arch:
            rez += f'{num} '
        return f'{rez}'

first = Archive('a', 1)
print(first.ns)
print(first.print_arch())
second = Archive('b', 2)
print(second.ns)
print(second.print_arch())
third = Archive('c', 3)
print(third.ns)
print(third.print_arch())
print(first.ns)

