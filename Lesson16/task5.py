def compare(num1,num2,num3):
    if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
        mess = "Треугольник существует!"
    else:
        mess = "Треугольник не существует!"
    return mess
num1 = int(input('Первая сторона? ---> '))
num2 = int(input('Вторая сторона? ---> '))
num3 = int(input('Третья сторона? ---> '))
y = compare(num1,num2,num3)
print(y)