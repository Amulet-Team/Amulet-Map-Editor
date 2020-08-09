import wx
import wx.lib.scrolledpanel
from typing import List

import PyMCTranslate

from amulet_map_editor.api.image import (
    UP_CARET,
    DOWN_CARET,
    TRASH,
    ADD_ICON,
    MAXIMIZE,
    MINIMIZE,
)
from amulet_map_editor.api.wx.ui.block_select import BlockDefine, EVT_PROPERTIES_CHANGE


class MultiBlockDefine(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, translation_manager, style=0):
        super().__init__(parent, style=style)
        self.SetupScrolling()

        self._translation_manager = translation_manager

        self._sizer = wx.BoxSizer(wx.VERTICAL)

        self._add_button = wx.BitmapButton(self, bitmap=ADD_ICON.bitmap(18, 18))
        self._sizer.Add(self._add_button, 0, wx.TOP | wx.LEFT | wx.RIGHT | wx.EXPAND, 5)

        self._block_picker_sizer = wx.BoxSizer(wx.VERTICAL)

        self._block_picker_sizer.Add(
            _CollapsibleBlockDefine(self, translation_manager), 0, wx.TOP | wx.EXPAND, 5
        )
        self._sizer.Add(
            self._block_picker_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5
        )

        self.SetSizerAndFit(self._sizer)
        self.Layout()

        self._add_button.Bind(wx.EVT_BUTTON, self._add)
        self._fix_enabled_buttons()

    def _add(self, evt):
        self.Freeze()
        self.collapse()
        block_picker = _CollapsibleBlockDefine(self, self._translation_manager)
        self._block_picker_sizer.Add(block_picker, 1, wx.TOP | wx.EXPAND, 5)
        self._block_picker_sizer.Layout()
        self._sizer.Layout()
        self.Layout()
        self._fix_enabled_buttons()
        self.Refresh()
        self.Thaw()

    def move_up(self, obj):
        sizer = self._block_picker_sizer
        index = [child.Window for child in sizer.GetChildren()].index(obj)

        sizer.Detach(obj)
        sizer.Insert(index - 1 if index > 0 else 0, obj, 0, wx.TOP | wx.EXPAND, 5)
        self._fix_enabled_buttons()
        self.Layout()

    def move_down(self, obj):
        sizer = self._block_picker_sizer
        length = sizer.ItemCount
        index = [child.Window for child in sizer.GetChildren()].index(obj)

        sizer.Detach(obj)
        sizer.Insert(
            index + 1 if index < length - 1 else length - 1,
            obj,
            0,
            wx.TOP | wx.EXPAND,
            5,
        )
        self._fix_enabled_buttons()
        self.Layout()

    def delete(self, obj):
        obj.Hide()
        obj.Destroy()
        self._fix_enabled_buttons()
        self.Layout()

    def collapse(self):
        for child in self._block_picker_sizer.GetChildren():
            child.Window.collapsed = True

    def _fix_enabled_buttons(self):
        windows: List[_CollapsibleBlockDefine] = [
            child.Window for child in self._block_picker_sizer.GetChildren()
        ]
        for window in windows:
            window.up_button.Enable()
            window.down_button.Enable()
            window.delete_button.Enable()

        if len(windows) >= 1:
            windows[0].up_button.Disable()
            windows[-1].down_button.Disable()
        if len(windows) == 1:
            windows[0].delete_button.Disable()


class _CollapsibleBlockDefine(wx.Panel):
    def __init__(self, parent: MultiBlockDefine, translation_manager, collapsed=False):
        super().__init__(parent, style=wx.BORDER_SIMPLE)

        self.EXPAND = MAXIMIZE.bitmap(18, 18)
        self.COLLAPSE = MINIMIZE.bitmap(18, 18)

        self._collapsed = collapsed

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        header_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(header_sizer, 0, wx.ALL, 5)

        self.expand_button = wx.BitmapButton(self, bitmap=self.EXPAND)
        header_sizer.Add(self.expand_button, 0, 5)

        self.up_button = wx.BitmapButton(self, bitmap=UP_CARET.bitmap(18, 18))
        header_sizer.Add(self.up_button, 0, wx.LEFT, 5)
        self.up_button.Bind(wx.EVT_BUTTON, lambda evt: parent.move_up(self))

        self.down_button = wx.BitmapButton(self, bitmap=DOWN_CARET.bitmap(18, 18))
        header_sizer.Add(self.down_button, 0, wx.LEFT, 5)
        self.down_button.Bind(wx.EVT_BUTTON, lambda evt: parent.move_down(self))

        self.delete_button = wx.BitmapButton(self, bitmap=TRASH.bitmap(18, 18))
        header_sizer.Add(self.delete_button, 0, wx.LEFT, 5)
        self.delete_button.Bind(wx.EVT_BUTTON, lambda evt: parent.delete(self))

        self.block_define = BlockDefine(self, translation_manager, wx.HORIZONTAL)
        sizer.Add(self.block_define, 1, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 5)
        self.collapsed = collapsed

        self.block_label = wx.StaticText(
            self,
            label=self._gen_block_string(),
            style=wx.ST_ELLIPSIZE_END | wx.ST_NO_AUTORESIZE,
            size=(500, -1),
        )
        header_sizer.Add(self.block_label, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)

        self.expand_button.Bind(
            wx.EVT_BUTTON, lambda evt: self._toggle_block_expand(parent)
        )
        self.block_define.Bind(EVT_PROPERTIES_CHANGE, self._on_properties_change)

    @property
    def collapsed(self) -> bool:
        return self._collapsed

    @collapsed.setter
    def collapsed(self, collapsed: bool):
        self._collapsed = collapsed
        if self._collapsed:
            self.expand_button.SetBitmap(self.EXPAND)
            self.block_define.Hide()
        else:
            self.expand_button.SetBitmap(self.COLLAPSE)
            self.block_define.Show()
        self.TopLevelParent.Layout()

    def _toggle_block_expand(self, parent: MultiBlockDefine):
        if self.collapsed:
            parent.collapse()
        self.collapsed = not self.collapsed

    def _on_properties_change(self, evt):
        self.block_label.SetLabel(self._gen_block_string())
        self.TopLevelParent.Layout()
        evt.Skip()

    def _gen_block_string(self):
        base = f"{self.block_define.namespace}:{self.block_define.block_name}"
        properties = ",".join(
            (
                f"{key}={value}"
                for key, value in self.block_define.str_properties.items()
            )
        )
        return f"{base}[{properties}]" if properties else base


if __name__ == "__main__":

    def main():
        app = wx.App()
        translation_manager = PyMCTranslate.new_translation_manager()
        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(MultiBlockDefine(dialog, translation_manager), 1, wx.EXPAND)
        dialog.Show()
        dialog.Fit()
        app.MainLoop()

    main()
