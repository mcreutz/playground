# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import wx.lib.agw.ribbon as rb

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1049,554 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		m_checkList1Choices = []
		self.m_checkList1 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0 )
		bSizer1.Add( self.m_checkList1, 0, wx.ALL, 5 )

		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_dataViewListCtrl1, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 0, wx.ALIGN_RIGHT, 5 )

		self.m_ribbonBar1 = rb.RibbonBar( self , wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_BAR_DEFAULT_STYLE )
		self.m_ribbonPage1 = rb.RibbonPage( self.m_ribbonBar1, wx.ID_ANY, u"MyRibbonPage" , wx.NullBitmap , 0 )
		self.m_ribbonPanel1 = rb.RibbonPanel( self.m_ribbonPage1, wx.ID_ANY, u"MyRibbonPanel" , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.m_ribbonBar1.Realize()

		bSizer1.Add( self.m_ribbonBar1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menu1.AppendSubMenu( self.m_menu11, u"MyMenu" )

		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menu1.AppendSeparator()

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu1, u"MyMenu" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_tool1 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.AddSeparator()

		self.m_tool2 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_infoCtrl1 = wx.InfoBar( self.m_toolBar1 )
		self.m_infoCtrl1.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.m_infoCtrl1.SetEffectDuration( 500 )
		self.m_toolBar1.AddControl( self.m_infoCtrl1 )
		self.m_toolBar1.Realize()


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


