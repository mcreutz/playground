import wx, gui

class CalcFrame(gui.MyFrame1):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MyFrame1.__init__(self,parent)
 
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of CalcFrame
frame = CalcFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()