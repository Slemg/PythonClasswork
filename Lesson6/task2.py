print("S = 1 + 2 + 3 + 4 + 5 + ....... + n")
s = 0
n = int(input("Введитe n: "))
for x in range(1, n+1):
    s+=x
print(s)