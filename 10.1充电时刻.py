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
# heappush函数用于增加堆的项。
from heapq import *
from random import shuffle  # shuffle()函数将序列的所有元素随机排序
data = range(10)
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print heap

heappush(heap, 0.5)
print heap  # 他们虽然不是按照严格排序的，但是也有规则的，这个特性称为堆属性

print heappop(heap)  # 将堆中最小的元素弹出，一般来说都是在索引0处的元素
print heappop(heap)
print heappop(heap)
print heappop(heap)  # 因为heappop在“幕后”会做一些精巧的位移操作
print heap

# heapify函数使用任意列表作为参数，并且通过尽肯能少的位移操作，将其转换为合法的堆
heap = [5, 8, 0, 3, 6, 1, 4, 2]
heapify(heap)
print heap

# heapreplace函数并不像其他函数那么常用。它弹出堆的最小元素，并且将新元素推入。
heapreplace(heap, 0.5)
print heap
heapreplace(heap, 10)
print heap  # 堆算法更快而且更有效地使用内存（更易用）

# 3.双端队列（以及其他集合类型）在需要按照元素增加的顺序来移除元素时非常有用。
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print q

q.pop()  # 跑出右边的元素
q.popleft()  # 双端队列好用的原因是它能够有效地在开头（左侧）增加和弹出元素，这是在列表中无法实现的。
print q

q.rotate(3)  # 右移三个元素
print q
q.rotate(-1)  # 左移一个元素
print q

# 10.3.5 time
# time模块
import time
print time.asctime()  # 将时间元组转换为字符串
print time.time()

# 10.3.6 random
# random
# 模块包括返回随机数的函数，可用于模拟或者用户任何产生随机输出的程序，注这里都是伪随机数，如果需要真的随机性，应该使用os模块的urandom函数。random模块内的SystemRandom类也是基于用猴子那个功能，可以让数据接近真正的随机性
import random
print random.random()  # 返回大于等于0小于1之间的随机实数n
'''
getrandbits(n)          以长整型形式返回n个随机位
uniform（a,b）			返回随机实数n，其中a <= n <b
randrange([start],stop,[step]) 返回range（start,stop,step）中的随机数
choice（seq）            从序列seq中返回随意元素
shuffle（seq[,random]）  原地指定序列seq
sample(seq,n)           从序列seq中选择n个随机且独立的元素
'''
from random import *
from time import *
date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
random_time = uniform(time1, time2)
print asctime(localtime(random_time))

# 例用户选择投掷的骰子数以及每个骰子具有的面数
'''from random import randrange
num = input('How many dice?')
sides = input('How many sides per die?')
sum = 0
for i in range(num): sum += randrange(sides) + 1
print 'The result is', sum
'''
# 希望程序能够在每次敲击回车的时候都为自己发一张牌，同事还要确保不会获得相同的牌。
values = range(1, 11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]
from pprint import pprint
pprint(deck[:12])

# 打乱顺序
from random import shuffle
shuffle(deck)
pprint(deck[:12])  # 只打印了前12张牌

'''i = 0
while deck:
	i+=1
	a = raw_input(deck.pop())# 返回了输入的内容，并且将其打印出来
print i'''

# 10.3.7 shelve
# 1 潜在的陷阱 shelve.open函数返回的对象并不是普通的映射是很重要的
import shelve
s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
s['x'].append('d')  # 'd'被添加到这个副本中，修改的版本还没有被保存
print s['x']

temp = s['x']  # 为了正确地使用shelve模块修改的临时对象，必须将临时变量绑定到获得的副本上，并且在它被修改后重新存储这个副本
temp.append('d')
s['x'] = temp
print s['x']

# 10.3.8 re 模块包含对正则表达式的支持
'''
1.什么是正则表达式
正则表达式是可以匹配文本片段的模式。最简单的正则表达式就是普通字符串，可以匹配其自身。
*通配符. 因为点号只能匹配一个字母，而不是两个或零个；它可以匹配“任何字符串”（除换行符外的任何单个字符），点号就成为通配符。
*对特殊字符进行转义 在正则表达式中如果将特殊字符作为普通字符使用会遇到问题。本例中可以使用'python\\.org'匹配'python.org'，使用两个反斜线的目的是（1）通过解释器转义；（2）通过re模块转义；
*字符集 使用中括号括住字符串来创建字符集，字符集可以匹配它所包括的任意字符，注意字符集只能匹配一个这样的字符。为了反转字符集，可以在开头使用^字符，比如'[^abc]'可以匹配任何除了a、b和c之外的字符;
*选择符和子模式，在字符串的每个字符都各不相同的情况下。只匹配'python'和'perl'，用管道可写成'python|perl'。用子模式前例也可写成'p(ython|erl)'。
*可选项和重复子模式 在子模式后面加上问号，它就变成了可选项。他可能出现在匹配字符串只能怪，但并非必须的。 原始字符串：r'(http://)?(www\.)?python\.org',有四种匹配结果。
重复模式：
（pattern)*:允许模式重复0次或多次；
（pattern）+：允许模式重复1次或多次；
（pattern){m,n}:允许模式重复m~n次；
前面的匹配模式都去匹配整个字符串
*字符串的开始和结尾 可以使用脱字符（^）标记开始，类似地，字符串结尾用美元符号（$）标识。
'''

'''
2.re模块的内容
re.match('p','python')返回真，在给定字符串的开头匹配正则表达式。
re.split则允许用任意场地的逗号和空格序列来分割字符串。 如果模式包含小括号，那么括起来的字符组合会散步在分割后的子字符串之间。
'''
# re.findall以列表形式返回给定模式的所有匹配项。比如，要在字符串中查找所有的单词
import re
pat = '[a-zA-Z]+'
text = '"Hm... Err -- are you sure?" he said. sounding insecure.'
print re.findall(pat, text)
# 查找标点符号
pat = r'[.?\-","]+'  # -横线进行了转义，不会将其解释为字符范围的一部分
print re.findall(pat, text)
# 函数re.sub的作用在于：使用给定的替换内容将匹配模式的子字符串（最左端并且非重叠的子字符串）替换掉。
pat = '{name}'
text = 'Dear {name} ...'
print re.sub(pat, 'Mr. Gumby', text)
# re.escape是一个很实用的函数，它可以对字符串中所有肯被解释为正则运算符的字符进行专业为应用函数
print re.escape('www.python.org')
print re.escape('But where is the ambiguity?')

'''
3.匹配对象和组
组就是放置在圆括号内的子模式。组的序号取决于它左侧的括号数。组0就是整个模式。
'There (was a (wee) (cooper)) who (lived in Fyfe)'
re匹配对象的重要方法
group() 获取给定子模式（组）的匹配项
start() 返回给定组的匹配项的开始位置
end() 返回给定组的匹配项的结束位置（和分片一样，不包括组的结束位置）
span() 返回一个组的开始和结束位置
方法end类似于start，但是返回结果是结束索引加1
注意：除了整体匹配外（组0），我们只能使用99个组，范围1~99
'''
m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
print m.group(1)
print m.start(1)
print m.end(1)
print m.span(1)

'''
4.作为替换的组号和函数
将函数作为替换内容可以让替换功能变得更加强大，MatchObject将作为函数的唯一参数，返回的字符串将会用做替换内容。
贪婪模式和非贪婪模式 +？运算符代替了+，意味着模式也会像之前那样对一个或者多个通配符进行匹配，但是它会进行尽可能少的匹配。
'''
emphasis_pattern = re.compile(r'''
	\* #Beginning emphasis tag -- an asterisk
	(  #Begin group for capturing phrase
	[^\*]+ #Capture anything except asterisks
	)  #End group
	\* #Ending emphasis tag
		''', re.VERBOSE)
print re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!')

'''
5.找出Email的发言人
后续细看
'''
'''
6.模板系统示例
模板是一种通过放入具体值从而得到某种已完成文本的文件。
后续细看
'''
# 10.3.9其他有趣的标准模块
# Python类库参考（http://python.org/doc/lib）

