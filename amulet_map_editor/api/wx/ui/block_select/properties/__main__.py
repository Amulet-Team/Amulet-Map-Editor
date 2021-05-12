import wx
import PyMCTranslate
from amulet_map_editor.api.wx.ui.block_select.properties import PropertySelect

if __name__ == "__main__":

    def main():
        translation_manager = PyMCTranslate.new_translation_manager()
        app = wx.App()
        for block in (("minecraft", "oak_fence"), ("modded", "block")):
            for cls in (
                PropertySelect,
                lambda *args: PropertySelect(*args, wildcard_mode=True),
            ):
                dialog = wx.Dialog(
                    None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
                )
                sizer = wx.BoxSizer()
                dialog.SetSizer(sizer)
                sizer.Add(
                    cls(dialog, translation_manager, "java", (1, 16, 0), False, *block),
                    1,
                    wx.ALL,
                    5,
                )

                def get_on_close(dialog_):
                    def on_close(evt):
                        dialog_.Destroy()

                    return on_close

                dialog.Bind(wx.EVT_CLOSE, get_on_close(dialog))
                dialog.Show()
                dialog.Fit()
        app.MainLoop()

    main()
