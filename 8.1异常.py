#!usr/bin/python
# -*- coding: UTF-8 -*-

# 8.1什么是异常（exception）
# Python用异常对象（exception object）来表示异常情况。回溯（Traceback）

# 8.2按照自己的方式出错
# 8.2.1raise语句
# 为了引发异常，可以使用一个类（应该是Exception（所有异常的基类）的子类）或者实例参数调用rais语句。

# 8.2.2自定义异常类
# 要确保从Exception类继承（不管是间接的或者直接的，也就是说继承其他的内键异常类也是可以的）。


class SomeCustomException(Exception):
    pass

# 8.3捕捉异常
# 可以用try/exception来实现
'''try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x/y
except ZeroDivisionError:
    print "The second number can't be zero!"'''


class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            # eval将字符串转换为表达式
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print "Division by zero is illegal"
            else:
                # 触发异常
                raise
calculator = MuffledCalculator()
print calculator.calc('10/2')

calculator.muffled = True
calculator.calc('10/0')

# 8.4不止一个except子句
'''try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x/y
except ZeroDivisionError:
    print "The second number can't be zero!"
except TypeError:
    print "That wasn't a number.was it?"'''

# 8.5用一个块捕捉两个异常
'''try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x/y
except (ZeroDivisionError,TypeError):
    print "Your numbers were bogus..."'''

# 8.6捕捉对象
'''try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x/y
except(ZeroDivisionError,TypeError),e:#python3.0中会被写成(ZeroDivisionError,TypeError) as e
    print e'''

# 8.7真正的全捕捉
'''try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x/y
except:#这样写很危险 ，这时用except Exception, e会更好些，或者对异常对象e进行一些检查
    print 'Something wrong happend...'''

# 8.8万事大吉
try:
    print 'A simple task'
except:  # 没有异常则会执行else语句
    print 'What? Something went wrong?'
else:
    'Ah... It went as planned.'

while True:
    try:
        x = input('Enter the first number:')
        y = input('Enter the second number:')
        value = x / y
        print 'x/y is', value
    except Exception, e:
        print 'Invalid input:', e
        print 'Invalid input.Please try again'
    else:
        break

# 8.9最后...... 可以用来在可能的异常后进行清理，多用于关闭文件或者网络套接字时会非常有用
try:
    1 / 0
except NameError:
    print "Unknwon variable"
else:
    print "That went well"
finally:
    print "Cleaning up"


# 8.10异常和函数，异常如果不被捕获则会上传至函数直至主程序（全局作用域），最终以堆栈跟踪的形式终止。
# 8.11异常之禅 应该养成尽可能使用if/else语句的习惯
