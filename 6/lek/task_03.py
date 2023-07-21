# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

import random
from sys import argv


def game(*args):
    start, stop, count = int(args[0]), int(args[1]), int(args[2])

    rnd = random.randint(start, stop)
    while int(input(f'{rnd} Введите число от {start} до {stop} у вас осталось {count} попыток: ')) != rnd:
        count -= 1
        if count<1:
            print('Вы не угадали')
            break
    else:
        print('Вы угадали')


game(argv[1], argv[2], argv[3])