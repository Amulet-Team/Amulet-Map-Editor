import wx
from typing import Tuple, Dict, Any, List

import PyMCTranslate
import amulet_nbt
from amulet.api.block import PropertyType
from ..base import BasePropertySelect
from .events import SinglePropertiesChangeEvent, EVT_SINGLE_PROPERTIES_CHANGE
from .automatic import AutomaticSingleProperty
from .manual import ManualSingleProperty
from amulet_map_editor.api.wx.ui.mc.api import NormalMCBlock


class SinglePropertySelect(BasePropertySelect, NormalMCBlock):
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
        version_number: Tuple[int, ...],
        force_blockstate: bool,
        namespace: str = None,
        base_name: str = None,
        properties: PropertyType = None,
        state: Dict[str, Any] = None,
    ):
        state = state or {}
        state.setdefault("properties", properties)
        BasePropertySelect.__init__(
            self,
            parent,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
            state=state,
        )

        self._manual_enabled = False
        self._simple = AutomaticSingleProperty(self)
        self._sizer.Add(self._simple, 0, wx.EXPAND)
        self._manual = ManualSingleProperty(self)
        self._sizer.Add(self._manual, 0, wx.EXPAND)
        self._simple.Bind(EVT_SINGLE_PROPERTIES_CHANGE, self._on_change)
        self._manual.Bind(EVT_SINGLE_PROPERTIES_CHANGE, self._on_change)
        self.push(True)

    def _init_state(self, state: Dict[str, Any]):
        NormalMCBlock.__init__(self, **state)

    def _on_push(self) -> bool:
        translator = self._translation_manager.get_version(
            self._platform, self._version_number
        ).block

        self._manual_enabled = self.base_name not in translator.base_names(
            self.namespace, self._force_blockstate
        )
        if self._manual_enabled:
            self._simple.Hide()
            self._manual.Show()
            self._manual.properties = self.properties
        else:
            self._manual.Hide()
            self._simple.Show()
            spec = translator.get_specification(
                self.namespace, self.base_name, self._force_blockstate
            )
            properties: Dict[str, List[str]] = spec.get("properties", {})
            defaults = spec.get("defaults", {})
            self._simple.states = {
                name: (
                    [amulet_nbt.from_snbt(p) for p in properties[name]],
                    properties[name].index(defaults[name]),
                )
                for name in properties
            }
            self._simple.properties = self.properties
        return True

    def _on_change(self, evt: SinglePropertiesChangeEvent):
        if evt.properties != self.properties:
            self._set_properties(evt.properties)
            wx.PostEvent(
                self,
                SinglePropertiesChangeEvent(self.properties),
            )


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    for block in (
        (
            "minecraft",
            "oak_fence",
            {
                "east": amulet_nbt.TAG_String("false"),
                "north": amulet_nbt.TAG_String("true"),
                "south": amulet_nbt.TAG_String("false"),
                "west": amulet_nbt.TAG_String("false"),
            },
        ),
        (
            "modded",
            "block",
            {
                "test": amulet_nbt.TAG_String("hello"),
            },
        ),
    ):
        dialog = wx.Dialog(
            None,
            title=f"SinglePropertySelect with block {block[0]}:{block[1]}",
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
        )
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        obj = SinglePropertySelect(
            dialog, translation_manager, "java", (1, 16, 0), False, *block
        )
        sizer.Add(
            obj,
            1,
            wx.ALL,
            5,
        )

        def on_change(evt: SinglePropertiesChangeEvent):
            print(evt.properties)

        obj.Bind(EVT_SINGLE_PROPERTIES_CHANGE, on_change)

        def get_on_close(dialog_):
            def on_close(evt):
                dialog_.Destroy()

            return on_close

        dialog.Bind(wx.EVT_CLOSE, get_on_close(dialog))
        dialog.Show()
        dialog.Fit()
