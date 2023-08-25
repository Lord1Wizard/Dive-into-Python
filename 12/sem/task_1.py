# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

class NumRez:
    def __init__(self, num, rez):
        self.num = num
        self.rez = rez

    def __str__(self):
        return f'{self.num}, {self.rez}'

    def to_str(self):
        return f'{self.num}, {self.rez}'


class Queue:
    def __init__(self, k):
        self.queue = list()
        self.k = k

    def add_element(self, num, rez):
        # Insert method to add element
        # if val not in self.queue:
        self.queue.insert(0, NumRez(num, rez))
        self.check_len()
        return True
        # return False

    def check_len(self):
        while len(self.queue) > self.k:
            self.remove_element()

    def remove_element(self):
        # Pop method to remove element
        if len(self.queue) > self.k:
            return self.queue.pop()
        return ("Queue is Empty")

    def __str__(self):
        rez = self.queue[0].to_str()
        for i in range(1, len(self.queue)):
            rez += '; ' + self.queue[i].to_str()
        return f'{rez}'


class Factorial:
    _instance = None

    def __new__(cls, k):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.archiv = Queue(k)
        return cls._instance

    def __call__(self, num):
        rez = 1
        for i in range(2, num+1):
            rez *= i
            # print(i)
        self.archiv.add_element(num, rez)
        return rez

    def achiv_print(self):
        return f'{self.archiv.__str__()}'

fac1 = Factorial(5)
fac = Factorial(5)
print(fac(5))
print(fac1(2))
print(fac(3))
print(fac(4))
print(fac.achiv_print())
print(fac(5))
print(fac.achiv_print())
print(fac(10))
print(fac.achiv_print())
