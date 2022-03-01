a, b = map(int, input().split())
d = int(a / b)
r = int(a % b)
f = "{:.5f}".format(d)
print(d, r, f)

