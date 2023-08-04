from random import randint

def main(func):
    def wrapper(upper_limit, find_try):
        if not 0 < upper_limit < 100:
            upper_limit = randint(1, 100)
        if not 0 < find_try < 10:
            find_try = randint(1, 10)
        func(upper_limit, find_try)
    return wrapper

@main
def try_to_guess(upper_limit, find_try):
    num = randint(1, upper_limit)
    print(f'Угадай число от 1 до {upper_limit}.\n')
    tmp = find_try
    while find_try > 0:
        guess_try = int(input('Введи число: '))
        find_try -= 1
        if guess_try < num:
            print('У меня больше.')
        if guess_try > num:
            print('У меня меньше.')
        if guess_try == num:
            print(f'\nТы угадал за {tmp - find_try} попыток! Число {num}.')
    else:
        print(f'\nНе угадал! Я загадал {num}.')



try_to_guess(10, 500)