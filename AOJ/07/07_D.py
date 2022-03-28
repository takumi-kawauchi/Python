# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:14:22 2022

@author: tayun
"""

n, m, l = map(int, input().split())
A = []
B = []
#行列Aの作成
for i in range(n):
    a = input().split()
    a1 = []
    for j in range(m):
        a1.append(int(a[j]))
    A.append(a1)
#行列Bの作成
for j in range(m):
    b = input().split()
    b1 = []
    for j in range(l):
        b1.append(int(b[j]))
    B.append(b1)
C = []
#行列の積を計算
for i in range(n):
    R = []
    for k in range(l):
        r = 0
        for j in range(m):
            r += A[i][j] * B[j][k]
        R.append(r)
    C.append(R)
#結果を出力    
for i in range(len(C)):
    print(*C[i])


           
    
    

    