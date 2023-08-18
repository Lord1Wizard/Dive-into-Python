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


class Address:
    def __init__(self, country, city, street):
        self.country = country or ''
        self.city = city or ''
        self.street = street or ''

    def say_address(self):
        return f'Адрес героя: {self.country}, {self.city}, {self.street}'


class Weapon:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand or 'Клинок'
        self.right_hand = right_hand or 'Лук'


class Hero(Person, Address, Weapon):
    def __init__(self, power, name=None, race=None, speed=None,
                 country=None, city=None, street=None, left_hand=None, right_hand=None):
        self.power = power
        Person.__init__(self, name, race, speed)
        Address.__init__(self, country, city, street)
        Weapon.__init__(self, left_hand, right_hand)

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2


p1 = Person('Сильвия', 'Эльф')
p2 = Hero('archery', 'Вася', 'Человек', 120, left_hand='Стрела', right_hand='Стрела')
print(f'{p1.name = }, {p1.race = }, {p1.level = }, {p1.health = }, {p1._Person__max_up_ = }')
print(f'{p2.power = }, {p2.name = }, {p2.race = }, {p2.level = }, {p2.health = }, {p2._Person__max_up_ = }')

p1.level_up()
print(f'{p1.name = }, {p1.race = }, {p1.level = }, {p1.health = }, {p1._Person__max_up_ = }')
print(f'{p2.name = }, {p2.race = }, {p2.level = }, {p2.health = }, {p2._Person__max_up_ = }')
print('----------------------------------------------')
p2.change_health(p1, 10)
print(f'{p1.name = }, {p1.race = }, {p1.level = }, {p1.health = }, {p1._Person__max_up_ = }')
print(f'{p2.name = }, {p2.race = }, {p2.level = }, {p2.health = }, {p2._Person__max_up_ = }')

p1.change_health(p2, 10)
print(f'{p1.name = }, {p1.race = }, {p1.level = }, {p1.health = }, {p1._Person__max_up_ = }')
print(f'{p2.name = }, {p2.race = }, {p2.level = }, {p2.health = }, {p2._Person__max_up_ = }')

Person.level = 100

print(f'{Person._Person__max_up_ = }, {p1._Person__max_up_ = }, {p2._Person__max_up_ = }')
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

# p1.max_up = 12
# p1.health = 100
print(f'{Person._Person__max_up_ = }, {p1._Person__max_up_ = }, {p2._Person__max_up_ = }')
print(f'{p1.health = }')
# print(f'{p1.health = }, {Person.health = }')
# print(f'{p1.health = }, {p2.health = }')

Person.max_up = 42
print(f'{Person.max_up = }, {p1._Person__max_up_ = }, {p2._Person__max_up_ = }')

p3 = Hero('archery', 'Kristina', 'Эльф', 120,
          country='Эльфляндия', street='Ночного эльфа', left_hand='Стрела')

print(f'{p3.say_address()}')
print(f'{p3.left_hand = }, {p3.right_hand = }')