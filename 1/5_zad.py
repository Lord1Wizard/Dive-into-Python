print(" "*20+"Таблица умножения")
for i in range(2,11):
    for j in range(2,6):
        print(f"{j} X {i} = {i*j}", end='\t\t')
    print()
print()
for i in range(2,11):
    for j in range(6,10):
        print(f"{j} X {i} = {i*j}", end='\t\t')
    print()