import wx
from wx.lib.scrolledpanel import ScrolledPanel
from typing import Iterable, Union


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


class SimpleNotebook(wx.Notebook):
    def __init__(self, parent, style=0):
        wx.Notebook.__init__(
            self,
            parent,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            style
        )


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


class SimpleChoiceAny(wx.Choice):
    def __init__(self, parent, sort=True):
        super().__init__(
            parent
        )
        self._items = ()
        self._sorted = sort

    def SetItems(self, items: Union[Iterable, dict]):
        """Set items. Does not have to be strings.
        If items is a dictionary the string of the values are show to the user and the key is returned from GetAny
        If it is just an iterable the string of the values are shown and the raw equivalent input is returned."""
        if not items:
            return
        if isinstance(items, dict):
            items = [[key, str(value)] for key, value in items.items()]
            if self._sorted:
                items = sorted(items, key=lambda x: x[1])
            self._items = [key for key, _ in items]
            super().SetItems([value for _, value in items])
        else:
            if self._sorted:
                self._items = tuple(sorted(items))
            else:
                self._items = tuple(items)
            super().SetItems([str(v) for v in self._items])
        self.SetSelection(0)

    def GetAny(self):
        """Return the value currently selected in the form before it was converted to a string"""
        return self._items[self.GetSelection()]


class SimpleDialog(wx.Dialog):
    def __init__(self, parent, title):
        wx.Dialog.__init__(
            self,
            parent,
            title=title,
            style=wx.CAPTION
        )
        sizer = SimpleSizer()
        self.SetSizer(sizer)
        self.custom_panel = SimplePanel(sizer)
        sizer.add_object(self.custom_panel)
        button_panel = SimplePanel(sizer, wx.HORIZONTAL)
        sizer.add_object(button_panel)

        ok_button = wx.Button(self, label='Ok')
        close_button = wx.Button(self, label='Close')
        button_panel.add_object(ok_button)
        button_panel.add_object(close_button)

        ok_button.Bind(wx.EVT_BUTTON, self._okay_event)
        close_button.Bind(wx.EVT_BUTTON, self._cancel_event)

    def _okay_event(self, evt):
        self.EndModal(wx.OK)
        evt.Skip()

    def _cancel_event(self, evt):
        self.EndModal(wx.CANCEL)
        evt.Skip()
