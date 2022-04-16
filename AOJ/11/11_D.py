# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 23:13:36 2022

@author: tayun
"""

class Dice:
    #インプットからの値によりサイコロの目を定義するための関数
    def __init__(self, num_list1):
        self.top = num_list1[0]
        self.front = num_list1[1]
        self.right = num_list1[2]
        self.left = num_list1[3]
        self.back = num_list1[4]
        self.bottom = num_list1[5]
    #全ての転がし方を試すための関数
    def orders(self, num_list2):
        #全通り試すことのできる命令のリストを作成
        for order in list("RRRRSRRRRSRRRRSRRRRSERRRRERRRRERRRR"):
            if order == "E" :
                self.top, self.left, self.bottom, self.right = \
                self.left, self.bottom, self.right, self.top
                #転がした後のサイコロの状態をリストに格納
                num_list1_up = [self.top, self.front, self.right, self.left, self.back, self.bottom]
                #転がした後のサイコロともう一つのサイコロが一致しているかどうかの判定
                if num_list1_up == num_list2:
                    return True
            if order == "S":
                self.top, self.front, self.bottom, self.back = \
                self.back, self.top, self.front, self.bottom
                num_list1_up = [self.top, self.front, self.right, self.left, self.back, self.bottom]
                if num_list1_up == num_list2:
                    return True
            if order == "R":
                self.right, self.front, self.left, self.back = \
                self.back, self.right, self.front, self.left
                num_list1_up = [self.top, self.front, self.right, self.left, self.back, self.bottom]
                if num_list1_up == num_list2:
                    return True
    
n = int(input())
#n個の空リストを作成
num_list = [None] * n
for i in range(n):
    num_list[i] = list(map(int, input().split()))
#全ての通り試す。
for i in range(n-1):
    for j in range(i+1, n):
        dice = Dice(num_list[i])
        if dice.orders(num_list[j]):
            print('No')
            break
    else:
        continue
    break
else:
    print('Yes')
