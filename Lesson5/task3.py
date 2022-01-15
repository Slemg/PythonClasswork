s = 0
x = 1 
print("S = 1 + 2 + 3 + 4 + 5 ....... + n")
n = int(input("Введите n: "))
while x <= n:
    s+=x
    x+=1
print(f"Сумма {s} при {x-1} слагаемых")
