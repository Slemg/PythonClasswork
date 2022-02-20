list_ss = [5,16,72,29,11,217,112,22,34] 
def copypaste(text,n):
        return text
text = list_ss
n = len(list_ss)
y = copypaste(text,n)
for i in range(n-2):
    list_ss.pop(1)
    n = len(list_ss)
print(y)

    