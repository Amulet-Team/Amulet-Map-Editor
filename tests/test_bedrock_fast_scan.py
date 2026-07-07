import struct

import numpy
import pytest
from amulet_nbt import CompoundTag, IntTag, NamedTag, StringTag

from amulet_map_editor.programs.edit.api.overview.bedrock_fast_scan import (
    TAG_DATA3D,
    TAG_SUBCHUNK,
    FastScanDecodeError,
    block_position_index,
    chunk_key,
    decode_heightmap,
    decode_storage,
    decode_subchunk_layer0,
)


def palette_entry(name: str) -> bytes:
    tag = NamedTag(
        CompoundTag(
            {
                "name": StringTag(name),
                "states": CompoundTag({}),
                "version": IntTag(18168865),
            }
        )
    )
    return tag.save_to(compressed=False, little_endian=True)


def build_storage(indices, names, bits_per_block):
    """Encode a block storage from a (4096,) index array — spec-faithful encoder."""
    out = bytearray([bits_per_block << 1])
    if bits_per_block:
        blocks_per_word = 32 // bits_per_block
        word_count = -(-4096 // blocks_per_word)
        words = numpy.zeros(word_count, numpy.uint32)
        for i, idx in enumerate(indices):
            word, slot = divmod(i, blocks_per_word)
            words[word] |= numpy.uint32(idx) << numpy.uint32(slot * bits_per_block)
        out += words.astype("<u4").tobytes()
    out += struct.pack("<I", len(names))
    for name in names:
        out += palette_entry(name)
    return bytes(out)


def build_subchunk(indices, names, bits_per_block, version=9, y_index=0):
    header = bytes([version, 1]) + (struct.pack("<b", y_index) if version == 9 else b"")
    return header + build_storage(indices, names, bits_per_block)


def test_chunk_key_overworld():
    assert chunk_key(1, -2, 0, TAG_DATA3D) == struct.pack("<ii", 1, -2) + b"\x2b"
    assert chunk_key(1, -2, 0, TAG_SUBCHUNK, -4) == struct.pack(
        "<ii", 1, -2
    ) + b"\x2f" + struct.pack("<b", -4)


def test_chunk_key_other_dimension():
    assert chunk_key(3, 4, 1, TAG_DATA3D) == struct.pack("<iii", 3, 4, 1) + b"\x2b"


def test_block_position_index():
    assert block_position_index(0, 0, 0) == 0
    assert block_position_index(1, 0, 0) == 256
    assert block_position_index(0, 1, 0) == 1
    assert block_position_index(0, 0, 1) == 16
    assert block_position_index(15, 15, 15) == 4095


@pytest.mark.parametrize("bits", [1, 2, 3, 4, 5, 6, 8, 16])
def test_storage_round_trip(bits):
    rng = numpy.random.default_rng(bits)
    palette_size = min(1 << bits, 40)
    indices = rng.integers(0, palette_size, 4096, dtype=numpy.uint32)
    names = [f"minecraft:block_{i}" for i in range(palette_size)]
    raw = build_storage(indices, names, bits)
    decoded, palette, end = decode_storage(raw, 0)
    assert (decoded == indices).all()
    assert [str(t.compound["name"]) for t in palette] == names
    assert end == len(raw)


def test_storage_zero_bits_is_all_index_zero():
    raw = build_storage(numpy.zeros(4096, numpy.uint32), ["minecraft:air"], 0)
    decoded, palette, end = decode_storage(raw, 0)
    assert (decoded == 0).all()
    assert len(palette) == 1
    assert end == len(raw)


@pytest.mark.parametrize("version", [8, 9])
def test_subchunk_layer0(version):
    indices = numpy.zeros(4096, numpy.uint32)
    indices[block_position_index(5, 10, 7)] = 1
    raw = build_subchunk(indices, ["minecraft:air", "minecraft:stone"], 2, version)
    decoded, palette = decode_subchunk_layer0(raw)
    assert decoded[block_position_index(5, 10, 7)] == 1
    assert str(palette[1].compound["name"]) == "minecraft:stone"


def test_subchunk_unknown_version_raises():
    raw = build_subchunk(numpy.zeros(4096, numpy.uint32), ["minecraft:air"], 1, 9)
    with pytest.raises(FastScanDecodeError):
        decode_subchunk_layer0(b"\x07" + raw[1:])


def test_decode_heightmap_transpose_and_bottom():
    # stored order is [z][x]; value = top y + 1 relative to bottom
    hm = numpy.zeros((16, 16), numpy.uint16)  # [z][x]
    hm[3, 5] = 132  # column x=5, z=3
    data3d = hm.astype("<u2").tobytes() + b"\x00" * 100  # trailing biome data
    heights = decode_heightmap(data3d, bottom=-64)
    assert heights.shape == (16, 16)
    assert heights.dtype == numpy.int32
    assert heights[5, 3] == 132 - 1 - 64  # (x, z) indexed, absolute top y = 67
    assert heights[3, 5] == 0 - 1 - 64  # untouched column


def test_decode_heightmap_too_short_raises():
    with pytest.raises(FastScanDecodeError):
        decode_heightmap(b"\x00" * 100, bottom=-64)


def test_decode_storage_is_warning_free(recwarn):
    import warnings

    indices = numpy.zeros(4096, numpy.uint32)
    raw = build_storage(indices, ["minecraft:air"], 1)
    with warnings.catch_warnings():
        warnings.simplefilter("error", FutureWarning)
        decode_storage(raw, 0)


def test_decode_storage_corrupt_palette_nbt_raises_decode_error():
    indices = numpy.zeros(4096, numpy.uint32)
    raw = build_storage(indices, ["minecraft:air"], 1)
    # truncate mid-palette: keep header+words+count but cut the NBT short
    truncated = raw[: len(raw) - 5]
    with pytest.raises(FastScanDecodeError):
        decode_storage(truncated, 0)


import os
from unittest.mock import MagicMock

from amulet_map_editor.programs.edit.api.overview.bedrock_fast_scan import (
    BedrockColourCache,
    BedrockFastScan,
)

GRASS = numpy.array((60, 180, 60, 255), numpy.uint8)
SNOW = numpy.array((250, 250, 250, 255), numpy.uint8)


def _resource_pack():
    rp = MagicMock()
    universal_grass = MagicMock(name="universal_grass")
    universal_snow = MagicMock(name="universal_snow")

    def to_universal(block, *args, **kwargs):
        mapping = {
            "grass_block": universal_grass,
            "snow_layer": universal_snow,
        }
        return mapping[block.base_name], None, False

    rp.translator.block.to_universal = to_universal
    colours = {id(universal_grass): GRASS, id(universal_snow): SNOW}
    rp.get_block_top_colour = lambda block: colours[id(block)]
    return rp


def test_colour_cache_air_is_transparent_without_translation():
    rp = _resource_pack()
    cache = BedrockColourCache(rp)
    colour = cache.get("minecraft:air", None)
    assert tuple(colour) == (0, 0, 0, 0)


def test_colour_cache_memoises_by_name_and_states():
    rp = _resource_pack()
    cache = BedrockColourCache(rp)
    a = cache.get("minecraft:grass_block", CompoundTag({}))
    b = cache.get("minecraft:grass_block", CompoundTag({}))
    assert (a == GRASS).all()
    assert a is b  # memoised


def test_colour_cache_translation_failure_is_magenta():
    rp = _resource_pack()
    cache = BedrockColourCache(rp)
    colour = cache.get("modded:mystery_block", CompoundTag({}))
    assert tuple(colour) == (255, 0, 255, 255)


class _FakeWrapper:
    """Stands in for LevelDBFormat: exposes .level_db."""

    def __init__(self, db):
        self.level_db = db


def _make_world(tmp_path):
    """Build a real temporary LevelDB with one synthetic chunk at (0, 0):
    flat grass at y=67 (heightmap value 132 relative to bottom -64), with a
    snow_layer on top of column (2, 2)."""
    from leveldb import LevelDB

    db = LevelDB(str(tmp_path / "db"), create_if_missing=True)
    hm = numpy.full((16, 16), 132, numpy.uint16)  # [z][x]
    hm[2, 2] = 133  # snow layer on column x=2, z=2 -> its top is the snow at 68
    db.put(chunk_key(0, 0, 0, TAG_DATA3D), hm.astype("<u2").tobytes() + b"\x00" * 64)
    # sub-chunk cy=4 holds y 64..79 -> local y 3 = 67, local y 4 = 68
    indices = numpy.zeros(4096, numpy.uint32)
    for x in range(16):
        for z in range(16):
            indices[block_position_index(x, 3, z)] = 1  # grass everywhere at y=67
    indices[block_position_index(2, 4, 2)] = 2  # snow layer at y=68 on (2,2)
    raw = build_subchunk(
        indices,
        ["minecraft:air", "minecraft:grass_block", "minecraft:snow_layer"],
        2,
        version=9,
        y_index=4,
    )
    db.put(chunk_key(0, 0, 0, TAG_SUBCHUNK, 4), raw)
    return db


def _make_level(db):
    level = MagicMock()
    level.level_wrapper = _FakeWrapper(db)
    bounds = MagicMock()
    bounds.min_y = -64
    level.bounds = lambda dimension: bounds
    return level


def test_scan_chunk_end_to_end(tmp_path, monkeypatch):
    # make create() accept the fake wrapper
    import amulet_map_editor.programs.edit.api.overview.bedrock_fast_scan as bfs

    monkeypatch.setattr(bfs, "LevelDBFormat", _FakeWrapper)
    db = _make_world(tmp_path)
    level = _make_level(db)
    scan = BedrockFastScan.create(level, "minecraft:overworld", _resource_pack())
    assert scan is not None
    result = scan.scan_chunk(0, 0)
    assert result is not None
    colours, heights = result
    assert heights[0, 0] == 67
    assert (colours[0, 0] == GRASS).all()
    # snow-cover rule: heightmap points at the snow layer itself here (133),
    # column (2,2) resolves to the snow block
    assert heights[2, 2] == 68
    assert (colours[2, 2] == SNOW).all()
    db.close()


def test_scan_chunk_missing_data3d_returns_none(tmp_path, monkeypatch):
    import amulet_map_editor.programs.edit.api.overview.bedrock_fast_scan as bfs

    monkeypatch.setattr(bfs, "LevelDBFormat", _FakeWrapper)
    db = _make_world(tmp_path)
    level = _make_level(db)
    scan = BedrockFastScan.create(level, "minecraft:overworld", _resource_pack())
    assert scan.scan_chunk(99, 99) is None
    db.close()


def test_scan_chunk_corrupt_subchunk_returns_none(tmp_path, monkeypatch):
    import amulet_map_editor.programs.edit.api.overview.bedrock_fast_scan as bfs

    monkeypatch.setattr(bfs, "LevelDBFormat", _FakeWrapper)
    db = _make_world(tmp_path)
    db.put(chunk_key(0, 0, 0, TAG_SUBCHUNK, 4), b"\x07garbage")
    level = _make_level(db)
    scan = BedrockFastScan.create(level, "minecraft:overworld", _resource_pack())
    assert scan.scan_chunk(0, 0) is None
    db.close()


def test_create_returns_none_for_non_bedrock():
    level = MagicMock()
    level.level_wrapper = object()  # not a LevelDBFormat
    assert BedrockFastScan.create(level, "minecraft:overworld", MagicMock()) is None


def test_create_returns_none_for_unknown_dimension(tmp_path, monkeypatch):
    import amulet_map_editor.programs.edit.api.overview.bedrock_fast_scan as bfs

    monkeypatch.setattr(bfs, "LevelDBFormat", _FakeWrapper)
    db = _make_world(tmp_path)
    level = _make_level(db)
    assert BedrockFastScan.create(level, "some:custom_dim", MagicMock()) is None
    db.close()
