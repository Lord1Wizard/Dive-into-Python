class Person:
    __max_up_ = 3
    _max_level = 80

    def __init__(self, name, race='unknow', speed=100):
        self.level = 1
        self.health = 100
        self.name = name
        self.race = race
        self._speed = speed
        self.up = 3

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up_)
    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1
        else:
            self.level = self._max_level

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)

    def change_health(self, other, quantity):
        self.health += quantity*2
        other.health -= quantity*2

p1 = Person('Сильвия', 'Эльф')
p2 = Hero('archery', 'Вася', 'Человек')
print(f'{p1.name = }, {p1.race = }, {p1.level = }, {p1.health = }, {p1._Person__max_up_ = }')
print(f'{p2.power = }, {p2.name = }, {p2.race = }, {p2.level = }, {p2.health = }, {p2._Person__max_up_ = }')

p1.level_up()
print(f'{p1.name = }, {p1.race = }, {p1.level = }, {p1.health = }, {p1.max_up = }')
print(f'{p2.name = }, {p2.race = }, {p2.level = }, {p2.health = }, {p2.max_up = }')

p1.change_health(p2, 10)
print(f'{p1.name = }, {p1.race = }, {p1.level = }, {p1.health = }, {p1.max_up = }')
print(f'{p2.name = }, {p2.race = }, {p2.level = }, {p2.health = }, {p2.max_up = }')

Person.level = 100

print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

# p1.max_up = 12
# p1.health = 100
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
print(f'{p1.health = }')
# print(f'{p1.health = }, {Person.health = }')
# print(f'{p1.health = }, {p2.health = }')

Person.max_up = 42
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
