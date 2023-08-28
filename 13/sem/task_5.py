# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

import json


class UserExeption(Exception):
    pass


class UserLevelExeption(UserExeption):
    pass


class UserPermissionExeption(UserExeption):
    pass


class FIORange:
    """Дискриптор для хранения фамилии имени отчества"""

    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        """Функция проверяет соответствие введенных данных"""
        if not value.isalpha():
            raise ValueError(f'{value} Должно быть текстом')
        if not value.istitle():
            raise ValueError(f'{value} Должно начинаться с заглавной')


class Dostup:
    """Дискриптор для хранения уровня доступа"""

    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        """Функция проверяет соответствие введенных данных"""
        try:
            value = int(value)
        except:
            raise ValueError(f'{value} Должно быть числом')
        if not 1 <= value <= 7:
            raise ValueError(f'{value} Должно быть от 1 до 7')


class User:
    user_name = FIORange()
    user_level = Dostup()

    def __init__(self, user_name, user_id, user_level=6):
        self.user_name = user_name
        self.user_id = user_id
        self.user_level = user_level

    def __eq__(self, other):
        if isinstance(other, User):
            return self.user_name == other.user_name and self.user_id == other.user_id
        return NotImplemented

    def __str__(self):
        return f'id = {self.user_id}, Name = {self.user_name}, Level = {self.user_level}'


if __name__ == '__main__':

    def json_load(path: str = 'my_file.json'):
        user_list = []
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        for key, value in data.items():
            name, level = value.popitem()
            user_list.append(User(name, key, level))
        return user_list


    def json_save(path: str = 'my_file.json', data: dict = {}):
        with open(path, 'w', encoding='utf-8') as f:
            for user in user_list:
                data[user.user_id] = {}
                data[user.user_id][user.user_name] = user.user_level
            json.dump(data, f, indent=2, ensure_ascii=False)


    def login():
        cur_user = None
        print(*user_list)
        try:
            name, pers_id = input('Введите данные для входа(Имя id) через пробел: ').split()
        except ValueError:
            raise UserPermissionExeption
        new_user = User(name, pers_id)
        for user in user_list:
            if new_user == user:
                cur_user = user
        if cur_user == None:
            raise UserPermissionExeption
        else:
            return cur_user


    user_list = json_load()
    cur_user = login()
    while True:

        try:
            name, pers_id, level = input('Введите данные(Имя id уровень) через пробел: ').split()
        except ValueError:
            break
        if cur_user.user_level <= level:
            user_list.append(User(name, pers_id, level))
            json_save()
        else:
            raise UserLevelExeption
