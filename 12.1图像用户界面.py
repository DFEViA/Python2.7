#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 12.3.3标签、标题和位置
'''import wx


app = wx.App()
win = wx.Frame(None, title="Simple Editor", size=(410, 335))
win.Show()
loadButton = wx.Button(win, label='Open', pos=(225, 5), size=(80, 25))
saveButton = wx.Button(win, label='Save', pos=(315, 5), size=(80, 25))
filename = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))
contents = wx.TextCtrl(win, pos=(5, 35), size=(
    390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)
app.MainLoop()
'''

# 一个很基础（但是不实用）的方法是使用pos和size参数在构造函数内设置和尺寸。

# 12.3.4更智能的布局
# 在wx内进行布局的最简单方法是使用尺寸器（sizer），最容易使用的工具就是wx.BoxSizer。

'''def load(event):
	file = open(filename.GetValue())
	contents.SetValue(file.read())
	file.close()

def save(event):
	file = open(filename.GetValue(), 'w')
	file.write(contents.GetValue())
	file.close()

app = wx.App()
win = wx.Frame(None, title="Simple Editor", size=(410, 335))

bkg = wx.Panel(win)

# 定义控件
loadButton = wx.Button(bkg, label='Open')
loadButton.Bind(wx.EVT_BUTTON, load)

saveButton = wx.Button(bkg, label='Save')
saveButton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style = wx.TE_MULTILINE | wx.HSCROLL)

# 定义布局
hbox = wx.BoxSizer()
hbox.Add(filename, proportion = 1, flag = wx.EXPAND)
hbox.Add(loadButton, proportion = 0, flag = wx.Left, border = 5)
hbox.Add(saveButton, proportion = 0, flag = wx.Left, border = 5)

vbox = wx.BoxSizer(wx.VERTICAL)# 构造函数主要用来创建对象时初始化对象
vbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
vbox.Add(contents, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()'''

# 12.3.4事件处理
# 在GUI术语中，用户执行的动作（比如点击按钮）叫做事件（event）。
# 利用不见的Bind方法可以将时间处理函数链接到给定的时间上。

# 12.3.6 完成了的程序

# 12.4 但是我宁愿用......
import wx

def hello(event):
	print 'Hello, world!'

app = wx.App()

win = wx.Frame(None, title = "Hello, wxPython!", size = (200, 100))

button = wx.Button(win, label= 'Hello')
button.Bind(wx.EVT_BUTTON, hello)

win.Show()
app.MainLoop()

# 12.4.1 使用TKinter
# 12.4.2 使用Jython和Swing

# 12.4.3 使用其他开发包

