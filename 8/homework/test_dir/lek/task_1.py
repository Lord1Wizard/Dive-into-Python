import json
a = 'Hello world!'
b = {key: value for key, value in enumerate(a)}
c = json.dumps(b, indent=3, separators=('; ', '= '))
print(type(b))
b = {1 : 'dhfhdsa'}
print(b)
print(c)

for key, value in enumerate(a):
    print(type(key), value)