#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 14:18
# @Author  : Weiqiang.long
# @Site    : 
# @File    : module_test.py
# @Software: PyCharm

# 以内建的sys模块为例，编写一个hello的模块

'一个测试模块'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()