#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 16:25
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t7.py
# @Software: PyCharm
import math
# TODO 函数
# 抽象
# 借助抽象，我们才能不关心底层的具体计算过程，而直接在更高的层次上思考问题


# 调用函数
# 调用求绝对值的函数abs
print(abs(100))
print(abs(-20))
print(abs(12.34))
# print(help(abs))

print('------------------------------------------------------------------------')

# max函数max()可以接收任意多个参数，并返回最大的那个
print(max(1,5,3))

print('------------------------------------------------------------------------')

# 数据类型转换
# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
print(int('123'))
# print(int('12.34'))   # 此行代码会报错，int函数只能将形式上是整数的字符串转换为整数
print(int(float('12.34')))
print(float('12.34'))
print(str(1.23))
print(str(1000))
print(bool(1))
print(bool(''))

print('------------------------------------------------------------------------')

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用abs函数

print('------------------------------------------------------------------------')

# 练习
# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
# hex()函数用于将10进制整数转换成16进制，以字符串形式表示
a = hex(12)
print(a)
print(type(a))

print('------------------------------------------------------------------------')

# 定义函数
'''
在 Python 中，定义一个函数要使用 def 语句，依次写出函数名、括号、
括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值
用 return 语句返回
'''
# 定义一个求绝对值的my_abs函数
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# # 调用my_abs函数
# print(my_abs(1))

'''
请注意，函数体内部的语句在执行时，一旦执行到 return 时，函数就执
行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现
非常复杂的逻辑。
如果没有 return 语句，函数执行完毕后也会返回结果，只是结果为 None。
return None 可以简写为 return
'''

print('------------------------------------------------------------------------')

# 空函数
# 如果想定义一个什么事也不做的函数，可以用pass语句,pass语句可以作为占位符
# def nop():
#     pass


# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError错误，见下面代码
# print(my_abs(1,2))

'''
当传入了不恰当的参数时，内置函数 abs 会检查出参数错误，而我们定
义的 my_abs 没有参数检查，会导致 if 语句出错，出错信息和 abs 不一样。
'''

# 修改my_abs的定义，对参数类型做检查，只允许整数和浮点型的参数
# 数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        # raise语句可以触发自己定义的异常，触发异常后，后面的代码就不会再执行
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 调用新的my_abs函数
# a = my_abs('A')
# print(a)


# 返回多个值
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 调用move函数
r = move(100, 100, 60, math.pi / 6)
print(r)
# Python的函数返回多值时，返回一个tuple
print(type(r))

'''
小结
定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用 return 随时返回函数结果；
函数执行完毕也没有 return 语句时，自动 return None。
函数可以同时返回多个值，但其实就是一个 tuple
'''

print('------------------------------------------------------------------------')

# 练习
# 请定义一个函数quadratic(a,b,c)，接收3个参数，返回一元二次方程：
# ax² + bx + c = 0 的两个解

# 提示：计算平方根可以调用math.sqrt()函数
'''
可以参考：
https://baike.baidu.com/item/%E4%B8%80%E5%85%83%E4%BA%8C%E6%AC%A1%E6%96%B9%E7%A8%8B/7231190?fr=aladdin
中的计算机法
'''
# 来源：http://blog.csdn.net/zmy_3/article/details/51164347
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a is not a number')
    if not isinstance(b,(int,float)):
        raise TypeError('b is not a number')
    if not isinstance(c,(int,float)):
        raise TypeError('c is not a number')
    d = b * b - 4 * a * c
    if a==0:
        if b==0:
            if c==0:
                return '方程根为全体实数'
            else:
                return '方程无根'
        else:
            x1 = c / b
            x2 = x1
            return x1, x2
    else:
        if d < 0:
            return '方程无根'
        else:
            x1 = (-b + math.sqrt(d)) / 2 / a
            x2 = (-b - math.sqrt(d)) / 2 /a
            return x1, x2

# 调用quadratic函数
print(quadratic(2,3,1))

print('------------------------------------------------------------------------')

# 函数的参数
'''
Python 的函数定义非常简单，但灵活度却非常大。除了正常定义的必选
参数外，还可以使用默认参数、可变参数和关键字参数
'''

# 位置参数
# 写一个计算x²的函数
# 对于power(x)函数，参数x就是一个位置参数，调用power函数时，必须传入有且仅有的一个参数x
def power(x):
    return x * x

# 调用power
print(power(9))

print('------------------------------------------------------------------------')

# 计算 x的四次方、x五次方……时，可以把power(x)修改为power(x,n)，用来计算x的n次方

# 修改后的power(x, n)函数有两个参数：x 和 n，这两个参数都是位置参数，
# 调用函数时，传入的两个值按照位置顺序依次赋给参数 x 和 n
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 调用power函数
print(power(5,4))

