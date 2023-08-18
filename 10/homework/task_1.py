class Animals():
    """Класс животные"""

    def __init__(self, name, voice='ggrr'):
        self.name = name
        self.__voice = voice

    def make_voice(self):
        return self.__voice

    def __str__(self):
        return f'Имя: {self.name}'


class Fish(Animals):
    """Класс рыба"""

    def __init__(self, species, *args, **kwargs):
        super().__init__(*args, **kwargs, voice='tssss')
        self.species = species

    def swim(self):
        return "I'm swimming"

    def __str__(self):
        return super().__str__() + f' Вид: {self.species}'


class Dog(Animals):
    """Класс Собака """
    def __init__(self, breed, *args, **kwargs):
        super().__init__(*args, **kwargs, voice='Gav-gav')
        self.breed = breed

    def runnning(self):
        return "I'm running"

    def __str__(self):
        return super().__str__() + f' Порода: {self.breed}'


class AnimalsCreater:
    """Фабрика животных"""
    def animal(format, *args, **kwargs):
        animal_creater = get_animal(format)
        return animal_creater(*args, **kwargs)


def get_animal(format):
    """В зависимости от format возращает нужный класс или генерирует ошибку если класса нет"""
    if format == 'Dog':
        return Dog
    elif format == 'Fish':
        return Fish
    else:
        raise ValueError(format)

z1 = AnimalsCreater.animal('Dog', 'Akita', 'Tosha')
z2 = AnimalsCreater.animal('Fish', 'Guppi', 'Vasia')
# z3 = AnimalsCreater.animal('Bird', 'Guppi', 'Vasia') # ValueError: Bird - этого класса нет
d1 = Dog('Labrador', 'Asya')
f1 = Fish('Akula', 'Megaladon')

list_animals = [z1, z2, d1, f1]

for animal in list_animals:
    print(animal)
    print(animal.make_voice())
    print(animal.__class__.__name__)

print(d1.runnning())
print(f1.swim())
