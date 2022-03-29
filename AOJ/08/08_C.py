# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:03:05 2022

@author: tayun
"""

import string
l = []
for j in range(len(string.ascii_lowercase)):
    l.append(string.ascii_lowercase[j])
r = []
for i in range(26):
    r.append(0)
while True:
    try:
        s = input() 
        for i in range(len(s)):
            if s[i] in l or s[i].swapcase() in l :
                j = l.index(s[i].lower())
                r[j] += 1
    except EOFError:
        break
for i in range(len(l)):
    print(l[i] + " : " + str(r[i]))
