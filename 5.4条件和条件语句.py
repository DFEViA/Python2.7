#!usr/bin/python
# -*- coding: UTF-8 -*-
from math import sqrt
x = y = [1, 2, 3]
z = [1, 2, 3]
print x == y
print x == z
print x is y
print x is z

print range(1, 100)

names = ['a', 'b', 'c', 'd']
ages = [1, 2, 3, 4]
print zip(names, ages)

while True:
    word = raw_input('Please enter a word:')
    if not word.strip():
        break
    # 处理word：
    print 'The word was' + word

print range(99, 80, -1)

for n in range(99, 80, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
    else:
        print "Didn't find it!"

# 列表推导式-轻量级循环
print[x * x for x in range(10)]
print[x * x for x in range(10) if x % 3 == 0]
print[(x, y) for x in range(3) for y in range(3)]

'''#5.7.1什么都没发生 pass
if name == 'Ralph Auldus Melish'
    print 'Welcome!'
elif name == 'Enid':
    #还没完......
    pass
elif name == 'Bill Gates':
    print 'Access Denied'
#5.7.2使用del删除，删除的只是名称，而不是列表本身（值）
#5.7.3使用exec和ecal执行和求值字符串'''
