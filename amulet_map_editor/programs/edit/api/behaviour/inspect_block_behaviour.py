from typing import TYPE_CHECKING
import wx
from wx.adv import RichToolTip
from amulet_map_editor import log

from .base_behaviour import BaseBehaviour
from .pointer_behaviour import PointerBehaviour
from ..events import (
    InputPressEvent,
    EVT_INPUT_PRESS,
)
from ..key_config import (
    ACT_INSPECT_BLOCK,
)

if TYPE_CHECKING:
    from ..canvas import EditCanvas


class InspectBlockBehaviour(BaseBehaviour):
    """Adds a popup with block information."""

    def __init__(self, canvas: "EditCanvas", pointer_behaviour: PointerBehaviour):
        super().__init__(canvas)
        self._pointer_behaviour = pointer_behaviour

    def bind_events(self):
        """Set up all events required to run."""
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)

    def _on_input_press(self, evt: InputPressEvent):
        """Logic to run each time the input press event is run."""
        if evt.action_id == ACT_INSPECT_BLOCK:
            self._inspect_block()
        evt.Skip()

    def _inspect_block(self):
        def truncate(s: str, max_line_length: int = None) -> str:
            if isinstance(max_line_length, int):
                max_line_length = max(-1, max_line_length)
                s = "\n".join(
                    [
                        line[: max_line_length - 3] + "..."
                        if len(line) > max_line_length
                        else line
                        for line in s.split("\n")
                    ]
                )
            return s

        full_msg = self._get_block_info_message()
        msg = truncate(full_msg, 150)
        tooltip = RichToolTip("Inspect Block", msg)
        x, y = self.canvas.mouse.xy
        tooltip.ShowFor(self.canvas, wx.Rect(x, y, 1, 1))

    def _get_block_info_message(self) -> str:
        x, y, z = self._pointer_behaviour.pointer_base
        try:
            block = self.canvas.world.get_block(x, y, z, self.canvas.dimension)
            chunk = self.canvas.world.get_chunk(x >> 4, z >> 4, self.canvas.dimension)
            block_entity = chunk.block_entities.get((x, y, z), None)
            platform = self.canvas.world.level_wrapper.platform
            version = self.canvas.world.level_wrapper.version
            translator = self.canvas.world.translation_manager.get_version(
                platform,
                version,
            )
            (version_block, version_block_entity, _,) = translator.block.from_universal(
                block, block_entity, block_location=(x, y, z)
            )
            if isinstance(version, tuple):
                version_str = ".".join(str(v) for v in version[:4])
            else:
                version_str = str(version)
            block_data_text = f"x: {x}, y: {y}, z: {z}\n\n{platform.capitalize()} {version_str}\n{version_block}"
            if version_block_entity:
                version_block_entity_str = str(version_block_entity)
                block_data_text = f"{block_data_text}\n{version_block_entity_str}"

            block_data_text = f"{block_data_text}\n\nUniversal\n{block}"
            if block_entity:
                block_entity_str = str(block_entity)
                block_data_text = f"{block_data_text}\n{block_entity_str}"

            if chunk.biomes.dimension == 2:
                biome = chunk.biomes[x % 16, z % 16]
                try:
                    block_data_text = f"{block_data_text}\n\nBiome: {self.canvas.world.biome_palette[biome]}"
                except Exception as e:
                    log.error(e)
            elif chunk.biomes.dimension == 3:
                biome = chunk.biomes[(x % 16) // 4, y // 4, (z % 16) // 4]
                try:
                    block_data_text = f"{block_data_text}\n\nBiome: {self.canvas.world.biome_palette[biome]}"
                except Exception as e:
                    log.error(e)

        except Exception as e:
            log.error(e)
            return str(e)
        else:
            return block_data_text
