l = []
while True :
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == "+" :
        l.append(a + b)
    elif op == "-" :
        l.append(a - b)
    elif op == "*" :
        l.append(a * b)
    elif op == "/" :
        l.append(a // b)
    elif op == "?" :
        break
print(*l)

