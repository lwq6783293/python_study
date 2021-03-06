#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 14:28
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t6.py
# @Software: PyCharm

# TODO 使用dict和set
# dict
'''
Python内置了字典:dict的支持，dict全称dictionary，在其他语言中也称为map，
使用键值对存储，具有极快的查找速度
'''

# 举例，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list
names = ['Michael','Bob','Tracy']
scores = [95,75,85]

# 自己练手的代码
n = 0
x = 0
while n < len(names):
    while x < len(scores):
        print([names[n],scores[x]])
        n = n + 1
        x = x + 1

print('------------------------------------------------------------------------')

# 用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，代码如下
d = {'Michael':95,'Bob':75,'Tracy':85}
print(type(d))
# print(help(dict))
print(d['Michael'])

# 把数据放入 dict 的方法，除了初始化时指定外，还可以通过 key 放入
d['Adam'] = 67
print(d['Adam'])

# 由于一个 key 只能对应一个 value，所以，多次对一个 key 放入 value，后面的值会把前面的值冲掉
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

'''
注意：如果key不存在，dict就会有如下报错：
print(d['Thomas'])
Traceback (most recent call last):
  File "C:/Users/Administrator/PycharmProjects/python_study/py3/t6.py", line 48, in <module>
    print(d['Thomas'])
KeyError: 'Thomas'
'''

# 要避免key不存在的错误，有两种方法，一种是通过in判断key是否存在
print('Thomas' in d)

# 第二种是通过dict提供的get方法，如果key不存在，可以返回None，或者自己制定的value
print(d.get('Thomas'))
print(d.get('Thomas',-1))
# 注意：返回 None 的时候 Python 的交互式命令行不显示结果

print('------------------------------------------------------------------------')

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d)
print(d.pop('Bob'))
print(d)

'''
和list比较，dict有以下几个特点：
    1.查找和插入的速度极快，不会随着key的增加而增加；
    2.需要占用大量的内存，内存浪费多。
而list相反：
    1.查找和插入的时间随着元素的增加而增加；
    2.占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
'''

'''
dict 的 key 必须是不可变对象。
这是因为 dict 根据 key 来计算 value 的存储位置，如果每次计算相同的
key 得出的结果不同，那 dict 内部就完全混乱了。这个通过 key 计算位
置的算法称为哈希算法（Hash）
'''
print('------------------------------------------------------------------------')

# set
# set和dict相似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3])
print(s)
print(type(s))
'''
注意，传入的参数[1, 2, 3]是一个 list，而显示的{1, 2, 3}只是告诉你
这个 set 内部有 1，2，3 这 3 个元素，显示的顺序也不表示 set 是有序的
'''

# 重复元素在set中自动被过滤掉
s = set([1,1,2,3,4,4,7,9])
print(s)

# 通过add(key)方法，可以添加元素到set中，可以重复添加，但不会有效果
s.add(5)
print(s)

# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)

print('------------------------------------------------------------------------')

'''
set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可
以做数学意义上的交集、并集等操作
'''
s1 = set([1,2,3])
s2 = set([2,3,4])
# 打印出s1与s2的交集
print(s1 & s2)
# 打印出s1与s2的并集
print(s1 | s2)

'''
set 和 dict 的唯一区别仅在于没有存储对应的 value，但是，set的原理和
dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对
象是否相等，也就无法保证 set 内部“不会有重复元素”
'''

print('------------------------------------------------------------------------')

# 再议不可变对象
# str是不变对象，而list是可变对象
# 对于可变对象，比如 list，对 list 进行操作， list 内部的内容是会变化的，比如:
a = ['c','b','a']
# sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
a.sort()
print(a)

print('------------------------------------------------------------------------')

# 而对于不可变对象，比如str，对str进行操作如下：
a = 'abc'
# replace()方法把字符串中的 old（旧字符串）替换成 new(新字符串)，如果指定第三个参数max，则替换不超过max次
print(a.replace('a','A'))
print(a)

print('------------------------------------------------------------------------')

# 虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍然是'abc'
a = 'abc'
b = a.replace('a','A')
print(b)
print(a)

