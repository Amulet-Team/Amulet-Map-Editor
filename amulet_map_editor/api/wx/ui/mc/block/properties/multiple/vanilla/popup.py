import wx
from typing import Tuple, Iterable, Optional, Sequence


class PropertyValueCheckList(wx.Panel):
    def __init__(
        self, parent: wx.Window, values: Iterable[str], selected: Iterable[bool]
    ):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self._toggle_checkbox = wx.CheckBox(self, style=wx.CHK_3STATE)
        self._toggle_checkbox.Set3StateValue(wx.CHK_CHECKED)
        sizer.Add(self._toggle_checkbox, 0, wx.ALL, 3)
        self._check_list_box = wx.CheckListBox(self, choices=values)
        self._check_list_box.SetCheckedStrings(
            [value for value, select in zip(values, selected) if select]
        )
        sizer.Add(self._check_list_box, 0)

        self._toggle_checkbox.Bind(wx.EVT_CHECKBOX, self._on_toggle)
        self._check_list_box.Bind(wx.EVT_LEFT_DOWN, self._on_left_down)

    @property
    def check_list_box(self) -> wx.CheckListBox:
        return self._check_list_box

    def _on_toggle(self, evt):
        if self._toggle_checkbox.GetValue():
            self._check_list_box.SetCheckedItems(
                list(range(self._check_list_box.GetCount()))
            )
        else:
            self._check_list_box.SetCheckedItems([])

    def update_check(self):
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
            self.update_check()


class PropertyValueComboPopup(wx.ComboPopup):
    def __init__(self, values: Iterable[str], selected: Iterable[bool]):
        super().__init__()
        self._check_list: Optional[PropertyValueCheckList] = None
        self._state = values, selected

    @property
    def _check_list_box(self) -> wx.CheckListBox:
        return self._check_list.check_list_box

    def GetCheckedStrings(self) -> Tuple[str]:
        return self._check_list_box.GetCheckedStrings()

    def SetCheckedStrings(self, strings: Sequence[str]):
        self._check_list_box.SetCheckedStrings(strings)
        self._check_list.update_check()

    def GetItems(self) -> Tuple[str]:
        return self._check_list_box.GetItems()

    def SetItems(self, strings: Sequence[str]):
        self._check_list_box.SetItems(strings)

    def Create(self, parent):
        self._check_list = PropertyValueCheckList(parent, *self._state)
        return True

    def GetControl(self):
        return self._check_list

    def GetStringValue(self):
        return "|".join(self.GetCheckedStrings())

    def GetAdjustedSize(self, minWidth, prefHeight, maxHeight):
        self.GetControl().Fit()
        return self.GetControl().GetSize()
