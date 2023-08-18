# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов

from random import randint


def main(func):
    limit = int(input('Введите предел:'))
    count = int(input('Введите количество попыток:'))

    def wrapper():
        nonlocal limit
        nonlocal count
        if not (0 < limit <= 100): limit = randint(1, 100)
        if not (0 < count <= 10): count = randint(1, 10)
        print(limit, count)
        func(limit, count)

    return wrapper


@main
def guess(limit, count):
    print(limit)
    number = randint(1, limit)
    while count > 0:
        in_num = int(input(f'Введите число от 1 до {limit}: '))
        if in_num == number:
            print('Вы угадали')
            break
        elif in_num < number:
            print('у меня больше')
        else:
            print('у меня меньше')
        count -= 1
        print(f'Осталось {count} попыток')

    else:
        print('У вас закончились попытки ')


guess()
