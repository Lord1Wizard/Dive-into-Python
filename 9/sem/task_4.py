# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def call_count(num):
    def decorator(func):
        result = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return decorator


@call_count(5)
def printer(string):
    print(string)
    return 'ок'

print(printer('сработало'))