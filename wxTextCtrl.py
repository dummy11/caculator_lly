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
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)


app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()