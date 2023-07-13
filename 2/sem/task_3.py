# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно
def convert(num, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    res=''
    while num > 0:
        res=digits[num%base]+res
        num //= base
    return res

number = int(input('Введите число'))

print(convert(number,2),convert(number,8))
print(bin(number),oct(number))


