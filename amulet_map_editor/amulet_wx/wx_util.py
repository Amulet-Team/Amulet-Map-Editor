import wx
from wx.lib.scrolledpanel import ScrolledPanel


class SimpleSizer:
    def __init__(self, sizer_dir=wx.VERTICAL):
        self.sizer = wx.BoxSizer(sizer_dir)

    def add_object(self, obj, space=1, options=wx.ALL):
        self.sizer.Add(
            obj,
            space,
            options,
            5
        )


class SimplePanel(wx.Panel, SimpleSizer):
    def __init__(self, parent, sizer_dir=wx.VERTICAL):
        wx.Panel.__init__(
            self,
            parent,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        SimpleSizer.__init__(self, sizer_dir)
        self.SetSizer(self.sizer)


class SimpleScrollablePanel(ScrolledPanel, SimpleSizer):
    def __init__(self, parent, sizer_dir=wx.VERTICAL):
        ScrolledPanel.__init__(
            self,
            parent,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        SimpleSizer.__init__(self, sizer_dir)
        self.SetSizer(self.sizer)
        self.SetupScrolling()
        self.SetAutoLayout(1)


class SimpleNotebook(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(
            self,
            parent,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            0
        )
