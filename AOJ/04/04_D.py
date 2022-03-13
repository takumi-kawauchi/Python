n = int(input())
a = input().split()
s = 0
for i in range(n) :
    s += int(a[i])
print(min(*a), max(*a), s)

