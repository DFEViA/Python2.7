#!usr/bin/python
# -*- coding: UTF-8 -*-

# 9.2构造方法 当一个对象被创建后，会立即调用构造方法。
# 在python中创建一个魔法方法很容易。只要把init方法的名字从简单的init修改为魔法版本__init__即可：

'''class FooBar:
    def __init__(self):
        self.somevar = 42
f = FooBar()
print f.somevar'''


class NewStyle(object):  # 新式类
    pass


class OldStyle:  # 旧式类
    pass


class FooBar:

    def __init__(self, value=42):
        self.somevar = value

f = FooBar("This is a constructor argument")
print f.somevar

# 9.2.1 重写一般方法和特殊的构造方法
'''class Brid:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print "Ahahaha..."
            self.hungry = False
        else:
            print "No Thanks"

B = Brid()
B.eat()
B.eat()

class SongBrid(Brid):
    def __init__(self):
        self.sound = 'Squawk'
    def sing(self):
        print self.sound
sb = SongBrid()
sb.sing()'''

# 9.2.2 调用未绑定的超类构造方法
'''class SongBrid(Brid):
    def __init__(self):
        Brid.__init__(self)#这样的方法称为未绑定方法
        self.sound = 'Squawk'
    def sing(self):
        print self.sound
sb = SongBrid()
sb.sing()'''

# 9.2.3 使用super函数
__metaclass__ = type  # super函数只在新式类中起作用，将下面的类全部定义为新式类，python3.0没有'旧式'类


class Brid():

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print "Ahahaha..."
            self.hungry = False
        else:
            print "No Thanks"


class SongBrid(Brid):

    def __init__(self):
        super(SongBrid, self).__init__()  # python3中不需要填写参数，实现超类init（）方法
        self.sound = 'Squawk'

    def sing(self):
        print self.sound

sb = SongBrid()
sb.sing()
sb.eat()
sb.eat()

# 9.3 成员访问
# 9.3.1 基本的序列和映射规则
# 序列和映射是对象的集合。
# 不太懂查资料

# 9.5 属性
# Python能隐藏访问器方法，让所有特性看起来一样。这些通过访问器定义的特性被称为属性。
# 9.5.1property函数的使用
'''__metaclass__ = type
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
    def getSize(self):
        return self.width,self.height
    size = property(getSize,setSize)#显示取值，然后是赋值，规则的制定

r = Rectangle()
r.width = 5
r.height = 3
print r.size

r.size = 150,100
print r.width
print r.height'''
# 9.5.2静态方法和类成员方法,在Python中并不是向来很重要，主要的原因是大部分情况下可以使用函数或者绑定方法代替。
# 静态方法的定义没有self参数，且能够被类本身直接调用.
# 类方法在定义时需要名为cls的类似于self参数，类成员方法可以直接用类的具体对象调用。但cls参数是自动被绑定到类的。
__metaclass__ = type


class MyClass:

    def smeth():
        print 'This is a static method'
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print 'This is a class method of', cls
    cmeth = classmethod(cmeth)
# 多个装饰器在应用时的顺序与指定顺序相反
__metaclass__ = type


class MyClass:

    @staticmethod  # 装饰器
    def smeth():
        print 'This is a static method'

    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls
# 注意例子中没有实例化类
MyClass().smeth()
MyClass().cmeth()

# 9.5.3 __getattr__、__setatrr__和它的朋友们
# 拦截（intercept）对象的所有特性访问时可能的
# 不太懂，细究


# 9.6迭代器
#__iter__，这个方法是迭代器规则的基础
# 9.6.1迭代器规则
# 迭代器的意思是重复做一些事很多次，实际上也能对其他对象进行迭代：实现__iter__方法的对象。
'''class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 0
    def next(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
fibs = Fibs()

for f in fibs:
    if f > 1000:
        print f
        break'''
# 9.6.2从迭代得到序列


class TestIterrator:
    value = 0

    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self
ti = TestIterrator()
print list(ti)

# 9.7生成器
# 生成器是一种用普通的函数语法定义的迭代器。
# 9.7.1创建生成器
# 任何包含yield语句的函数称为生成器。


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print num

# 9.7.2递归生成器
# 后续再看

# 9.7.3通用生成器
# 生成器的函数和生成器的迭代器。生成器的函数使用def语句定义的，博涵yeild的部分，生成器的迭代器是这个函数返回的部分。

# 9.7.4生成器方法

# 9.7.5模拟生成器

# 9.8八皇后问题
# 9.8.1生成器和回溯
# 9.8.4寻找冲突


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

# 先过后续再看，重点