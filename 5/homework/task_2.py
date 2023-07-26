# ✔Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Ivan', 'Fedor', 'Ekaterina']
salarys = [12_000, 25_000, 30_000]
prizes = ['20.25%', '10.25%', '30%']

#однострочный генератор
my_dict={n : float(s) * float(p[:-1]) / 100 for n, s, p in zip(names,salarys,prizes)}
print(my_dict)

# Функция с проверкой длинны списков
def calculation_salary(name, salary, prize):
    """Функция на вход принимает три списка на выходе словарь. если списки не равны генерируется Exception """
    res = dict()
    if len(name) == len(salary) == len(prize):
        for n in zip(name, salary, prize):
            res[n[0]] = float(n[1]) * float(n[2][:-1]) / 100
        return res
    else:
        raise Exception('Списки разной длинны')


try:
    n = calculation_salary(names,salarys,prizes)
    print(n)
except Exception as e:
    print(e.args)
