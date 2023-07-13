# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.


import decimal
import math

decimal.getcontext().prec = 42
while True:
    diam = decimal.Decimal(input('Введите диаметр: '))
    if diam > 1000:
        print('Диаметр должен быть не больше 1000')
        continue
    pi = decimal.Decimal(math.pi)
    s = pi * (diam / 2) ** 2
    print(s)
    le = pi * diam
    print(le)
    break
