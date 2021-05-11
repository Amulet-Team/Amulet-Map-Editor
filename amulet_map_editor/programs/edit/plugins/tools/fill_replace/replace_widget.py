from typing import List, Iterable, Tuple
import wx
from wx.lib import newevent

from amulet.api.block import Block, UniversalAirBlock

LeftRightBorder = wx.LEFT | wx.RIGHT
BottomBorder = LeftRightBorder | wx.BOTTOM

BlockCloseEvent, EVT_BLOCK_CLOSE = newevent.NewEvent()


class BlockPickButton(wx.Button):
    def __init__(self, parent: wx.Window, block: Block, **kwargs):
        super().__init__(parent, label=block.full_blockstate, **kwargs)
        self._block = block

    @property
    def block(self) -> Block:
        return self._block

    @block.setter
    def block(self, block: Block):
        if not isinstance(block, Block):
            raise ValueError(f"block must be a Block instance.")
        self._block = block
        self.SetLabel(block.full_blockstate)


class BlockEntry(wx.Panel):
    def __init__(self, parent: wx.Window, block: Block, show_weight=False, **kwargs):
        super().__init__(parent, **kwargs)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)
        self._block_button = BlockPickButton(self, block)
        sizer.Add(self._block_button, 1)
        self._weight = wx.SpinCtrlDouble(self, initial=100.0, min=0.0, max=100.0)
        self._weight.SetDigits(2)
        sizer.Add(self._weight)
        self._close_button = wx.Button(self, label="❌")
        self._close_button.Bind(wx.EVT_BUTTON, self._on_close)
        self._close_button.SetMinSize((28, 28))
        sizer.Add(self._close_button)
        self.show_weight(show_weight)

    def _on_close(self, evt):
        evt2 = BlockCloseEvent()
        evt2.SetEventObject(self)
        wx.PostEvent(self, evt2)

    @property
    def block(self) -> Block:
        """The universal block contained within this widget."""
        return self._block_button.block

    @block.setter
    def block(self, block: Block):
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
    def __init__(self, parent: wx.Window, **kwargs):
        super().__init__(parent, **kwargs)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(top_sizer, 0, wx.EXPAND | wx.ALL, 5)
        find_label = wx.StaticText(self, label=self.name, style=wx.ALIGN_CENTER_HORIZONTAL)
        top_sizer.Add(find_label, 1, wx.ALIGN_CENTER_VERTICAL)

        self._add_button = wx.Button(self, label="➕")
        self._add_button.Bind(wx.EVT_BUTTON, lambda evt: self._add_block())
        self._add_button.SetMinSize((28, 28))
        top_sizer.Add(self._add_button)

        self._block_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._block_sizer, 0, wx.EXPAND, 0)

        self._blocks: List[BlockEntry] = []
        self._add_block()

    def _add_block(self):
        block = BlockEntry(self, UniversalAirBlock)
        block.Bind(EVT_BLOCK_CLOSE, self._remove_block)
        self._block_sizer.Add(block, 0, wx.EXPAND | BottomBorder, 5)
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
    def blocks(self) -> Tuple[Block]:
        """The universal blocks contained within this widget."""
        return tuple(entry.block for entry in self._blocks)

    @blocks.setter
    def blocks(self, blocks: Iterable[Block]):
        blocks = tuple(blocks)
        while len(self._blocks) > len(blocks):
            window = self._blocks.pop()
            window.Destroy()
        while len(self._blocks) < len(blocks):
            self._add_block()
        for block, window in zip(blocks, self._blocks):
            window.block = block


class FindWidget(BaseBlockContainer):
    @property
    def name(self) -> str:
        return "Find"


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
        return "Fill"

    @property
    def weights(self) -> Tuple[float]:
        """The weighting values for the blocks contained in this widget. May be unused."""
        return tuple(entry.weight for entry in self._blocks)


class ReplaceOperationWidget(wx.Panel):
    def __init__(self, parent: wx.Window, **kwargs):
        kwargs["style"] = kwargs.get("style", 0) | wx.BORDER_SIMPLE
        super().__init__(parent, **kwargs)
        self._replace = False

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self._find = FindWidget(self)
        self._find.Hide()
        sizer.Add(self._find, 0, wx.EXPAND, 0)

        self._swap_button = wx.Button(self, wx.ID_ANY, u"▲ Swap ▼")
        self._swap_button.Bind(wx.EVT_BUTTON, self._swap_blocks)
        self._swap_button.Hide()
        sizer.Add(self._swap_button, 0, wx.EXPAND | BottomBorder, 5)

        self._fill = FillWidget(self)
        sizer.Add(self._fill, 0, wx.EXPAND, 0)

        self.Layout()

    def _swap_blocks(self, evt):
        self.Freeze()
        self._find.blocks, self._fill.blocks = self._fill.blocks, self._find.blocks
        self.GetTopLevelParent().Layout()
        self.Thaw()

    def replace(self, replace: bool):
        self._find.Show(replace)
        self._swap_button.Show(replace)


if __name__ == "__main__":

    def main():
        app = wx.App()
        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(
            ReplaceOperationWidget(dialog),
            1,
            wx.ALL | wx.EXPAND,
            5,
        )
        dialog.Show()
        dialog.Fit()
        dialog.Bind(wx.EVT_CLOSE, lambda evt: dialog.Destroy())
        app.MainLoop()

    main()
