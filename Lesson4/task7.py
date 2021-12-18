number = int(input("Каким номером стоит Вася: "))
multiplicity = 2

if number % multiplicity == 0:
    print('Он скажет <второй>')
elif number % multiplicity > 0:
    print(" Он скажет <первый> ")
