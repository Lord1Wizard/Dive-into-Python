# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.
import string

with open('dict.txt', 'r') as f:
    inp_str = f.read()
    f.close()
inp_str = inp_str.translate(str.maketrans('', '', string.punctuation)).lower().split()
my_dict = {}
for item in inp_str:
    my_dict[item] = my_dict.get(item, 0) + 1
sorted_values = sorted(my_dict.values(), reverse=True) # Sort the values

sorted_dict = {}
for i in sorted_values:
    for k in my_dict.keys():
        if my_dict[k] == i:
            sorted_dict[k] = my_dict[k]
i = 0
for key, value in sorted_dict.items():
    if i < 10:
        i += 1
    else:
        break
    print(key , value)
