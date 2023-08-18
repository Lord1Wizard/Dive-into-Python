import time


def main(func):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result

    return wrapper


@main
def factorial(n):
    f = 1
    print(n)
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
