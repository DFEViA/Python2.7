#!usr/bin/python
# -*- coding: UTF-8 -*-

# 13.1 Python数据库API

# 注重看下第10章的shelve模块

# 13.1.1 全局变量

# 任何支持2.0版本DB API的数据库模块都必须定义3个描述模块特性的全局变量。
# 3种全局变量apilevel、threadsafety、paramstyle

# 13.1.2 异常
# 为了尽可能准确地处理错误，API中定义了一些异常类。他们被定义在一种层次结构中，所有可以通过一个except快捕捉多种异常。

# 回滚（Rollback）指的是程序或数据处理错误，将程序或数据恢复到上一次正确状态的行为。回滚包括程序回滚和数据回滚等类型。

# 13.1.3连接和游标
# 为了使用基础数据库系统，首先必须连接到它。
'''
通过connect函数，连接数据库，推荐将这些作为关键字参数使用
dsn 数据源名称，给出该参数表示数据库依赖
user 用户名
password 用户密码
host 主机名
database 数据库名
'''
'''
close()   关闭连接之后，连接对象和它的游标均不可用
commit()  如果支持的话就提交挂起的事务，否则不做任何事
rollback() 回滚挂起的事务(可能不可用)
cursor() 返回连接的游标对象
'''

# rollback方法可能不可用，因为不是所有的数据库都支持事务（事务是一系列动作）。如果可用，那么它就可以“撤销”所有未提交的事务。

# cursor方法将我们引入另一个主题：游标对象。通过游标执行SQL查询并检查结果。游标比连接支持更多的方法。而且可能在程序中更好用。

# 13.1.4类型

# 13.2 SQLite和PySQLite
# SQLite并不需要作为独立的服务器运行，并且不基于集中式数据库存储机制，而是直接作用本地文件

# 13.2.1入门

'''
import sqlite3
conn = sqlite3.connect('somedatabase.db')

# 获得连接的游标
curs = conn.cursor()

# 这个游标可以用来执行SQL查询。完成查询并且做出某些更改后确保已经进行提交，这样才可以将这些修改真正地保存到文件中
conn.commit()
# 在每次修改数据库后都进行提交，而不是仅仅在准备关闭时才提交，准备关闭数据库时，使用close方法
conn.close()
'''

# 13.2.2 数据库应用程序示例
'''import sqlite3

def convert(value):
	if value.startswith('~'):
		return value.strip('~')
	if not value:
		value = '0'
	return value

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
'''CREATE TABLE food(
	id	     Text      PRIMARY KEY,
	desc     Text,
	water    FLOAT,
	kcal     FLOAT,
	protein  FLOAT,
	fat      FLOAT,
	ash      FLOAT,
	carbs    FLOAT,
	fiber    FLOAT,
	sugar    FLOAT
	)'''
	''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'	

for line in open('ABBREV.txt'):
	fields = line.split('^')
	vals = [convert(f) for f in fields[:10]] # 列表推导式，轻量级循环
	print vals
	curs.execute(query, vals)

conn.commit()
conn.close()
'''
# 2.搜索和处理结果
# 需要创建连接并且获得该链接的游标，使用execute方法执行SQL查询，用fetchall等方法提取结果。
# 


