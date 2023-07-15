# ✔Функция принимает на вход три списка одинаковой длины: ✔имена str, ✔ставка int, ✔премия str с указанием процентов вида «10.25%».
# ✔Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔Сумма рассчитывается как ставка умноженная на процент премии.


def grants_dict(names, pays, percents):
    percents = list(map(lambda x: float(x[:-1])/100, percents))
    return {name: pay*percents for name, pay, percents in zip(names, pays, percents)}


names = ['Иван', 'Петр', 'Михаил']
pays = [10000, 15000,20000]
percents = ['50.25%', '20%', '30.6%']

print(grants_dict(names, pays, percents))
# 2 вариант
def treat(list_a, list_b, list_c):
    res_dict= {}
    for i in range(len(list_a)):
        res_dict[list_a[i]] = list_b[i] * float(list_c[i][:-1])/100
    return res_dict


# однострочник: {k: v for k, v in zip(name, [x[0] * float(x[1][:-1]) / 100 for x in zip(pays, percents)])}