#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 15.1 屏幕抓取
'''
屏幕抓取是程序下载网页并且提取信息的过程。
第一个方案是使用叫做Tidy（Python库）的程序和XHTML解析；
第二个方案则使用Beautiful Soup库，它专门为屏幕抓取设计；
'''

# 15.1.1 Tidy和XHTML解析
'''
Python标准库中有很多支持接过话格式的库，例如HTML和XML。XHTML是HTML最新的方言，是XML的一种形式。
1、Tidy是什么
Tidy是用来修复不规范且随意的HTML的工具。
Tidey不能修复HTML文件的所有问题，但是它会确保文件的格式是正确的（也就是所有元素都正确嵌套）。
2、获取Tidy库
3、在Python中使用命令行Tidy

from subprocess import Popen, PIPE

text = open('messy.html').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)

tidy.stdin.write(text)
tidy.stdin.close()

print tidy.stdout.read()

4、但为什么用XHTML
XHTML和旧版本的HTML之间的最主要区别是XHTML对于显式关闭所有元素要求更加严格。

5、使用HTMLParser
使用HTMLParser的意思就是继承它，并且对handle_starttage或handle_data等事件处理方法进行覆盖。
'''

# 15.1.2 Beautiful Soup
# Beautiful Soup是个小模块，用来解析和检查经常在网上看到的那类乱七八糟而且不规范的HTML。

# 15.2 使用CGI（Common Gateway Interface）创建动态网页

# 本章第一部分讨论的是客户端技术，现在来看看服务器端。
# CGI是网络服务器可以讲查询传递到专门的程序中并且在网页上显示结果的标准机制。
# 它是创建万维网应用程序而不用编写特殊用途的应用服务器的简单方法。
# cgitb是另外一个在CGI脚本开发过程中的有用模块。

# 15.2.1 第一步：准备网络服务器
# CGI程序也应该放在通过网络可以访问的目录中。并且必须将他们表示为CGI脚本，这样网络服务器就不会将普通源代码作为网页处理。
# 1、将脚本放在叫做cgi-bin的子目录中。
# 2、把脚本文件扩展名改为.cgi。

# 15.2.2 第二步：加入Pound Bang行

# 15.2.3 第三部：设置文件许可
# 要确保每个人都可以读取和执行脚本文件（否则服务器就没法运行它了），但是还要确保只有你可以写入（这样就没有人可以修改脚本了）。
# chmod 755 somescript.cgi 在做好所有这些准备后，应该能将脚本作为网页打开，并且执行。
# 一般来说不允许CGI脚本修改计算机上的任何文件。

# 15.2.4 CGI风险
# 如果允许CGI脚本写服务器上的文件，那么除非非常小心地编写代码。否则可能会造成数据的损毁。
# 调研cgi脚本不能被执行的问题

# 15.2.7 使用cgi模块
# 输入时通过HTML表单提供给CGI脚本的键-值对，或称字段。

# 15.2.8 简单的表单

# 15.3 更进一步：mod_python
# 它是Apache网络服务器的扩展（模块），最重要的是它提供了在Python中编写Apache处理程序的功能，

# CGI处理程序
# 使用CGI处理程序而不使用普通CGI的主要原因是性能。

# 15.3.3 PSP

# mod_python 后面再看
