# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
from random import randint
from chek import chek_queen as queen

i=0
my_set = set ()
# Размер доски не рекомендую ставить больше 8 - очень долго ждать случайного совпадения
COUNT = 8
# все возможные варианты для поля COUNT на COUNT
print(f'Все возможные варианты для поля {COUNT} на {COUNT}')
queen.arrangement(r=1,count=COUNT)


print(f'\n4 случайных варианта для поля {COUNT} на {COUNT} без проверки на уникальность.\n Ожидаем надписи стоп по окончании генерации')
# Печать 4 случайных варианта без проверки на уникальность
while i<4:
    my_dict = {}
    for j in range(COUNT):
        my_dict[str(j+1)] = str(randint(1,COUNT))
    # if len(my_dict)>COUNT-1:
    # print(my_dict)
    if queen.check(my_dict,COUNT):
        print(f'№ {i+1}. {my_dict = }')
        i += 1

print('Стоп')