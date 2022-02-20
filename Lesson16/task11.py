def compare(num1):
    if num1 % 2 == 0:
        mess = "Парное!"
    else:
        mess = "Непарное!"
    return mess
num1 = int(input('Число? ---> '))
y = compare(num1)
print(y)