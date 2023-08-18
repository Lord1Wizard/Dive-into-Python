# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
from random import randint


def main():
    limit = int(input('Введите предел:'))
    count = int(input('Введите количество попыток:'))

    def guess():
        print(limit)
        # limit = limit+2
        number = randint(1, limit)
        nonlocal count
        while count > 0:
            in_num=int(input('Введите число'))
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
    return guess

a = main()
a()
a()