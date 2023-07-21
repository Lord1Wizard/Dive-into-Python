data = {10, 9, 8, 1, 6, 3}
a, b, c, *d, e = data
print(a, b, c, d, e)
print(type(data))

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 244, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j!= 1)
res = list(mult)
print(f'{len(res)=}\n{res}')
print(type(res))

res = [i + j for i in x if i % 2 != 0 for j in y if j!= 1]
print(f'{len(res)=}\n{res}')
print(type(res))

my_setcomp = {chr(i) for i in range(97,123)}
print(my_setcomp)

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 244, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j!= 1}
print(f'{len(res)=}\n{res}')

my_dictcomp = {i:chr(i) for i in range(97,123)}
print(my_dictcomp)

def factorial(n):
    number = 1
    result = []
    for i in range(1, n+1):
        number *= i
        result.append(number)
    return result

def factorial_gen(n):
    number = 1
    for i in range(1, n+1):
        number *= i
        yield number


for i, num in enumerate(factorial_gen(10), start=1):
    print(f'{i}! = {num}')