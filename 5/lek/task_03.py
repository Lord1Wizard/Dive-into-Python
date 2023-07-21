# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

inp_str = 'abcdef'
my_dict1 = {i: ord(i) for i in inp_str}
print(my_dict1)
dict_iter = iter(my_dict1)
for i in range(0, 5):
    print(next(dict_iter))
