# ✔Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы.
# ✔Слова выводятся отсортированными согласно кодировки Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.


def str_printer(str_input):
    res = ''
    str_input = str_input.split()
    str_input.sort()
    maxx  = max([len(i) for i in str_input])
    for n, s in enumerate(str_input,1):
        res += (f'{n} {s:>{maxx}}\n')
    return res

print(str_printer('Клара украла коралы'))

# 2 вариант
def str_printer(str_input):
    res = ''
    str_input = str_input.split()
    str_input.sort()
    maxx = max([len(i) for i in str_input])
    for n, s in enumerate(str_input, 1):
        res = res + (f"{n} {s:>{maxx}}\n")
    return res


print(str_printer('Карл у Клары украл кораллы'))

