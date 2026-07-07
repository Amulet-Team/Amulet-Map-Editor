"""Fast raw-format scanning of Bedrock (LevelDB) worlds for the overview map.

Reads Data3D heightmaps and sub-chunk block storages directly from the world
database, skipping the universal translation layer, so the per-chunk cost is
one small db read plus numpy decoding. Block colours are resolved through the
normal translation pipeline once per unique block state and memoised.

Format summary (1.18+ chunks, verified against a real 1.26 world):
- Data3D record (tag 0x2b): first 512 bytes are a 256 x uint16 little-endian
  heightmap indexed [z * 16 + x]; each value is the top block's y + 1
  relative to the dimension bottom. 3D biome data follows (unused here).
- Sub-chunk record (tag 0x2f + int8 y): [version(8|9)][storage count]
  [y index (v9 only)] then per storage: a header byte (bits_per_block << 1),
  bit-packed uint32 little-endian index words (indices packed low to high,
  block index = x << 8 | z << 4 | y), an int32 palette count and palette
  entries as little-endian uncompressed NBT {name, states, version}.
  Storage layer 0 is the block layer; layer 1 (if present) is waterlogging.
- Keys are <ii (cx, cz) plus the tag byte, with an int32 dimension index
  inserted before the tag for the nether (1) and the end (2).

Any chunk that fails to parse falls back to the slow scan path, so this
module can never make the overview less correct - only faster.
"""

import logging
import struct
from typing import List, Optional, Tuple

import numpy
import amulet_nbt

log = logging.getLogger(__name__)

TAG_DATA3D = 0x2B
TAG_SUBCHUNK = 0x2F

_SUPPORTED_SUBCHUNK_VERSIONS = (8, 9)
_MAX_BITS_PER_BLOCK = 16


class FastScanDecodeError(Exception):
    """A chunk record does not match the expected Bedrock format."""


def chunk_key(
    cx: int, cz: int, dimension_index: int, tag: int, sub_y: Optional[int] = None
) -> bytes:
    """Build a LevelDB key for a chunk record.

    :param dimension_index: 0 overworld (omitted), 1 nether, 2 end.
    """
    key = struct.pack("<ii", cx, cz)
    if dimension_index:
        key += struct.pack("<i", dimension_index)
    key += bytes([tag])
    if sub_y is not None:
        key += struct.pack("<b", sub_y)
    return key


def block_position_index(x: int, ly: int, z: int) -> int:
    """The index of a block position within a sub-chunk storage (XZY order)."""
    return x << 8 | z << 4 | ly


def decode_storage(
    value: bytes, offset: int
) -> Tuple[numpy.ndarray, List[amulet_nbt.NamedTag], int]:
    """Decode one block storage.

    :return: (indices (4096,) uint32, palette NamedTags, offset after storage)
    """
    try:
        header = value[offset]
        offset += 1
        bits_per_block = header >> 1
        if bits_per_block == 0:
            indices = numpy.zeros(4096, numpy.uint32)
        elif bits_per_block <= _MAX_BITS_PER_BLOCK:
            blocks_per_word = 32 // bits_per_block
            word_count = -(-4096 // blocks_per_word)
            words = numpy.frombuffer(value, "<u4", word_count, offset)
            offset += word_count * 4
            shifts = numpy.arange(blocks_per_word, dtype=numpy.uint32) * bits_per_block
            mask = numpy.uint32((1 << bits_per_block) - 1)
            indices = (
                ((words[:, None] >> shifts[None, :]) & mask)
                .ravel()[:4096]
                .astype(numpy.uint32)
            )
        else:
            raise FastScanDecodeError(f"bits per block {bits_per_block} > 16")
        (palette_count,) = struct.unpack_from("<I", value, offset)
        offset += 4
        if palette_count > 4096:
            raise FastScanDecodeError(f"palette count {palette_count} > 4096")
        palette = []
        for _ in range(palette_count):
            try:
                read_context = amulet_nbt.ReadContext()
                tag = amulet_nbt.load(
                    value[offset:],
                    compressed=False,
                    little_endian=True,
                    read_context=read_context,
                )
            except Exception as e:
                # any palette parse failure must route to the slow-path fallback
                raise FastScanDecodeError(f"palette NBT parse failed: {e}")
            palette.append(tag)
            offset += read_context.offset
        return indices, palette, offset
    except FastScanDecodeError:
        raise
    except (IndexError, ValueError, struct.error) as e:
        raise FastScanDecodeError(str(e))


def decode_subchunk_layer0(
    value: bytes,
) -> Tuple[numpy.ndarray, List[amulet_nbt.NamedTag]]:
    """Decode layer 0 (the block layer) of a version 8/9 sub-chunk record."""
    try:
        version = value[0]
        if version not in _SUPPORTED_SUBCHUNK_VERSIONS:
            raise FastScanDecodeError(f"unsupported sub-chunk version {version}")
        num_storages = value[1]
        if num_storages < 1:
            raise FastScanDecodeError("sub-chunk has no block storages")
        offset = 3 if version == 9 else 2  # v9 has a y-index byte
        indices, palette, _ = decode_storage(value, offset)
        return indices, palette
    except FastScanDecodeError:
        raise
    except IndexError as e:
        raise FastScanDecodeError(str(e))


def decode_heightmap(data3d: bytes, bottom: int) -> numpy.ndarray:
    """Decode the Data3D heightmap to absolute top-block heights.

    The stored heightmap is 256 uint16 LE indexed [z*16 + x]; each value is
    the top block's y + 1 relative to the dimension bottom.

    :return: (16, 16) int32 indexed (x, z) of each column's top-block y.
    """
    if len(data3d) < 512:
        raise FastScanDecodeError(f"Data3D record too short ({len(data3d)} bytes)")
    stored = numpy.frombuffer(data3d, "<u2", 256, 0).reshape(16, 16)  # [z][x]
    return stored.T.astype(numpy.int32) - 1 + bottom


from amulet.api.block import Block
from amulet.level.formats.leveldb_world import LevelDBFormat

from amulet_map_editor.api.opengl.resource_pack.resource_pack import model_lock

_AIR_NAMES = frozenset(("minecraft:air", "minecraft:cave_air", "minecraft:void_air"))
_TRANSPARENT = numpy.zeros(4, numpy.uint8)
_TRANSPARENT.setflags(write=False)
_MAGENTA = numpy.array((255, 0, 255, 255), numpy.uint8)
_MAGENTA.setflags(write=False)

_DIMENSION_INDICES = {
    "minecraft:overworld": 0,
    "minecraft:the_nether": 1,
    "minecraft:the_end": 2,
}


class BedrockColourCache:
    """Memoised bedrock block name/states -> map colour.

    The expensive translation happens once per unique block state in the
    world (hundreds) instead of once per chunk (hundreds of thousands).
    """

    def __init__(self, resource_pack):
        self._resource_pack = resource_pack
        self._cache = {}

    def get(self, name: str, states) -> numpy.ndarray:
        states_key = states.to_snbt() if states is not None else ""
        key = (name, states_key)
        colour = self._cache.get(key)
        if colour is None:
            if name in _AIR_NAMES:
                colour = _TRANSPARENT
            else:
                try:
                    namespace, _, base_name = name.partition(":")
                    if not base_name:
                        namespace, base_name = "minecraft", name
                    properties = dict(states) if states is not None else {}
                    block = Block(namespace, base_name, properties)
                    with model_lock:
                        universal, _, _ = (
                            self._resource_pack.translator.block.to_universal(block)
                        )
                        colour = self._resource_pack.get_block_top_colour(universal)
                except Exception:
                    log.debug(
                        f"Could not resolve colour for {name}{states_key}",
                        exc_info=True,
                    )
                    colour = _MAGENTA
            self._cache[key] = colour
        return colour


class BedrockFastScan:
    """Reads chunk top-colours straight from a Bedrock world's LevelDB."""

    def __init__(self, db, dimension_index: int, bottom: int, colours):
        self._db = db
        self._dimension_index = dimension_index
        self._bottom = bottom
        self._colours = colours

    @classmethod
    def create(cls, level, dimension: str, resource_pack):
        """Return a fast scanner for the level/dimension, or None if the
        level is not a Bedrock LevelDB world or the dimension is unknown."""
        try:
            wrapper = level.level_wrapper
        except AttributeError:
            return None
        if not isinstance(wrapper, LevelDBFormat):
            return None
        dimension_index = _DIMENSION_INDICES.get(dimension)
        if dimension_index is None:
            return None
        try:
            db = wrapper.level_db
            bottom = int(level.bounds(dimension).min_y)
        except Exception:
            log.warning("Could not initialise bedrock fast scan", exc_info=True)
            return None
        return cls(db, dimension_index, bottom, BedrockColourCache(resource_pack))

    def _get_subchunk(self, cx: int, cz: int, cy: int, cache: dict):
        """Fetch+decode a sub-chunk's layer 0, memoised per scan_chunk call.
        Returns (indices, palette) or None if the record does not exist."""
        if cy not in cache:
            try:
                value = self._db.get(
                    chunk_key(cx, cz, self._dimension_index, TAG_SUBCHUNK, cy)
                )
            except KeyError:
                cache[cy] = None
            else:
                cache[cy] = decode_subchunk_layer0(value)
        return cache[cy]

    def _block_name_states(self, cx, cz, y, x, z, cache):
        """The (name, states) at an absolute position, or None if the
        sub-chunk record is absent."""
        cy, ly = divmod(y, 16)
        decoded = self._get_subchunk(cx, cz, cy, cache)
        if decoded is None:
            return None
        indices, palette = decoded
        entry = palette[int(indices[block_position_index(x, ly, z)])].compound
        name = str(entry.get("name", ""))
        return name, entry.get("states")

    def scan_chunk(self, cx: int, cz: int):
        """Fast top-colour scan of one chunk.

        :return: (colours (16,16,4) uint8 (x,z), heights (16,16) int32 (x,z))
            or None if this chunk cannot be fast-scanned (fall back).
        """
        try:
            try:
                data3d = self._db.get(
                    chunk_key(cx, cz, self._dimension_index, TAG_DATA3D)
                )
            except KeyError:
                return None
            heights = decode_heightmap(data3d, self._bottom)
            colours = numpy.zeros((16, 16, 4), numpy.uint8)
            subchunk_cache: dict = {}
            for x in range(16):
                for z in range(16):
                    y = int(heights[x, z])
                    top = self._block_name_states(cx, cz, y, x, z, subchunk_cache)
                    if top is None:
                        continue  # missing sub-chunk record: transparent
                    name, states = top
                    # snow-cover rule: decorative blocks (snow layers etc.)
                    # can sit one block above the motion-blocking heightmap
                    above = self._block_name_states(cx, cz, y + 1, x, z, subchunk_cache)
                    if above is not None and above[0] not in _AIR_NAMES:
                        name, states = above
                        heights[x, z] = y + 1
                    colours[x, z] = self._colours.get(name, states)
            return colours, heights
        except FastScanDecodeError:
            log.debug(f"Fast scan fell back for chunk ({cx}, {cz})", exc_info=True)
            return None
        except Exception:
            log.warning(
                f"Unexpected fast-scan error for chunk ({cx}, {cz})", exc_info=True
            )
            return None
