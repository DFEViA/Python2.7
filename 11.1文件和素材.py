#!usr/bin/python
# -*- coding: UTF-8 -*-

#11.1 打开文件
# open函数用来打开文件 open(name[, mode[, buffering]])
# open函数使用一个文件名作为唯一的强制参数，然后返回一个文件对象。

#11.1.1 文件模式
'''
'r' 读模式
'w' 写模式
'a' 追加模式
'b' 二进制模式(可添加到其他模式中使用)
'+' 读/写模式(可添加到其他模式中使用)
'''
#11.1.2 缓冲
'''
open函数的第三个参数控制着文件的缓冲，参数是0，I/O（输入/输出）就是无缓冲的，所有读写操作直接针对硬盘；
参数是1，I/O就是有缓冲的（意味着Python使用内存来代替硬盘，让程序更快）。大于1的数字代表缓冲区的大小（单位是字节），
-1（或者是任何负数）代表使用默认的缓冲区大小。
'''
#11.2 基本文件方法
#三种标准的流：sys.stdin;sys.stdout;sys.stderr

#11.2.1 读和写
#文件(或流)最重要的能力是提供或者接受数据。如果有一个名为f的类文件对象，那么久可以用f.write方法和f.read方法（以字符串形式）写入和读取数据。
'''
f = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt', 'w')
f.write('Hello,')# 所提供的参数string 会被追加到文件中已存在部分的后面
f.write('World!')
f.close()

f = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt', 'r')
print f.read(4)# 先读取字符数“4”
print f.read() # 然后读取了剩下的文件。
'''

#11.2.2 管式输出
# （|）管道符号将一个命令的标准输出和下一个命令的标准输入连在一起。
# cat somefile.txt | python somescript.py 本章内的例子把文件都当成流来操作-也就是说只能按照从头到尾的顺序读数据。
# seek和tell来直接访问感兴趣的部分（这种做法成为随机访问）

#11.2.3 读写行
# readlines方法可以读取一个文件中的所有行并将其作为列表返回
# writelines方法和readlines相反，它会把所有的字符串写入文件。主要，程序不会增加新航，需要自己添加。没有writeline方法，因为能使用write。
# 注意：在使用其他的符号作为换行符的平台上，用“\r”（Mac中）和“\r\n”（Windows中）代替“\n”（由os.linesep决定。

#11.2.4 关闭文件
# 应该牢记使用close（）方法关闭文件。可以避免某些操作系统或设置中进行无用的修改，这样做也会避免用完系统中所打开文件的配额。
# 如果想却倒文件被关闭了，那么应该使用try/finally语句。并且在finally子句中调用close方法。
# with语句也可以实现上面这种情况
# with open("somefile.txt") as somefile:
#	do_something(somefile) 
# 上下文管理器

#11.2.5 使用基本文件方法
#read(n)
f = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt')
print f.read(7)
print f.read(4)
f.close()

#然后是read()
f = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt')
print f.read()
f.close()

#接着是readline()
f = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt')
for i in range(3):
	print str(i)+ ':' + f.readline(),# 加逗号少去了空行
f.close()

#以及readlines() 本例中所使用的是文件对象自动关闭的方式
import pprint
pprint.pprint(open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt').readlines())

#下面是写文件，首先是write（string）
f = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt', 'w')
f.write('this\nis no\nhaiku')
f.close()

#最后是writelines(list)
f = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt', 'w')
f.writelines(lines)
f.close()

#11.3 对文件内容进行迭代

#11.3.1按字节处理

#11.3.2按行操作

#11.3.3读取所有内容
'''
f = open(filename)
for char in f.read():
	process(char)
f.close()

f = open(filename)
for line in f.readlines():
	process(line)
f.close()
'''

#11.3.4使用fileinput实现懒惰行迭代
#在需要对一个非常大的文件进行迭代行的操作时，readlines会占用太多的内存。这个时候可以使用while循环和ReadLine方法来替代。
'''
import fileinput
for line fileinput.input(filename):
	process(line)# 没有显示的关闭文件的操作，尽管在使用完以后，文件的确应该关闭，但是只要没有向文件写入内容，那么不关闭文件也是可以的。
'''

# 11.3.5 文件迭代器
'''
f = open(filename)
for line in f:
	process(line)
f.close()
'''

# 主要sys.stdin是可迭代的，就像其他的文件对象。
'''
import sys
for line in sys.stdin:
	process(line)
'''

f = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt', 'w')
f.write('First line\n')
f.write('Second line\n')
f.write('Third line\n')
f.close()
lines = list(open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt'))
print lines
first, second, third = open('/Users/xulongwei/Desktop/Python2.7Study/Demo/somefile.txt')
print first #使用print来向文件写入内容，这会在提供的字符串后面增加新的行
print second
print third

