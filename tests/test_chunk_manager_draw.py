from unittest.mock import MagicMock

from amulet_map_editor.api.opengl.mesh.level.region import ChunkManager


def _make_region(rx, rz):
    region = MagicMock()
    region.rx = rx
    region.rz = rz
    region.last_drawn = 0
    return region


def test_draw_culls_region_at_min_boundary_and_draws_edge_overlapping_region():
    # region_size defaults to 16, so each region spans 16 chunks.
    manager = ChunkManager("ctx", MagicMock())

    # region (0, 0) spans chunks x in [0, 15]. Its last chunk (15) is
    # min_cx - 1, i.e. entirely outside the rect, so it must be culled.
    # This is the Finding 1 regression case: (rx + 1) * region_size == min_cx.
    culled_region = _make_region(0, 0)

    # region (1, 0) spans chunks x in [16, 31] and starts exactly at
    # min_cx, overlapping the rect edge, so it must be drawn.
    edge_region = _make_region(1, 0)

    # region (10, 0) spans chunks x in [160, 175], entirely beyond
    # max_cx, so it must be culled.
    far_region = _make_region(10, 0)

    manager._regions[(0, 0)] = culled_region
    manager._regions[(1, 0)] = edge_region
    manager._regions[(10, 0)] = far_region

    manager.draw(MagicMock(), (0, 0, 0), visible_rect=(16, 0, 100, 100))

    culled_region.draw.assert_not_called()
    edge_region.draw.assert_called_once()
    far_region.draw.assert_not_called()
