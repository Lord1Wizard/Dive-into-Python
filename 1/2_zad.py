year =int(input('Введите год'))
if year % 4 !=0 or year % 100 ==0 and year % 400 !=0 :
    rezult = 'обычный'
else:
    rezult= 'высокосный'
print(rezult)