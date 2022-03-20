m, f, r = map(int, input().split())
result = []
while True :
     s = m + f
     if m == -1 and f == -1 and r == -1 :
         break
     elif m == -1 or f == -1 or s < 30 :
        result.append("F")
     elif s >= 80 :
        result.append("A")
     elif s >= 65 and s < 80 : 
        result.append("B")
     elif (s >= 50 and s < 65) or (s >= 30 and s < 50 and r >= 50) :
        result.append("C")
     elif s >= 30 and s < 50 :
        result.append("D")
     m, f, r = map(int, input().split())
for i in range(len(result)):
    print(result[i])
