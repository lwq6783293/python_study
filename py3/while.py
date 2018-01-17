#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 16:26
# @Author  : Weiqiang.long
# @Site    : 
# @File    : while.py
# @Software: PyCharm

# 猜大小游戏
import random

# uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内
s = int(random.uniform(1,10))
print(s)
m = int(input('输入整数:'))
while m != s:
    if m > s:
        print('大了')
        m = int(input('输入整数:'))
    if m < s:
        print('小了')
        m = int(input('输入整数:'))
    if m == s:
        print('ok')
        break;

#