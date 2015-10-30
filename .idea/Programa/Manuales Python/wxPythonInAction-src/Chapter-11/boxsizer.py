import wx
from blockwindow import BlockWindow

labels = "one two three four".split()

class TestFrame(wx.Frame):
    title = "none"
    def __init__(self):
        wx.Frame.__init__(self, None, -1, self.title)
        sizer = self.CreateSizerAndWindows()
        self.SetSizer(sizer)
        self.Fit()
        
class VBoxSizerFrame(TestFrame):
    title = "Vertical BoxSizer"
    
    def CreateSizerAndWindows(self):



        sizer = wx.BoxSizer(wx.HORIZONTAL)

        sizer = wx.BoxSizer(wx.VERTICAL)
        return sizer
    

class HBoxSizerFrame(TestFrame):
    title = "Horizontal BoxSizer"

    def CreateSizerAndWindows(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        dg_st=wx.StaticText(self, -1, "DATOS GENERALES")
        sizer.Add(dg_st, flag=wx.ALIGN_CENTER)





app = wx.PySimpleApp()
frameList = [VBoxSizerFrame, HBoxSizerFrame]
for klass in frameList:
    frame = klass()
    frame.Show()
app.MainLoop()
