numbers = []
k = 0
a = int(input("Введите число №1 "))
b = int(input("Введите число №2 "))
c = int(input("Введите число №3 "))
d = int(input("Введите число №4 "))
numbers.append(a)
numbers.append(b)
numbers.append(c)
numbers.append(d)
for i in numbers:
    k+=i
print(k)