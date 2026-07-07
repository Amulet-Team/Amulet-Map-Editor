"""Pure math for top-down (orthographic) map navigation."""

from typing import Tuple


def screen_delta_to_world(
    dx: float, dy: float, fov: float, aspect_ratio: float, width: int, height: int
) -> Tuple[float, float]:
    """Convert a screen-pixel delta to the world-block delta under the cursor.

    :param fov: orthographic half-height in blocks.
    :return: (world dx, world dz) — the world movement of a point that stays
        under a cursor moving by (dx, dy) pixels.
    """
    width = max(1, width)
    height = max(1, height)
    return (
        dx * 2.0 * fov * aspect_ratio / width,
        dy * 2.0 * fov / height,
    )


def zoom_towards(
    camera_x: float,
    camera_z: float,
    cursor_x_frac: float,
    cursor_y_frac: float,
    old_fov: float,
    new_fov: float,
    aspect_ratio: float,
) -> Tuple[float, float]:
    """Camera position that keeps the block under the cursor stationary while
    zooming from old_fov to new_fov.

    :param cursor_x_frac: cursor x as a fraction of canvas width (0..1).
    :param cursor_y_frac: cursor y as a fraction of canvas height (0..1).
    """
    # world position currently under the cursor
    cursor_world_x = camera_x + (cursor_x_frac - 0.5) * 2.0 * old_fov * aspect_ratio
    cursor_world_z = camera_z + (cursor_y_frac - 0.5) * 2.0 * old_fov
    scale = new_fov / old_fov
    return (
        cursor_world_x - (cursor_world_x - camera_x) * scale,
        cursor_world_z - (cursor_world_z - camera_z) * scale,
    )
