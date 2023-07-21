# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

def quest(question, ansvers, try_count):
    count = try_count
    while try_count:
        print(question)
        ansver = input('Ваш ответ: ')
        if ansver in ansvers:
            print(f'Бинго')
            break
        else:
            print(f'Ответ неверный осталось {count-try_count} попыток')
            try_count -= 1
    else:
        print('Попытки исчерпаны')