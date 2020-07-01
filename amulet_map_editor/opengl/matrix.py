import math
import numpy
from typing import Optional


def rotation_matrix(
        pitch: float,  # pitch (y axis) in radians
        yaw: float,  # pitch (transformed z axis) in radians
        roll: Optional[float] = None  # pitch (transformed x axis) in radians
):
    c = math.cos(yaw)
    s = math.sin(yaw)

    y_rot = numpy.array(
        [
            [c, 0, -s, 0],
            [0, 1, 0, 0],
            [s, 0, c, 0],
            [0, 0, 0, 1]
        ],
        dtype=numpy.float64
    )

    c = math.cos(pitch)
    s = math.sin(pitch)

    x_rot = numpy.array(
        [
            [1, 0, 0, 0],
            [0, c, s, 0],
            [0, -s, c, 0],
            [0, 0, 0, 1]
        ],
        dtype=numpy.float64
    )

    mat = numpy.matmul(y_rot, x_rot)

    if roll:
        c = math.cos(pitch)
        s = math.sin(pitch)

        z_rot = numpy.array(
            [
                [c, s, 0, 0],
                [-s, c, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ],
            dtype=numpy.float64
        )
        mat = numpy.matmul(mat, z_rot)

    return mat


def projection_matrix(
        fovy: float,  # field of view in the vertical direction in radians
        aspect,  # aspect ratio x/y
        z_near,  # near clipping distance
        z_far  # far clipping distance
):
    # camera projection
    f = 1 / math.tan(fovy / 2)
    return numpy.array(
        [
            [f / aspect, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, (z_far + z_near) / (z_near - z_far), -1],
            [0, 0, (2 * z_far * z_near) / (z_near - z_far), 0]
        ],
        dtype=numpy.float64
    )
