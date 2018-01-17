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

# if判断条件还可以简写，比如写成:
# if x:
#     print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

print('------------------------------------------------------------------------')

# 再议input
'''
下面的例子反应出Python的input()方法返回的数据类型是str，str不能直接和整数比较，
必须先把str转换成整数。Python提供了int()函数来完成这件事
'''
# birth = input('birth:')
# print(type(birth))
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
'''
输入 1982，结果报错：
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() > int()
'''
# 正确的写法：
# s = input('birth:')
# birth = int(s)
# print(type(birth))
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
#
# print('------------------------------------------------------------------------')

# 练习
'''
小明身高 1.75，体重 80.5kg。请根据 BMI 公式（体重除以身高的平方）
帮小明计算他的 BMI 指数，并根据 BMI 指数：
 低于 18.5：过轻
 18.5-25：正常
 25-28：过重
 28-32：肥胖
 高于 32：严重肥胖
用 if-elif 判断并打印结果：
'''
height = 1.75
weight = 80
bmi = weight/(height**2)
print(bmi)
if bmi > 32:
    print('高于32：严重肥胖')
elif bmi > 28:
    print('28-32：肥胖')
elif bmi > 25:
    print('25-28：过重')
elif bmi > 18.5:
    print('18.5-25：正常')
else:
    print('低于18.5：过轻')











