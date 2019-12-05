#!/usr/bin/python
# -*- coding: utf-8 -*-
# with 语句使得文件之类的对象可以确保总能及时准确地进行清理
with open('文件/chen.txt') as f:
  for line in f:
    print(line)