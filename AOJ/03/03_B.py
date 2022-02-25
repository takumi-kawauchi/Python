i = 0
l = []
while True :
    x = int(input())
    l.append(x)
    i += 1
    if x == 0 :
        break
for j in range(i-1) :
    print("Case {}: {}".format(j+1,l[j]))

