from typing import List, Iterable, Tuple, Optional
import wx
from wx.lib import newevent

import PyMCTranslate
from amulet.api.block import Block, UniversalAirBlock
from amulet.api.block_entity import BlockEntity
from amulet_map_editor import lang
from .block_dialog import BlockSelectDialog

LeftRightBorder = wx.LEFT | wx.RIGHT
BottomBorder = LeftRightBorder | wx.BOTTOM

BlockCloseEvent, EVT_BLOCK_CLOSE = newevent.NewEvent()

VersionType = Tuple[str, Tuple[int, ...], bool]

BlockStorage = Tuple[Block, Optional[BlockEntity]]


def _check_version(version: VersionType):
    assert isinstance(version, tuple) and len(version) == 3
    assert isinstance(version[0], str)
    assert isinstance(version[1], tuple) and all(isinstance(v, int) for v in version[1])
    assert isinstance(version[2], bool)


class BlockPickButton(wx.Button):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        version: VersionType,
        block: BlockStorage,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)
        self._translation_manager = translation_manager
        self._version = version
        self._block = block
        self._update_button()
        self.Bind(wx.EVT_BUTTON, self._on_press)

    @property
    def version(self) -> VersionType:
        return self._version

    @version.setter
    def version(self, version: VersionType):
        _check_version(version)
        self._version = version
        self._update_button()

    def _on_press(self, evt):
        platform, verison_number, force_blockstate = self._version
        dialog = BlockSelectDialog(
            self,
            self._translation_manager,
            self._block,
            platform,
            verison_number,
            force_blockstate,
        )
        response = dialog.ShowModal()
        if response == wx.ID_OK:
            self.block = dialog.universal_block
        dialog.Destroy()

    def _update_button(self):
        platform, version, force_blockstate = self._version
        block, block_entity = self._block
        block, block_entity, _ = self._translation_manager.get_version(
            platform, version
        ).block.from_universal(block, block_entity, force_blockstate=force_blockstate)
        if not isinstance(block, Block):
            block, block_entity, _ = self._translation_manager.get_version(
                platform, version
            ).block.from_universal(UniversalAirBlock, force_blockstate=force_blockstate)
        self.SetLabel(block.full_blockstate)

    @property
    def block(self) -> BlockStorage:
        """The universal block object stored in this button."""
        return self._block

    @block.setter
    def block(self, block: BlockStorage):
        if not (
            isinstance(block, tuple)
            and len(block) == 2
            and isinstance(block[0], Block)
            and block[1] is None
            or (isinstance(block[1], BlockEntity))
        ):
            raise ValueError(f"block must be a tuple of Block and BlockEntity.")
        self._block = block
        self._update_button()


class BlockEntry(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        version: VersionType,
        block: BlockStorage,
        show_weight=False,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)
        self._block_button = BlockPickButton(self, translation_manager, version, block)
        sizer.Add(self._block_button, 1)
        self._weight = wx.SpinCtrlDouble(self, initial=100.0, min=0.0, max=100.0)
        self._weight.SetDigits(2)
        sizer.Add(self._weight)
        self._close_button = wx.Button(self, label="❌")
        self._close_button.Bind(wx.EVT_BUTTON, self._on_close)
        self._close_button.SetMinSize((28, 28))
        sizer.Add(self._close_button)
        self.show_weight(show_weight)

    @property
    def version(self) -> VersionType:
        return self._block_button.version

    @version.setter
    def version(self, version: VersionType):
        self._block_button.version = version

    def _on_close(self, evt):
        evt2 = BlockCloseEvent()
        evt2.SetEventObject(self)
        wx.PostEvent(self, evt2)

    @property
    def block(self) -> BlockStorage:
        """The universal block contained within this widget."""
        return self._block_button.block

    @block.setter
    def block(self, block: BlockStorage):
        self._block_button.block = block

    @property
    def weight(self) -> float:
        """The weighting value for this entry. May be unused."""
        return self._weight.GetValue()

    @weight.setter
    def weight(self, weight: float):
        self._weight.SetValue(weight)

    def show_weight(self, show: bool = True):
        """Show or hide the weight entry."""
        self._weight.Show(show)
        self.Layout()

    def show_close(self, show: bool = True):
        """Show or hide the close button."""
        self._close_button.Show(show)
        self.Layout()

    def enable_close(self, enable: bool = True):
        self._close_button.Enable(enable)


class BaseBlockContainer(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        version: VersionType,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)
        self._translation_manager = translation_manager
        self._version = version

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(top_sizer, 0, wx.EXPAND, 5)
        find_label = wx.StaticText(
            self, label=self.name, style=wx.ALIGN_CENTER_HORIZONTAL
        )
        top_sizer.Add(find_label, 1, wx.ALIGN_CENTER_VERTICAL)

        self._add_button = wx.Button(self, label="➕")
        self._add_button.Bind(wx.EVT_BUTTON, lambda evt: self._add_block())
        self._add_button.SetMinSize((28, 28))
        top_sizer.Add(self._add_button)

        self._block_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._block_sizer, 0, wx.EXPAND, 0)

        self._blocks: List[BlockEntry] = []
        self._add_block()

    @property
    def version(self) -> VersionType:
        return self._version

    @version.setter
    def version(self, version: VersionType):
        _check_version(version)
        self._version = version
        for block in self._blocks:
            block.version = version

    def _add_block(self):
        block = BlockEntry(
            self, self._translation_manager, self._version, (UniversalAirBlock, None)
        )
        block.Bind(EVT_BLOCK_CLOSE, self._remove_block)
        self._block_sizer.Add(block, 0, wx.EXPAND | wx.TOP, 5)
        self._blocks.append(block)
        if len(self._blocks) == 1:
            self._blocks[-1].enable_close(False)
        if len(self._blocks) == 2:
            for block in self._blocks:
                block.enable_close()
        elif len(self._blocks) >= 2:
            self._blocks[-1].enable_close()
        self.GetTopLevelParent().Layout()

    def _remove_block(self, evt):
        window = evt.GetEventObject()
        if isinstance(window, BlockEntry):
            self._destroy_window(window)

    def _destroy_window(self, window: BlockEntry):
        if window in self._blocks:
            self._blocks.remove(window)
            window.Destroy()
            if len(self._blocks) == 1:
                block = self._blocks[-1]
                block.enable_close(False)
                block.show_weight(False)
            self.GetTopLevelParent().Layout()

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def blocks(self) -> Tuple[BlockStorage, ...]:
        """The universal blocks contained within this widget."""
        return tuple(entry.block for entry in self._blocks)

    @blocks.setter
    def blocks(self, blocks: Iterable[BlockStorage]):
        blocks = tuple(blocks)
        while len(self._blocks) > len(blocks):
            self._destroy_window(self._blocks[-1])
        while len(self._blocks) < len(blocks):
            self._add_block()
        for block, window in zip(blocks, self._blocks):
            window.block = block


class FindWidget(BaseBlockContainer):
    @property
    def name(self) -> str:
        return lang.get("program_3d_edit.fill_tool.find")


class FillWidget(BaseBlockContainer):
    def _add_block(self):
        super()._add_block()
        if len(self._blocks) == 2:
            for block in self._blocks:
                block.show_weight()
        elif len(self._blocks) >= 2:
            self._blocks[-1].show_weight()
        self.GetTopLevelParent().Layout()

    @property
    def name(self) -> str:
        return lang.get("program_3d_edit.fill_tool.fill")

    @property
    def weights(self) -> Tuple[float]:
        """The weighting values for the blocks contained in this widget. May be unused."""
        return tuple(entry.weight for entry in self._blocks)


class ReplaceOperationWidget(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        version: VersionType,
        **kwargs,
    ):
        kwargs["style"] = kwargs.get("style", 0) | wx.BORDER_SIMPLE
        super().__init__(parent, **kwargs)
        self._replace = False

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self._find = FindWidget(self, translation_manager, version)
        self._find.Hide()
        sizer.Add(self._find, 0, wx.EXPAND | wx.ALL, 5)

        self._swap_button = wx.Button(
            self, wx.ID_ANY, lang.get("program_3d_edit.fill_tool.swap")
        )
        self._swap_button.Bind(wx.EVT_BUTTON, self._swap_blocks)
        self._swap_button.Hide()
        sizer.Add(self._swap_button, 0, wx.EXPAND | wx.ALL, 5)

        self._fill = FillWidget(self, translation_manager, version)
        sizer.Add(self._fill, 0, wx.EXPAND | wx.ALL, 5)

        self.Layout()

    @property
    def version(self) -> VersionType:
        return self._fill.version

    @version.setter
    def version(self, version: VersionType):
        self._find.version = version
        self._fill.version = version

    def _swap_blocks(self, evt):
        self.Freeze()
        self._find.blocks, self._fill.blocks = self._fill.blocks, self._find.blocks
        self.GetTopLevelParent().Layout()
        self.Thaw()

    def replace(self, replace: bool):
        self._find.Show(replace)
        self._swap_button.Show(replace)
