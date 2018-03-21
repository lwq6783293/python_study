#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 17:39
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test4.py
# @Software: PyCharm

from py3.new_test.test3 import *

# 获取对象信息

'''
当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
'''

# 使用type()
print(type(123))

print(type('str'))

# 如果一个变量指向函数或者类，也可以用 type()判断
print(type(abs))

# 但是 type()函数返回的是什么类型呢？它返回对应的 Class 类型。如果
# 我们要在 if 语句中判断，就需要比较两个变量的 type 类型是否相同
print(type(123)==type(456))


print('------------------------------------------------------')

'''
判断基本数据类型可以直接写 int， str 等，但如果要判断一个对象是否
是函数怎么办？可以使用 types 模块中定义的常量
'''
import types
def fn():
    pass


print(type(fn)==types.FunctionType)

print(type(abs)==types.BuiltinFunctionType)

print(type(lambda x: x)==types.LambdaType)

print('---------------------------------------------------------')

# 使用 isinstance()
'''
对于 class 的继承关系来说，使用 type()就很不方便。我们要判断 class
的类型，可以使用 isinstance()函数。
我们回顾上次的例子，如果继承关系是：
object -> Animal -> Dog -> Husky
那么， isinstance()就可以告诉我们，一个对象是否是某种类型。先创
建 3 种类型的对象
'''
a = Animal()
d = Dog()
c = Cat()

print(isinstance(c, Cat))

print(isinstance(c, Dog))

print(isinstance(c, Animal))

print(type(Animal))

print('---------------------------------------------------------')

# 使用dir
'''
如果要获得一个对象的所有属性和方法，可以使用 dir()函数，它返回
一个包含字符串的 list，比如，获得一个 str 对象的所有属性和方法
'''
print(dir('ABC'))

print(dir(Animal))


class MyDog(object):
    def __len__(self):
        return 100


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x



dog = MyDog()
print(len(dog))

obj = MyObject()

print(hasattr(obj, 'x'))

print(obj.x)

print(hasattr(obj, 'y'))

print(setattr(obj, 'y', 10))

print(hasattr(obj, 'y'))

print(getattr(obj, 'y'))

print(obj.y)

# 如果试图获取不存在的属性，会抛出 AttributeError 的错误
# 可以传入一个 default 参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404)) # # 获取属性'z'，如果不存在，返回默认值 404

print('---------------------------------------------------------')

# 也可以获得对象的方法
print(hasattr(obj, 'power')) # 判断obj有没有power()方法

print(getattr(obj, 'power')) # 获取属性power()

fn = getattr(obj, 'power') # 获取属性power，并赋值到变量fn
print(fn) # fn指向obj.power

print(fn()) # 调用fn()与调用obj.power()是一样的














