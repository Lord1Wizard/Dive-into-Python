# from typing import Callable


# def add_one_str(a: str) -> Callable[[str], str]:
def add_one_str(a: str):
    def add_two_str(b: str):
        return a + ' ' + b

    return add_two_str


print(add_one_str('Hello1')('world1'))

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('friend'))
print(hello('World'))
print(bye('Alex'))

def add_one_str_to_list(a: str):
    names = []
    def add_two_str(b: str):
        names.append(b)
        return a + ', ' + ', '.join(names)

    return add_two_str
hello = add_one_str_to_list('Hello')
bye = add_one_str_to_list('Good bye')
print(hello('Alex'))
print(hello('Karina'))
print(bye('Alena'))
