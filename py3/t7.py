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

print('------------------------------------------------------------------------')

# 默认参数
# 如果经常计算x²，所以，完全可以把第二个参数 n 的默认值设定为 2
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 调用power()函数
print(power(3))
print(power(3,3))

# 默认函数最大的优势是能降低调用函数的难度，当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面
# 变化小的参数就可以作为默认参数

print('------------------------------------------------------------------------')

# 例如：一年级小学生注册的函数，需要传入name和gender两个参数：
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

# 调用enroll函数
print(enroll('longweiqiang', 'F'))

print('------------------------------------------------------------------------')

# 如果要继续传入年龄、城市等信息时，可以把年龄和城市设为默认参数
def enroll(name, gender, age=6, city='Shanghai'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

# 调用enroll函数
print(enroll('longweiqiang', 'F'))
print(enroll('longweiqiang', 'F', 5, 'Changsha'))
# 可以按顺序提供默认参数
print(enroll('longweiqiang', 'F', 7))
# 也可以不按顺序提供部分默认参数，但需要把参数名写上
print(enroll('longweiqiang', 'F', city='Tianjin'))

print('------------------------------------------------------------------------')

# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，
# 演示如下：
# 先定义一个函数，传入一个list，添加一个END再返回
def add_end(L=[]):
    L.append('END')
    return L

# 正常调用时，结果没问题
print(add_end([1,2,3]))

# 使用默认参数调用，一开始结果也没问题
print(add_end())

# 当再次调用时，结果就不对了
print(add_end())
'''
原因解释如下：
Python 函数在定义的时候，默认参数 L 的值就被计算出来了，即[]，因
为默认参数 L 也是一个变量，它指向对象[]，每次调用该函数，如果改
变了 L 的内容，则下次调用时，默认参数的内容就变了，不再是函数定
义时的[]了。
所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
'''

print('------------------------------------------------------------------------')

# 要修改上面的例子，我们可以用 None 这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 现在，无论调用多少次，都不会有问题
print(add_end())
print(add_end())
print(add_end())

print('------------------------------------------------------------------------')

# 可变参数
'''
在 Python 函数中，还可以定义可变参数。顾名思义，可变参数就是传
入的参数个数是可变的，可以是 1 个、 2 个到任意个，还可以是 0 个
'''
# 举例：
# 以数学题为例，给定一组数字a，b，c....,请计算a²+b²+c²+....
# 要定义这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c...作为一个list或tuple
# 传进来，这样函数定义如下：
def calc(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum

# 但是调用的时候，需要先组装出一个list或tuple
print(calc([1,2,3]))
print(calc((1,3,5,7)))

# 把函数的参数改为可变参数
def calc(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum

'''
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
但是，调用该函数时，可以传入任意个参数，包括0个参数
'''

# 如果已经有一个 list 或者 tuple，可以写成如下
nums = [1,2,3]
print(calc(nums[0], nums[1], nums[2]))

# 上面的写法可行，但是太复杂，所以Python允许在list或tuple签名加一个*号，把list或tuple的元素变成可变参数传进去
# *nums 表示把 nums 这个 list 的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
print(calc(*nums))

