def compare(num1):
    if num1 <= 2 or num1 == 12:
        mess = "winter!"
    elif num1 >2 and num1 <=5 :
        mess = "spring!"
    elif num1 >5 and num1 <=8:
        mess = "summer!"
    elif num1 >8 and num1 <=11:
        mess = "autumn!"
    else:
        mess = "нет такого номера для месяца!"
    return mess
num1 = int(input('Номер месяца? ---> '))
y = compare(num1)
print(y)