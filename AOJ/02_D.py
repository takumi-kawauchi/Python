W,H,x,y,r = map(int,input().split())
if H < y + r or 0 > y - r or  W < x + r or 0 > x - r :
    print("No")
else:
    print("Yes")
