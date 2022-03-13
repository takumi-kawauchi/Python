l = []
m = []
r = []
a, b = map(int, input().split())
while a != 0 and b != 0 :
    for i in range(b):
        l.append("#")
    m.append(l)
    r.append(a)
    l =[] 
    a, b = map(int, input().split())
for i in range(len(r)):
    for j in range(r[i]) :
        m[i] = ''.join(m[i])
        print(m[i])
    print("")
