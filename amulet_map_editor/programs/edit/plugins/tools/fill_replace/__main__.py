import wx
import PyMCTranslate
from amulet_map_editor.programs.edit.plugins.tools.fill_replace.fill_replace_widget import (
    FillReplaceWidget,
)

if __name__ == "__main__":

    def main():
        app = wx.App()
        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(
            FillReplaceWidget(dialog, PyMCTranslate.new_translation_manager()),
            1,
            wx.ALL | wx.EXPAND,
            5,
        )
        dialog.Show()
        dialog.Fit()
        dialog.Bind(wx.EVT_CLOSE, lambda evt: dialog.Destroy())
        app.MainLoop()

    main()
