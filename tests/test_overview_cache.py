import os

import numpy
import pytest

from amulet_map_editor.programs.edit.api.overview.cache import (
    TILE_PIXELS,
    OverviewTileCache,
    tile_of_chunk,
)


@pytest.fixture
def cache(tmp_path, monkeypatch):
    monkeypatch.setenv("CACHE_DIR", str(tmp_path))
    return OverviewTileCache(r"C:\worlds\my test world", "minecraft:overworld")


def test_tile_of_chunk():
    assert tile_of_chunk(0, 0) == (0, 0)
    assert tile_of_chunk(31, 31) == (0, 0)
    assert tile_of_chunk(32, 0) == (1, 0)
    assert tile_of_chunk(-1, -33) == (-1, -2)


def test_round_trip(cache):
    pixels = numpy.random.default_rng(0).integers(
        0, 255, (TILE_PIXELS, TILE_PIXELS, 4), dtype=numpy.uint8
    )
    complete = {(0, 0), (5, 7), (-3, 12)}
    cache.save_tile(0, 0, pixels, complete)
    loaded = cache.load_tile(0, 0)
    assert loaded is not None
    loaded_pixels, loaded_complete = loaded
    assert (loaded_pixels == pixels).all()
    assert loaded_complete == complete


def test_missing_tile_returns_none(cache):
    assert cache.load_tile(9, 9) is None


def test_corrupt_tile_returns_none(cache):
    pixels = numpy.zeros((TILE_PIXELS, TILE_PIXELS, 4), numpy.uint8)
    cache.save_tile(1, 1, pixels, set())
    # corrupt the png
    png_path = cache._tile_png_path(1, 1)
    with open(png_path, "wb") as f:
        f.write(b"not a png")
    assert cache.load_tile(1, 1) is None


def test_list_and_clear(cache):
    pixels = numpy.zeros((TILE_PIXELS, TILE_PIXELS, 4), numpy.uint8)
    cache.save_tile(0, 0, pixels, set())
    cache.save_tile(-2, 3, pixels, set())
    assert set(cache.list_tiles()) == {(0, 0), (-2, 3)}
    cache.clear()
    assert cache.list_tiles() == []
    assert cache.load_tile(0, 0) is None


def test_dimensions_are_isolated(tmp_path, monkeypatch):
    monkeypatch.setenv("CACHE_DIR", str(tmp_path))
    overworld = OverviewTileCache(r"C:\worlds\w", "minecraft:overworld")
    nether = OverviewTileCache(r"C:\worlds\w", "minecraft:the_nether")
    pixels = numpy.zeros((TILE_PIXELS, TILE_PIXELS, 4), numpy.uint8)
    overworld.save_tile(0, 0, pixels, set())
    assert nether.load_tile(0, 0) is None


def test_double_negative_tile_coords_round_trip(cache):
    pixels = numpy.zeros((TILE_PIXELS, TILE_PIXELS, 4), numpy.uint8)
    cache.save_tile(-2, -3, pixels, {(-70, -90)})
    loaded = cache.load_tile(-2, -3)
    assert loaded is not None
    assert loaded[1] == {(-70, -90)}
    assert (-2, -3) in cache.list_tiles()


def test_numpy_integer_coords_are_serialized(cache):
    pixels = numpy.zeros((TILE_PIXELS, TILE_PIXELS, 4), numpy.uint8)
    complete = {(numpy.int64(3), numpy.int64(4))}
    cache.save_tile(0, 1, pixels, complete)
    loaded = cache.load_tile(0, 1)
    assert loaded is not None
    assert loaded[1] == {(3, 4)}


def test_no_tmp_files_left_behind(cache):
    pixels = numpy.zeros((TILE_PIXELS, TILE_PIXELS, 4), numpy.uint8)
    cache.save_tile(2, 2, pixels, set())
    leftovers = [n for n in os.listdir(cache._dir) if n.endswith(".tmp")]
    assert leftovers == []


def test_concurrent_saves_of_same_tile_do_not_error(cache):
    import threading

    pixels = numpy.zeros((TILE_PIXELS, TILE_PIXELS, 4), numpy.uint8)
    errors = []

    def save(n):
        try:
            for _ in range(10):
                cache.save_tile(0, 0, pixels, {(n, 0)})
        except Exception as e:
            errors.append(e)

    threads = [threading.Thread(target=save, args=(i,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert errors == []
    loaded = cache.load_tile(0, 0)
    assert loaded is not None  # last-writer-wins, file intact
    leftovers = [n for n in os.listdir(cache._dir) if n.endswith(".tmp")]
    assert leftovers == []


def test_stale_tmp_files_cleaned_on_init(tmp_path, monkeypatch):
    monkeypatch.setenv("CACHE_DIR", str(tmp_path))
    first = OverviewTileCache(r"C:\worlds\w2", "minecraft:overworld")
    stale = os.path.join(first._dir, "tile.0.0.png.12345-0.tmp")
    with open(stale, "wb") as f:
        f.write(b"junk")
    again = OverviewTileCache(r"C:\worlds\w2", "minecraft:overworld")
    assert not os.path.exists(stale)
