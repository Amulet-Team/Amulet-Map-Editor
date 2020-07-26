import wx
import wx.lib.scrolledpanel

import PyMCTranslate

from amulet_map_editor.amulet_wx.ui.block_select.block import EVT_BLOCK_CHANGE
if __name__ != '__main__':
    from amulet_map_editor.amulet_wx.ui.block_select.block_define import BlockDefine


class _BlockPicker(wx.Panel):
    class CollpasedBlockDefine(wx.Panel):
        def __init__(self, parent: "_BlockPicker"):
            super().__init__(parent)

            sizer = wx.BoxSizer(wx.HORIZONTAL)

            self.expand_btn = wx.Button(
                self, wx.ID_ANY, "Expand", wx.DefaultPosition, wx.DefaultSize, 0
            )
            sizer.Add(self.expand_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.mv_up_btn = wx.Button(
                self, wx.ID_ANY, "Move Up", wx.DefaultPosition, wx.DefaultSize, 0
            )
            sizer.Add(self.mv_up_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.mv_dwn_btn = wx.Button(
                self, wx.ID_ANY, "Move Down", wx.DefaultPosition, wx.DefaultSize, 0
            )
            sizer.Add(self.mv_dwn_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.delete_btn = wx.Button(
                self, wx.ID_ANY, "Delete", wx.DefaultPosition, wx.DefaultSize, 0
            )
            sizer.Add(self.delete_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.block_label = wx.StaticText(
                self, wx.ID_ANY, "N/A", wx.DefaultPosition, wx.DefaultSize, 0
            )
            self.block_label.Wrap(-1)

            sizer.Add(self.block_label, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.SetSizer(sizer)
            self.Layout()

            self.expand_btn.Bind(
                wx.EVT_BUTTON, lambda evt: parent.panel_change("expand", evt)
            )
            self.mv_up_btn.Bind(wx.EVT_BUTTON, parent.move_up)
            self.mv_dwn_btn.Bind(wx.EVT_BUTTON, parent.move_down)
            self.delete_btn.Bind(wx.EVT_BUTTON, parent.delete)

    class ExpandedBlockDefine(wx.Panel):
        def __init__(self, parent, translation_manager):
            super().__init__(parent)

            sizer_1 = wx.BoxSizer(wx.VERTICAL)

            sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

            self.expand_btn = wx.Button(
                self, wx.ID_ANY, "Collapse", wx.DefaultPosition, wx.DefaultSize, 0
            )
            sizer_2.Add(self.expand_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.mv_up_btn = wx.Button(
                self, wx.ID_ANY, "Move Up", wx.DefaultPosition, wx.DefaultSize, 0
            )
            sizer_2.Add(self.mv_up_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.mv_dwn_btn = wx.Button(
                self, wx.ID_ANY, "Move Down", wx.DefaultPosition, wx.DefaultSize, 0
            )
            sizer_2.Add(self.mv_dwn_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.delete_btn = wx.Button(
                self, wx.ID_ANY, "Delete", wx.DefaultPosition, wx.DefaultSize, 0
            )
            sizer_2.Add(self.delete_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.block_label = wx.StaticText(
                self, wx.ID_ANY, "N/A", wx.DefaultPosition, wx.DefaultSize, 0
            )
            self.block_label.Wrap(-1)

            sizer_2.Add(self.block_label, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.expand_btn.Bind(
                wx.EVT_BUTTON, lambda evt: parent.panel_change("collapse", evt)
            )
            self.mv_up_btn.Bind(wx.EVT_BUTTON, parent.move_up)
            self.mv_dwn_btn.Bind(wx.EVT_BUTTON, parent.move_down)
            self.delete_btn.Bind(wx.EVT_BUTTON, parent.delete)

            sizer_1.Add(sizer_2)
            self.block_define = BlockDefine(self, translation_manager, wx.HORIZONTAL)
            sizer_1.Add(self.block_define, 0, wx.ALL, 5)

            self.SetSizerAndFit(sizer_1)
            self.Layout()

            self.block_define._block_picker.Bind(EVT_BLOCK_CHANGE, self.on_block_change)

        def on_block_change(self, evt):
            self.block_label.SetLabelText(f"{evt.namespace}:{evt.block_name}")
            evt.Skip()

        def gen_block_string(self):
            base = f"{self.block_define._block_picker.namespace}:{self.block_define._block_picker.block_name}"
            properties = ','.join(
                (
                    f"{key}={value}" for key, value in self.block_define._property_picker.properties.items()
                )
            )
            return f"{base}[{properties}]" if properties else base

    def __init__(self, parent, translation_manager):
        super().__init__(parent, style=wx.SIMPLE_BORDER)

        self.expanded = _BlockPicker.ExpandedBlockDefine(self, translation_manager)
        self.collapsed = _BlockPicker.CollpasedBlockDefine(self)

        self.expanded.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.expanded)
        self.sizer.Add(self.collapsed)

        self.SetSizerAndFit(self.sizer)
        self.Layout()

    def panel_change(self, action, evt):
        if action == "collapse":
            self.expanded.Hide()
            self.collapsed.block_label.SetLabelText(
                self.expanded.gen_block_string()
            )
            self.collapsed.Show()
        elif action == "expand":
            self.collapsed.Hide()
            self.expanded.Show()
        self.SetSizerAndFit(self.sizer)
        self.Layout()
        parent = self.GetParent()
        while parent is not None:
            parent.Layout()
            parent = parent.GetParent()

    def move_up(self, evt):
        parent = self.GetParent()
        sizer = parent.GetSizer()
        index = [child.Window for child in sizer.GetChildren()].index(self)

        sizer.Detach(self)
        sizer.Insert(index - 1 if index > 0 else 0, self, 0, wx.ALL, 5)
        parent.Layout()

    def move_down(self, evt):
        parent = self.GetParent()
        sizer = parent.GetSizer()
        length = sizer.ItemCount
        index = [child.Window for child in sizer.GetChildren()].index(self)

        sizer.Detach(self)
        sizer.Insert(index + 1 if index < length else length, self, 0, wx.ALL, 5)
        parent.Layout()

    def delete(self, evt):
        parent = self.GetParent()
        sizer = parent.GetSizer()
        self.Hide()
        self.Destroy()
        sizer.Layout()
        parent.Layout()
        parent.Refresh()


class MultiBlockDefine(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, translation_manager):
        super(MultiBlockDefine, self).__init__(parent, style=wx.SIMPLE_BORDER)
        self.SetupScrolling()

        self.translation_manager = translation_manager

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.block_picker_sizer = wx.BoxSizer(wx.VERTICAL)

        self.block_picker_sizer.Add(
            _BlockPicker(self, translation_manager), 0, wx.ALL | wx.EXPAND, 5
        )

        self.sizer.Add(self.block_picker_sizer)

        self.add_button = wx.Button(self, label="+")
        self.sizer.Add(self.add_button, 0, wx.ALL, 5)

        self.SetSizerAndFit(self.sizer)
        self.Layout()

        self.add_button.Bind(wx.EVT_BUTTON, self.add_block_picker)

    def add_block_picker(self, evt):
        block_picker = _BlockPicker(self, self.translation_manager)
        self.block_picker_sizer.Add(block_picker, 0, wx.ALL | wx.EXPAND, 5)
        self.block_picker_sizer.Layout()
        self.sizer.Layout()
        self.Layout()
        self.Refresh()


if __name__ == "__main__":
    app = wx.App()
    import wx.lib.inspection
    from amulet_map_editor.amulet_wx.ui.block_select.block_define import BlockDefine

    wx.lib.inspection.InspectionTool().Show()

    def main():
        translation_manager = PyMCTranslate.new_translation_manager()
        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(MultiBlockDefine(dialog, translation_manager), 1, wx.ALL | wx.EXPAND, 5)
        dialog.Show()
        dialog.Fit()
        app.MainLoop()

    main()
