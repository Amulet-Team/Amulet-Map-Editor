"""Java 26.3+ chunk block palette compatibility for amulet-core 1.9.

From 26.3 Snapshot 7 (DataVersion 5009) Minecraft stores block states as:
- a compact StringTag block id when using the default state
- a compound with ``id`` / ``properties`` instead of ``Name`` / ``Properties``
"""

from __future__ import annotations

from typing import Iterable

from amulet.api.block import Block
from amulet.level.interfaces.chunk.anvil.anvil_1444 import Anvil1444Interface
from amulet.level.interfaces.chunk.anvil.anvil_3463 import Anvil3463Interface
from amulet.level.loader import Interfaces
from amulet_nbt import CompoundTag, ListTag, StringTag

# 26.3 Snapshot 7
_JAVA_BLOCK_STATE_ID_VERSION = 5009
_APPLIED = False
_INTERFACE_KEY = "amulet_map_editor.compat.anvil_5009"


def _split_namespaced_name(namespaced: str) -> tuple[str, str]:
    if ":" in namespaced:
        namespace, base_name = namespaced.split(":", 1)
        return namespace, base_name
    return "minecraft", namespaced


def _decode_block_palette(palette: ListTag) -> list:
    blockstates = []
    for entry in palette:
        if isinstance(entry, StringTag):
            namespace, base_name = _split_namespaced_name(entry.py_str)
            properties = {}
        else:
            name_tag = entry.get("id")
            if name_tag is None:
                name_tag = entry.get("Name")
            if not isinstance(name_tag, StringTag):
                raise ValueError(f"Block palette entry has no id/Name: {entry}")
            namespace, base_name = _split_namespaced_name(name_tag.py_str)
            props_tag = entry.get("properties")
            if props_tag is None:
                props_tag = entry.get("Properties", CompoundTag({}))
            properties = props_tag.py_dict if isinstance(props_tag, CompoundTag) else {}
        blockstates.append(
            Block(namespace=namespace, base_name=base_name, properties=properties)
        )
    return blockstates


def _encode_block_palette_26_3(blockstates: Iterable[Block]) -> ListTag:
    palette = ListTag()
    for block in blockstates:
        entry = CompoundTag()
        entry["id"] = StringTag(f"{block.namespace}:{block.base_name}")
        if block.properties:
            string_properties = {
                key: value
                for key, value in block.properties.items()
                if isinstance(value, StringTag)
            }
            if string_properties:
                entry["properties"] = CompoundTag(string_properties)
        palette.append(entry)
    return palette


class Anvil5009Interface(Anvil3463Interface):
    @staticmethod
    def minor_is_valid(key: int):
        return key >= _JAVA_BLOCK_STATE_ID_VERSION

    @staticmethod
    def _encode_block_palette(blockstates: Iterable[Block]) -> ListTag:
        return _encode_block_palette_26_3(blockstates)


def apply_java_26_3_block_palette_compat() -> None:
    global _APPLIED
    if _APPLIED:
        return

    Anvil1444Interface._decode_block_palette = staticmethod(_decode_block_palette)
    Anvil3463Interface.minor_is_valid = staticmethod(
        lambda key: 3454 <= key < _JAVA_BLOCK_STATE_ID_VERSION
    )
    Interfaces._objects[_INTERFACE_KEY] = Anvil5009Interface()
    _APPLIED = True
