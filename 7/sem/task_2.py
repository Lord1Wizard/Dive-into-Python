# Напишите функцию, которая генерирует псевдоимена.
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔Полученные имена сохраните в файл
from random import random, randint, sample, shuffle

COSONANT = 'бвгджзйклмнпрстфхчцшщ'
VOWEL ='аеёиоуыэюя'

def name_gen(filename):
    a = randint(4, 7)
    v = randint(1, a - 2)
    s = sample(VOWEL, v) + sample(COSONANT, a - v)
    shuffle(s)
    print(''.join(s).title())
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(''.join(s).title()+'\n')

name_gen('name.txt')0