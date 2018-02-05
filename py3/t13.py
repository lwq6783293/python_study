#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 15:33
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t13.py
# @Software: PyCharm

# TODO 装饰器

# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
# def now():
#     print('2018-02-25')
#
# f = now
# print(f())
#
# # __name__属性，可以拿到函数的名字
# print(f.__name__)
# print(now.__name__)

'''
现在，假设我们要增强 now()函数的功能，比如，在函数调用前后自动
打印日志，但又不希望修改 now()函数的定义，这种在代码运行期间动
态增加功能的方式，称之为“装饰器”（Decorator）
'''
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-02-25')

# 调用 now()函数，不仅会运行 now()函数本身，还会在运行 now()函数前打印一行日志
print(now())





