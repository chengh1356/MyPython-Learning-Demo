#_*_coding:utf-8_*_ 

# 输出
# str() 用于将值转化为适于人阅读的形式
# repr() 转化为供解释器读取的形式
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s
print str(s)

for x in range(1, 11):
  print repr(x).rjust(2), repr(x*x).rjust(3),repr(x*x*x).rjust(4)

for x in range(1, 11):
  print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)

# 左侧填充0
print u"\n左侧填充0"
print '12'.zfill(5)
print '-3.14'.zfill(7)
print '3.14159265359'.zfill(7)  

# str.format()'!s' 
# (应用 str() )和 '!r' (应用 repr())可以在格式化之前转换值
print "\nstr.format()"
print "We are the {} who say '{}!'".format('knights','Ni')
print 'This {food} is {adjective}.'.format(
  food='spam', adjective='absolutely horrible')

# ‘**’ 标志将这个字典以关键字参数的方式传入
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}  
print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)