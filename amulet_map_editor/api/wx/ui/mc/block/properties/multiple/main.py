import wx
from typing import Tuple, Dict, Any, List

import PyMCTranslate
import amulet_nbt
from amulet.api.block import PropertyTypeMultiple
from amulet_map_editor.api.wx.ui.mc.base import WildcardMCBlock
from ..base import BasePropertySelect

from .automatic import AutomaticMultipleProperty
from .manual import ManualMultipleProperty
from .events import MultiplePropertiesChangeEvent, EVT_MULTIPLE_PROPERTIES_CHANGE


class MultiplePropertySelect(BasePropertySelect, WildcardMCBlock):
    """
    This is a UI which lets the user pick zero or more values for each property.
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
        namespace: str,
        base_name: str,
        selected_properties: PropertyTypeMultiple = None,
        all_properties: PropertyTypeMultiple = None,
        state: Dict[str, Any] = None,
    ):
        state = state or {}
        state.setdefault("selected_properties", selected_properties or {})
        state.setdefault("all_properties", all_properties)
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
        self._simple = AutomaticMultipleProperty(self)
        self._sizer.Add(self._simple, 1, wx.EXPAND)
        self._manual = ManualMultipleProperty(self)
        self._sizer.Add(self._manual, 1, wx.EXPAND)
        self._simple.Bind(EVT_MULTIPLE_PROPERTIES_CHANGE, self._on_change)
        self._manual.Bind(EVT_MULTIPLE_PROPERTIES_CHANGE, self._on_change)
        self.push(True)

    def _init_state(self, state: Dict[str, Any]):
        WildcardMCBlock.__init__(self, **state)

    def _on_push(self) -> bool:
        self.Freeze()
        translator = self._translation_manager.get_version(
            self._platform, self._version_number
        ).block

        self._manual_enabled = self.base_name not in translator.base_names(
            self.namespace, self.force_blockstate
        )
        if self._manual_enabled:
            self._simple.Hide()
            self._manual.Show()
            self._manual.all_properties = self.all_properties
            self._manual.selected_properties = self.selected_properties
        else:
            self._manual.Hide()
            self._simple.Show()
            spec = translator.get_specification(
                self.namespace, self.base_name, self._force_blockstate
            )
            properties: Dict[str, List[str]] = spec.get("properties", {})
            self._simple.all_properties = {
                name: [amulet_nbt.from_snbt(p) for p in properties[name]]
                for name in properties
            }
            self._simple.selected_properties = self.selected_properties
        self.Thaw()
        return True

    def _on_change(self, evt: MultiplePropertiesChangeEvent):
        if evt.selected_properties != self.selected_properties:
            self._set_selected_properties(evt.selected_properties)
            wx.PostEvent(
                self,
                MultiplePropertiesChangeEvent(self.selected_properties),
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
                "east": (
                    amulet_nbt.TAG_String("true"),
                    amulet_nbt.TAG_String("false"),
                ),
                "north": (
                    amulet_nbt.TAG_String("true"),
                    amulet_nbt.TAG_String("false"),
                ),
                "south": (amulet_nbt.TAG_String("false"),),
                "west": (amulet_nbt.TAG_String("true"),),
            },
        ),
        (
            "modded",
            "block",
            {
                "test": (
                    amulet_nbt.TAG_String("hello"),
                    amulet_nbt.TAG_String("hello2"),
                ),
            },
        ),
    ):
        dialog = wx.Dialog(
            None,
            title=f"MultiplePropertySelect with block {block[0]}:{block[1]}",
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
        )
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        obj = MultiplePropertySelect(
            dialog, translation_manager, "java", (1, 16, 0), False, *block
        )

        sizer.Add(
            obj,
            1,
            wx.ALL,
            5,
        )

        def on_change(evt: MultiplePropertiesChangeEvent):
            print(evt.selected_properties)

        def get_on_close(dialog_):
            def on_close(evt):
                dialog_.Destroy()

            return on_close

        obj.Bind(EVT_MULTIPLE_PROPERTIES_CHANGE, on_change)
        dialog.Bind(wx.EVT_CLOSE, get_on_close(dialog))
        dialog.Show()
        dialog.Fit()
