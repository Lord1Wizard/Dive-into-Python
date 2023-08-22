class User:
    """A User training class"""

    def __init__(self, name: str, equipment: list = None):
        """Added the name parametr."""
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
        print(f'Создал {self.name = }')

    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


u_1 = User('Спеленгер', ['протонный ускоритель', 'ловушка'])
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
u_3 = User(name='Спеленгер',equipment=['протонный ускоритель', 'ловушка'])
ghostdusters =[u_1, u_2, u_3]
print(f'Документация класса {User.__doc__ = }')
# print(help(User))
print(u_1)
print(repr(u_1))
print(f'{u_1 = }')
print(f'{ghostdusters = }')
print(*ghostdusters, sep='\n')
