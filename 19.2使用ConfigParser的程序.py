#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ConfigParser import ConfigParser

CONFIGFILE = "python.txt"

config = ConfigParser()
#读取配置文件：
config.read(CONFIGFILE)

#打印初始的问候语：
#要查看的区段是'message'
print config.get('messages', 'greeting')

#使用配置文件的一个问题读取半径：
radius = input(config.get('messages', 'question') +' ')# input参数为打印输入信息，在输入参数

#打印配置文件的结果信息
#以逗号借宿，已在同一行显示
print config.get('messages', 'result_message'),

#getfloat()将config值转换为float类型：
print config.getfloat('numbers', 'pi') * radius**2