#!/usr/bin/python
# -*- coding: UTF-8 -*-
import area
'''from area import 
height = 3
width = 4
correct_answer = 12
answer = area(height, width)
if answer == correct_answer:
    print 'Test passer'
else:
    print 'Test faild'''

print[n for n in dir(area) if not n.startswith('_')]
print area.__file__