#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 7.1对象的魔力
# 对象的三大优点：多态、封装、继承
# 7.1.1多态
# 再精细补充
# 7.2.2封装
# 封装是对全局作用中其他区域隐藏多余消息的原则。
# 7.1.3继承

# 7.2类和类型
# 子类和超类
# 定义自雷致死个定义更多（也有可能是重载已经存在的）的方法的过程。

# 7.2.2创建自己的类
_metaclass_ = type  # 确定使用新式类


class Person:

    def setName(self, name):  # self指的是类实力对象本身
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, world! I'm %s." % self.name

foo = Person()
bar = Person()
foo.setName("laozhang")
bar.setName("laowang")
foo.greet()
bar.greet()

print foo.name
bar.name = 'Yoda'
bar.greet()

# 7.2.3特性、函数和方法
# 再论私有化

# Python并不直接支持私有方式，而要考程序员自己把握在外部进行特性修改的实际。
# 为了让方法或者特性变为私有（从外部无法访问），只要在它的名字前面加上双下划线即可：


class Secretive:
    # 变为私有

    def __inaccessible(self):  # 通过类名._方法名还是可以访问这些私有方法
        print "Bet you can't see me..."

    def accessible(self):
        print "The secretmessage is:"
        # 在类内部还能使用
        self.__inaccessible()
s = Secretive()
s.accessible()
# Python并没有真正的私有化支持

# 7.2.4类的命名空间
# 并不是所有Python程序员都知道类的定义其实就是执行代码块，这一点非常有用，比如，在累的定义区并不只限使用def语句：
# 所有位于class语句中的代码都在特殊的命名空间中执行——类命名空间


class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1
m1 = MemberCounter()
m1.init()
print MemberCounter.members

m2 = MemberCounter()
m2.init()
print MemberCounter.members
# 上面的代码中，在类作用域定义了一可供所有成员（实例）访问的变量，用来计算类的成员数量。
# 就像方法一样，类作用域内的变量也可以被所有实例访问
print m1.members
print m2.members

# 7.2.5指定超类
# 将其他类名写在class语句后的圆括号内可以指定超类


class Filter:

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]  # 列表推导式-轻量级循环


class SPAMFilter(Filter):  # SPAMFilter是Filter的子类

    def init(self):
        self.blocked = ['SPAM']
# Filter是个用于过滤序列的通用类，事实上它不能过滤任何东西
f = Filter()
f.init()
print f.filter([1, 2, 3])

s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'QWEQW', 'QWEQ'])

# 7.2.6调查继承
# 使用内键的issubclass函数：
print issubclass(SPAMFilter, Filter)
print issubclass(Filter, SPAMFilter)

# 使用__bases__查找已知类的基类（们）：
print SPAMFilter.__bases__

# 使用isinstance方法检查一个对象是否是一个类的实例：
s = SPAMFilter()
print isinstance(s, SPAMFilter)
print isinstance(s, Filter)
print isinstance(s, str)
# 使用instance并不是个好习惯，使用多态会更好一些。
# 如果只想知道一个对象属于哪个类，可以使用__class__特性：
print s.__class__


# 7.2.7多个超类:先继承的类中的方法会重写后继承的类中的方法。
class Calcaulator:

    def calculate(self, expression):
        self.value = eval(expression)


class Talker:

    def talk(self):
        print 'Hi, my value is', self.value


class TalkingCalculator(Calcaulator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()

# 7.2.8接口和内省
# hasattr函数是否已经存在
print hasattr(tc, 'talk')
print hasattr(tc, 'fnord')

'''
面向对象设计：
1、写下问题的描述（程序要做什么？），把所有名词、动词和形容词加下划线。
2、对于所有名字，用作可能的类。
3、对于所有多那个词，用作可能的特性。
4、对于所有形容词，用作可能的特性。
5、把所有的方法和特性分配到类。
'''
