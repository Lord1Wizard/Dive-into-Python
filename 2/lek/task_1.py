a = 5
print(type(a),id(a))
print(isinstance(a, int))
a = 'hello world'
print(type(a),id(a))
print(isinstance(a, int))
a = 42.0 * 3.141592 / 2.71828
print(type(a),id(a))
print(isinstance(a, (int, float, complex)))
num = 2 + 2 * 2
digit = 36 / 6
print(num, digit)
print(num == digit)
print(num is digit)
digit = num
print(num, digit)
print(num is digit)
x = 42
y = 'text'
z = 3.14159
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
# print(hash(my_list))
str = input('input text')
print(type(str), id(str), hash(str))
