#!/usr/bin/python
# -*- coding: utf-8 -*-
# 默认只读 ，r
# 'w'只写，'r+'读写
# 对JPEG,EXE 要加上二进制方式'b'
# f = open(u'car.jpg','rb')
f = open(u'chen.txt','a+')
f.read()
f.write('chen\n')
f.close()
