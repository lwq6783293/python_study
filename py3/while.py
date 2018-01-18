#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 16:26
# @Author  : Weiqiang.long
# @Site    : 
# @File    : while.py
# @Software: PyCharm

# 猜大小游戏
# 来源:http://www.runoob.com/python/python-while-loop.html
import random
import sys
import time

# uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内
# s = int(random.uniform(1,10))
# print(s)
# m = int(input('输入整数:'))
# while m != s:
#     if m > s:
#         print('大了')
#         m = int(input('输入整数:'))
#     if m < s:
#         print('小了')
#         m = int(input('输入整数:'))
#     if m == s:
#         print('ok')
#         break;


# 猜拳小游戏
# 来源:http://www.runoob.com/python/python-while-loop.html
# while 1:
#     s = int(random.randint(1,3))
#     if s==1:
#         ind = '石头'
#     elif s==2:
#         ind = '剪子'
#     elif s==3:
#         ind = '布'
#     m = input('输入 石头、剪子、布，输入"end"结束游戏:')
#     blist = ['石头','剪子','布']
#     if (m not in blist) and (m != 'end'):
#         print('输入错误，请重新输入！')
#     elif (m not in blist) and (m=='end'):
#         print('\n游戏退出中...')
#         break
#     elif m==ind:
#         print('电脑出了:' + ind + ',平局')
#     elif (m=='石头' and ind=='剪子') or (m=='剪子' and ind=='布') or (m=='布' and ind=='石头'):
#         print('电脑出了:' + ind + ',你赢了')
#         # print('\n游戏退出中...')
#         # break
#     elif (m=='石头' and ind=='布') or (m=='剪子' and ind=='石头') or (m=='布' and ind=='剪子'):
#         print('电脑出了:' + ind + ',你输了')



# 自己默写的练习
# while 1:
#     s = int(random.randint(1,3))
#     if s==1:
#         ind = '石头'
#     elif s==2:
#         ind = '剪刀'
#     elif s==3:
#         ind = '布'
#     blist = ['石头','剪刀','布']
#     m = input("请输入石头、剪刀、布，输入end退出游戏:")
#     if (m not in blist and m != 'end'):
#         print('输入有误，请重新输入！')
#     elif (m not in blist and m=='end'):
#         print('\n游戏即将退出...')
#         break
#     elif m==ind:
#         print('电脑出了:' + ind + ',平局')
#     elif (m=='石头' and ind=='剪刀') or (m=='剪刀' and ind=='布') or (m=='布' and ind=='石头'):
#         print('电脑出了:' + ind + ',你赢了')
#     # 此处直接把上面的elif判断条件反过来写,增加代码可读性
#     elif (m=='剪刀' and ind=='石头') or (m=='布' and ind=='剪刀') or (m=='石头' and ind=='布'):
#         print('电脑出了:' + ind + ',你输了')




# 摇骰子游戏
# 来源:http://www.runoob.com/python/python-while-loop.html
# TODO 此例子抽时间再看
# result = []
# while True:
#     result.append(int(random.uniform(1,7)))
#     result.append(int(random.uniform(1,7)))
#     result.append(int(random.uniform(1,7)))
#     print(result)
#     count = 0
#     index = 2
#     pointStr = ""
#     while index >= 0:
#         currPoint = result[index]
#         count += currPoint
#         index -= 1
#         pointStr += " "
#         pointStr += str(currPoint)
#     if count <= 11:
#         sys.stdout.write(pointStr + " -> " + "小" + "\n")
#         time.sleep( 1 )   # 睡眠一秒
#     else:
#         sys.stdout.write(pointStr + " -> " + "大" + "\n")
#         time.sleep( 1 )   # 睡眠一秒
#     result = []

# 九九乘法口诀表
# 来源:http://www.runoob.com/python/python-while-loop.html
i = 1
while i:
    j = 1
    while j:
        print(j,"*",i,"=",j*i,'')
        if i==j:
            break
        j = j + 1
        if j >= 10:
            break
    print("\n")
    i = i + 1
    if i >= 10:
        break
