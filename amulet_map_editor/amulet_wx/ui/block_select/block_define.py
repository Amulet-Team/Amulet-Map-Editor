import wx
import wx.lib.scrolledpanel
from typing import Tuple

import PyMCTranslate
import amulet_nbt
from amulet.api.block import PropertyType

from amulet_map_editor.amulet_wx.ui.version_select import (
    VersionSelect,
    EVT_VERSION_CHANGE,
)
from amulet_map_editor.amulet_wx.ui.block_select.block import (
    BlockSelect,
    EVT_BLOCK_CHANGE,
)

if __name__ != "__main__":
    from amulet_map_editor.amulet_wx.ui.block_select.properties import PropertySelect


class BlockDefine(wx.Panel):
    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        orientation=wx.VERTICAL,
        platform: str = None,
        version_number: Tuple[int, int, int] = None,
        force_blockstate: bool = None,
        namespace: str = None,
        block_name: str = None,
        properties: PropertyType = None,
        nbt: amulet_nbt.TAG_Compound = None,
        show_nbt: bool = True,
        **kwargs,
    ):
        super().__init__(parent)

        sizer = wx.BoxSizer(orientation)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(left_sizer, 1, wx.EXPAND)
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        if orientation == wx.HORIZONTAL:
            sizer.Add(right_sizer, 1, wx.EXPAND | wx.LEFT, 5)
        else:
            sizer.Add(right_sizer, 1, wx.EXPAND | wx.TOP, 5)

        self._version_picker = VersionSelect(
            self,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            **kwargs,
        )
        left_sizer.Add(self._version_picker, 0, wx.EXPAND)

        self._block_picker = BlockSelect(
            self,
            translation_manager,
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            namespace,
            block_name,
            **kwargs,
        )
        left_sizer.Add(self._block_picker, 1, wx.EXPAND | wx.TOP, 5)
        self._version_picker.Bind(EVT_VERSION_CHANGE, self._on_version_change)

        self._property_picker = PropertySelect(
            self,
            translation_manager,
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            self._block_picker.namespace,
            self._block_picker.block_name,
            properties,
        )
        right_sizer.Add(self._property_picker, 1, wx.EXPAND)
        self._block_picker.Bind(EVT_BLOCK_CHANGE, self._on_block_change)

        self.SetSizerAndFit(sizer)
        self.Layout()

    def _on_version_change(self, evt):
        self._block_picker.version = (
            evt.platform,
            evt.version_number,
            evt.force_blockstate,
        )
        evt.Skip()

    def _on_block_change(self, evt):
        self._property_picker.version_block = (
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            evt.namespace,
            evt.block_name,
        )
        evt.Skip()


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

            sizer_1.Add(sizer_2, 0, wx.ALL, 5)
            self.block_define = BlockDefine(self, translation_manager, wx.HORIZONTAL)
            sizer_1.Add(self.block_define, 0, wx.ALL, 5)

            self.SetSizerAndFit(sizer_1)
            self.Layout()

            self.block_define._block_picker.Bind(EVT_BLOCK_CHANGE, self.on_block_change)

        def on_block_change(self, evt):
            self.block_label.SetLabelText(f"{evt.namespace}:{evt.block_name}")
            evt.Skip()

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
            self.collapsed.block_label.SetLabelText(self.expanded.block_label.GetLabelText())
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


class ComplexBlockPicker(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, translation_manager):
        super(ComplexBlockPicker, self).__init__(parent, style=wx.SIMPLE_BORDER)
        self.SetupScrolling()

        self.translation_manager = translation_manager

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.block_picker_sizer = wx.BoxSizer(wx.VERTICAL)

        self.block_picker_sizer.Add(
            _BlockPicker(self, translation_manager), 0, wx.TOP | wx.BOTTOM, 5
        )

        self.sizer.Add(self.block_picker_sizer)

        self.add_button = wx.Button(self, label="+")
        self.sizer.Add(self.add_button, 0, wx.ALL, 5)

        self.SetSizerAndFit(self.sizer)
        self.Layout()

        self.add_button.Bind(wx.EVT_BUTTON, self.add_block_picker)

    def add_block_picker(self, evt):
        # index = self.block_picker_sizer.ItemCount
        # for i, child in enumerate(self.block_picker_sizer.GetChildren()):
        #    if not child.IsShown:
        #        index = i - 1
        #        break

        block_picker = _BlockPicker(self, self.translation_manager)
        # self.block_picker_sizer.Insert(index, block_picker)
        self.block_picker_sizer.Add(block_picker, 0, wx.TOP | wx.BOTTOM, 5)
        self.block_picker_sizer.Layout()
        self.sizer.Layout()
        self.Layout()
        self.Refresh()


if __name__ == "__main__":
    app = wx.App()
    import wx.lib.inspection

    wx.lib.inspection.InspectionTool().Show()
    from amulet_map_editor.amulet_wx.ui.block_select.properties import PropertySelect

    def main():
        translation_manager = PyMCTranslate.new_translation_manager()
        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(
            ComplexBlockPicker(dialog, translation_manager), 1, wx.ALL | wx.EXPAND, 5
        )
        dialog.Layout()
        dialog.Show()
        dialog.Fit()
        app.MainLoop()

    main()
