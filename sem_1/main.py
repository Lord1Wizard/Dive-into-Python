# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input("Введите n"))
    e = int(input("Введите e"))
    i=0
    summa=0
    while i < n :
        if i % e != 0 :
            summa+=i
        i+=2
    print(summa)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/