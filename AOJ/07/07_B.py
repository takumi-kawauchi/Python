l = []
m = []
r = []
result = []
n, x = map(int, input().split())
while True :
    if x == 0 and n == 0 :
        break
    m = []
    r = []
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            for k in range(1, n+1) :
                s = i + j + k
                if i == j or j == k or i == k :
                    break
                elif s == x :
                    l.append(i)
                    l.append(j)
                    l.append(k)
                    m.append(l)
                l = []
    for i in range(len(m)):
        m[i] = sorted(m[i])
        if m[i] not in r :
            r.append(m[i])
    result.append(len(r))
    n, x = map(int, input().split())
for i in range(len(result)):
    print(result[i])
