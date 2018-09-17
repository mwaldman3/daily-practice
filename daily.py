import wx

class FlashCardFrame(wx.Frame):
	def __init__(self, *args, **kw):
		super(FlashCardFrame, self).__init__(*args, **kw)
		
		pnl = wx.Panel(self)
		st = wx.StaticText(pnl, label="abcdef", pos=(25,25))
		font = st.GetFont()
		font.PointSize += 10
		st.SetFont(font)

if __name__ == '__main__':
	app = wx.App()
	frm = FlashCardFrame(None, title='Daily Practice')
	frm.Show()
	app.MainLoop()
	