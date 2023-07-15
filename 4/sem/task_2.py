# ✔Напишите функцию, которая принимает строку текста.
# ✔Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.


def to_ord(str_input):

    return sorted(set(map(ord, list(str_input))),reverse=True)

# 2 вариант
# to_ord = lambda x: sorted(set(map(ord, list(x))), reverse = True)



print(to_ord('Карл у Клары украл кораллы'))