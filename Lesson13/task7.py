programmists  = {
    "Тим": "08.06.1955",
    "Дональд": "10.01.1938",
    "Брендан": "04.07.1961",
    "Соломон": "28.03.1983"
}

name = str(input("Имя программиста? (Тим/Дональд/Брендан/Соломон) "))
if name in programmists.keys():
    for g in programmists.keys():
        if g == name:
            print(f"{name} родился {programmists[g]} ")
else:
    print(f"Нет такого имени {name}!")