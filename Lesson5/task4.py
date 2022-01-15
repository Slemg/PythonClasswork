print("k! = 1*2*3*4*5*6......*k")
k = int(input("Введите факториал: "))
p = 1
i = 1
while i<=k:
    p=p*i
    i+=1
    print(p)