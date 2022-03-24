r, c = map(int, input().split())
l =[]
m = []
o = []
#入力内容をリストに格納
for i in range(r) :
    l = input().split()
    for j in range(c):
        l[j] = int(l[j])
    m.append(l)
#行の合計を計算
for i in range(len(m)):
    m[i].append(sum(m[i]))
#列の合計を計算
for j in range(len(m[0])):
    s_r = 0
    for k in range(r):
        s_r += m[k][j]
    o.append(s_r)
m.append(o)
#出力
for i in m :
    print(*i)
