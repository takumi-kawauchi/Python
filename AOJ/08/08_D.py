# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:47:20 2022

@author: tayun
"""

s = input()
p = input()
count = 0
for i in range(len(s)):
    s = s[-1] + s
    s = s[:-1]
    if p in s :
        count = 1
        break
if count == 1 :
    print("Yes")
else:
    print("No")

    
    