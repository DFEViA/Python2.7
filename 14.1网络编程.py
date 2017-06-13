#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python是一个很强大的网络编程工具
# 14.1少数几个网络设计模块
# 14.1.1 socket模块
#在网络编程的一个基本组件就是套接字（socket）。
#套接字主要是两个程序之间的“信息通道”，程序可能（通过网络连接）分布在不同的计算机上，通过套接字相互发送消息。

#套接字包括两个：服务器套接字和客户机套接字。
#创建一个服务器套接字后，让它等待连接，这样它就是某个网络地址处（IP地址和一个端口号的组合）监听。

#处理客户端套接字通常比处理服务器端套接字容易，客户机只是简单的连接，完成事务，断开连接。
#一个套接字就是一个socket模块中的socket类的实例。
'''
套接字实例化需要三个参数：
第1个参数是地址族（默认是socket.AF_INET）;
第2个参数是流（socket.SOCK_STREAM, 默认值）或数据报（socket.SOCK_DGRAM）套接字；
第3个参数是使用的协议（默认是0，使用默认值即可）
'''

#listen方法只有一个参数，及服务器未处理的连接的长度（即允许排队等待的连接数目，这些连接在停止接收之前等待接收）

#服务器端套接字开始监听后，它就可以接受客户端的连接。这个步骤使用accept方法来完成。这个方法会阻塞（等待）知道客户端连接，然后该方法就返回一个格式为（client，address）的元组。
#阻塞或者同步网络编程、非阻塞或者叫做异步网络编程
#套接字有两个方法：send和recv（用于接收），用于传输数据。

# 14.1.2 urllib 和 urllib2模块
# 在能使用的各种网络工作库中，功能最轻大的是urllib和urllib2.它们能让通过网络访问文件，就像那些文件存在于你的电脑上一样。通过一个简单的函数调用，几乎可以把任何URL所指向的东西用做程序的输入。
# 1.打开远程文件
# 可以像打开本地文件一样打开远程文件，不同之处是可以使用只读模式
import re
from urllib import urlopen
from urllib import urlretrieve
from urllib import urlcleanup

'''
webpage = urlopen('http://www.python.org')# urlopen返回的类文件对象支持close、read、readline、readlines方法
text = webpage.read()
#print text
m = re.search('<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE) #中括号脱字符后面的"是除去引号的意思, 在子模式后面加上问号表示可选项
print m.group(0)
print m.group(1)
'''

# 2.获取远程文件
# 函数urlopen提供一个能从中读取数据的类文件对象。
# 希望urllib为你下载文件并在本地文件中存储一个文件的副本，那么可以使用urlretrieve。
# urlretrieve返回一个元组（filename,headers）而不是类文件对象
# 如果想要为下载的副本指定文件名，可以在urlretrieve函数的第二个参数中给出
# urlretrieve('http://www.python.org', './python_webpage_html')
# urlcleanup() 如果没有指定文件名，文件会存在临时的文件，调用此函数会复制清理工作

# 看URL和CGI的知识

# 14.1.3 其他模块

# 14.2 SocketServer和它的朋友们
# SocketServer模块是标准库中很多服务器框架的基础，这些服务器框架包括BaseHTTPServer、SimpleHTTPServer、CGIHTTPServer、SimpleXMLRPCServer、DocXMLRPCServer,所有这些服务器框架都为基础服务器增加了特定的功能。

# SocketServer包含了4个基本的类：针对TCP套接字流的TCPServer；针对UDP数据报套接字的UDPServer；以及针对性不强的UnixStreamServer和UnixDatagramServer
# 为了写一个使用SocketServer框架的服务器，大部分代码会在一个请求处理程序（request handler）中
# StreamRequestHandler在连接被处理完后会负责关闭连接。还要注意使用''表示的是服务器正在其上运行的机器的主机名。

# 14.3 多连接
# 到目前为止讨论的服务器解决方案都是同步的：即一次只能连接一个客户机并处理它的请求。
# 同时能处理多个连接很重要，有3中主要的方法能实现这个目的：分叉（forking）、线程（threading）以及异步I/O。

# 什么是分叉和线程处理
# 分享会有自己的内存副本，一个进程成为父进程，另一个成为子进程。
# 线程是轻量级的进程或子进程，所有的线程都存在于相同的（真正的）进程中，共享内存。
# Stackless Python

# 14.3.1 使用SocketServer进行分叉和线程处理
# windows不支持分叉

# 14.3.2 带有select和poll的异步I/O
# poll的伸缩性更好，但它只能在UNIX系统中使用
# select函数需要3个序列作为它的必选参数，此外还有一个可选的以秒为单位的超时时间作为第4个参数。
# 服务器是个简单的记录器（logger），它输出（在本地）来自客户机的所有数据。
# 使用poll的简单服务器
# 14.4 Twisted
# 后期细看