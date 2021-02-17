"""A collection of classes for wx objects to abstract away
the repeated code and make working with wx a bit more simple."""

import wx
from wx.lib.scrolledpanel import ScrolledPanel
from typing import Iterable, Union, Any, List, Optional, Sequence, Dict, Tuple

from amulet_map_editor import log


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


class SimpleChoiceAny(wx.Choice):
    """An extension for wx.Choice that enables showing and returning objects that are not strings."""

    def __init__(self, parent: wx.Window, sort=True, reverse=False):
        super().__init__(parent)
        self._values: List[Any] = []  # the data hidden behind the string
        self._keys: List[str] = []  # the strings shown to the user
        self._sorted = sort
        self._reverse = reverse

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

    def SetItems(
        self,
        items: Union[Iterable[StringableType], Dict[StringableType, Any]],
        default: StringableType = None,
    ):
        """Set items. Does not have to be strings.
        If items is a dictionary the string of the values are show to the user and the key is returned from GetAny
        If it is just an iterable the string of the values are shown and the raw equivalent input is returned."""
        if not items:
            return
        if isinstance(items, dict):
            items: List[Tuple[str, Any]] = [
                (str(value), key) for key, value in items.items()
            ]
            if self._sorted:
                items = sorted(items, key=lambda x: x[0], reverse=self._reverse)
            self._keys = [key.strip() for key, _ in items]
            self._values = [value for _, value in items]
        else:
            if self._sorted:
                self._values = list(sorted(items))
                if self._reverse:
                    self._values.reverse()
            else:
                self._values = list(items)
            self._keys = [str(v).strip() for v in self._values]
        super().SetItems(self._keys)
        if default is not None and default in self._values:
            self.SetSelection(self._values.index(default))
        else:
            self.SetSelection(0)

    def SetValue(self, value: Any):
        if value in self._keys:
            self.SetSelection(self._keys.index(value))

    def GetAny(self) -> Optional[Any]:
        """Return the value currently selected in the form before it was converted to a string"""
        log.warning(
            "SimpleChoiceAny.GetAny is being depreciated and will be removed in the future. Please use SimpleChoiceAny.GetCurrentObject instead",
            exc_info=True,
        )
        return self.GetCurrentObject()

    def GetCurrentObject(self) -> Optional[Any]:
        """Return the value currently selected in the form before it was converted to a string"""
        if self._values:
            return self._values[self.GetSelection()]

    def GetCurrentString(self) -> str:
        """Get the string form of the value currently selected."""
        return self.GetString(self.GetSelection())


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
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(bottom_sizer, 0, wx.EXPAND)
        bottom_sizer.AddStretchSpacer()
        button_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        bottom_sizer.Add(button_sizer, flag=wx.ALL, border=5)
