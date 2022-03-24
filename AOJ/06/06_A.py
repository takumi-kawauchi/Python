l = []
n = int(input())
a = input().split()
for i in range(n):
    l.append(int(a[i]))
l.reverse()
print(*l)

