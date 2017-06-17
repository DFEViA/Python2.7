#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi
form = cgi.FileStorage()

name = form.getvalue('name', 'world')

print """Content-type: text/html

<html>
  <head>
    <title>Greeting Page</tittle>
  </head>
  <body>
    <h1>Hello, %s!</h1>


    <form action='simple3.cgi'>
    Change name <input type='text' name='name' />
    <input type='submit' />
    </form>
  </body>
</html>
""" % name