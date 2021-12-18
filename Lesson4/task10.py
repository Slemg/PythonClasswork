import math


x = int(input("Введите x "))
if x > 0:
    y = 2*x-10
elif x == 0:
    y = 0
else:
    y = 2*math.fabs(x)-1
    
print(y)
