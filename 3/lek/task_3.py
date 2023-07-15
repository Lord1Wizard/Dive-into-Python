# Словари, dict
# {}

a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(a == b == c)

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
x = 10
my_dict['ten'] = x
print(my_dict)

print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))
print(my_dict)

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())
for key in my_dict.keys():
    print(key)
print(my_dict.values())
for value in my_dict.values():
    print(value)

print(my_dict.items())
for tuple_data in my_dict.items():
    print(tuple_data)
for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')

spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')

spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
#err = my_dict.pop('six') # KeyError: 'six'
#err = my_dict.pop() # TypeError: pop expected at least 1 argument, got 0

my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)
