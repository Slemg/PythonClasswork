def infinite_information(name,surname):
    info = f"{name} {surname}"
    return info
    



while True:
    print("Если тебе надоели,введи out")
    n = input("Как тебя зовут?")
    if n == "out":
        break
    s = input("Какая у тебя фамилия?")
    y = infinite_information(n,s)
    print(y)


def num():
    a = 1
    for i in range(1, 16):
        print(a)
num()


def number(t, r):
    print(t * r)

item = input("Введите символ или слово: ")
n = int(input("введите кол-во символов"))
#number(int(input("введите кол-во символов"))) #вызов функции
number(item, n)



def describe_pet(animal_type, pet_name):
    # Выводит информацию о животном.
    print(f"\nУ меня есть {animal_type}.")
    print(f"Мой {animal_type} и его зовут {pet_name.title()}.")

describe_pet("хомяк", "гарри")
describe_pet("собака", "вилли")


def describe_pet(animal_type, pet_name):
    # Выводит информацию о животном.
    r = f"\nУ меня есть {animal_type}."
    r += f"\nМой {animal_type} и его зовут {pet_name.title()}."
    return r
#y = f(x)
s = describe_pet("хомяк", "гарри")
print(s)



def user(name, surname, age) :
    r = f"\tЕго зовут {name}, \n\tЕго фамилия {surname},\n\tЕму {age}"
    return r
user_name = input()
user_surname = input()
user_age = input()

result = user(user_name, user_surname, user_age)
print(result)



def user_info(name, surname, age) :
    r = f"\tЕго зовут {name}, \n\tЕго фамилия {surname},\n\tЕму {age}"
    return r
while True :
    user_name = input()
    user_surname = input()
    user_age = input()
    result = user_info(user_name, user_surname, user_age)
    print(result)
    if user_name == "out" or user_surname == "out" or user_age == "out" :
        break