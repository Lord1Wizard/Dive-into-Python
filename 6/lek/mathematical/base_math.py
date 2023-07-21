"""
FOur BAse MATH OPERATION
"""

_START_SUM = 0
_START_MULT = 1
_BEGINNING = 0
_CONYTINUATION =1

def add(*args):
    res = _START_SUM
    for item in args:
        res += item
    return res

def sub(*args):
    res = args[_BEGINNING]
    for item in args[_CONYTINUATION:]:
        res -= item
    return res

def mul(*args):
    res = _START_MULT
    for item in args:
        res *= item
    return res

def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONYTINUATION:]:
        res /= item
    return  res

if __name__ == '__main__':
    print(f'{add(2,4) = }')
    print(f'{add(2,4,6,8) = }')
    print(f'{sub(10,8) = }')
    print(f'{mul(2,2,2,2) = }')
    print(f'{div(-100,5,-2) = }')


