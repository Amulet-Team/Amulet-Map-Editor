from typing import Tuple, List
from amulet_map_editor import lang
from .base import BaseBlockContainer
from .block_entry import FillBlockEntry


class FillBlockContainer(BaseBlockContainer):
    _blocks: List[FillBlockEntry]

    @property
    def name(self) -> str:
        return lang.get("program_3d_edit.fill_tool.fill")

    def _add_block(self):
        super()._add_block()
        if len(self._blocks) == 2:
            for block in self._blocks:
                block.show_weight()
        elif len(self._blocks) >= 2:
            self._blocks[-1].show_weight()
        self.GetTopLevelParent().Layout()

    def _create_block(self) -> FillBlockEntry:
        return FillBlockEntry(
            self, self._translation_manager, *self._version
        )

    def _destroy_block_entry(self, window: FillBlockEntry):
        super()._destroy_block_entry(window)
        if len(self._blocks) == 1:
            block = self._blocks[-1]
            block.show_weight(False)
            self.GetTopLevelParent().Layout()

    @property
    def weights(self) -> Tuple[float, ...]:
        """The weighting values for the blocks contained in this widget. May be unused."""
        return tuple(entry.weight for entry in self._blocks)
