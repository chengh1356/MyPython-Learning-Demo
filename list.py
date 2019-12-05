#_*_coding:utf-8_*_ 
a = [66.25,333,333,1,1234.5]
# 统计总数
print a.count(333),a.count(66.25),a.count('x')
# 插入
a.insert(2,-1)
a.append(333)
print a
print a.index(333)
# 删除取到的第一个333
a.remove(333)
print a
a.reverse()
print a
# 排序
a.sort()
print a
# 末尾取出
print a.pop()
print a
