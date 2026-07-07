from unittest.mock import MagicMock

import numpy
import pytest
from amulet.api.errors import ChunkDoesNotExist, ChunkLoadError

from amulet_map_editor.programs.edit.api.overview.scanner import OverviewScanner
from amulet_map_editor.programs.edit.api.overview.scan import ERROR_COLOURS


def _make_chunk(palette_len=2):
    chunk = MagicMock()
    sub = numpy.ones((16, 16, 16), numpy.uint32)  # all palette index 1
    chunk.blocks.sub_chunks = [0]
    chunk.blocks.get_sub_chunk = lambda cy: sub
    chunk.block_palette = [MagicMock(name=f"block{i}") for i in range(palette_len)]
    return chunk


@pytest.fixture
def scanner(tmp_path, monkeypatch):
    monkeypatch.setenv("CACHE_DIR", str(tmp_path))
    level = MagicMock()
    level.level_path = "test_world"
    level.all_chunk_coords = lambda dimension: {(0, 0), (1, 0)}
    level.get_chunk = lambda cx, cz, dimension: _make_chunk()
    resource_pack = MagicMock()
    # index 0 = air (transparent), index 1 = grey stone
    colours = [
        numpy.zeros(4, numpy.uint8),
        numpy.array((128, 128, 128, 255), numpy.uint8),
    ]
    resource_pack.get_block_top_colour = lambda block: colours[
        int(block._mock_name[5:])
    ]
    return OverviewScanner(level, "overworld", resource_pack)


def test_scans_all_chunks_and_reports_progress(scanner):
    assert scanner.progress() == 0.0
    assert scanner.scan_next() is True
    assert scanner.scan_next() is True
    assert scanner.scan_next() is False  # queue drained
    assert scanner.progress() == 1.0


def test_scanned_pixels_land_in_the_right_patch(scanner):
    while scanner.scan_next():
        pass
    pixels = scanner.tile_pixels(0, 0)
    assert pixels is not None
    # chunk (0,0) occupies pixels [0:16, 0:16] (z rows, x cols); all stone
    assert (pixels[0:16, 0:16] == (128, 128, 128, 255)).all()
    # chunk (1,0) occupies x pixels 16:32
    assert (pixels[0:16, 16:32, 3] == 255).all()
    # unscanned area stays transparent
    assert (pixels[100:116, 100:116, 3] == 0).all()


def test_dirty_tiles_drained_once(scanner):
    while scanner.scan_next():
        pass
    dirty = scanner.take_dirty_tiles()
    assert [(t[0], t[1]) for t in dirty] == [(0, 0)]
    assert scanner.take_dirty_tiles() == []


def test_chunk_does_not_exist_is_transparent_and_complete(tmp_path, monkeypatch):
    monkeypatch.setenv("CACHE_DIR", str(tmp_path))
    level = MagicMock()
    level.level_path = "w"
    level.all_chunk_coords = lambda dimension: {(0, 0)}

    def raise_missing(cx, cz, dimension):
        raise ChunkDoesNotExist()

    level.get_chunk = raise_missing
    scanner = OverviewScanner(level, "overworld", MagicMock())
    assert scanner.scan_next() is True
    assert scanner.progress() == 1.0
    assert (scanner.tile_pixels(0, 0)[0:16, 0:16, 3] == 0).all()


def test_chunk_load_error_shows_error_patch(tmp_path, monkeypatch):
    monkeypatch.setenv("CACHE_DIR", str(tmp_path))
    level = MagicMock()
    level.level_path = "w"
    level.all_chunk_coords = lambda dimension: {(2, 3)}

    def raise_error(cx, cz, dimension):
        raise ChunkLoadError()

    level.get_chunk = raise_error
    scanner = OverviewScanner(level, "overworld", MagicMock())
    scanner.scan_next()
    pixels = scanner.tile_pixels(0, 0)
    # chunk (2,3): x pixels 32:48, z pixels 48:64; colours indexed (z, x)
    patch = pixels[48:64, 32:48]
    assert (patch == ERROR_COLOURS.transpose(1, 0, 2)).all()


def test_mark_chunk_changed_rescans(scanner):
    while scanner.scan_next():
        pass
    scanner.mark_chunk_changed((0, 0))
    assert scanner.scan_next() is True
    assert scanner.scan_next() is False


def test_flush_and_reload_from_cache(scanner, tmp_path, monkeypatch):
    while scanner.scan_next():
        pass
    scanner.flush()
    # a new scanner for the same world sees the cached tiles as complete
    level = MagicMock()
    level.level_path = "test_world"
    level.all_chunk_coords = lambda dimension: {(0, 0), (1, 0)}
    scanner2 = OverviewScanner(level, "overworld", MagicMock())
    assert scanner2.progress() == 1.0
    assert scanner2.scan_next() is False
    assert (scanner2.tile_pixels(0, 0)[0:16, 0:16, 3] == 255).all()


def test_stale_patch_dropped_after_dimension_switch(scanner):
    import numpy

    # capture the generation a worker would have seen before the switch
    with scanner._lock:
        stale_generation = scanner._generation
    stale_patch = numpy.full((16, 16, 4), 77, numpy.uint8)

    scanner.set_dimension("nether")

    scanner._write_patch((0, 0), stale_patch, stale_generation)
    pixels = scanner.tile_pixels(0, 0)
    # the stale write must have been dropped: either no tile exists yet or
    # the patch area is untouched (not 77)
    assert pixels is None or not (pixels[0:16, 0:16] == 77).any()


def test_current_generation_patch_is_written(scanner):
    import numpy

    with scanner._lock:
        generation = scanner._generation
    patch = numpy.full((16, 16, 4), 77, numpy.uint8)
    scanner._write_patch((0, 0), patch, generation)
    pixels = scanner.tile_pixels(0, 0)
    assert pixels is not None
    assert (pixels[0:16, 0:16] == 77).all()


def test_completed_tile_saved_without_flush(tmp_path, monkeypatch):
    import numpy
    from unittest.mock import MagicMock

    monkeypatch.setenv("CACHE_DIR", str(tmp_path))
    from amulet_map_editor.programs.edit.api.overview.scanner import OverviewScanner
    from amulet_map_editor.programs.edit.api.overview.cache import OverviewTileCache

    level = MagicMock()
    level.level_path = "eager_save_world"
    # a full tile: chunks (0..31, 0..31) all exist as empty (ChunkDoesNotExist)
    from amulet.api.errors import ChunkDoesNotExist

    coords = {(x, z) for x in range(32) for z in range(32)}
    level.all_chunk_coords = lambda dimension: coords

    def raise_missing(cx, cz, dimension):
        raise ChunkDoesNotExist()

    level.get_chunk = raise_missing
    scanner = OverviewScanner(level, "overworld", MagicMock())
    while scanner.scan_next():
        pass
    # tile fully scanned -> must be on disk WITHOUT calling flush()
    cache = OverviewTileCache("eager_save_world", "overworld")
    assert cache.load_tile(0, 0) is not None


def test_camera_chunk_applied_by_worker_not_caller(scanner):
    scanner.set_camera_chunk(1, 0)
    # nothing touched the queue yet; the first scan_next applies the pending
    # camera and therefore scans the nearest chunk (1, 0) first
    assert scanner.scan_next() is True
    pixels = scanner.tile_pixels(0, 0)
    assert (pixels[0:16, 16:32, 3] == 255).all()  # chunk (1,0) patch scanned
    assert (pixels[0:16, 0:16, 3] == 0).all()  # chunk (0,0) not yet


def test_load_items_use_fast_path_when_available(scanner):
    import numpy
    from amulet_map_editor.api.opengl.mesh.level.load_queue import ChunkLoadQueue

    fast = MagicMock()
    fast_colours = numpy.full((16, 16, 4), (1, 2, 3, 255), numpy.uint8)
    fast_heights = numpy.full((16, 16), 70, numpy.int32)
    fast.scan_chunk = MagicMock(return_value=(fast_colours, fast_heights))
    scanner._fast_scan = fast

    assert scanner.scan_next() is True
    assert fast.scan_chunk.call_count == 1
    # fast result landed in the tile (flat heights -> shade is neutral)
    pixels = scanner.tile_pixels(0, 0)
    scanned = pixels[..., 3] == 255
    assert scanned.any()
    assert (pixels[scanned][:, :3] == (1, 2, 3)).all()


def test_fast_path_none_falls_back_to_slow(scanner):
    fast = MagicMock()
    fast.scan_chunk = MagicMock(return_value=None)
    scanner._fast_scan = fast

    assert scanner.scan_next() is True  # slow path produced the patch
    assert fast.scan_chunk.call_count == 1
    pixels = scanner.tile_pixels(0, 0)
    assert (pixels[..., 3] == 255).any()  # slow path stone from _make_chunk


def test_urgent_items_never_use_fast_path(scanner):
    fast = MagicMock()
    fast.scan_chunk = MagicMock(return_value=None)
    scanner._fast_scan = fast
    # drain the initial LOAD queue via slow path
    while scanner.scan_next():
        pass
    fast.scan_chunk.reset_mock()

    scanner.mark_chunk_changed((0, 0))  # PRIORITY_URGENT
    assert scanner.scan_next() is True
    fast.scan_chunk.assert_not_called()


def test_eager_save_is_debounced(scanner, monkeypatch):
    import types

    # Drain the initial scan so tile (0,0) already holds its scanned chunks.
    while scanner.scan_next():
        pass

    # Treat a tile with any complete chunk as "complete" so the eager-save path
    # fires without needing a full 1024-chunk tile.
    monkeypatch.setattr(scanner, "_tile_target_count", lambda tile_coords: 1)
    save_mock = MagicMock()
    monkeypatch.setattr(scanner._cache, "save_tile", save_mock)

    # Drive the clock the scanner reads (without touching the real time module).
    clock = [1000.0]
    monkeypatch.setattr(
        "amulet_map_editor.programs.edit.api.overview.scanner.time",
        types.SimpleNamespace(time=lambda: clock[0]),
    )

    # First completion after patching: eager save fires.
    scanner.mark_chunk_changed((0, 0))
    assert scanner.scan_next() is True
    assert save_mock.call_count == 1

    # Second completion within the 5s window: debounced, no extra save, and the
    # tile is left unsaved for a later wave/flush to pick up.
    scanner.mark_chunk_changed((0, 0))
    assert scanner.scan_next() is True
    assert save_mock.call_count == 1

    # flush() ignores the debounce and saves the still-unsaved tile.
    scanner.flush()
    assert save_mock.call_count == 2

    # After the debounce window elapses, eager save fires again.
    clock[0] += 6.0
    scanner.mark_chunk_changed((0, 0))
    assert scanner.scan_next() is True
    assert save_mock.call_count == 3
