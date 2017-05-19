#!/user/bin/env python
# encoding: utf-8

"""
@Version: python2.7
@Author: 'linyue.li'
@License: personality reserved
@Site: 'www.dummy11.cm'
@File_name: .py
@Time : 2017/05/05 15:20
@Discription: ...
"""

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None, id=-1, title="Hello Huntersun", pos=(-1,-1),size=(100,200),style=wx.DEFAULT_FRAME_STYLE|wx.CAPTION)
        self.Show()

app = wx.App()
frame = MyFrame()
app.MainLoop()

