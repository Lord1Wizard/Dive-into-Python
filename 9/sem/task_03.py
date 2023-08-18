# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json
import os


def json_saver(func):
    if os.path.isfile(f'{func.__name__}.json'):
        with open(f'{func.__name__}.json', 'r', encoding='utf-8') as f_read:
            my_dict = json.load(f_read)
    else:
        my_dict = {}

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f_write:
            my_dict.update({'args: ' + str(args): 'result: ' + str(result)})
            print(my_dict)
            json.dump(my_dict, f_write, indent=2, ensure_ascii=False)
        return result

    return wrapper


@json_saver
def summa(a, b, c):
    return a + b + c


summa(1, 1, 3)
