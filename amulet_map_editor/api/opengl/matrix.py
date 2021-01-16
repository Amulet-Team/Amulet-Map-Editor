import math
import numpy
from amulet.utils.matrix import (
    scale_matrix,
    rotation_matrix_xy,
    rotation_matrix_yx,
    rotation_matrix_xyz,
    transform_matrix,
    displacement_matrix,
    inverse_transform_matrix,
)

TransformationMatrixType = numpy.ndarray


def perspective_matrix(
    fovy: float,  # field of view in the vertical direction in radians
    aspect,  # aspect ratio x/y
    z_near,  # near clipping distance
    z_far,  # far clipping distance
) -> TransformationMatrixType:
    # camera projection
    f = 1 / math.tan(fovy / 2)
    return numpy.array(
        [
            [f / aspect, 0, 0, 0],
            [0, f, 0, 0],
            [
                0,
                0,
                (z_far + z_near) / (z_near - z_far),
                (2 * z_far * z_near) / (z_near - z_far),
            ],
            [0, 0, -1, 0],
        ],
        dtype=numpy.float64,
    )


def orthographic_matrix(
    radius: float,  # the viewable distance in the vertical direction in blocks
    aspect,  # aspect ratio x/y
    near,  # near clipping distance
    far,  # far clipping distance
) -> TransformationMatrixType:
    """The orthographic matrix to convert camera space to screen space."""
    bottom = -radius
    top = radius
    left = bottom * aspect
    right = top * aspect
    return numpy.array(
        [
            [2 / (right - left), 0, 0, -(right + left) / (right - left)],
            [0, 2 / (top - bottom), 0, -(top + bottom) / (top - bottom)],
            [0, 0, -2 / (far - near), -(far + near) / (far - near)],
            [0, 0, 0, 1],
        ]
    )
