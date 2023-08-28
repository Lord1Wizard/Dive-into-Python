# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_key(input_dict, key=None, value=None):
    try:
        return input_dict[key]
    except :
        return value


if __name__ == '__main__':
    my_dict = {'1': 2, '2': 4}
    print(my_dict.get('1'))
    print(get_key(my_dict, '3', 6))