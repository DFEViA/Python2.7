#!usr/bin/python
# -*- coding: UTF-8 -*-

# 10.1模块
import math
print math.sin(0)

# 10.1.1模块是程序
import sys
sys.path.append('/Users/xulongwei/Desktop/Test')
import hello

# 模块主要用于定义，比如变量、函数和类等。此外，因为只需要定义这些东西一次，导入模块多次和导入一次的效果是一样的。

# 10.1.2模块用于定义
# 1.在模块中定义函数

sys.path.append('/Users/xulongwei/Desktop/Test')
import hello2
hello2.hello()

# 模块用来定义函数、类和其他一些内容，但是有些时候（事实上是经常），在模块中添加一些检查模块本身是否正常工作的测试代码是很有用的。
# “告知”模块本身是作为程序运行还是导入到其他程序。为了实现这一点，需要使用__name__变量

hello2.test()

# 10.1.3让你的模块可用
# 1.将模块放置在正确的位置
# 将模块放置在site-packages目录下，所有程序就能可以直接import导入

import sys
import pprint
pprint.pprint(sys.path)

# 2.告诉编译器去哪里找
# 在.bashrc文件里这只环境变量

# 3.命名模块，包含模块代码的文件的名字要和模块名一样——再加上.py扩展名

# 10.1.4包
# 包基本上就就是另外一类模块，有趣的地方就是它们能包含其他模块。当模块存储文件中时，包就是模块所在的目录。为了python将其作为包对白，他必须包含一个命名为__init__py的文件（模块）。

'''
	import drawing            (1)
	import drawing.colors     (2)
	from drawing import shapes(3)
	(1)导入后可以使用__init__模块可以使用，但其他两个模块不可使用；（2）执行后，但只能通过全名drawing.colors来使用。（3）可以通过短名shapes来使用；
'''
# 10.2探究模块
# 10.2.1模块中有什么
# 1.使用dir 查看
import copy
# 这个列表推导式是个包含dir(copy)中所有不以下划线开头的名字
print[n for n in dir(copy) if not n.startswith('_')]

# 2.__all__变量 设定all会把其他程序不需要或不想要的变量、函数和类，过滤出去，如果不设定all。用import
# *语句默认将会输出模块中素有不以下划线开头的全局名称。
print copy.__all__

# 10.2.2 用help获取帮助
# help(copy.copy)

print copy.copy.__doc__  # doc文档字符串

# help(copy)

# 10.2.3 文档

# 10.2.4 使用源代码
print copy.__file__  # 如果文件名以.pyc结尾，只要查看相应的以.py结尾的文件即可

# 10.3 标准库：一些最爱
# sys.argv函数 描述：命令行参数，包括脚本名称

# 10.3.2 os
# os模块为你提供了访问多个操作系统服务功能

# 10.3.4 集合、堆和双端队列
print set(range(10))
print set([1, 2, 1, 2, 3, 4, 5, 5, 6])  # 集合元素是唯一的，无序的
# 除了检查成员资格外，还可以使用标准的集合操作，比如求并集和交集，可以使用方法，也可以使用对整数进行位操作时使用的操作。
mySets = []
for i in range(10):
    mySets.append(set(range(i, i + 5)))
print reduce(set.union, mySets)
# 集合是可变的，所有不能用做字典中的键 另一个问题集合本身只能包含不可变值，所以也就不能包含其他集合
a = set()
b = set()
a.add(frozenset(b))  # frozenset构造函数创建给定集合的副本，不管是将集合作为其他集合成员还是字典的键

# 堆（heap），他是优先队列的一种。优先队列能够以人任意顺序增加对象，并且能在任何时间（可能在增加对象的同时）找到（也可能移除）最小的元素。
