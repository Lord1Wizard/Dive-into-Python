# String строки
pi  = 3.14159
print(f'Число Пи с точностью два знака: {pi:.2f}')
data = [3264, 329384, 234234, 2342342342, 234234,232]
for item in data:
    print(f'{item:>10}')

for item in data:
    print(f'{item:<10}')

for item in data:
    print(f'{item:^10}')

num = 2 * pi * data[1]
print(f'{num = :_}')

link = 'https://github.com/Lord1Wizard/Dive-into-Python/tree/main/2/homework'
urls = link.split('/')
print(urls)

# a, b, c = input('Введите три числа через пробел:').split()
# print(c, b, a)
#
# a, b, c, *_ = input('Введите не менее трех чисел через пробел:').split()
# print(c, b, a)

data = ['https:', '', 'github.com', 'Lord1Wizard', 'Dive-into-Python', 'tree', 'main', '2', 'homework']
url = '/'.join(data)
print(url)

text = 'однажды в СТУДЕНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

text = 'Однажды в студеную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))