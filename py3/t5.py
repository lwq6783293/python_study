#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 17:49
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t5.py
# @Software: PyCharm
# TODO 条件判断练习

# TODO if
age = 20
if age >= 18:
    print('your age is',age)
    print('adult')

print('------------------------------------------------------------------------')

# 也可以给if添加一个else语句，意思是，如果if判断是False，不要只想if的内容，去把else执行了
age = 3
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

print('------------------------------------------------------------------------')

# 使用elif做更细致的判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

print('------------------------------------------------------------------------')




