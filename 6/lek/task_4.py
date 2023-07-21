import random as rnd
import mathematical.base_math as bm


START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(bm.sub(STOP, START))

print(f'{rnd.randint(START, STOP) = }')
print(f'{rnd.uniform(START, STOP) = }')
print(f'{rnd.choice(data) = }')
print(f'{rnd.randrange(START, STOP, STEP) = }')

print(f'{data = }')
rnd.shuffle(data)
print(f'{data = }')

print(f'{rnd.sample(data, 3) = }')
print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100]))
# print(f'{rnd.sample(data, 3, counts=[2, 4, 6, 8, 42, 73]) = }')

