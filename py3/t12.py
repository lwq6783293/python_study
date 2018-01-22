#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 16:17
# @Author  : Weiqiang.long
# @Site    : 
# @File    : t12.py
# @Software: PyCharm

# TODO 生成器
'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，
列表容量肯定是有限的。而且，创建一个包含 100 万个元素的列表，不
仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面
绝大多数元素占用的空间都白白浪费了

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循
环的过程中不断推算出后续的元素呢？这样就不必创建完整的 list，从
而节省大量的空间。在 Python 中，这种一边循环一边计算的机制，称
为生成器： generator
'''
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个
# 列表生成式的[]改成()，就创建了一个generator
from collections import Iterable

L = [x*x for x in range(10)]
print(L)

g = (x*x for x in range(10))
print(g)
'''
创建L和g的区别仅在于最外层的[]和()，L是一个list,而g是一个generator
'''
# generator打印需要注意
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
'''
next()返回迭代器的下一个项目
next 语法:next(iterator, [default])
参数说明:iterator -- 可迭代对象,
        default -- 可选，用于设置在没有下一个元素时返回该默认值，
        如果不设置，又没有下一个元素则会触发 StopIteration 异常
'''
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('------------------------------------------------------------------------')

# 此处会报错，原因是generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，知道计算到最后一个元素
# 没有更多元素时，抛出StopIteration的错误
# print(next(g))

# 直接调用next(g)太繁琐，正确的方法是使用for循环，因为generator也是可迭代对象
# 判断generator是否可迭代
print(isinstance(g,Iterable))

print('------------------------------------------------------------------------')

# 使用for循环
g = (x*x for x in range(10))
for n in g:
    print(n)
'''
所以，我们创建了一个 generator 后，基本上永远不会调用 next()，而是
通过 for 循环来迭代它，并且不需要关心 StopIteration 的错误
'''

print('------------------------------------------------------------------------')

# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# 调用fib函数，输出斐波那契数列的前 N 个数
print(fib(10))

print('------------------------------------------------------------------------')

# 要把 fib 函数变成generator，只需要把print(b)改为 yield b 就可以了
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # 如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个 generator
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(10))

'''
这里，最难理解的就是 generator 和函数的执行流程不一样。函数是顺
序执行，遇到 return 语句或者最后一行函数语句就返回。而变成
generator 的函数，在每次调用 next()的时候执行，遇到 yield 语句返回，
再次执行时从上次返回的 yield 语句处继续执行
'''

# 举个例子：定义一个generator，依次返回数字1,3,5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值
o = odd()
print(next(o))
print(next(o))
print(next(o))
# print(next(o))

'''
可以看到， odd 不是普通函数，而是 generator，在执行过程中，遇到 yield
就中断，下次又继续执行。执行 3 次 yield 后，已经没有 yield 可以执
行了，所以，第 4 次调用 next(o)就报错
'''

print('------------------------------------------------------------------------')

'''
回到fib的例子，我们在循环过程中不断调用 yield，就会不断中断。
当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
同样的，把函数改成generator后，我们基本上从来不会用 next()来获取
下一个返回值，而是直接使用for循环来迭代
'''
for n in fib(10):
    print(n)

print('------------------------------------------------------------------------')

'''
但是用 for 循环调用 generator 时，发现拿不到 generator 的 return 语句
的返回值。如果想要拿到返回值，必须捕获 StopIteration 错误，返回值
包含在 StopIteration 的 value 中
'''
g = fib(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break



