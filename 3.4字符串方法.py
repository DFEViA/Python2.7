#!usr/bin/python
# -*- coding: UTF-8 -*-
from string import maketrans
from string import capwords

# 3.4.1find方法
# 返回要查询的字符串第一个字符索引位置
print 'hello world hello a boy'.find('hello')

# find方法还可以接受可选的起始点和结束点参数
subject = '$$$ Get rich now!!! $$$'
print subject.find('$$$')
print subject.find('$$$', 1)  # 只提供起始点
print subject.find('!!!')
print subject.find('!!!', 0, 16)
# 注意：由其实和终止指定的范围（第二和第三个参数）包含第一个索引，但不包含第二个索引。这在Python中是个惯例

# 3.4.2join方法(连接字符串)
seq = ['1', '2', '3', '4', '5']
sep = '+'
sep.join(seq)
print sep.join(seq)

# 3.4.3lower方法
name = 'Gumby'
names = ['gumby', 'smith', 'jones']
if name.lower()in names:
    print 'Found it'

# 3.4.4replace方法
print 'This is a  is test'.replace('is', 'eez')

# 3.4.5split方法
print '1+2+3+4+5'.split('+')
print '/usr/bin/env'.split('/')
print 'Using the default'.split()

# 3.4.6strip方法
print '  internal whitespace is kept  '.strip()
# 也可以指定需要去除的字符，将它们列为参数即可
print '*** SPAM * for * everyone!!! ***'.strip(' *!')

# 3.4.7translate方法
table = maketrans('cs', 'kz')  # 先创建表
print len(table)
print table[97:123]
print maketrans('', '')[97:123]
# 创建这个表以后，可以将它用作translate方法的参数，进行字符串的转换如下：
print 'this is an incredible test'.translate(table)
# translate的第二个参数是可选的，这个参数是用来指定需要删除的字符。
print 'this is an incredible test'.translate(table, ' ')

# capwords函数再调查

