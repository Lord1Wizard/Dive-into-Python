# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json


def json_saver(func):
    def wrapper(*args, **kwargs):
        with open(f'{func.__name__}.json','a') as file:
            temp_dict = {'args' : args}
            temp_dict.update(kwargs)
            result = func(*args, **kwargs)
            temp_dict['result'] = result
            json.dump(temp_dict, file, indent=3, ensure_ascii=False)
        return result
    return wrapper
@json_saver
def example(a,b,c ='5'):
    return max(a,b,c)

print(example(1,2,3))