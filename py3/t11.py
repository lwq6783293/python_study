#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 15:02
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t11.py
# @Software: PyCharm

# TODO 列表生成式
'''
列表生成式即 List Comprehensions，是 Python 内置的非常简单却强大的
可以用来创建 list 的生成式
'''
# 例如，要生成list[1,2,3,4,5,6,7,8,9,10]可以用list(range(1,11))
import os

print(list(range(1,11)))

print('------------------------------------------------------------------------')

# 但如果要生成[1*1, 2*2, 3*3..., 10*10]时，上述方法就不行了
# 方法一是利用循环
L = []
for x in range(1,11):
    L.append(x*x)
print(L)

print('------------------------------------------------------------------------')

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成商品的list
print([x*x for x in range(1,11)])
'''
写列表生成式时，把要生成的元素 x * x 放到前面，后面跟for循环，就可以把list创建出来
'''

print('------------------------------------------------------------------------')

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x*x for x in range(1,11) if x % 2 == 0])

print('------------------------------------------------------------------------')

# 还可以使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
print([m + n for m in 'AB' for n in 'XY'])

print('------------------------------------------------------------------------')

# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])

print('------------------------------------------------------------------------')

# for循环可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代出key和value
d = {'x':'A', 'y':'B', 'z':'C'}
for k,v in d.items():
    print(k, '=', v)

print('------------------------------------------------------------------------')

# 因此，列表生成式也可以使用两个变量来生成list
print([k + '=' + v for k,v in d.items()])

# 最后把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
# 用列表生成式把所有字符串变成小写
'''
Python lower()方法转换字符串中所有大写字符为小写
用法:str.lower()
'''
print([s.lower() for s in L])

print('------------------------------------------------------------------------')

'''
如果 list 中既包含字符串，又包含整数，由于非字符串类型没有 lower()
方法，所以列表生成式会报错
'''
L = ['Hello', 'World', 18, 'IBM', 'Apple', None]
# print([s.lower() for s in L])
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 1, in <listcomp>
AttributeError: 'int' object has no attribute 'lower'
'''

# 使用内建的isinstance函数可以判断一个变量是不是字符串
'''
isinstance()函数来判断一个对象是否是一个已知的类型，类似type()
语法:isinstance(object, classinfo)
参数:object -- 实例对象,classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组
返回值:如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False
'''
x = 'abc'
y = 123
print(isinstance(x,str))
print(isinstance(y,str))

print('------------------------------------------------------------------------')

# 通过添加 if 语句保证列表生成式能正确地执行
L2 = [s.lower() for s in L if isinstance(s,str) == True]
# 期待输出: ['hello', 'world', 'ibm', 'apple']
print(L2)




