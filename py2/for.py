#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 11:19
# @Author  : Weiqiang.long
# @Site    : 
# @File    : for.py
# @Software: PyCharm
#右下三角格式输出九九乘法表
 #左下三角格式输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (j,i,i*j)),
    print '\n'