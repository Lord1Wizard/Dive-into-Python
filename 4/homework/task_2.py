# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.alse)

def is_hashable(val) -> bool:
    """Функция для проверки на хешируемость"""
    try:
        hash(val)
    except TypeError:
        return False
    return True

def to_dict(**kwargs):
    output = {}
    for k, v in kwargs.items():
        if is_hashable(v):
            output[v] = k
        else:
            output[str(v)] = k
    return output


print(to_dict(spisok=[1, 2, 3], some={4, 5, 6}, a=10, b=2.3, c='str'))
print(to_dict(name='Pankaj', age=34))


