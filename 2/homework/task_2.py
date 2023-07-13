# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import  fractions
while True:
    inp_str1 = input('Введите первое дробное число')
    inp_str2 = input('Введите второе дробное число')
    inp_str1 = inp_str1.split('/')
    inp_str2 = inp_str2.split('/')
    f1 = fractions.Fraction(int(inp_str1[0]), int(inp_str1[1]))
    f2 = fractions.Fraction(int(inp_str2[0]), int(inp_str2[1]))
    print(f1+f2)
    print(f1 * f2)

    if len(inp_str1) != 2 or len(inp_str2) != 2:
        print('Дробные числа через "/"\n например: 3/7')
        continue
    print('Сумма чисел равна: ',float(inp_str1[0])/float(inp_str1[1])+float(inp_str2[0])/float(inp_str2[1]))
    print('Произведение чисел равно: ',float(inp_str1[0])/float(inp_str1[1])*float(inp_str2[0])/float(inp_str2[1]))

    break