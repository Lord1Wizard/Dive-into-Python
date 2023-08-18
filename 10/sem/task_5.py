# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Enimals():

    def __init__(self, name, voice='ggrr'):
        self.name = name
        self.__voice = voice

    def make_voice(self):
        return self.__voice

    def __str__(self):
        return f'Имя: {self.name}'

class Fish(Enimals):

    def __init__(self, species, *args, **kwargs):
        super().__init__(*args, **kwargs, voice='tssss')
        self.species = species

    def swim(self):
        return "I'm swimming"
    def __str__(self):
        return super().__str__() + f' Вид: {self.species}'

class Dog(Enimals):

    def __init__(self, breed, *args, **kwargs):
        super().__init__(*args, **kwargs, voice='Gav-gav')
        self.breed = breed

    def runnning(self):
        return "I'm running"

    def __str__(self):
        return super().__str__() + f' Порода: {self.breed}'


d1 = Dog('Akita', 'Tosha')
print(d1.runnning())
print(d1.make_voice())
print(d1)
f1 = Fish('Akula', 'Megaladon')
print(f1.swim())
print(f1.make_voice())
print(f1)
