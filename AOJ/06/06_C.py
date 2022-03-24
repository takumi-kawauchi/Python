m = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())
count = 0
while count < n :
    b, f, r, v = map(int,input().split())
    m[b-1][f-1][r-1] += v
    count += 1
for i in range(4) :
    for j in range(3):
        print(' ' + ' '.join(map(str, m[i][j])))
    if i <= 2 :
        print("####################")
