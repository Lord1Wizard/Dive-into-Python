# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


mult = (i for i in range(100) if i % 2 == 0 and i%10+i//10%10!=8)
my_list = list(mult)
print(my_list)

# Второй вариант
mult1=(i for i in range(0 ,101, 2) if sum(map(int, str(i))) != 8)

