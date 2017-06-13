#!/usr/bin/python
# -*- coding: UTF-8 -*-

#食品数据库查询程序
import sqlite3, sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE %s' % sys.argv[1]
print query
curs.execute(query)

#curs.description存储的是关于表没列属性的一些信息，序列包裹着元组，子序列的第一个值就是标的属性名称
names = [f[0] for f in curs.description]
print names
'''
for f in curs.description:
	names = f[0]
	print f[0]
print names
'''

#curs.fetchall()存储的是根据query语句获得的纯数据，形式也是序列包裹着元组，因为属性的目的是确定的，用元组
for row in curs.fetchall(): # 使用execute方法执行SQL查询，用fetchall等方法提取结果
 	print row
	for pair in zip(names, row):# zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。
		print pair
		print '%s: %s' %pair
	print # 打印空行