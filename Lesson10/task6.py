hardware = ["bit","site","video"]
software = ["virus","link","display"]
for i in hardware:
    print(i)
for i in software:
    print(i)
hardware.pop(-1)
software.pop(-1)
hardware.append("code")    
software.append("tab")
print("Loading...")
for i in hardware:
    print(i)
for i in software:
    print(i)
print("Мы заменили последние элементы списков!")