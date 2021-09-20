import wx
from typing import Tuple, Iterable, Optional

from amulet.api.block import PropertyValueType
import amulet_nbt


class PropertyValueCheckList(wx.Panel):
    def __init__(self, parent: wx.Window, values: Iterable[str]):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self._toggle_checkbox = wx.CheckBox(self, style=wx.CHK_3STATE)
        self._toggle_checkbox.Set3StateValue(wx.CHK_CHECKED)
        sizer.Add(self._toggle_checkbox, 0, wx.ALL, 3)
        self._check_list_box = wx.CheckListBox(self, choices=values)
        self._check_list_box.SetCheckedStrings(values)
        sizer.Add(self._check_list_box, 0)

        self._toggle_checkbox.Bind(wx.EVT_CHECKBOX, self._on_toggle)
        self._check_list_box.Bind(wx.EVT_LEFT_DOWN, self._on_left_down)

    @property
    def checked_snbt(self) -> Tuple[str, ...]:
        return self._check_list_box.GetCheckedStrings()

    @checked_snbt.setter
    def checked_snbt(self, checked_snbt: Iterable[str]):
        self._check_list_box.SetCheckedStrings(checked_snbt)

    @property
    def checked_nbt(self) -> Tuple[PropertyValueType, ...]:
        nbt = []
        for entry in self._check_list_box.GetCheckedStrings():
            try:
                nbt.append(amulet_nbt.from_snbt(entry))
            except:
                pass
        return tuple(nbt)

    @checked_nbt.setter
    def checked_nbt(self, checked_nbt: Iterable[PropertyValueType]):
        self._check_list_box.SetCheckedStrings([v.to_snbt() for v in checked_nbt])

    @property
    def all_nbt(self) -> Tuple[PropertyValueType, ...]:
        nbt = []
        for entry in self._check_list_box.GetStrings():
            try:
                nbt.append(amulet_nbt.from_snbt(entry))
            except:
                pass
        return tuple(nbt)

    def _on_toggle(self, evt):
        if self._toggle_checkbox.GetValue():
            self._check_list_box.SetCheckedItems(
                list(range(self._check_list_box.GetCount()))
            )
        else:
            self._check_list_box.SetCheckedItems([])

    def _update_check(self):
        items = self._check_list_box.GetCheckedItems()
        if len(items) == self._check_list_box.GetCount():
            self._toggle_checkbox.Set3StateValue(wx.CHK_CHECKED)
        elif len(items) == 0:
            self._toggle_checkbox.Set3StateValue(wx.CHK_UNCHECKED)
        else:
            self._toggle_checkbox.Set3StateValue(wx.CHK_UNDETERMINED)

    def _on_left_down(self, evt):
        # not sure why I need to do this but it works
        item = self._check_list_box.HitTest(evt.GetPosition())
        if item >= 0:
            self._check_list_box.Check(
                item, check=not self._check_list_box.IsChecked(item)
            )
            self._update_check()


class PropertyValueComboPopup(wx.ComboPopup):
    def __init__(self, values: Iterable[str]):
        super().__init__()
        self._check_list: Optional[PropertyValueCheckList] = None
        self._values = values

    @property
    def all_nbt(self) -> Tuple[PropertyValueType, ...]:
        return self._check_list.all_nbt

    @property
    def checked_nbt(self) -> Tuple[PropertyValueType, ...]:
        return self._check_list.checked_nbt

    @checked_nbt.setter
    def checked_nbt(self, checked_nbt: Iterable[PropertyValueType]):
        self._check_list.checked_nbt = checked_nbt

    def Create(self, parent):
        self._check_list = PropertyValueCheckList(parent, self._values)
        return True

    def GetControl(self):
        return self._check_list

    def GetStringValue(self):
        return "|".join(self._check_list.checked_snbt)

    def GetAdjustedSize(self, minWidth, prefHeight, maxHeight):
        self.GetControl().Fit()
        return self.GetControl().GetSize()
