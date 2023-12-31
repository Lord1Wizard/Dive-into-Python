import time


def main(func):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result

    return wrapper


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(100) = }')
control = main(factorial)
print(f'{control.__name__}')
print(f'{control(100000) = }')
