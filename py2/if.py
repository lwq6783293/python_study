#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 15:40
# @Author  : Weiqiang.long
# @Site    : 
# @File    : if.py
# @Software: PyCharm

number = 23
guess = int(raw_input("请输入一个整数:"))

if guess == number:
    print "恭喜你，答对了。"
    print "但是你没赢得任何奖励。"
elif guess < number:
    print "答错了哦，比这个数字要高一点。"
else:
    print "答错了哦，比这个数字要低一点。"

# 这个语句块在if语句执行完毕后执行
print "Done"
