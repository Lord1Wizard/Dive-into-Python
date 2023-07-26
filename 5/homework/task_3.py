# Создайте функцию генератор чисел Фибоначчи

def fib():
    """Функция генератор чисел Фибоначчи"""
    fib1 = 1
    fib2 = 0
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        yield fib2

gen =fib()

for i in range(10):
    print(next(gen))

