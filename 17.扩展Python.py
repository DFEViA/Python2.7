#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
python意味着易用且能帮助提高开发速度。达到这种程序的灵活性需要以效率作为沉重的代价
17.1 考虑哪个更重要
（1）在Python中开发一个原型（prototype）程序
（2）分析程序并且找出瓶颈
（3）用C语言作为扩展来重写出现瓶颈的代码
这样的架构的好处是，你可以使用高级语言（Python）开发复杂系统，同时也可以用低级语言（C语言）来开发对速度要求很高的小型（或较简单的）组件。
封装可能的瓶颈。
正文中引用的文档（针对CPython、Jython和IronPython的）也讨论了嵌入方法。

17.2 非常简单的途径：Jython和IronPython

17.3 编写C语言扩展
有几个项目的目的是简化编写C语言扩展的过程，其中最有名的是SWIG

17.3.1 SWIG
SWIG是简单包装盒接口生成器的缩写。它是一个能用于几种语言的工具。
一方面，可以通过它使用C语言或者C++编写扩展代码。
1.它是做什么
2.更喜欢pi
回文（例如ipreferpi）是忽略掉空格和标点后，正着读反着读一样的句子。
3.接口文件
在接口文件中，就像在一个头文件中做的那样，只需要声明导出的所有的函数（和变量）即可。
4.运行SWIG
唯一需要的是-python选项
swig -python palindrome.i
这些步骤过后，应该得到两个新文件一个是palindrome_wrap.c,另一个是pailndrome.py
5.编译、连接以及使用
编译可能是最有技巧的部分。
2.7没有找到Python.h文件
gcc -dynamic -I$PYTHON_HOME/include/python3.6m -c palindrome.c
gcc -dynamic -I$PYTHON_HOME/include/python3.6m -c palindrome_wrap.c
gcc -dynamiclib palindrome_wrap.o palindrome.o -o _palindrome.so -Wl,-undefined,dynamic_lookup #多个空格可能就会命令执行失败
6.一条通过编译器的魔法深林的捷径
Distutils直接支持SWIG，而只是写些代码以及接口文件，然后运行Distutils脚本。
17.3.2 自己研究
后续再看
'''