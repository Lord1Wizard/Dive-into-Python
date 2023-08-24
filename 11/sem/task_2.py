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
    _instance = None
    # Value = None
    def __new__(cls, string, number):
        print('new')
        if not isinstance(cls._instance, cls ):
            cls._instance = object.__new__(cls)
            cls.Value=[]
        # else:
        #     cls.Value.append()
        return cls._instance

    def __init__(self, string, number):
        print('init')
        # if Archive.Value is None
        self.Value = NumStr(string, number)

    def __str__(self):
        return f'{self.Value.number, self.Value.string}'

first = Archive('a',1)
print(first)
second = Archive('b',2)
print(first)

print(second)
print(first)
# print(second.Value.number)