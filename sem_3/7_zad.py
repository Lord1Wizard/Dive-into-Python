#✔Пользователь вводит строку текста.
# ✔Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

input_str = 'Пользователь вводит строку текста'

count_dict1 = {}
count_dict2 = {}

for i in input_str:
    count_dict1.update({i: input_str.count(i)})
print(count_dict1)

for i in input_str:
    if i not in count_dict2:
        count_dict2.update({i: 1})
    else:
        count_dict2.update({i: count_dict2.get(i)+1})
print(count_dict2)
