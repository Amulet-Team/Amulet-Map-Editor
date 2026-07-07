from amulet_map_editor.programs.edit.api.behaviour.ortho_navigation import (
    screen_delta_to_world,
    zoom_towards,
)


def test_full_width_drag_moves_full_visible_width():
    wx_, wz = screen_delta_to_world(
        800, 0, fov=100, aspect_ratio=2.0, width=800, height=400
    )
    assert wx_ == 400.0  # 2 * fov * aspect
    assert wz == 0.0


def test_full_height_drag_moves_full_visible_height():
    wx_, wz = screen_delta_to_world(
        0, 400, fov=100, aspect_ratio=2.0, width=800, height=400
    )
    assert wx_ == 0.0
    assert wz == 200.0  # 2 * fov


def test_zero_size_canvas_is_safe():
    screen_delta_to_world(10, 10, 100, 1.0, 0, 0)  # must not raise


def test_zoom_towards_centre_keeps_camera():
    x, z = zoom_towards(50.0, -20.0, 0.5, 0.5, 100.0, 50.0, 1.5)
    assert (x, z) == (50.0, -20.0)


def test_zoom_towards_corner_keeps_corner_block_fixed():
    old_fov, new_fov, aspect = 100.0, 50.0, 2.0
    cam_x, cam_z = 0.0, 0.0
    frac_x, frac_y = 1.0, 0.0  # top-right corner
    corner_world_x = cam_x + (frac_x - 0.5) * 2 * old_fov * aspect  # 200
    corner_world_z = cam_z + (frac_y - 0.5) * 2 * old_fov  # -100
    new_x, new_z = zoom_towards(cam_x, cam_z, frac_x, frac_y, old_fov, new_fov, aspect)
    # under the new fov, the same corner fraction must map to the same world pos
    assert new_x + (frac_x - 0.5) * 2 * new_fov * aspect == corner_world_x
    assert new_z + (frac_y - 0.5) * 2 * new_fov == corner_world_z


def test_zoom_out_is_inverse_of_zoom_in():
    x1, z1 = zoom_towards(10.0, 20.0, 0.25, 0.75, 100.0, 50.0, 1.0)
    x2, z2 = zoom_towards(x1, z1, 0.25, 0.75, 50.0, 100.0, 1.0)
    assert abs(x2 - 10.0) < 1e-9 and abs(z2 - 20.0) < 1e-9
