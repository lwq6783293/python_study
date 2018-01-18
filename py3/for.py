#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 11:46
# @Author  : Weiqiang.long
# @Site    : 
# @File    : for.py
# @Software: PyCharm

# 冒泡排序
# 来源:http://www.runoob.com/python/python-for-loop.html

# 定义一个list
arsys = [1,3,2,7,45,9,10,8,4,6,11,5]
for i in range(len(arsys)):
    for j in range(i+1):
        if arsys[i] < arsys[j]:
            # 实现两个变量的互换
            arsys[i],arsys[j] = arsys[j],arsys[i]
print(arsys)

