import wx

from amulet_map_editor.programs.edit.canvas.events import (
    SelectToolEnabledEvent,
    OperationToolEnabledEvent,
    ImportToolEnabledEvent,
    ExportToolEnabledEvent
)


class ToolSelect(wx.Panel):
    def __init__(self, canvas):
        wx.Panel.__init__(self, canvas)

        self.select_button = wx.Button(self, label="Select")
        self.select_button.Bind(wx.EVT_BUTTON, self._select_evt)
        self.operation_button = wx.Button(self, label="Operation")
        self.operation_button.Bind(wx.EVT_BUTTON, self._operation_evt)

        self.import_button = wx.Button(self, label="Import")
        self.import_button.Bind(wx.EVT_BUTTON, self._import_evt)
        self.export_button = wx.Button(self, label="Export")
        self.export_button.Bind(wx.EVT_BUTTON, self._export_evt)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.select_button)
        sizer.Add(self.operation_button)
        sizer.Add(self.import_button)
        sizer.Add(self.export_button)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def _select_evt(self, evt):
        wx.PostEvent(self, SelectToolEnabledEvent())

    def _operation_evt(self, evt):
        wx.PostEvent(self, OperationToolEnabledEvent())

    def _import_evt(self, evt):
        wx.PostEvent(self, ImportToolEnabledEvent())

    def _export_evt(self, evt):
        wx.PostEvent(self, ExportToolEnabledEvent())
