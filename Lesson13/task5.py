n = int(input("Введите число "))
z = 0
for i in range (1,n+1):
    holder = {
        i : i*i
    }
    for i,g in holder.items():
        print(f"Квадрат числа {i}: {g}")
        z+=g
print(f"Cумма квадратов {z}")