#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 16.1先测试，后编码
# 对程序的各个部分建立测试也是非常重要的（这称为单元测试）。
# 测试驱动编程，Test-driven programming

# 16.1.1 精确的需求说明
# 在软件开发的中，首先明确软件要解决什么问题-目的是很么。可以写一份需求说明来明确程序的目标
# 可以在Python内明确需求，让解释器检查是否满足，这无疑是一个好消息。
'''
16.1.2 为改变而计划
自动化测试除了在编写程序上给予巨大帮助外，还可以避免在实施修改时增加错误。
如果程序设计的足够好（使用了大量的抽象和分装），改变产生的影响就应该是局部的，并且只影响代码的一部分。
代码覆盖度：覆盖度是测试知识中重要的部分。
16.1.3 测试的4步
测试驱动开发过程：
1、指出需要的新特性。可以记录下来，然后为其编写一个测试。
2、编写特性的概要代码，在试图让测试成功前，先要看到它失败。
3、为特性的概要编写虚设代码。
4、现在重写代码，从而保证测试一直成功。
16.2 测试工具 
unitest: 通用测试框架
doctest: 简单一些的模块，是检查文档用的，但是对于编写单元测试也很在行。

16.2.1 doctest
为了获得更多输入，可以为脚本设定-v(意为verbose，即详述)选项开关：
testmod函数检查模块的文档字符串（你也看到了，不包括任何测试）以及函数的文档字符串
注意：不要盲目地相信测试，并且应该保证测试足够多的例子。x**2和x**x的结果是一样的。

16.2.2 unittest
doctest简单易用，unittest（基于Java的流行测试框架JUnit）则更灵活和强大。
利用它，可以更加结构化的编写大型且轴向的测试组。
也有针对unittest的GUI。请参见PyUnit(unittest的另一个名字)的网页：http://pyunit.sf.net获取更多信息。

16.3 单元测试以外的内容
源代码检查一种寻找代码中普通错误或者问题的方法。分析则是检查程序到底跑多快的方法。
16.3.1 使用PyChecker和PyLint检查源代码
16.3.2 分析

''' 
import profile
import pstats
from my_math import product
profile.run('product(1,2)')
#p = pstats.Stats('my_math.profile')

