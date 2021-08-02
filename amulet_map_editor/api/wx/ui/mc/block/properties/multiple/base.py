import wx

from amulet.api.block import PropertyTypeMultiple


class BaseMultipleProperty(wx.Panel):
    def __init__(self, parent: wx.Window):
        super().__init__(parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

    @property
    def all_properties(self) -> PropertyTypeMultiple:
        """
        All the states defined for every property.
        This contains all values regardless of if they are selected or not.
        """
        raise NotImplementedError

    @all_properties.setter
    def all_properties(self, all_properties: PropertyTypeMultiple):
        raise NotImplementedError

    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        """
        The values that are checked for each property.
        This UI can have more than one property value checked (ticked).
        """
        raise NotImplementedError

    @selected_properties.setter
    def selected_properties(self, selected_properties: PropertyTypeMultiple):
        raise NotImplementedError
