import wx

from amulet_map_editor.plugins.programs.edit.events import (
    SelectToolEnabledEvent,
    OperationToolEnabledEvent
)


class ToolSelect(wx.Panel):
    def __init__(self, canvas):
        wx.Panel.__init__(self, canvas)

        self.select_button = wx.Button(self, label="Select")
        self.select_button.Bind(wx.EVT_BUTTON, self._select_evt)
        self.operation_button = wx.Button(self, label="Operation")
        self.operation_button.Bind(wx.EVT_BUTTON, self._operation_evt)

        # self.import_button = wx.Button(self, label="Import")
        # self.export_button = wx.Button(self, label="Export")

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.select_button)
        sizer.Add(self.operation_button)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def _select_evt(self, evt):
        wx.PostEvent(self, SelectToolEnabledEvent())

    def _operation_evt(self, evt):
        wx.PostEvent(self, OperationToolEnabledEvent())
