# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def counter(num):
    def main(func):
        count = 0
        my_list=[]
        def wrapper(*args, **kwargs):
            nonlocal count
            while count < num:
                count += 1
                print(count, num)
                my_list.append(func(count,*args, **kwargs))
            return my_list

        return wrapper
    return main


@counter(4)
def summa(a, b, c):
    return a + b + c


print(summa(1, 2))
