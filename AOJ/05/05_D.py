def Check_Num(x) :
    if x % 3 == 0 :
        return True
    else :
        return False
def Include3(x) :
    x = str(x)
    if '3' in x :
        return True
l = []
n = int(input())
for i in range(3,n+1):
    if Check_Num(i) == True :
        l.append(i)
    elif Include3(i) == True :
        l.append(i)
print(*l)
