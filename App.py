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
    pass

class App(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent = None, id=-1 , title='spavce')
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()








