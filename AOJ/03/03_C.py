l = []
while True :
    x, y = map(int, input().split())
    if x == 0 and y == 0 :
        break
    elif x < y :
        l.append([x, y])
    else:
        l.append([y, x])
    
for i in range(len(l)):
    print(*l[i])

