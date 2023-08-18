# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import json
import os
from random import randint

def json_saver(func):
    if os.path.isfile(f'{func.__name__}.json'):
        with open(f'{func.__name__}.json', 'r', encoding='utf-8') as f_read:
            my_dict = json.load(f_read)
    else:
        my_dict = {}

    # @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f_write:
            my_dict.update({'args: ' + str(args): 'result: ' + str(result)})
            json.dump(my_dict, f_write, indent=2, ensure_ascii=False)
        return result

    return wrapper

def create_csv():
    """ Генерация csv файла с тремя случайными числами в каждой строке"""
    count = randint(100, 1000)
    with open('my_file.csv', 'w', newline='', encoding='utf-8') as f_csv:
        csv_write = csv.writer(f_csv, delimiter=';')
        for _ in range(count):
            csv_write.writerow([randint(-10, 10) for _ in range(3)])

def calculation_roots(func):
    def wrapper(*args,**kwargs):
        with open('my_file.csv', 'r', encoding='utf-8') as f_csv:
            csv_read = csv.reader(f_csv, delimiter=';')
            for line in csv_read:
                func(int(line[0]), int(line[1]), int(line[2]))
    return wrapper
@calculation_roots
@json_saver
def korni(a, b, c):
    if a == 0:
        if b == 0:
            return 'такого не может быть'
        else:
            return f'x={-c / b}'
    d = b * b - 4 * a * c
    if d > 0:
        x1 = -(b + d ** 0.5) / 2 * a
        x2 = -(b - d ** 0.5) / 2 * a
        return f'{d = } {x1 = } {x2 = }'
    elif d == 0:
        x = -b / 2 * a
        return f'{d = } x1 = x2 = {x}'
    else:
        return f'{d = } нет действительных корней'


create_csv()
korni()

