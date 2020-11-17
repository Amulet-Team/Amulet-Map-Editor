import math
import numpy
from amulet.utils.matrix import (
    scale_matrix,
    rotation_matrix,
    transform_matrix,
    displacement_matrix,
)


def projection_matrix(
    fovy: float,  # field of view in the vertical direction in radians
    aspect,  # aspect ratio x/y
    z_near,  # near clipping distance
    z_far,  # far clipping distance
) -> numpy.ndarray:
    # camera projection
    f = 1 / math.tan(fovy / 2)
    return numpy.array(
        [
            [f / aspect, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, (z_far + z_near) / (z_near - z_far), -1],
            [0, 0, (2 * z_far * z_near) / (z_near - z_far), 0],
        ],
        dtype=numpy.float64,
    )
