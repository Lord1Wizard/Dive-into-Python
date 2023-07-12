# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔Целое положительное число
# ✔Вещественное положительное или отрицательное число
# ✔Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква ✔Строку в нижнем регистре в остальных случаях

input_str = input('Введите строку')
if input_str.isdigit():
    print('Целое положительное', int(input_str))
else:
    try:
        print('Вещественное положительное или отрицательное число', float(input_str))
    except:
        if any(i.isupper() for i in input_str):
            print('Строку в нижнем регистре ',input_str.upper())
        else:
            print('Строку в нижнем регистре',input_str.lower())