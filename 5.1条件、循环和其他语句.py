#!usr/bin/python
# -*- coding: UTF-8 -*-
# 5.1.1 使用逗号输出
import math as foobar
from math import sqrt as sqr

print 'Age:', 42
# 如果在结尾处加上逗号，那么接下来的语句会与前一条语句在同一行打印
print 'Hello',
print 'world!'

print foobar.sqrt(4)
print sqr(4)

# 序列解包或可选代解包
x, y, z = 1, 2, 3
print x, y, z

x, y = y, x
print x, y, z

values = 1, 2, 3
print values
x, y, z = values
print x, y, z

scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print scoundrel
print key, value

# 5.2.2链式赋值是将同一个值付赋给多个变量的捷径。

# 5.3.3增量赋值

fnord = 'foo'
fnord += 'bar'
fnord *= 2
print fnord
