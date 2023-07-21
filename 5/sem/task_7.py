# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def prime_numbers_gen(n):
    for i in range(2,n+1):
        err = 0
        for j in range(2,i//2+1):
            if i%j==0:
                err = 1
        if err == 0 and i!=1:
            yield i

def prime_numbers_gen1(n):
    count =0
    for i in range(2,n+1):
        err = 0
        for j in range(2,i//2+1):
            # print(i, j)
            if i%j==0:
                err = 1
        if err == 0:
            yield i

for i, z in enumerate(prime_numbers_gen(20), start=1):
    print(f'{i} {z}')

# 2
def simple_generator(n):
    count = 0
    current = 2
    while count <= n:
        flag = True
        for i in range(2, current//2+1):
            if not current % i:
                flag = False
        current += 1
        if flag:
            count += 1
            yield current-1

generator = simple_generator(10)

print(*generator)

# 3
def nums(N):
    print([i for i in range(2, N) if all(i % j != 0 for j in range(2, i))])