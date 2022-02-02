numbers = []
k = 0
n = int(input("Введите кол-во чисел: "))
while True:
    a = int(input("Введите значение: "))
    numbers.append(a)
    if len(numbers) >= n:
        break
for i in numbers:
    k += i
print(k)