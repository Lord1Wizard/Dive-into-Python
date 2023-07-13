# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

base = 16
digits = '0123456789abcdefghijklmnopqrstuvwxyz'
res = ''

num = int(input('Введите число: '))
print(hex(num))
while num > 0:
    res = digits[num % base] + res
    num //= base
print(res)
