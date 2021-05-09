from amulet_map_editor.api.wx.ui.version_select import PlatformSelect, VersionSelect

if __name__ == "__main__":
    import wx
    import PyMCTranslate

    def main():
        translation_manager = PyMCTranslate.new_translation_manager()
        app = wx.App()
        for cls in (
            PlatformSelect,
            lambda *args: VersionSelect(*args, show_force_blockstate=False),
            VersionSelect,
        ):
            dialog = wx.Dialog(None)
            sizer = wx.BoxSizer()
            dialog.SetSizer(sizer)
            sizer.Add(cls(dialog, translation_manager), 0, wx.ALL, 5)
            dialog.Show()
            dialog.Fit()

            def get_on_close(dialog_):
                def on_close(evt):
                    dialog_.Destroy()
                return on_close
            dialog.Bind(wx.EVT_CLOSE, get_on_close(dialog))
        app.MainLoop()

    main()
