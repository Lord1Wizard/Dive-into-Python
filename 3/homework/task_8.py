# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
import random

things = {'ноутбук', 'планшет', 'телефон на андроиде', 'iphone', 'ipad', 'ipod', 'airpods'}
friends_dict = {}
# Автоматическое заполнения списка вещей взятых друзьями
COUNT_MIN = 3 # минимальное количество вещеЙ которое может взять каждый друг
num_friends = int(input('Ведите количество друзей: '))
for i in range(num_friends):
    friends_dict[f'friend {i}'] = tuple(random.sample(things, int(random.random()*(len(things)-COUNT_MIN))+COUNT_MIN))

        # Ручное заполнение списка для проверки
        # Вещи которые взяли все:  {'ноутбук', 'планшет'}
        # Уникальные вещи :  {'airpods', 'iphone'}
        # ------- Вещи которые есть у всех друзей, кроме одного -------
        # Друг friend 1 не взял {'ipod'}
        # Друг friend 3 не взял {'телефон на андроиде'}
# friends_dict['friend 0'] = ('планшет', 'ноутбук', 'телефон на андроиде', 'ipod')
# friends_dict['friend 1'] = ('планшет', 'ноутбук', 'телефон на андроиде', 'iphone')
# friends_dict['friend 2'] = ('планшет', 'ноутбук', 'телефон на андроиде', 'ipod')
# friends_dict['friend 3'] = ('планшет', 'ноутбук', 'airpods', 'ipod')

intersection_set = things
difference_set = set()
union_set = set()
for key, value in friends_dict.items():
    print(f'{key} Взял с собой в поход - {sorted(set(value),reverse=True)}')
    temp_set = set(value)
    # Вещи которые взяли все
    intersection_set = intersection_set & temp_set
    # Вещи уникальны, есть только у одного друга
    difference_set = (difference_set - temp_set) | (temp_set - union_set)
    union_set = union_set | temp_set
print('\nВещи которые взяли все: ', intersection_set)
print('\nУникальные вещи : ', difference_set)
# Вещи есть у всех друзей кроме одного
print('\n------- Вещи которые есть у всех друзей, кроме одного -------')
for key_curr, value_cur in friends_dict.items():
    intersection_set = things
    for key, value in friends_dict.items():
        temp_set = set(value)
        # Вещи которые взяли все друзья но не проверяется текущий
        if key_curr != key:
            intersection_set = intersection_set & temp_set
    # Проверяем что из того что взяли все друзья не взял текущий  друг
    common_items = intersection_set - set(value_cur)
    if common_items:
        print(f'Друг {key_curr} не взял {common_items}')
