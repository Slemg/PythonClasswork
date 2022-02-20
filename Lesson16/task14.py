def guide(num1):
    return num1
num1 = input('Чью площадь хотите узнать?(трикутник,круг,прямокутник) ---> ')
y = guide(num1)

if y == "трикутник":
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



elif y == "трикутник": 
    def triangle(num1_triangle,num2_triangle):
        mess = num1_triangle*num2_triangle
        return mess
num1_triangle = int(input('Сторона треугольника,на которую проведена высота? '))
num2_triangle = int(input('Высота треугольника? '))
y = triangle(num1_triangle,num2_triangle)
print(y)

elif y == "круг": 
    def circle(num1_circle,num2_circle):
        mess = num2_circle*num1_circle**2
        return mess
num1_circle = int(input('радиус круга? '))
num2_circle = 3,14
y = circle(num1_circle,num2_circle)
print(y)

else y == "прямокутник": 
    def rectangle(num1_rectangle,num2_rectangle):
        mess = num1_rectangle*num2_rectangle
        return mess
num1_rectangle = int(input('Длина прямоугольника? '))
num2_rectangle = int(input('Ширина прямоугольника? '))
y = rectangle(num1_rectangle,num2_rectangle)
print(y)

else:
    print("нет такой фигуры!")




