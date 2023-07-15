# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы.
# ✔Слова выводятся отсортированными согласно кодировки Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.


#input_str=input('Введите предложение')
input_str = 'Пользователь вводит строку текста'
sub_string = input_str.split()
sub_string.sort()
print(sub_string)
max_len = 0
for i in sub_string:
    if len(i) > max_len:
        max_len = len(i)

for i in range(len(sub_string)):
    #print(f'{i}{(max_len-len(sub_strings[i])*' '} {sub_strings[i]}:>')
    print(f'{i}{sub_string[i]:>{max_len + 1}}')

# 2 решение
words = input('Введите предложение >>> ').split()

max_len = len(max(words, key = len))

# for i in range(len(sorted(words))):
#     print(f"{i+1}.{words[i].rjust(max_len+1)}")

for i in range(len(words)):
    print(f"{i+1}.{sorted(words)[i]: >{max_len+1}}")