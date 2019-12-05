#!/usr/bin/python
# -*- coding: utf-8 -*-
# 元组
def tuple():
  empty = ()
  singleton='hello',
  print len(empty)
  print len(singleton)
  t = 12345,54321,'hello!'
  x,y,z = t
  print u"拆分：x:",x,"y:",y,"z:",z
  t = t , "chen"
  print u"整合：",t

# 集合,set
def sets():
  basket = ['apple','orange','apple','pear','orange','banana']
  fruit = set(basket)
  print u"去重：",fruit
  print u"orage是否存在:",'orange' in fruit
  a = set('abracadabra')
  b = set('alacazam')
  print "a:",a
  print "b:",b
  print u"去除b中含有的:",a - b

# 字典，无序的键值对集合,{key:value}
def dictionary():
  tel = {'jack':4098,'sape':4139}
  print tel
  tel['guido']=4127
  print u"增：",tel
  del tel['sape']
  print u"删：",tel
  print u"查jack值:",tel['jack']
  print u"查keys：",tel.keys()
  tel['jack']=1111
  print u"改:",tel

# 转变成字典，dict
def dictToDictionary():
  tel2 = [('sape', 4139), ('guido', 4127), ('jack', 4098)]
  print u"\n原构造函数",tel2
  print u"dict转变成字典",dict(tel2)

# 获取循环的索引位置和对应值，enumerate()
def getEnumerate():
  print u"\n用enumerate()获取循环的索引位置和对应值"
  for i,v in enumerate(['tic','tac','toe']):
    print "key: {0}  value: {1}".format(i,v)

def getZip():
  questions = ['name','quest','favorite color']
  answers = ['lancelot','the holy grail','blue']
  print u"\n用zip()整体打包"
  for q,a in zip(questions,answers):
    print 'What is your {0}? It is {1}.'.format(q,a)  


