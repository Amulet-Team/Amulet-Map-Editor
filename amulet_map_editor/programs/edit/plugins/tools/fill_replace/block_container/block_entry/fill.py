import wx

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple
from amulet.api.block import PropertyType
from .base import BaseBlockEntry
from .custom_fill_button import CustomBlockDefineButton


class FillBlockEntry(BaseBlockEntry):
    """A UI element that holds a block button, weight entry and close button"""

    _button_props = BaseBlockEntry._button_props + ("properties",)

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        properties: PropertyType = None,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)
        self._init_close_button()
        self._block_button = CustomBlockDefineButton(
            self,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
            properties,
            max_char_length=40,
        )
        self._sizer.Add(self._block_button, 1)
        self._weight = wx.SpinCtrlDouble(self, initial=1.0, min=0.0, max=1.0, inc=0.1)
        self._weight.SetDigits(2)
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

    def set_from_source(self, from_source: bool):
        self._block_button.set_from_source(from_source)
