texts = ['Привет','ЗДАРОВА','привеТСТвую']
res = map(lambda x: x.lower(), texts)
print(*res)

numbers = [42, -3, 1024]
res = tuple(filter(lambda x: x>0, numbers))
print(res)

names = ['Иван', 'Николай', 'Петр']
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary*award:.2f}')

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Петр", 109_000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3,key=lambda x: x[1]))

print(min(lst_1, default='empty'))
print(min(*lst_2))
print(min(lst_3,key=lambda x: x[1]))

my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))

if all(map(lambda x: x>0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')

if any(map(lambda x: x>0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')

print(chr(97))
print(chr(1105))
print(chr(128519))

print(ord('a'))
print(ord('а'))

SIZE = 10

def func(a, b, c):
    x = a + b
    print(locals())
    z =x + c
    return z

func(1, 2, 3)

def func1(a, b, c):
    x = a + b
    print(globals())
    z =x + c
    return z

print(globals())
print(f'{func1(1, 2, 3) = }')

print(vars(int))