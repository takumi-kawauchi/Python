A = []
B = []
n, m = map(int, input().split())
for i in range(n):
    l = []
    l = input().split()
    for j in range(m):
        l[j] = int(l[j])
    A.append(l)
for j in range(m):
    B.append(int(input()))
for i in range(n):
    r = 0
    for j in range(m):
        r += A[i][j] * B[j]
    print(r)

