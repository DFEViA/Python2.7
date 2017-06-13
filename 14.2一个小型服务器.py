#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

#把本地地址绑定到套接字上
s.bind((host, port))

s.listen(5)
while True:
	c, addr = s.accept()
	print 'Got connection form', addr
	c.send('Thank you for connecting')
	c.close()