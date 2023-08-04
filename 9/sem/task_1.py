# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
from random import randint


def main():
    upper_limit, find_try = int(input('Предел? ')), int(input('Попыток? '))
    def try_to_guess():
        lower_limit = 1
        num = randint(lower_limit, upper_limit)
        print(f'Угадай число от{lower_limit} до{upper_limit}\n')
        nonlocal find_try
        tmp = find_try
        while find_try > 0:
            guess_try = int(input('Введите число: '))
            find_try -= 1
            if guess_try < num:
                print('У меня больше')
            if guess_try > num:
                print('У меня меньше')
            if guess_try == num:
                print(f'\nТы угадал за {tmp - find_try} попыток! Число {num}.')
        else:
                print(f'\nНе угадал! Я загадал {num}.')
    return try_to_guess


a = main()
a()