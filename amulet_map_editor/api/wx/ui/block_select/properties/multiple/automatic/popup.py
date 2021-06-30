import wx
from typing import Tuple, Iterable


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
    def value(self) -> str:
        return self._check_list_box.GetStringSelection()

    @value.setter
    def value(self, value: str):
        self._check_list_box.SetStringSelection(value)

    @property
    def extra_values(self) -> Tuple[str]:
        return self._check_list_box.GetCheckedStrings()

    @extra_values.setter
    def extra_values(self, extra_values: Iterable[str]):
        self._check_list_box.SetCheckedStrings(extra_values)

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
        self.pvcl: PropertyValueCheckList = None
        self._values = values

    def Create(self, parent):
        self.pvcl = PropertyValueCheckList(parent, self._values)
        # self.pvcl.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        return True

    def OnLeftDown(self, evt):
        item = self.pvcl._check_list_box.HitTest(evt.GetPosition())
        if item >= 0:
            self.pvcl._check_list_box.Check(
                item, check=self.pvcl._check_list_box.IsChecked(item)
            )

    def GetControl(self):
        return self.pvcl

    def GetStringValue(self):
        return "|".join(self.pvcl.extra_values)

    def GetAdjustedSize(self, minWidth, prefHeight, maxHeight):
        self.GetControl().Fit()
        return self.GetControl().GetSize()
