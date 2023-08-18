# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
import json
import os
from random import randint

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

def main(func):

    def wrapper():
        limit = int(input('Введите предел:'))
        count = int(input('Введите количество попыток:'))
        # nonlocal limit
        # nonlocal count
        if not (0 < limit <= 100): limit = randint(1, 100)
        if not (0 < count <= 10): count = randint(1, 10)
        print(limit, count)
        func(limit, count)

    return wrapper

def counter(num):
    def decor(func):

        def wrapper(*args, **kwargs):
                for _ in range(num):
                    print(num)
                    func(*args, **kwargs)

        return wrapper
    return decor

@counter(2)
@main
@json_saver
def guess(limit, count):
    print(limit)
    count_temp = count
    number = randint(1, limit)
    while count > 0:
        in_num = int(input(f'Введите число от 1 до {limit}: '))
        if in_num == number:
            print('Вы угадали')
            return f'you won in {count_temp-count+1} attempts'
            # break
        elif in_num < number:
            print('у меня больше')
        else:
            print('у меня меньше')
        count -= 1
        print(f'Осталось {count} попыток')

    else:
        print('У вас закончились попытки ')
        return 'count be over'


guess()
