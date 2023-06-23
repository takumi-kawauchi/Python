# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:26:01 2022

@author: tayun
"""
result = []
while True:
    l = []
    s = input()
    if s == "-" :
        break
    else:
        m = int(input())
        for i in range(m):
            l.append(int(input()))
        for j in range(m):
            for k in range(l[j]):
                s += s[0]
                s = s[1:]
        result.append(s)
for i in range(len(result)):
    print(result[i])
