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


class ExampleFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.CreateStatusBar()  # A Statusbar in the bottom of the window
        self.toolbar = self.CreateToolBar()
        ##self.toolbar.AddSimpleTool(wx.NewId(), images.getNewBitmap(), "New", "Long help for 'New'")
        self.toolbar.Realize()

        panel = wx.Panel(self)
        panel.SetBackgroundColour('Red')
        self.quote = wx.StaticText(panel, label="Your quote: ", pos=(20, 30))
        self.button1 = wx.Button(panel, label="启动", pos=(40,50))
        self.button = wx.Button(panel, label="关闭")
        self.Show()


app = wx.App(False)
ExampleFrame(None)
app.MainLoop()