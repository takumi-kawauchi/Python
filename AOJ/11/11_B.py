# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:43:02 2022

@author: tayun
"""

#クラスを定義（サイコロ）
class Dice:
    #インプットからの値によりサイコロの目を定義するための関数
    def __init__(self, num_list):
        self.top = num_list[0]
        self.front = num_list[1]
        self.right = num_list[2]
        self.left = num_list[3]
        self.back = num_list[4]
        self.bottom = num_list[5]
                
    
    #全ての転がし方を試すための関数
    def orders(self, num_top, num_front):
        #全通り試すことのできる命令のリストを作成
        for order in list("RRRRSRRRRSRRRRSRRRRSERRRRERRRRERRRR"):
            if order == "E" :
                self.top, self.left, self.bottom, self.right = \
                self.left, self.bottom, self.right, self.top
                #指定された上面、前面の値と一致したら、その時に右面を返す。
                if self.top == num_top and self.front == num_front:
                    return self.right 
            if order == "S":
                self.top, self.front, self.bottom, self.back = \
                self.back, self.top, self.front, self.bottom
                if self.top == num_top and self.front == num_front:
                    return self.right
            if order == "R":
                self.right, self.front, self.left, self.back = \
                self.back, self.right, self.front, self.left
                if self.top == num_top and self.front == num_front:
                    return self.right 
    
num_list = list(map(int, input().split()))
order_num = int(input())
#複数の命令に対応できるように結果を格納するためのリストを用意。
result = []
dice = Dice(num_list)
for _ in range(order_num):
    num_top, num_front = map(int, input().split())
    result.append(dice.orders(num_top, num_front))
for _ in result:
    print(_)



