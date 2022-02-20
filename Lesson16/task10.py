list_ss = [2,7,1,4,2,3,9,3,5,6] 
def copypaste(text,n):
        return text
text = list_ss
n = len(list_ss)
y = copypaste(text,n)
for i in range(n):
    list_ss.pop(0)
    list_ss.append("*")
    n = len(list_ss)
zxc = "".join(y)
print(zxc)
    
