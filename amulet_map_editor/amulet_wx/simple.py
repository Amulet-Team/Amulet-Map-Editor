import wx
from wx.lib.scrolledpanel import ScrolledPanel
from typing import Iterable, Union, Any, List


class SimpleSizer:
    def __init__(self, sizer_dir=wx.VERTICAL):
        self.sizer = wx.BoxSizer(sizer_dir)

    def add_object(self, obj, space=1, options=wx.ALL):
        self.sizer.Add(
            obj,
            space,
            options,
            5
        )


class SimplePanel(wx.Panel, SimpleSizer):
    def __init__(self, parent, sizer_dir=wx.VERTICAL):
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
    def __init__(self, parent, sizer_dir=wx.VERTICAL):
        ScrolledPanel.__init__(
            self,
            parent,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        SimpleSizer.__init__(self, sizer_dir)
        self.SetSizer(self.sizer)
        self.SetupScrolling()
        self.SetAutoLayout(1)


class SimpleText(wx.StaticText):
    def __init__(self, parent, text):
        super().__init__(
            parent,
            wx.ID_ANY,
            text,
            wx.DefaultPosition,
            wx.DefaultSize,
            0
        )


class SimpleChoice(wx.Choice):
    def __init__(self, parent, choices=()):
        super().__init__(
            parent,
            choices=choices
        )
        if choices:
            self.SetSelection(0)

    def GetCurrentString(self) -> str:
        return self.GetString(self.GetSelection())


class SimpleChoiceAny(wx.Choice):
    def __init__(self, parent, sort=True):
        super().__init__(
            parent
        )
        self._values: List[Any] = []
        self._keys: List[str] = []
        self._sorted = sort

    @property
    def values(self) -> List[Any]:
        return self._values

    def SetItems(self, items: Union[Iterable, dict]):
        """Set items. Does not have to be strings.
        If items is a dictionary the string of the values are show to the user and the key is returned from GetAny
        If it is just an iterable the string of the values are shown and the raw equivalent input is returned."""
        if not items:
            return
        if isinstance(items, dict):
            items = [[str(value), key] for key, value in items.items()]
            if self._sorted:
                items = sorted(items, key=lambda x: x[0])
            self._keys = [key for key, _ in items]
            self._values = [value for _, value in items]
        else:
            if self._sorted:
                self._values = list(sorted(items))
            else:
                self._values = list(items)
            self._keys = [str(v) for v in self._values]
        super().SetItems(self._keys)
        self.SetSelection(0)

    def SetValue(self, value: Any):
        if value in self._keys:
            self.SetSelection(self._keys.index(value))

    def GetAny(self):
        """Return the value currently selected in the form before it was converted to a string"""
        return self._values[self.GetSelection()]


class SimpleDialog(wx.Dialog, SimpleSizer):
    def __init__(self, parent, title, sizer_dir=wx.VERTICAL):
        wx.Dialog.__init__(
            self,
            parent,
            title=title,
            style=wx.CAPTION | wx.RESIZE_BORDER
        )
        SimpleSizer.__init__(self)
        self.SetSizer(self.sizer)
        self.custom_panel = SimplePanel(self, sizer_dir)
        self.add_object(self.custom_panel, 0)
        button_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        self.add_object(button_sizer, 0)
