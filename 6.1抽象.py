#!usr/bin/python
# -*- coding: UTF-8 -*-
# 6.1 懒惰即美德
# 计算斐波那契数列


def fibs(num):
    fibs = [0, 1]
    for i in range(num):
        print i
        fibs.append(fibs[-2] + fibs[-1])
    print fibs


'''num = input('How many Fibonacci numbers do you want?')
fibs(num)'''

# 6.3创建函数
# 6.3.1记录函数


def square(x):
    'Calculates the square of the number x'
    return x * x
print square.__doc__

'''print help(square)'''

# 6.3.2并非真正函数的函数


def test():
    print 'This is printed'
    return
    print 'This is not'

# 6.4.2我能改变参数吗
storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

me = 'Magnus lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]

print storage['first']['Magnus']
print storage['middle']['Lie']

my_sister = 'Anne Lie Hetland'
storage['first'].setdefault('Anne', []).append(my_sister)
storage['middle'].setdefault('Lie', []).append(my_sister)
storage['last'].setdefault('Hetland', []).append(my_sister)

print storage['first']['Anne']
print storage['middle']['Lie']


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)

print storage
print lookup(storage, 'middle', 'Lie')

# 如果我的参数不可变呢


def inc(x): return x + 1
foo = 10
foo = inc(foo)
print foo


def inx(c): c[0] = c[0] + 1
foo = [10]
inx(foo)
print foo

# 6.4.3关键字参数和默认值


def hello_1(greeting, name):
    print '%s,%s!' % (greeting, name)
# 这类使用参数名提供的参数叫做关键字参数
hello_1(greeting='Hello', name='world')


def hello_4(name, greeting='Hello', punctuation='!'):
    print '%s,%s%s' % (greeting, name, punctuation)
# 各种调用方式
hello_4('Mars')
hello_4('Mars', 'Howday', '...')
hello_4('Mars', greeting='Top of the morning to ya')

# 6.4.4收集参数


def print_params(*params):
    print params
# 返回的是元组
print_params(1, 2)
# 参数前的星号将所有值防止在同一个元组中。可以说是将这些值收集起来，然后使用.
# 注意可以联合普通参数


def print_params_3(**params):
    print params
# 返回的是字典而不是元组
print_params_3(x=1, y=2, z=3)

# 综合运用


def print_params_4(x, y, z=3, *pospar, **keypar):
    print x, y, z
    print pospar
    print keypar

print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)

# 反转过程
# 如何将参数收集元组和字典已经讨论过了


def add(x, y): return x + y

params = (1, 2)
print add(*params)
# 星号*、**只在定义函数（允许使用不定数目的参数）或者调用（"分割"字典或者序列）时才有用。

# 6.4.6练习使用参数


def story(**kwds):
    return 'Once upon a time. there was a '\
           '%(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print 'Received redundant parameters:', others
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step >0'
    if stop is None:  # 如果没有为stop提供值
        start, stop = 0, start  # 指定参数
    result = []
    i = start  # 计算start索引
    while i < stop:  # 直到计算到stop的索引
        result.append(i)  # 将索引添加到result中
        i += step  # 用step（>0）增加索引
    return result

print story(job='King', name='Gumby')
params = {'job': 'language', 'name': 'Python'}
print story(**params)

print power(2, 3)
print power(3, 3, 'Hello,world')

print interval(10)
print power(*interval(3, 7))

# 6.5作用域
x = 1
scope = vars()
print scope['x']
scope['x'] += 1
print x

# 这类"不可见的字典"叫做命名空间或者作用域。


def combine(parameter):
    print parameter + globals()['parameter']
parameter = 'berry'
combine('Shrub')

# 重绑定全局变量
x = 1


def change_global():
    global x
    x = x + 1
change_global()
print x

# 函数嵌套


def multiplier(factor):
    def multiplyByFactor(number):  # 类似multiplyByFactor函数存储子封闭的行为叫做闭包
        return number * factor
    return multiplyByFactor

doubule = multiplier(2)
print doubule(5)
