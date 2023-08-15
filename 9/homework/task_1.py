import csv
import json
import os
from random import randint


def find_root_test(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0 and a != 0:
        x1 = (-b + discr ** (1 / 2)) / (2 * a)
        x2 = (-b - discr ** (1 / 2)) / (2 * a)
        return f'X1 = {x1}, X2 = {x2}'
    elif discr == 0:
        x = -b / (2 * a)
        return f'X = {x}'
    else:
        return 'нет'


def give_numbers():
    quant = randint(100, 1000)
    with open('three_random_numbers.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for _ in range(quant):
            writer.writerow([randint(-50, 50) for _ in range(3)])


def json_save(func):
    def wrapper(*args, **kwargs):
        if os.path.isfile('result.json'):
            with open('result.json') as f_read:
                data = json.load(f_read)
        else:
            data = {}
        with open('result.json', 'w') as f_write:
            data.update({'args: ' + str(args): 'roots: ' + func(*args, **kwargs)})
            json.dump(data, f_write, indent=2, ensure_ascii=False)
        result = func(*args, **kwargs)
        return result

    return wrapper


def root_csv(func):
    def wrapper(*args, **kwargs):
        with open('three_random_numbers.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                a, b, c = map(int, line)
                func(a, b, c)
        result = func(*args, **kwargs)
        return result

    return wrapper


@root_csv
@json_save
def find_root(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0 and a != 0:
        x1 = (-b + discr ** (1 / 2)) / (2 * a)
        x2 = (-b - discr ** (1 / 2)) / (2 * a)
        return f'X1 = {x1}, X2 = {x2}'
    elif discr == 0:
        x = -b / (2 * a)
        return f'X = {x}'
    else:
        return 'нет'

give_numbers()
print(find_root(1, 2, -3))