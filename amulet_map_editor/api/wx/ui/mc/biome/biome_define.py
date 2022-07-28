import PyMCTranslate
import wx

from amulet.api.data_types import VersionNumberTuple, PlatformType
from amulet_map_editor.api.wx.ui.mc.base.base_define import BaseDefine
from amulet_map_editor.api.wx.ui.mc.biome.identifier_select.biome_identifier_select import (
    BiomeIdentifierSelect,
)
from amulet_map_editor.api.wx.ui.mc.biome.identifier_select.events import (
    EVT_BIOME_ID_CHANGE,
)
from amulet_map_editor.api.wx.ui.mc.state import BiomeResourceIDState

_BiomeChangeEventType = wx.NewEventType()
EVT_BIOME_CHANGE = wx.PyEventBinder(_BiomeChangeEventType)


class BiomeChangeEvent(wx.PyEvent):
    def __init__(
        self,
        platform: PlatformType,
        version_number: VersionNumberTuple,
        force_blockstate: bool,
        namespace: str,
        base_name: str,
    ):
        wx.PyEvent.__init__(self, eventType=_BiomeChangeEventType)
        self._platform = platform
        self._version_number = version_number
        self._force_blockstate = force_blockstate
        self._namespace = namespace
        self._base_name = base_name

    @property
    def platform(self) -> PlatformType:
        return self._platform

    @property
    def version_number(self) -> VersionNumberTuple:
        return self._version_number

    @property
    def force_blockstate(self) -> bool:
        return self._force_blockstate

    @property
    def namespace(self) -> str:
        return self._namespace

    @property
    def base_name(self) -> str:
        return self._base_name


class BiomeDefine(BaseDefine):
    """
    A UI that merges a version select widget with a biome select widget.
    """

    state: BiomeResourceIDState
    _identifier_select: BiomeIdentifierSelect

    def __init__(
        self,
        parent,
        state: BiomeResourceIDState,
        *,
        show_pick_biome: bool = False,
        orientation=wx.VERTICAL,
    ):
        assert isinstance(state, BiomeResourceIDState)
        super().__init__(
            parent,
            state,
            orientation=orientation,
        )
        self._identifier_select = BiomeIdentifierSelect(
            self,
            state,
            show_pick=show_pick_biome,
        )
        self._identifier_select.Bind(EVT_BIOME_ID_CHANGE, self._post_change)
        self._top_sizer.Add(self._identifier_select, 1, wx.EXPAND | wx.TOP, 5)

    @classmethod
    def from_data(
        cls,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        show_pick_biome: bool = False,
        orientation=wx.VERTICAL,
        **kwargs,
    ):
        return cls(
            parent,
            BiomeResourceIDState(translation_manager, **kwargs),
            show_pick_biome=show_pick_biome,
            orientation=orientation,
        )

    def _post_change(self, evt):
        wx.PostEvent(
            self,
            BiomeChangeEvent(
                self.state.platform,
                self.state.version_number,
                self.state.force_blockstate,
                self.state.namespace,
                self.state.base_name,
            ),
        )


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(
        None,
        title="BiomeDefine",
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    obj = BiomeDefine.from_data(dialog, translation_manager, orientation=wx.HORIZONTAL)

    def on_biome_change(evt: BiomeChangeEvent):
        print(
            evt.platform,
            evt.version_number,
            evt.force_blockstate,
            evt.namespace,
            evt.base_name,
        )

    obj.Bind(EVT_BIOME_CHANGE, on_biome_change)

    sizer.Add(
        obj,
        1,
        wx.ALL | wx.EXPAND,
        5,
    )
    dialog.Show()
    dialog.Fit()
    dialog.Bind(wx.EVT_CLOSE, lambda evt: dialog.Destroy())

    def set_data(
        platform: PlatformType,
        version: VersionNumberTuple,
        force_blockstate: bool,
        namespace: str,
        base_name: str,
    ):
        with obj.state as state:
            state.platform = platform
            state.version_number = version
            state.force_blockstate = force_blockstate
            state.namespace = namespace
            state.base_name = base_name

    interval = 1_000
    wx.CallLater(
        interval * 1, set_data, "java", (1, 17, 0), False, "minecraft", "end_highlands"
    )
    wx.CallLater(
        interval * 2,
        set_data,
        "bedrock",
        (1, 17, 0),
        False,
        "minecraft",
        "birch_forest_hills_mutated",
    )
    wx.CallLater(
        interval * 3, set_data, "java", (1, 17, 0), False, "minecraft", "random"
    )
    wx.CallLater(
        interval * 4, set_data, "bedrock", (1, 17, 0), False, "minecraft", "random"
    )


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
