def message(name, age):
    print(f"Hello, {name}, age: {age}")





#Основной код программы
n = input('Введите свое имя--')
i = input('Введите свой возраст--')
message(n, i)

def summ():
    c = a + b
    return c
a = int(input("a ="))
b = int(input("b ="))


y = summ(a, b)
print(y)

def pet(animal_type, name_pet):
    # print(f"У меня есть {animal_type}")
    # print(f"Его зовут {name_pet}")
    mess = f"У меня есть {animal_type}. Его зовут {name_pet}."
    return mess
# y = f(x)

y = pet("Dog", "Lalli")
print(y)