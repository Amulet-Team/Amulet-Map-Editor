from typing import Dict, Tuple

import numpy

EMPTY_HEIGHT = -(2**20)

# red checkerboard shown for chunks that error on load
ERROR_COLOURS = numpy.zeros((16, 16, 4), numpy.uint8)
_xx, _zz = numpy.meshgrid(numpy.arange(16), numpy.arange(16), indexing="ij")
ERROR_COLOURS[(_xx + _zz) % 2 == 0] = (200, 60, 60, 255)
ERROR_COLOURS[(_xx + _zz) % 2 == 1] = (150, 40, 40, 255)


def top_colours(
    sub_chunks: Dict[int, numpy.ndarray], palette_colours: numpy.ndarray
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Find the colour and height of the top visible block in each column.

    :param sub_chunks: cy -> (16, 16, 16) palette index array indexed (x, y, z)
    :param palette_colours: (N, 4) uint8 RGBA colour per palette index.
        Alpha 0 means the block is invisible (air).
    :return: colours (16, 16, 4) uint8 and heights (16, 16) int32,
        both indexed (x, z). Columns with no visible block have alpha 0
        and height EMPTY_HEIGHT.
    """
    colours = numpy.zeros((16, 16, 4), numpy.uint8)
    heights = numpy.full((16, 16), EMPTY_HEIGHT, numpy.int32)
    unset = numpy.ones((16, 16), bool)
    visible = palette_colours[:, 3] > 0
    for cy in sorted(sub_chunks, reverse=True):
        if not unset.any():
            break
        sub = numpy.asarray(sub_chunks[cy])
        vis = visible[sub]  # (16, 16, 16) bool, indexed (x, y, z)
        has_visible = vis.any(axis=1)  # (16, 16) indexed (x, z)
        # index of the highest visible block in each column
        top_local = 15 - numpy.argmax(vis[:, ::-1, :], axis=1)  # (16, 16)
        top_index = numpy.take_along_axis(sub, top_local[:, None, :], axis=1)[:, 0, :]
        update = unset & has_visible
        colours[update] = palette_colours[top_index[update]]
        heights[update] = cy * 16 + top_local[update]
        unset &= ~has_visible
    return colours, heights


def shade(colours: numpy.ndarray, heights: numpy.ndarray) -> numpy.ndarray:
    """Classic map relief shading: columns higher than their northern
    neighbour get brighter, lower get darker.

    :param colours: (16, 16, 4) uint8 indexed (x, z)
    :param heights: (16, 16) int32 indexed (x, z)
    :return: a new shaded (16, 16, 4) uint8 array.
    """
    north = numpy.roll(heights, 1, axis=1)
    north[:, 0] = heights[:, 0]  # chunk border: neutral shading
    diff = numpy.clip(heights - north, -8, 8).astype(numpy.float32)
    factor = 1.0 + 0.04 * diff
    out = colours.copy()
    rgb = out[..., :3].astype(numpy.float32) * factor[..., None]
    out[..., :3] = rgb.round().clip(0, 255).astype(numpy.uint8)
    return out
