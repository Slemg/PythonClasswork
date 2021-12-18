side1 = int(input("Введите сторону: "))
side2 = int(input("Введите сторону: "))
side3 = int(input("Введите сторону: "))

if side1 > side2 + side3 or side2 > side3 + side1 or side3 > side2 + side1:
    print("Треугольника не существует") 


elif side1**2 > side2**2 + side3**2 or side2**2 > side3**2 + side1**2 or  side3**2 > side2**2 + side1**2:
    x = ("Треугольник существует,он тупоугольный")

elif side1**2 < side2**2 + side3**2 or side2**2 < side3**2 + side1**2 or  side3**2 < side2**2 + side1**2: 
    x = ("Треугольник существует,он остроугольный")

elif side1**2 == side2**2 + side3**2 or side2**2 == side3**2 + side1**2 or  side3**2 == side2**2 + side1**2: 
    x = ("Треугольник существует,он прямоугольный")

if side2 == side3  or side1 == side3 or side1 == side2:
 y = (" и равнобедренный")
 print(x+y)
else:
 z = (" и разносторонний")
 print(x+z)






