l = []
while True:
    x = str(input())
    if int(x) == 0 :
        break
    r = 0
    for i in range(len(x)):
        r += int(x[i])        
    l.append(r)  
for i in range(len(l)):
    print(l[i])
    
