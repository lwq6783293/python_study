
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 16:35
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test3.py
# @Software: PyCharm

# 继承和多态

'''
在 OOP 程序设计中，当我们定义一个 class 的时候，可以从某个现有的
class 继承，新的 class 称为子类（Subclass），而被继承的 class 称为基
类、父类或超类（Base class、 Super class）
'''

class Animal(object):
    def run(self):
        print('Animal is running...')


# 继承Animal类
class Dog(Animal):
    # 也可以对子类增加一些方法
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


'''
继承有什么好处？最大的好处是子类获得了父类的全部功能。由于
Animial 实现了 run()方法，因此， Dog 和 Cat 作为它的子类，什么事也没
干，就自动拥有了 run()方法
'''
dog = Dog()
print(dog.run())

print(dog.eat())

cat = Cat()
print(cat.run())


'''
当我们定义
一个 class 的时候，我们实际上就定义了一种数据类型。我们定义的数
据类型和 Python 自带的数据类型，比如 str、 list、 dict 没什么两样
'''
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

# 判断一个变量是否是某个类型可以用 isinstance()判断
print(isinstance(a, list))

print(isinstance(b, Animal))

print(isinstance(c, Dog))


'''
Dog 是从 Animal 继承下来的，当我
们创建了一个 Dog 的实例 c 时，我们认为 c 的数据类型是 Dog 没错，但 c
同时也是 Animal 也没错， Dog 本来就是 Animal 的一种！
'''
print(isinstance(c, Animal))

'''
所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数
据类型也可以被看做是父类。但是，反过来就不行
'''
b = Animal()
# Dog 可以看成 Animal，但 Animal 不可以看成 Dog
print(isinstance(b, Dog))

print('----------------------------------------------------')

# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal 类型的变量
def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Animal()))

print(run_twice(Dog()))

print(run_twice(Cat()))


# 现在，如果我们再定义一个 Tortoise类型，也从 Animal 派生
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


print(run_twice(Tortoise()))

print('-------------------------------------------------------')

class Timer(object):
    def run(self):
        print('Start...')


t = Timer()
print(t.run())




