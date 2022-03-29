l = []
l1 = []
m = []
m1 =[]
num = []
a, b = map(int, input().split())
while a != 0 and b != 0 :
    #必要なリストの要素を作る
    for i in range(b):
        l.append("#")
    for i in range(b-2) :
        m.append(".")
    m.insert(0,"#")
    m.append("#")
    #複数回繰り返すためにインデックスをそろえて、一旦別のリストに入れておく
    l1.append(l)
    m1.append(m)
    #後にまとめて出力するために行の数を他の要素とインデックスをそろえて格納
    num.append(a)
    #空にして、同じリスト名で繰り返せるようにする
    l =[] 
    m =[]
    a, b = map(int, input().split())
#上で作った要素を行の数に合わせて出力
for i in range(len(num)):
    #リストの中身の要素だけを取り出すための処理
    l1[i] = ''.join(l1[i])
    m1[i] = ''.join(m1[i])
    for j in range(num[i]) :
        #１行目の最終行はl1を、それ以外はm1を出力する
        if j == 0 or j == num[i] -1 :
            print(l1[i])
        else :
            print(m1[i])
    #１行空けて出力するための処理だが、もっと違う方法がある気が…
    print("")
