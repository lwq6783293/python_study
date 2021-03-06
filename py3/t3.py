#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 18:42
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t3.py
# @Software: PyCharm

# TODO list练习
# list:是一种有序的集合，可以随时添加和删除其中的元素
# 列出班里所有同学的名字，就可以用一个list表示：
classmates = ['Michael','Bob','Tracy']
# 打印classmates
print(classmates)
print('------------------------------------------------------------------------')

# 变量classmates就是一个list，用len()函数可以获得list元素的个数
print(len(classmates))
print('------------------------------------------------------------------------')

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(classmates[0])
print(classmates[1])
print(classmates[2])
print('------------------------------------------------------------------------')

# 此list的长度只有3，当索引超出了范围时，python会报一个IndexError错误，要确保索引不要越界
# print(classmates[3])

# 最后一个元素的索引是len(classmates)-1,得到2,那么classmates最大索引则等于2
print(len(classmates)-1)
print('------------------------------------------------------------------------')

# 如果要取最后一个元素，出了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])
print('------------------------------------------------------------------------')

# 以此类推，可以获取倒数第2个，倒数第3个
print(classmates[-2])
print(classmates[-3])
print('------------------------------------------------------------------------')

# 需要注意，这种方法也不能索引越界，否则依然会报IndexError错误
# print(classmates[-4])

# list是一个可变的有序列表，所以，可以往list中追加元素到末尾
# append() 方法用于在列表末尾添加新的对象
classmates.append('Adam')

# 打印添加了新对象后的classmates
print(classmates)
print('------------------------------------------------------------------------')

# 也可以把元素插入到指定的位置，比如索引号为1的位置
# insert() 函数用于将指定对象插入列表的指定位置
classmates.insert(1,'Jack')

# 打印添加了新对象后的classmates
print(classmates)
print('------------------------------------------------------------------------')

# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(classmates.pop())
print(classmates)
print('------------------------------------------------------------------------')

# 要删除指定位置的元素，用pop(i)方法，i代表索引位置
print(classmates.pop(1))
print(classmates)
print('------------------------------------------------------------------------')

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)
print('------------------------------------------------------------------------')

# list里面的元素的数据类型也可以不同，比如
L = ['Apple',123,True]
print(L)
print('------------------------------------------------------------------------')

# list元素也可以是另一个list，比如
S = ['Python','Java',['asp','php'],'Scheme']
print(S)
print('------------------------------------------------------------------------')

# 要注意S只有4个元素，其中S[2]又是一个list
print(len(S))

print(len(S[2]))
print(S[2])
print('------------------------------------------------------------------------')

# 如果拆开写就更容易理解了
p = ['asp','php']
s = ['python','java',p,'scheme']

# 要拿到'php'，可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组
print(p[1])
print(s[2][1])
print('------------------------------------------------------------------------')

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0
l = []
print(len(l))


