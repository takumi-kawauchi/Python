l = []
l = input().split(', ')
for i in range(len(l)):
    l[i] = l[i].swapcase()
print(*l, sep=", ")
    
