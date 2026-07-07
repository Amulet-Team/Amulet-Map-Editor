import numpy

from amulet_map_editor.api.opengl.resource_pack.resource_pack import (
    mean_texture_colour,
)


def _image_with_patch(colour, alpha=255):
    image = numpy.zeros((64, 64, 4), numpy.uint8)
    image[16:32, 16:32, :3] = colour
    image[16:32, 16:32, 3] = alpha
    return image


def test_mean_of_solid_patch():
    image = _image_with_patch((100, 150, 200))
    # bounds select exactly the 16x16 patch: 16/64=0.25 .. 32/64=0.5
    colour = mean_texture_colour(image, (0.25, 0.25, 0.5, 0.5))
    assert colour.dtype == numpy.uint8
    assert tuple(colour) == (100, 150, 200, 255)


def test_fully_transparent_region_gives_zero_alpha():
    image = numpy.zeros((64, 64, 4), numpy.uint8)
    colour = mean_texture_colour(image, (0.0, 0.0, 0.25, 0.25))
    assert colour[3] == 0


def test_alpha_weighted_mean_ignores_transparent_pixels():
    image = numpy.zeros((2, 2, 4), numpy.uint8)
    image[0, 0] = (200, 0, 0, 255)  # one opaque red pixel
    # other three pixels transparent black
    colour = mean_texture_colour(image, (0.0, 0.0, 1.0, 1.0))
    assert colour[0] == 200  # red not diluted by transparent black
    assert colour[3] == 255 // 4 + 1 or colour[3] == 255 // 4  # mean alpha ~64


def test_mean_texture_colour_result_is_fresh_per_call():
    image = _image_with_patch((10, 20, 30))
    a = mean_texture_colour(image, (0.25, 0.25, 0.5, 0.5))
    b = mean_texture_colour(image, (0.25, 0.25, 0.5, 0.5))
    assert a is not b  # pure function returns fresh arrays


def test_get_block_top_colour_returns_read_only_cached_array():
    import numpy
    import pytest
    from unittest.mock import MagicMock
    from amulet_map_editor.api.opengl.resource_pack.resource_pack import (
        OpenGLResourcePack,
    )

    pack = OpenGLResourcePack.__new__(OpenGLResourcePack)
    pack._block_top_colours = {}
    pack._image = numpy.full(64 * 64 * 4, 255, numpy.uint8)
    pack._image_width = 64
    pack._image_height = 64
    model = MagicMock()
    model.faces = {"up": object()}
    model.texture_index = {"up": [0]}
    model.textures = ["some/texture"]
    model.tint_verts = {"up": numpy.ones(12, numpy.float32)}
    pack.get_block_model = lambda block: model
    pack.texture_bounds = lambda path: (0.0, 0.0, 0.5, 0.5)

    block = object()
    colour = pack.get_block_top_colour(block)
    assert colour[3] == 255
    with pytest.raises((ValueError, RuntimeError)):
        colour[0] = 0  # cached colour must be read-only
    assert pack.get_block_top_colour(block) is colour  # memoised
