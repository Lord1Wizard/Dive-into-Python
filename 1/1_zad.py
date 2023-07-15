
name = "Alex"
age = None
a = 42
print(id(a))
a = 6
print(id(a))
print(name, age, a, 456, 'text',sep=' (=^.^=) ', end=' # ')
print('Any text')

#res = input('Print yuor text: ')
#print('Ты написал ',res)

#age = int(input('Сколько тебе лет?'))
pwd = 'text'
res = input("Введите пароль: ")
if res == pwd:
    print('Доступ разрешен')
else:
    print('Достуа ограничен')
print('Работа завершена')
color = input('Твой любимый цвет')

animals = ['cat', 'dog', 'wolf', 'rate','dragon']

for i, j in enumerate(animals, start=1):
    print(i,j)