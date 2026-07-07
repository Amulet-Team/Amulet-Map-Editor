import numpy

from amulet_map_editor.programs.edit.api.overview.scan import (
    EMPTY_HEIGHT,
    ERROR_COLOURS,
    shade,
    top_colours,
)

# palette: 0=air (transparent), 1=stone (grey), 2=grass (green)
PALETTE = numpy.array(
    [(0, 0, 0, 0), (128, 128, 128, 255), (60, 180, 60, 255)], numpy.uint8
)


def test_flat_layer():
    sub = numpy.zeros((16, 16, 16), numpy.uint32)
    sub[:, 3, :] = 2  # grass at local y=3
    colours, heights = top_colours({0: sub}, PALETTE)
    assert colours.shape == (16, 16, 4)
    assert (colours == (60, 180, 60, 255)).all()
    assert (heights == 3).all()


def test_higher_block_wins():
    sub = numpy.zeros((16, 16, 16), numpy.uint32)
    sub[:, 3, :] = 2
    sub[5, 10, 5] = 1  # stone above grass in one column
    colours, heights = top_colours({0: sub}, PALETTE)
    assert tuple(colours[5, 5]) == (128, 128, 128, 255)
    assert heights[5, 5] == 10
    assert tuple(colours[0, 0]) == (60, 180, 60, 255)


def test_higher_sub_chunk_wins():
    low = numpy.zeros((16, 16, 16), numpy.uint32)
    low[:, :, :] = 1
    high = numpy.zeros((16, 16, 16), numpy.uint32)
    high[0, 0, 0] = 2
    colours, heights = top_colours({0: low, 4: high}, PALETTE)
    assert tuple(colours[0, 0]) == (60, 180, 60, 255)
    assert heights[0, 0] == 4 * 16 + 0
    assert tuple(colours[1, 1]) == (128, 128, 128, 255)
    assert heights[1, 1] == 15


def test_all_air_is_transparent():
    sub = numpy.zeros((16, 16, 16), numpy.uint32)
    colours, heights = top_colours({0: sub}, PALETTE)
    assert (colours[..., 3] == 0).all()
    assert (heights == EMPTY_HEIGHT).all()


def test_empty_sub_chunks_dict():
    colours, heights = top_colours({}, PALETTE)
    assert (colours[..., 3] == 0).all()
    assert (heights == EMPTY_HEIGHT).all()


def test_shade_brightens_south_facing_slopes():
    colours = numpy.full((16, 16, 4), (100, 100, 100, 255), numpy.uint8)
    heights = numpy.zeros((16, 16), numpy.int32)
    heights[:, 8:] = 4  # a step up midway along z
    shaded = shade(colours, heights)
    # column at the step (z=8) is higher than its northern neighbour -> brighter
    assert shaded[0, 8, 0] > 100
    # flat area unchanged
    assert shaded[0, 4, 0] == 100
    # alpha untouched
    assert (shaded[..., 3] == 255).all()


def test_error_patch_shape():
    assert ERROR_COLOURS.shape == (16, 16, 4)
    assert (ERROR_COLOURS[..., 3] == 255).all()
