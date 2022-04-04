# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 00:03:33 2022

@author: tayun
"""

Str = input()
q = int(input())
order_l = []
for i in range(q):
    order = input()
    order_l.append(order)
for i in range(q):
    ls = order_l[i].split()
    if ls[0] == "print" :
        print(Str[int(ls[1]):int(ls[2])+1])
    elif ls[0] == "reverse":
        Str_r = Str[int(ls[1]):int(ls[2])+1]
        Str = Str[:int(ls[1])] + Str_r[::-1] + Str[int(ls[2])+1:] 
    else:
        Str = Str[:int(ls[1])] + ls[3] + Str[int(ls[2])+1:]
