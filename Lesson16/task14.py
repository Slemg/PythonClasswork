def triangle(num1_triangle,num2_triangle):
         mess = num1_triangle*num2_triangle
         return mess
def compare(num1,num2,num3):
        if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
            mess = "Треугольник существует!"
        else:
            mess = "Треугольник не существует!"
        return mess

def circle(num1_circle,num2_circle):
         mess = num2_circle*num1_circle**2
         return mess
def rectangle(num1_rectangle,num2_rectangle):
         mess = num1_rectangle*num2_rectangle
         return mess



def guide(num1):
    return num1
num1 = input('Чью площадь хотите узнать?(трикутник,круг,прямокутник) ---> ')
y = guide(num1)
if num1 == "трикутник":
    num1 = int(input('Первая сторона? ---> '))
    num2 = int(input('Вторая сторона? ---> '))
    num3 = int(input('Третья сторона? ---> '))
    y = compare(num1,num2,num3)
    print(y)
    if y == "Треугольник существует!":
        num1_triangle = int(input('Длина стороны треугольника,на которую проведена высота? '))
        num2_triangle = int(input('Высота треугольника? '))
        zxc = triangle(num1_triangle,num2_triangle)
        print(f"Площадь треугольника: {zxc} см")
    else:
        print("Невозможно подсчитать площадь!")

elif num1 == "круг":
   num1_circle = int(input('радиус круга? '))
   num2_circle = 3.14
   x = circle(num1_circle,num2_circle)
   print(f"Площадь круга: {x} см")
elif num1 == "прямокутник":
    num1_rectangle = int(input('Длина прямоугольника? '))
    num2_rectangle = int(input('Ширина прямоугольника? '))
    z = rectangle(num1_rectangle,num2_rectangle)
    print(f"Площадь прямоугольника: {z} см")

    








# def circle(num1_circle,num2_circle):
#         mess = num2_circle*num1_circle**2
#         return mess
# 

# def rectangle(num1_rectangle,num2_rectangle):
#         mess = num1_rectangle*num2_rectangle
#         return mess














# elif y == "круг": 
#     
# else y == "прямокутник": 
#     

# else:
#     print("нет такой фигуры!")




