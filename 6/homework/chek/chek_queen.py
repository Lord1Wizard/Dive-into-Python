# количество найденных вариантов
num = 0


def check(my_dict, count=8):
    """Проверяет переданный словарь размером count по умолчанию 8"""
    my_sety = set()
    # проверка диаганали
    for key, value in my_dict.items():
        my_sety.add(value)
        for key_t, value_t in my_dict.items():
            if not (key == key_t and value == value_t):
                if abs(int(key) - int(key_t)) == abs(int(value) - int(value_t)):
                    return False
    # Проверка вертикали горизонтали
    if not (len(my_dict) == len(my_sety) == count):
        return False
    return True


def arrangement(my_temp_dict={}, r=1, count=8):
    """Рекурсивно находит все 92 возможных варианта для размера count по умолчанию 8
    r - начало поля включилельно
    count - конец поля включительно
    делал сам на джаве 5 семинар GeekBrains. в доказательство файл на джаве 'main.java'"""
    if r == count+1:
        global num
        if check(my_temp_dict, r-1):
            num += 1
            print(f'№ {num}. {my_temp_dict = }')
    for i in range(1,count+1):
        if check(my_temp_dict, r-1):
            my_temp_dict[str(r)] = str(i)
            arrangement(my_temp_dict, r + 1, count)
            del my_temp_dict[str(r)]


if __name__ == '__main__':
    # Правильный словарь
    my_dict = {'1': '8', '2': '4', '3': '1', '4': '3', '5': '6', '6': '2', '7': '7', '8': '5'}
    # Ошибочный '1': '3', '2': '4' бьют друг друга
    # my_dict = {'1': '3', '2': '4', '3': '1', '4': '3', '5': '6', '6': '2', '7': '7', '8': '5'}
    print(check(my_dict, 8))
    # для поля 8 на 8 поставить 8 ферзей
    num = 0
    arrangement()
    # для поля 1-4 на 1-4 поставить 4 ферзя
    num = 0
    arrangement( r=1,count= 4)
