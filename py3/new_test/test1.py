#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 14:48
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test1.py
# @Software: PyCharm

from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)

