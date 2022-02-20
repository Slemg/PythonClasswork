def compare_max(num1,num2,num3):
        mess = max(num1,num2,num3)
        return mess
num1 = int(input('Первое число? ---> '))
num2 = int(input('Второе число? ---> '))
num3 = int(input('Третье число? ---> '))
y = compare_max(num1,num2,num3)
print(f"Самое большок число {y}")