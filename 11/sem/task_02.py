class Archive:
    _instance = None

    def __new__(cls, string, number):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._string_archive = []
            cls._instance._number_archive = []
        else:
            cls._instance._string_archive.append(cls._instance.string)
            cls._instance._number_archive.append(cls._instance.number)
        return cls._instance

    def __init__(self, string, number):
        self.string = string
        self.number = number

    def __str__(self):
        return f"{self.number, self.string}"


    def string_archive(self):
        return self._string_archive


    def number_archive(self):
        return self._number_archive



first = Archive('a', 1)
print(first.string_archive(),  first.number_archive(), first)
first = Archive('z', 0)
print(first.string_archive(),  first.number_archive(), first)
first = Archive('x', 9)
print(first.string_archive(),  first.number_archive(), first)
second = Archive('b', 2)

print(second.string_archive(), second.number_archive(), second)

third = Archive('c', 3)
print(third.string_archive(), third.number_archive(), third)

print(first.string_archive(),  first.number_archive(), first)
