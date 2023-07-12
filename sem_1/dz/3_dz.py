# ✔Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

num = randint(0, 1000)
count = 10
while True:
    print('Попытка №', count, num)
    a = int(input('Введите число от 0 до 1000: '))
    count -= 1
    i = 0
    if not count:
        print('Попытки закончились')
        break
    if a > 1000 or a < 0:
        print('Введено число не из указанного интервала.')
        continue
    if a < num:
        print('Введенное число меньше задуманного')
        continue
    elif a > num:
        print('Введенное число больше задуманного')
        continue
    else:
        print('Вы угадали')
        break
