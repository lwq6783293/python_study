#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 17:13
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t8.py
# @Software: PyCharm

# TODO 高级特性
# 构造一个1,3,5,7,....,99的列表，可以通过循环实现
# 打印1-99的奇数列表
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)