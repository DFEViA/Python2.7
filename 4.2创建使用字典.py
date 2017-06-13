#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 字典的格式化字符串

# 字典方法
# clear方法清除字典中所有的项。这是个原地操作，所有无返回值
d = {}
d['name'] = 'Gumby'
d['age'] = '42'
print d
d.clear()
print d
returned_value = d.clear()
print returned_value

# fromkeys方法使用给定的键建立新的字典，每个键默认对应的值为None
print {}.fromkeys(['name', 'age'])
print dict.fromkeys(['name', 'age'], '(unknonwn)')
