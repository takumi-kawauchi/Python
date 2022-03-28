# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:14:22 2022

@author: tayun
"""

n, m, l = map(int, input().split())
A = []
B = []
for i in range(n):
    a = input().split()
    a1 = []
    for j in range(m):
        a1.append(int(a[j]))
    A.append(a1)
for j in range(m):
    b = input().split()
    b1 = []
    for j in range(l):
        b1.append(int(b[j]))
    B.append(b1)
R = []
for i in range(n):
    h = []
    for k in range(l):
        r = 0
        for j in range(m):
            r += A[i][j] * B[j][k]
        h.append(r)
    R.append(h)    
for i in range(len(R)):
    print(*R[i])


           
    
    

    