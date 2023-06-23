l = []
n = int(input())
a = input().split()
for i in range(n) :
    l.append(int(a[i]))
print(min(l), max(l), sum(l))
