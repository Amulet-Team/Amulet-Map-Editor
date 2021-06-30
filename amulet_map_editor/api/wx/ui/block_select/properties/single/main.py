import wx
from typing import Tuple

import PyMCTranslate
from amulet.api.block import PropertyType
from ..base_property import BasePropertySelect
from ..events import PropertiesChangeEvent
from .automatic import AutomaticSingleProperty
from .manual import ManualSingleProperty


class SinglePropertySelect(BasePropertySelect):
    """
    This is a UI which lets the user pick one value for each property for a given block.
    If the block is known it will be populated from the specification.
    If it is not known the user can populate it themselves.
    """

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str,
        version_number: Tuple[int, int, int],
        force_blockstate: bool,
        namespace: str,
        block_name: str,
        properties: PropertyType = None,
    ):
        super().__init__(
            parent,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            block_name,
            style=wx.BORDER_SIMPLE,
        )

        self._manual_enabled = False
        self._simple = AutomaticSingleProperty(self, translation_manager)
        self._sizer.Add(self._simple, 1, wx.EXPAND)
        self._manual = ManualSingleProperty(self, translation_manager)
        self._sizer.Add(self._manual, 1, wx.EXPAND)

        if properties is None:
            properties = {}
        self._set_properties(properties)
        self._rebuild_ui()

    @property
    def properties(self) -> PropertyType:
        """
        The selected values for each property.

        :return: A dictionary mapping property name to the nbt value.
        """
        return self._get_properties()

    @properties.setter
    def properties(self, properties: PropertyType):
        self._set_properties(properties)
        wx.PostEvent(self, PropertiesChangeEvent())

    def _get_properties(self) -> PropertyType:
        """Get the selected values for each property."""
        if self._manual_enabled:
            return self._manual.properties
        else:
            return self._simple.properties

    def _set_properties(self, properties: PropertyType):
        """Set the selected values for each property."""
        self.Freeze()
        if self._manual_enabled:
            self._manual.properties = properties
        else:
            self._simple.properties = properties
        self.TopLevelParent.Layout()
        self.Thaw()

    def _rebuild_ui(self):
        self.Freeze()
        translator = self._translation_manager.get_version(
            self._platform, self._version_number
        ).block

        self._manual_enabled = self._block_name not in translator.base_names(
            self._namespace, self._force_blockstate
        )
        if self._manual_enabled:
            self._simple.Hide()
            self._manual.Show()
        else:
            self._manual.Hide()
            self._simple.Show()
            self._simple.rebuild_ui(
                translator.get_specification(
                    self._namespace, self._block_name, self._force_blockstate
                )
            )
        self.Thaw()


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    for block in (("minecraft", "oak_fence"), ("modded", "block")):
        dialog = wx.Dialog(
            None,
            title=f"SinglePropertySelect with block {block[0]}:{block[1]}",
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
        )
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(
            SinglePropertySelect(
                dialog, translation_manager, "java", (1, 16, 0), False, *block
            ),
            1,
            wx.ALL,
            5,
        )

        def get_on_close(dialog_):
            def on_close(evt):
                dialog_.Destroy()

            return on_close

        dialog.Bind(wx.EVT_CLOSE, get_on_close(dialog))
        dialog.Show()
        dialog.Fit()
