#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 17:51
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t2.py
# @Software: PyCharm

print('包含中文的str')

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

# 使用十六进制写中文两个字
print('\u4e2d\u6587')

# bytes 类型的数据用带 b 前缀的单引号或双引号表示
x = b'ABC'
print(x)

# 以 Unicode 表示的 str 通过 encode()方法可以编码为指定的 bytes
print('ABC'.encode('ascii'))
print('中文'.encode('UTF-8'))

# 计算str包含多少个字符，可以用len()函数
print(len('中文'))


# 格式化输出
# 常见占位符有：
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print('Hello,%s'%'world')
print('Hi,%s,you have $%d.,test is %f'%('Michael',1000,2.3))

# 格式化整数和浮点数还可以指定是否补 0 和整数与小数的位数
print('%2d-%02d'%(3,1))
# 使用%.2f来控制输出的小数位数
print('%.2f'%3.1415)
# 如果你不太确定应该用什么， %s 永远起作用，它会把任何数据类型转换为字符串
print('Age:%s. Gender:%s'%(25,True))
# 用%%来表示一个%
print('growth rate: %d %%'%7)

# 练习
# 小明的成绩从去年的 72 分提升到了今年的 85 分，请计算小明成绩提升
# 的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后 1 位
s1 = 72
s2 = 85
r = (s2-s1)/s2*100
print('提升了:%.1f%%'%r)
