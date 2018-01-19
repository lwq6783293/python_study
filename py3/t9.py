#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 17:17
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t9.py
# @Software: PyCharm

# TODO 切片
# 取一个list或tuple的部分元素是非常常见的操作。比如，一个lsit如下：
L = ['Michael','Sarah','Tracy','Bob','Jack']

# 要求：取前3个元素

# 笨办法
print([L[0],L[1],L[2]])

# 取前 N 个元素，也就是索引为 0-(N-1)的元素，可以用循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

# 利用切片来写
'''
对这种经常取指定索引范围的操作，用循环十分繁琐，因此， Python 提
供了切片（Slice）操作符，能大大简化这种操作
'''
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2,正好是3个元素
print(L[0:3])

# 如果第一个索引是0，还可以省略
print(L[:3])

# 也可以从索引1开始，取出2个元素出来
print(L[1:3])
