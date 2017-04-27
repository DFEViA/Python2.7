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
print[n for n in dir(copy) if not n.startswith('_')]

