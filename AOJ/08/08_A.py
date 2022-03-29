# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:36:13 2022

@author: tayun
"""

l = []
l = input().split(', ')
for i in range(len(l)):
    l[i] = l[i].swapcase()
print(*l, sep=", ")



    
    