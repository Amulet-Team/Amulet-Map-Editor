"""A collection of classes for wx objects to abstract away
the repeated code and make working with wx a bit more simple."""

import wx
from wx.lib.scrolledpanel import ScrolledPanel
from typing import Iterable, Union, Any, List, Optional, Sequence, Dict, Tuple


class SimpleSizer:
    def __init__(self, sizer_dir=wx.VERTICAL):
        self._sizer = self.sizer = wx.BoxSizer(sizer_dir)

    def add_object(self, obj, space=1, options=wx.ALL):
        self.sizer.Add(obj, space, options, 5)


class SimplePanel(wx.Panel, SimpleSizer):
    def __init__(self, parent: wx.Window, sizer_dir=wx.VERTICAL):
        wx.Panel.__init__(
            self,
            parent,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        SimpleSizer.__init__(self, sizer_dir)
        self.SetSizer(self.sizer)


class SimpleScrollablePanel(ScrolledPanel, SimpleSizer):
    """A scrolled panel that automatically sets itself up."""

    def __init__(self, parent: wx.Window, sizer_dir=wx.VERTICAL, **kwargs):
        ScrolledPanel.__init__(self, parent, **kwargs)
        SimpleSizer.__init__(self, sizer_dir)
        self.SetSizer(self.sizer)
        self.SetupScrolling()
        self.SetAutoLayout(1)

    def DoGetBestSize(self):
        sizer = self.GetSizer()
        if sizer is None:
            return -1, -1
        else:
            sx, sy = sizer.CalcMin()
            return (
                sx + wx.SystemSettings.GetMetric(wx.SYS_VSCROLL_X),
                sy + wx.SystemSettings.GetMetric(wx.SYS_HSCROLL_Y),
            )


class SimpleChoice(wx.Choice):
    """A wrapper for wx.Choice that sets up the UI for you."""

    def __init__(
        self,
        parent: wx.Window,
        choices: Sequence[str] = (),
        default: Optional[str] = None,
    ):
        super().__init__(parent, choices=choices)
        if choices:
            if default is not None and default in choices:
                self.SetSelection(choices.index(default))
            else:
                self.SetSelection(0)

    def GetCurrentString(self) -> str:
        return self.GetString(self.GetSelection())


StringableType = Any
ChoicesType = Iterable[Union[StringableType, Tuple[Any, str]]]


class ChoiceRaw(wx.Choice):
    """
    An extension for wx.Choice that enables handling for more than just strings.
    The normal wx.Choice class only allows the storage of string objects.
    This became an issue when more complex data needed to be displayed in a choice.
    This class can be created from an iterable of any object and the result of str(obj) will be displayed to the user.
    It can also be given a iterable of tuples containing the object and a string to show to the user.
    """

    def __init__(
        self,
        parent: wx.Window,
        *,
        choices: ChoicesType = (),
        default: Any = None,
        sort=True,
        reverse=False
    ):
        super().__init__(parent)
        self._values: List[Any] = []  # the data hidden behind the string
        self._keys: List[str] = []  # the strings shown to the user
        self._sorted = sort
        self._reverse = reverse
        if choices:
            self.SetItems(choices)
            self.SetObject(default)

    @property
    def keys(self) -> Tuple[str, ...]:
        """Get the string values displayed to the user"""
        return tuple(self._keys)

    @property
    def values(self) -> Tuple[Any, ...]:
        """Get the data hidden behind the string value"""
        return tuple(self._values)

    @property
    def items(self) -> Tuple[Tuple[str, Any], ...]:
        """Get the string value and the data hidden behind the value"""
        return tuple(zip(self._keys, self._values))

    def _set_items(self, items: Iterable[Tuple[Any, str]], default: Any = None):
        if items:
            if self._sorted:
                items = sorted(items, key=lambda x: x[1], reverse=self._reverse)
            self._values, self._keys = zip(*items)
            super().SetItems(self._keys)
            if default in self._values:
                self.SetSelection(self._values.index(default))
            else:
                self.SetSelection(0)

    def SetItems(
        self,
        items: Union[
            Iterable[Tuple[Any, str]],
            Iterable[StringableType],
            Dict[StringableType, Any],
        ],
        default: StringableType = None,
    ):
        """
        Set items. Does not have to be strings.
        Can be an iterable of any object and the result of str(obj) will be displayed to the user.
        If the object is a tuple
        It can also be given a iterable of tuples containing the object and a string to show to the user.


        If items is a dictionary the string of the values are show to the user and the key is returned from GetCurrentObject
        If it is just an iterable the string of the values are shown and the raw equivalent input is returned."""
        if isinstance(items, dict):
            items = tuple(items.items())
        else:
            items_ = []
            for item in items:
                if (
                    isinstance(item, (tuple, list))
                    and len(item) == 2
                    and isinstance(item[1], str)
                ):
                    item = (item[0], str(item[1]))
                else:
                    item = (item, str(item))
                items_.append(item)
            items = items_
        self._set_items(items, default)

    def SetObject(self, obj: Any):
        """Set the selected item from the data hidden behind the text."""
        if obj in self._values:
            self.SetSelection(self._values.index(obj))
        elif self.GetCurrentSelection() == wx.NOT_FOUND and self._values:
            self.SetSelection(0)

    def SetValue(self, key: Any):
        """Set the selected item based on the text in the choice."""
        if key in self._keys:
            self.SetSelection(self._keys.index(key))
        elif self.GetCurrentSelection() == wx.NOT_FOUND and self._values:
            self.SetSelection(0)

    def GetCurrentObject(self) -> Optional[Any]:
        """Return the value currently selected in the form before it was converted to a string"""
        if self._values:
            return self._values[self.GetSelection()]

    def GetCurrentString(self) -> str:
        """Get the string form of the value currently selected."""
        return self.GetString(self.GetSelection())


SimpleChoiceAny = ChoiceRaw


class SimpleDialog(wx.Dialog):
    """A dialog with ok and cancel buttons set up."""

    def __init__(self, parent: wx.Window, title, sizer_dir=wx.VERTICAL):
        wx.Dialog.__init__(
            self, parent, title=title, style=wx.CAPTION | wx.RESIZE_BORDER
        )
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self.sizer = wx.BoxSizer(sizer_dir)
        sizer.Add(self.sizer, 1, wx.EXPAND)
        self.bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.bottom_sizer, 0, wx.EXPAND)
        self.bottom_sizer.AddStretchSpacer()
        button_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        self.bottom_sizer.Add(button_sizer, flag=wx.ALL, border=5)
