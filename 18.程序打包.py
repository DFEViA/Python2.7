#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
包、模块、类

用于发布Python包的工具包Distutils能让程序轻松地用Python编写安装脚本。
这些脚本可以用来建立用于发布的存档文件
18.1 Distutils基础
#后续看setuptools
python setup.py bulid、python setup.py install
这就是安装Python模块、包（packages）和扩展的标准机制。

18.2 打包
写完供用户安装模块使用的setup.py脚本以后，就可以用它来建立存档文件
18.2.1 建立存档文件
你可以使用sdist命令（用于“源代码发布”）
python setup.py sdist
如果重构了包并且想重新打包，那么请删除MANIFEST文件，以便于重新开始打包
#18.2.2 创建Windows安装程序或RPM包

18.3 编译扩展

18.4 使用py2exe创建可执行程序
py2exe作为Distutils的扩展可用来创建可执行的Windows程序（.exe文件），如果不想让用户单独安装Python结束期的话，它就能大显神威了。
MacOS,那么可以参考Bob Ippolito的py2app
'''


