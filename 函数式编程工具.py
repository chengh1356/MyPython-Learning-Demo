#coding:utf8
# 过滤器,filter
def f(x):return x % 3 == 0 or x % 5 == 0

print u"\n取2到25之间的能被3或5整除的序列："
print filter(f,range(2,25))

# 每个元素调用function返回值,map
def cube(x):return x**3

print u"\n取出1到11，每个值的3次方:"
print map(cube,range(1,11))

# 返回单值，循环调用
def add(x,y):return x+y

print u"\n计算1到10的整数的和:"
print reduce(add,range(1,11))

# 列表推导式
print u"\n列表推导式"
def mul(n):
  squares = []
  for x in range(n):
    squares.append(x**2)
  return squares 
print u"常规:",mul(10)
squares = [x**2 for x in range(10)]
print u"推导:" ,squares 

squares2 = [(x,y)for x in [1,2,3] for y in [3,1,4]if x != y]
print u"取x,y不相等的元素:",squares2  

matrix = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]
squares3 = [[row[i] for row in matrix]for i in range(4)]
print u"转置前：",matrix
print u"转置：",squares3

# 删除,del
a = [-1,1,66.25,333,333,1234.5]
print u"删除前：",a
del a[2:4]
print u"删除序列号为2,3的:",a
del a[:]
print u"删除所有：",a