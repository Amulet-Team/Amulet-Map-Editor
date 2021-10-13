from typing import List
from amulet_map_editor import lang
from .base import BaseBlockContainer
from .block_entry import FindBlockEntry


class FindBlockContainer(BaseBlockContainer):
    _blocks: List[FindBlockEntry]

    @property
    def name(self) -> str:
        return lang.get("program_3d_edit.fill_tool.find")

    def _create_block(self) -> FindBlockEntry:
        return FindBlockEntry(self, self.state)
