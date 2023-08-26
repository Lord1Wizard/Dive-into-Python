# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv
import os


class FIORange:
    """Клас для хранения фамилии имени отчества"""

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


class Student:
    """Клас для хранения данных о студенте и его усп5еваемости"""
    f = FIORange()
    i = FIORange()
    o = FIORange()

    def __init__(self, f, i, o, p_file_name):
        self.f = f
        self.i = i
        self.o = o
        self.lesson = self.csv_read(p_file_name)

    def csv_read(self, p_file_name):
        """Функция чтения списка предметов"""
        my_dict = {}
        if os.path.isfile(p_file_name):
            with open(p_file_name, 'r', newline='', encoding='utf-8') as f_csv:
                csv_read = csv.reader(f_csv, delimiter=';')
                for i, line in enumerate(csv_read):
                    my_dict[line[0]] = {'lesson': [], 'test': []}
        return my_dict

    def __call__(self, les_name, value, type_les='lesson'):
        """Функция добавления оценок"""
        self.validate(les_name, value, type_les)
        self.lesson[les_name][type_les].append(value)

    def calculate_test(self, les_name):
        """Функция считает средний бал по тестам по конкретному предмету"""
        rez = 0
        for value in self.lesson[les_name]['test']:
            rez += value
        rez /= len(self.lesson[les_name]['test'])
        return rez

    def calculate_lesson(self):
        """Функция считает средний бал по всем предметам"""
        rez = 0
        count = 0
        for les_name in self.lesson:
            for value in self.lesson[les_name]['lesson']:
                rez += value
                count += 1
        return rez / count

    def validate(self, les_name, value, type_les):
        """Функция проверяет соответствие введенных данных"""
        if not les_name in self.lesson.keys():
            raise ValueError(f'{les_name} - такого предмета нет')
        if not isinstance(value, int):
            raise ValueError(f'Оценка "{value}" должна быть числом')
        if not (type_les == 'lesson' or type_les == 'test'):
            raise ValueError(f'"{type_les = }" для урока должна быть либо "lesson" либо "test"')
        if type_les == 'lesson':
            if not 2 <= value <= 5:
                raise ValueError(f'Оценка "{value}" для урока должна быть числом от 2 до 5')
        if type_les == 'test':
            if not 0 <= value <= 100:
                raise ValueError(f'Оценка "{value}" для теста должна быть числом от 0 до 100')

    def __str__(self):
        """Функция формирует строковое представление для класса Student"""
        rez = f'{self.f} {self.i} {self.o}\n'
        rez += f'    lesson \n'
        for les_name in self.lesson:
            rez += f'       {les_name} : {self.lesson[les_name]["lesson"]}\n'
        rez += f'    test \n'
        for les_name in self.lesson:
            rez += f'       {les_name} : {self.lesson[les_name]["test"]}\n'
        return rez


if __name__ == '__main__':
    s1 = Student('Ivanon', 'Vasiliy', 'Petrovich', 'lession.csv')
    s1('русский язык', 4)
    s1('математика', 4, )
    s1('русский язык', 5, 'lesson')
    s1('русский язык', 5, 'lesson')
    s1('русский язык', 49, 'test')
    s1('русский язык', 49, 'test')
    s1('русский язык', 49, 'test')
    s1('русский язык', 49, 'test')
    s2 = Student('Sidorow', 'Vasiliy', 'Petrovich', 'lession.csv')
    s2('русский язык', 5)
    s2('математика', 5, )
    s2('физика', 5, 'lesson')
    s2('физика', 5, 'lesson')
    s2('физика', 59, 'test')
    s2('физика', 59, 'test')
    s2('русский язык', 49, 'test')
    s2('физика', 49, 'test')
    print(s1)
    print(s1.calculate_lesson())
    print(s1.calculate_test('русский язык'))
    print(s2)
    print(s2.calculate_lesson())
    print(s2.calculate_test('физика'))