n = int(input())
l = [[] for i in range(4)]
r = ['S', 'H', 'C', 'D']
count = 0
while count < n :
    a, b = input().split()
    b = int(b)
    if a == 'S' :
        l[0].append(b)
    elif a == 'H' :
        l[1].append(b)
    elif a == 'C' :
        l[2].append(b)
    elif a == 'D' :
        l[3].append(b)
    count += 1
for i in range(4) :
    for j in range(1,14):
        if j in l[i] :
            continue
        else:
            print(r[i], j)
