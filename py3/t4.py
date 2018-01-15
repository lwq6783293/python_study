#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 14:10
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t4.py
# @Software: PyCharm
# TODO tuple练习

# 另一种有序列表叫元组:tuple。tuple和list非常相似，但是tuple一旦初始化就不能修改
# 列出同学的名字
classmates = ('Michael','Bob','Tracy')
print(type(classmates))
'''
现在， classmates 这个 tuple 不能变了，它也没有 append()， insert()这样
的方法。其他获取元素的方法和 list 是一样的，你可以正常地使用
classmates[0]， classmates[-1]，但不能赋值成另外的元素
'''

# tuple 的陷阱：当你定义一个 tuple 时，在定义的时候， tuple 的元素就必须被确定下来，比如
t = (1,2)
print(t)

# 定义一个空的tuple，可以写成()
t = ()
print(t)

# 但是，要定义一个只有1个元素的tuple，不能用如下写法
t = (1)
print(t)
print(type(t))
# 此写法定义的不是tuple,是1这个数！这是因为括号()既可以标识tuple，又可以表示数学公式中的小括号，这就产生了歧义
# 因此，python规定，这种情况下，按小括号进行计算，计算结果自然是1

# 只有1个元素的tuple定义时必须加一个逗号，来消除歧义
t = (1,)
print(t)
print(type(t))

# 可变的tuple
# 如果tuple中包含了list，可以更换list中的元素，但tuple的元素是无法更改的
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


# 练习
# 请用索引取出下面 list 的指定元素
L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]

# 打印apple
print(L[0][0])

# 打印Python
print(L[1][1])

# 打印Lisa
print(L[2][2])

