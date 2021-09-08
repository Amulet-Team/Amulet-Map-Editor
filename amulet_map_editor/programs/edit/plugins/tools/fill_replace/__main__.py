import wx
import PyMCTranslate
from amulet_map_editor.programs.edit.plugins.tools.fill_replace.fill_replace_widget import (
    FillReplaceWidget,
)
from amulet_map_editor.api.wx.ui.events import EVT_CHILD_SIZE, ChildSizeEvent

if __name__ == "__main__":
    class FillReplaceTool(wx.BoxSizer):
        def __init__(self, canvas):
            wx.BoxSizer.__init__(self, wx.VERTICAL)
            self._panel = wx.Panel(canvas)
            self.Add(self._panel)
            panel_sizer = wx.BoxSizer(wx.VERTICAL)
            self._panel.SetSizer(panel_sizer)
            self._operations = FillReplaceWidget(
                self._panel,
                PyMCTranslate.new_translation_manager(),
            )
            panel_sizer.Add(self._operations, 1, wx.LEFT | wx.TOP, 5)
            self._button = wx.Button(self._panel, label="Run Operation")
            panel_sizer.Add(self._button, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.TOP | wx.FIXED_MINSIZE, 5)


    def main():
        app = wx.App()
        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        cls = FillReplaceTool(dialog)
        sizer.Add(
            cls,
            1,
            wx.ALL,
            5,
        )
        dialog.Show()
        dialog.Fit()
        def do_layout(evt):
            dialog.Layout()
        dialog.Bind(EVT_CHILD_SIZE, do_layout)
        dialog.Bind(wx.EVT_CLOSE, lambda evt: dialog.Destroy())
        wx.lib.inspection.InspectionTool().Show()
        app.MainLoop()

    main()
