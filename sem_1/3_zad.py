while True:
    num =int(input('Введите число от 1 до 999'))
    if num < 1 or num > 999:
        continue
    if 10 > num > 0:
        result = f"Введена одна цифра, её квадрат равен {num**2}"
    elif 100 > num > 9:
        result = f"Введено двузначное число, произведение цифр равно {(num//10)*(num%10)}"
    else:
        result=f"Введено трехзначное число, отзеркаленное : {int(str(num)[::-1])}"
    print(result)
    break

