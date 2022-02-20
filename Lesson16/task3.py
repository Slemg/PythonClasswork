def compare(num1,num2):
    if num1 > num2:
        mess = f"{num1} больше чем {num2}!"
    elif num2 > num1:
        mess = f"{num2} больше чем {num1}!"
    else:
        mess = "equal"
    return mess
num1 = int(input('Первое число? ---> '))
num2 = int(input('Второе число? ---> '))
y = compare(num1,num2)
print(y)