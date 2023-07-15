# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

dict_companies = {}

company_names = ["aaa", "bbb", "ccc"]
aaa_digit = [10, -20, 30, 40]
bbb_digit = [21, 212, -44]
ccc_digit = [333, -3333, 22222]

dict_companies[company_names[0]] = aaa_digit
dict_companies[company_names[1]] = bbb_digit
dict_companies[company_names[2]] = ccc_digit

def is_all_rentable(companies):
    return all([sum(i) > 0 for i in companies.values()])

print(is_all_rentable(dict_companies))