#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 16:13
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test2.py
# @Software: PyCharm

# 类和实例

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    # 允许外部代码要获取 name 和 score，增加get_name，get_score两个方法
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 允许外部代码修改 score，可以再给 Student 类增加set_score 方法
    def set_score(self, score):
        # 对参数做检查，避免传入无效的参数
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


# 调用
bart = Student('Bart Simpson', 60)
print(bart.print_score())
print(bart.get_grade())
print(bart.get_name())
print(bart.set_score(90))
print(bart.get_score())
