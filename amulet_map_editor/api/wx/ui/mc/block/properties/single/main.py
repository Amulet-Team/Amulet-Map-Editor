import wx

import PyMCTranslate
import amulet_nbt
from amulet.api.data_types import VersionNumberTuple
from amulet.api.block import PropertyType
from ..base import BasePropertySelect
from .events import SinglePropertiesChangeEvent, EVT_SINGLE_PROPERTIES_CHANGE
from .vanilla import VanillaSingleProperty
from .modded import ModdedSingleProperty
from amulet_map_editor.api.wx.ui.mc.state import State, BlockState


class SinglePropertySelect(BasePropertySelect):
    """
    This is a UI which lets the user pick one value for each property for a given block.
    If the block is known it will be populated from the specification.
    If it is not known the user can populate it themselves.
    """

    state: BlockState

    _vanilla: VanillaSingleProperty
    _modded: ModdedSingleProperty

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        state: BlockState = None,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        properties: PropertyType = None,
    ):
        if not isinstance(state, BlockState):
            state = BlockState(
                translation_manager,
                platform=platform,
                version_number=version_number,
                force_blockstate=force_blockstate,
                namespace=namespace,
                base_name=base_name,
                properties=properties,
            )
        super().__init__(parent, translation_manager, state=state)

        self._vanilla = self._create_automatic()
        self._sizer.Add(self._vanilla, 1, wx.EXPAND)
        self._modded = self._create_manual()
        self._sizer.Add(self._modded, 1, wx.EXPAND)

    def _create_automatic(self) -> VanillaSingleProperty:
        return VanillaSingleProperty(self, self.state)

    def _create_manual(self) -> ModdedSingleProperty:
        return ModdedSingleProperty(self, self.state)

    def _on_state_change(self):
        if self.state.is_changed(State.BaseName):
            vanilla = self.state.base_name in self.state.valid_base_names
            self._vanilla.Show(vanilla)
            self._modded.Show(not vanilla)


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    for block in (
        {
            "namespace": "minecraft",
            "base_name": "oak_fence",
            "properties": {
                "east": amulet_nbt.TAG_String("false"),
                "north": amulet_nbt.TAG_String("true"),
                "south": amulet_nbt.TAG_String("false"),
                "west": amulet_nbt.TAG_String("false"),
            },
        },
        {
            "namespace": "modded",
            "base_name": "block",
            "properties": {
                "test": amulet_nbt.TAG_String("hello"),
            },
        },
    ):
        dialog = wx.Dialog(
            None,
            title=f"SinglePropertySelect with block {block['namespace']}:{block['base_name']}",
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
        )
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        obj = SinglePropertySelect(
            dialog,
            translation_manager,
            platform="java",
            version_number=(1, 16, 0),
            force_blockstate=False,
            **block,
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
