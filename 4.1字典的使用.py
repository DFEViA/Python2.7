#!usr/bin/python
# -*- coding: UTF-8 -*-
phonebook = {'Alice':'2341','Beth':'9102','Cecil':'3258' }
print phonebook['Alice']
#字典中的键是唯一的（其他类型的映射也是如此），而值并不唯一

#dict函数
items = [('name','Gumby'),('age',42)]
d = dict(items)
print d

#dict函数也可以通过关键字参数来创建字典
d = dict(name = 'Gumby',age=42)
print d

#4.2.2基本字典操作
#代码清单
people = {

    'xulongwei':{
        'addr':'朝阳路',
        'phone':'2341'
    },
    'changjinxin':{
        'addr':'昌平',
        'phone':'1231'
    },
    'huanchanjuan':{
        'addr':'宋庄',
        'phone':'1245'
    }
}
#针对电话号码和地址使用的描述性标签，会在打印输出的时候用到
labels = {
    'phone':'phone number',
    'addr':'address'
}
name = raw_input('Name:')
request = raw_input('Phone number(p) or address(a)?')
#查找电话号码还是地址"？使用正确的键：
#使用正确的键
if request == 'p':key = 'phone'
if request == 'a':key = 'addr'

if name in people:print "%s's %s is %s." %\
                        (name,labels[key],people[name][key])
