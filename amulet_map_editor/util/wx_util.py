import wx


class SimplePanel(wx.Panel):
    def __init__(self, parent, sizer_dir=wx.VERTICAL):
        super(SimplePanel, self).__init__(
            parent,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        self.sizer = wx.BoxSizer(sizer_dir)
        self.SetSizer(self.sizer)

    def add_object(self, obj):
        self.sizer.Add(
            obj,
            0,
            wx.ALL,
            5
        )
