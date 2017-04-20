#!usr/bin/python
# -*- coding: UTF-8 -*-

#9.2构造方法 当一个对象被创建后，会立即调用构造方法。
#在python中创建一个魔法方法很容易。只要把init方法的名字从简单的init修改为魔法版本__init__即可：

'''class FooBar:
    def __init__(self):
        self.somevar = 42
f = FooBar()
print f.somevar'''

class NewStyle(object):#新式类
    pass
class OldStyle:#旧式类
    pass


class FooBar:
    def __init__(self, value = 42):
        self.somevar = value

f = FooBar("This is a constructor argument")
print f.somevar

#9.2.1 重写一般方法和特殊的构造方法
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

#9.2.2 调用未绑定的超类构造方法
'''class SongBrid(Brid):
    def __init__(self):
        Brid.__init__(self)#这样的方法称为未绑定方法
        self.sound = 'Squawk'
    def sing(self):
        print self.sound
sb = SongBrid()
sb.sing()'''

#9.2.3 使用super函数
__metaclass__ = type#super函数只在新式类中起作用，将下面的类全部定义为新式类，python3.0没有'旧式'类
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
        super(SongBrid,self).__init__() #python3中不需要填写参数，实现超类init（）方法
        self.sound = 'Squawk'
    def sing(self):
        print self.sound

sb = SongBrid()
sb.sing()
sb.eat()
sb.eat()

#9.3 成员访问
#9.3.1 基本的序列和映射规则
#序列和映射是对象的集合。
#不太懂查资料

#9.5 属性
#Python能隐藏访问器方法，让所有特性看起来一样。这些通过访问器定义的特性被称为属性。
#9.5.1property函数的使用
__metaclass__ = type
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
print r.height
#9.5.2静态方法和类成员方法

#Test

#Test too

#Test hhh

#0001111