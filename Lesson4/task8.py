side1 = int(input("Введите сторону: "))
side2 = int(input("Введите сторону: "))
side3 = int(input("Введите сторону: "))
if side1 > side2 + side3 or side2 > side3 + side1 or side3 > side2 + side1:
    print("Треугольника не существует")

elif side1**2 > side2**2 + side3**2 and side2 == side3:
    print("Треугольник существует,он тупоугольный и равнобедренный")
elif side2**2 > side3**2 + side1**2 and side1 == side3:
    print("Треугольник существует,он тупоугольный и равнобедренный")
elif side3**2 > side2**2 + side1**2 and side2 == side1:
    print("Треугольник существует,он тупоугольный и равнобедренный")
elif side1**2 < side2**2 + side3**2 and side2 == side3:
    print("Треугольник существует,он остроугольный и равнобедренный")
elif side2**2 < side1**2 + side3**2 and side1 == side3:
    print("Треугольник существует,он остроугольный и равнобедренный")
elif side3**2 < side2**2 + side1**2 and side2 == side1:
    print("Треугольник существует,он остроугольный и равнобедренный")
elif side1**2 == side2**2 + side3**2 and side2 == side3:
    print("Треугольник существует,он прямоугольный и равнобедренный")
elif side2**2 == side3**2 + side1**2 and side1 == side3:
    print("Треугольник существует,он прямоугольный и равнобедренный")
elif side3**2 == side1**2 + side2**2 and side2 == side1:
    print("Треугольник существует,он прямоугольный и равнобедренный")
elif side1**2 > side2**2 + side3**2 and side2 > side3 or side3 > side2:
    print("Треугольник существует,он тупоугольный и разносторонний")
elif side2**2 > side1**2 + side3**2 and side3 > side1 or side3 > side1:
    print("Треугольник существует,он тупоугольный и разносторонний")
elif side3**2 > side1**2 + side2**2 and side2 > side1 or side1 > side2:
    print("Треугольник существует,он тупоугольный и разносторонний")
elif side1**2 < side2**2 + side3**2 and side2 > side3 or side3 > side2:
    print("Треугольник существует,он остроугольный и разносторонний")
elif side2**2 < side1**2 + side3**2 and side3 > side1 or side3 > side1:
    print("Треугольник существует,он остроугольный и разносторонний")
elif side3**2 < side2**2 + side1**2 and side2 > side1 or side1 > side2:
    print("Треугольник существует,он остроугольный и разносторонний")
elif side1**2 == side2**2 + side3**2 and side2 > side3 or side3 > side2:
    print("Треугольник существует,он прямоугольный и разносторонний")
elif side2**2 == side3**2 + side1**2 and side3 > side1 or side3 > side1:
    print("Треугольник существует,он прямоугольный и разносторонний")
elif side3**2 == side2**2 + side1**2 and side2 > side1 or side1 > side2:
    print("Треугольник существует,он прямоугольный и разносторонний")




