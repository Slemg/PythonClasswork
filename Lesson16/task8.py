def registration(text1,text2):
    mess = f"<{text1}>{text2}<{text1}>"
    return mess
text1 = input('Тег? ---> ')
text2 = input('Рядок? ---> ')
y = registration(text1,text2)
print(y)