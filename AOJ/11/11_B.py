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
    
    #命令通りにサイコロを転がすための関数
    def orders(self, order):
        if order == "E" :
            self.top, self.left, self.bottom, self.right = \
            self.left, self.bottom, self.right, self.top
        if order == "S":
            self.top, self.front, self.bottom, self.back = \
            self.back, self.top, self.front, self.bottom
        if order == "W":
            self.top, self.left, self.bottom, self.right = \
            self.right, self.top, self.left, self.bottom
        if order == "N":
            self.top, self.front, self.bottom, self.back = \
            self.front, self.bottom, self.back, self.top
    
    #転がし終わった後、上面の数字を取得する関数
    def show_top(self):
        return self.top
