import wx

from .base import BaseBlockEntry
from .custom_fill_button import CustomBlockDefineButton, SrcBlockState


class FillBlockEntry(BaseBlockEntry):
    """A UI element that holds a block button, weight entry and close button"""

    def __init__(
        self,
        parent: wx.Window,
        state: SrcBlockState,
    ):
        super().__init__(parent)
        self._init_close_button()
        self._block_button = CustomBlockDefineButton(
            self,
            state,
            max_char_length=40,
        )
        self._sizer.Add(self._block_button, 1)
        self._weight = wx.SpinCtrl(self, initial=1, min=0, max=100)
        self._sizer.Add(self._weight)
        self.show_weight(False)

    @property
    def block_button(self) -> CustomBlockDefineButton:
        return self._block_button

    @property
    def weight(self) -> float:
        """The weighting value for this entry."""
        return self._weight.GetValue()

    @weight.setter
    def weight(self, weight: float):
        self._weight.SetValue(weight)

    def show_weight(self, show: bool = True):
        """Show or hide the weight entry."""
        self._weight.Show(show)
        self.Layout()

    def show_from_source(self, from_source: bool):
        self._block_button.show_from_source(from_source)
