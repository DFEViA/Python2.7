#!/usr/bin/python

import cgi
form = cgi.FieldStorage()

name = form.getvalue('name', 'world')

print 'Content-type: text/plain\n\n'

print 'Hello, %s!' % name