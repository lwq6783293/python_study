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

print('------------------------------------------------------------------------')

# 关键字参数
'''
可变参数允许你传入 0 个或任意个参数，这些可变参数在函数调用时自
动组装为一个 tuple。而关键字参数允许你传入 0 个或任意个含参数名的
参数，这些关键字参数在函数内部自动组装为一个 dict。
'''
def person(name, age, **kw):
    print('name:',name, 'age:',age, 'other:',kw)

# 函数person出了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
print(person('longweiqiang', 30))

# 也可以传入任意个数的关键字参数
print(person('longweiqiang', 26, city='Shanghai'))

'''
关键字参数的作用在于它可以扩展函数的功能。
比如，在 person 函数里，我们保证能接收到 name 和 age 这两个参数，
但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，
除了用户名和年龄是必填项外，其他都是可选项，
利用关键字参数来定义这个函数就能满足注册的需求
'''

# 和可变参数类似，也可以先组装出一个 dict，然后，把该 dict 转换为关键字参数传进去
extra = {'city':'Beijing', 'job':'Engineer'}
print(person('longweiqiang', 22, city=extra['city'], job=extra['job']))

# 简化写法
'''
**extra 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到函
数的**kw 参数， kw 将获得一个 dict，注意 kw 获得的 dict 是 extra 的一份
拷贝，对 kw 的改动不会影响到函数外的 extra
'''
print(person('longweiqiang', 20, **extra))

print('------------------------------------------------------------------------')

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于到底传入了哪些，就需要再函数内部通过kw检查
# 举例：检查是否有city和job参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:',name, 'age:',age, 'other:',kw)

# 但是调用者仍可以传入不受限制的关键字参数
print(person('longweiqiang', 18, city='Shanghai', zipcode='123456'))

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。定义如下
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print('name:',name, 'age:',age, 'city:',city, 'job:',job)

# 调用
print(person('longweiqiang', 10, city='Shanghai', job='Engineer'))

# 注意：命名关键字参数必须传入参数名，这个位置参数不同。如果没有传入参数名，调用将报错
# print(person('longweiqiang', 25, 'Shanghai', 'Engineer'))
# 报错信息：TypeError: person() takes 2 positional arguments but 4 were given
# 报错原因：由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数

# 命名关键字参数可以有缺省值，从而简化调用
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

# 由于命名关键字参数city具有默认值，调用时，可不传入city参数
print(person('longweiqiang', 33, job='Engineer'))

'''
注意：
使用命名关键字参数时，要特别注意， *不是参数，而是特殊分隔符。
如果缺少*， Python 解释器将无法识别位置参数和命名关键字参数
    def person(name, age, city, job):
        # 缺少 *， city 和 job 被视为位置参数
        pass
'''

print('------------------------------------------------------------------------')

# 参数组合
'''
在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键
字参数和命名关键字参数，这 5 种参数都可以组合使用，除了可变参数
无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必
选参数、默认参数、可变参数/命名关键字参数和关键字参数
'''

# 定义一个函数，包含上述若干种参数
def f1(a, b, c=0, *args, **kw):
    print('a = ',a, 'b = ',b, 'c = ',c, 'args = ',args, 'kw = ',kw)

def f2(a, b, c=0, *, d, **kw):
    print('a = ',a, 'b = ',b, 'c = ',c, 'd = ',d, 'kw = ',kw)

print(f1(1,2))
print(f1(1,2,c=3))
print(f1(1,2,3,'a','b'))
print(f1(1,2,3,'a','b',x=99))
print(f2(1,2,d=99,ext=None))

# 还可以通过一个tuple和dict，调用上述函数
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
print(f1(*args, **kw))

args = (1,2,3)
kw = {'d':88,'x':'#'}
print(f2(*args, **kw))
'''
所以，对于任意函数，都可以通过类似 func(*args, **kw)的形式调用它，
无论它的参数是如何定义的
'''

'''
小结：
Python 的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：
*args 是可变参数， args 接收的是一个 tuple；
**kw 是关键字参数， kw 接收的是一个 dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入： func(1, 2, 3)，又可以先组装 list 或 tuple，
再通过*args 传入： func(*(1, 2, 3))；

关键字参数既可以直接传入： func(a=1, b=2)，又可以先组装 dict，再通
过**kw 传入： func(**{'a': 1, 'b': 2})。
使用*args 和**kw 是 Python 的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数
'''

print('------------------------------------------------------------------------')

# 递归函数
'''
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，
这个函数就是递归函数
'''
# 举个例子，我们来计算阶乘 n! = 1 x 2 x 3 x ... x n，用函数 fact(n)表示
# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n

# 所以， fact(n)可以表示为 n x fact(n-1)，只有 n=1 时需要特殊处理。
# 于是，fact(n)用递归的方式写出来就是
def fact(n):
    if n==1:
        return 1
    b = fact(n - 1)
    a = n * b
    return a

# 调用递归函数
print(fact(5))

'''
如果我们计算 fact(5)，可以根据函数定义看到计算过程如下：
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''

'''
递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可
以写成循环的方式，但循环的逻辑不如递归清晰
'''

'''
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈
（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层
栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
所以，递归调用的次数过多，会导致栈溢出。可以试试 fact(1000)
'''
# print(fact(1000))

print('------------------------------------------------------------------------')

'''
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的
效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
尾递归是指，在函数返回的时候，调用自身本身，并且， return 语句不
能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递
归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
'''

'''
上面的 fact(n)函数由于 return n * fact(n - 1)引入了乘法表达式，所
以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把
每一步的乘积传入到递归函数中
'''
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
'''
可以看到， return fact_iter(num - 1, num * product)仅返回递归函数本
身， num - 1 和 num * product 在函数调用前就会被计算，不影响函数调用
'''

# 调用上述函数
print(fact_iter(5,1))
# print(fact_iter(1000,1))
'''
遗憾的是，大多数编程语言没有针对尾递归做优化， Python 解释器也没
有做优化，所以，即使把上面的 fact(n)函数改成尾递归方式，也会导
致栈溢出
'''

print('------------------------------------------------------------------------')

# 利用递归函数移动汉诺塔:
# TODO 待练习
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

print(move(4, 'A', 'B', 'C'))


