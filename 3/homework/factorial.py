import time

def fact_mod1(n):
    fact = 1
    for i in range(2, n):
        fact *= i
        while fact % 10 == 0:
            fact = fact // 10
        if fact > 100000:
            fact = fact % 100000
    return f'{fact%10}'
print(fact_mod1(10000))
def fact_mod(n):
    start = time.time()
    fact=1
    k=0
    for j in range(1, n//100):

        for i in range(2, 100):
            fact *= i
            while fact % 10 == 0:
                fact = fact // 10
            if fact > 1000:
                fact = fact % 1000
        k = j * 100
        # print(k)
    if n > 99:
        k += 100
    for i in range(2, n%100):
        if i == n-1:
            print(fact)
        fact *= i
        while fact % 10 == 0:
            fact = fact // 10
        if fact > 1000:
            fact = fact % 1000
    k += n%100-1
    end = time.time()
    return f'{k},{fact%10}'
    # print("The time of execution of above program is :",(end - start), "s")

def fact_old(n):
    start = time.time()
    fact = 1
    for i in range(2,n):
        # if i == 376:
        #     print(i,fact)
        fact *= i
    while fact%10 == 0:
        fact = fact//10
    end = time.time()
    return f'{i},{fact%10}'
    # print("The time of execution of above program is :", (end - start) , "ms")


# for i in range(3,10000):
#     str_1 = fact_mod1(i+1)
#     str_2 = fact_old(i+1)
#     if i%1000 == 0:
#         print(i)
#     if str_1 != str_2:
#         print(i)
#         print(str_1, str_2)
def byte_mmultiplication(a:int, b:int) -> int:
    # Операции сдвига влево << и сдвига вправо >>
    # x = 5  # сдвиг влево на 3 знака, умножение на 2**3 = 8
    # y = x << 3  # y = x*2**3 = 40
    # print('x = ', x)
    # print('y = x<<3 = ', y)
    result = 0
    while (b!=0):
        if(b & 0x1 == 0x1):
            # print('result += a')
            result += a
        b>>=1
        # print('b>>=1')
        a<<=1
        # print('a<<=1')
    return result

# print(byte_mmultiplication(1,3))
