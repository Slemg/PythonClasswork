import math


x = int(input("Введите x "))
y = int(input("Введите y "))
if x > y:
    z = math.sqrt(x*y)
else:
    z = math.e*x + math.e*y
print(z)
