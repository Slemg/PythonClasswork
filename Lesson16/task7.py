def integer(num1,num2,num3,summa, comma=1):
    if num3 == "+": 
        summa = num1 + num2
    elif num3 == "-": 
        summa = num1 - num2
    elif num3 == "*": 
        summa = num1 * num2
    elif num3 == "/": 
        summa = num1 / num2
    else:
        summa = "Unknown operation"
        return summa
    return f"{summa:.{comma}f}"
num1 = int(input('Первое число? ---> '))
num2 = int(input('Второе число? ---> '))
num3 = (input('Операция (+, -, *, /)? ---> '))
summa = 0
y = integer(num1,num2,num3,summa,2)
print(y)