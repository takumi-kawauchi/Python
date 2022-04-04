# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 22:32:46 2022

@author: tayun
"""

import string
t_p = 0
h_p = 0
t_l = []
h_l = []
l = string.ascii_lowercase
n = int(input())
for i in range(n):
    t, h = map(str, input().split())
    t_l.append(t)
    h_l.append(h)
for i in range(len(t_l)):
    t = t_l[i]
    h = h_l[i]
    if t == h :
        t_p += 1
        h_p += 1
    elif t > h :
        t_p += 3
    else:
        h_p += 3
print(t_p, h_p)
