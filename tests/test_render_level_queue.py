from unittest.mock import MagicMock

from amulet_map_editor.api.opengl.mesh.level.level import RenderLevel
from amulet_map_editor.api.opengl.mesh.level.load_queue import ChunkLoadQueue


def _make_render_level(render_distance=2):
    level = MagicMock()
    level.dimensions = ["overworld"]
    resource_pack = MagicMock()
    rl = RenderLevel("test_context", resource_pack, level)
    rl.render_distance = render_distance
    return rl


def test_camera_move_enqueues_missing_chunks_nearest_first():
    rl = _make_render_level(render_distance=1)
    rl.camera_location = (8, 100, 8)  # chunk (0, 0)
    queue = rl._load_queue
    # 3x3 = 9 chunks around (0, 0)
    assert len(queue) == 9
    coords, priority = queue.pop()
    assert coords == (0, 0)
    assert priority == ChunkLoadQueue.PRIORITY_LOAD


def test_camera_move_within_same_chunk_enqueues_nothing_new():
    rl = _make_render_level(render_distance=1)
    rl.camera_location = (8, 100, 8)
    n = len(rl._load_queue)
    rl.camera_location = (9, 100, 9)  # still chunk (0, 0)
    assert len(rl._load_queue) == n


def test_loaded_chunks_are_not_re_enqueued():
    rl = _make_render_level(render_distance=1)
    rl._chunk_manager = MagicMock()
    rl._chunk_manager.__contains__ = lambda self_, coords: coords == (2, 2)
    # drop items enqueued during construction (before the mock was in place)
    rl._load_queue.clear()
    rl.camera_location = (40, 100, 40)  # chunk (2, 2)
    popped = set()
    while True:
        item = rl._load_queue.pop()
        if item is None:
            break
        popped.add(item[0])
    assert (2, 2) not in popped
    assert len(popped) == 8


def test_rebuild_changed_pushes_verify_items():
    rl = _make_render_level(render_distance=1)
    rl._chunk_manager = MagicMock()
    rl._chunk_manager.chunk_coords = lambda: iter([(5, 5), (6, 5)])
    rl.rebuild_changed()
    assert (5, 5) in rl._load_queue
    assert (6, 5) in rl._load_queue


def test_dimension_change_clears_queue():
    rl = _make_render_level(render_distance=1)
    rl.camera_location = (8, 100, 8)
    assert len(rl._load_queue) > 0
    rl.dimension = "nether"
    # queue is re-seeded for the new dimension around the camera
    assert len(rl._load_queue) == 9


def test_negative_camera_coordinates_use_floored_chunk():
    rl = _make_render_level(render_distance=1)
    rl._load_queue.clear()
    rl.camera_location = (-0.5, 100, -0.5)  # true chunk (-1, -1)
    coords, priority = rl._load_queue.pop()
    assert coords == (-1, -1)


def test_region_merge_is_mutually_exclusive_and_rate_limited():
    import threading
    import time as time_module

    rl = _make_render_level(render_distance=1)
    active = 0
    max_active = 0
    calls = 0
    lock = threading.Lock()

    def slow_rebuild():
        nonlocal active, max_active, calls
        with lock:
            active += 1
            calls += 1
            max_active = max(max_active, active)
        time_module.sleep(0.05)
        with lock:
            active -= 1

    rl._chunk_manager = MagicMock()
    rl._chunk_manager.rebuild = slow_rebuild
    rl._rebuild_time = 0.0  # make the first call eligible immediately

    threads = [threading.Thread(target=rl._try_region_merge) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert max_active == 1  # never concurrent
    assert calls == 1  # rate limit: only the first eligible call ran


def test_detail_disabled_stops_enqueue_and_drops_load_items():
    rl = _make_render_level(render_distance=1)
    rl._load_queue.clear()
    rl.detail_enabled = False
    rl.camera_location = (40, 100, 40)  # chunk boundary crossing
    assert len(rl._load_queue) == 0  # no churn while suppressed


def test_detail_disabled_load_items_are_dropped_by_worker():
    rl = _make_render_level(render_distance=1)
    # queue was seeded while enabled (during construction)
    assert len(rl._load_queue) > 0
    rl.detail_enabled = False
    while rl.thread_action():
        pass
    assert len(rl._load_queue) == 0
    assert rl._chunk_manager.chunk_coords() is not None  # nothing built: see below
    # no RenderChunk was constructed: the real chunk manager stayed empty
    assert list(rl.chunk_manager.chunk_coords()) == []


def test_detail_disabled_urgent_items_are_remembered_and_replayed():
    rl = _make_render_level(render_distance=1)
    rl._load_queue.clear()
    rl.detail_enabled = False
    rl._load_queue.push((5, 5), ChunkLoadQueue.PRIORITY_URGENT)
    assert rl.thread_action() is True
    assert len(rl._load_queue) == 0
    rl.detail_enabled = True  # replay
    coords, priority = rl._load_queue.pop()
    assert (coords, priority) == ((5, 5), ChunkLoadQueue.PRIORITY_URGENT)


def test_detail_disabled_verify_still_fires_on_chunk_changed():
    rl = _make_render_level(render_distance=1)
    rl._load_queue.clear()
    rl.detail_enabled = False
    changed = []
    rl.on_chunk_changed = changed.append
    rl._chunk_manager = MagicMock()
    rl._chunk_manager.render_chunk_needs_rebuild = lambda coords: True
    rl._chunk_manager.__contains__ = lambda self_, coords: False
    rl._load_queue.push((3, 3), ChunkLoadQueue.PRIORITY_VERIFY)
    assert rl.thread_action() is True
    assert changed == [(3, 3)]
    # geometry rebuild deferred, not queued
    assert len(rl._load_queue) == 0
    assert (3, 3) in rl._stale_geometry


def test_reenable_reseeds_load_queue():
    rl = _make_render_level(render_distance=1)
    rl.detail_enabled = False
    while rl.thread_action():
        pass
    rl.detail_enabled = True
    assert len(rl._load_queue) == 9  # 3x3 around the camera reseeded


def test_stale_geometry_replay_is_race_safe():
    import threading

    rl = _make_render_level(render_distance=1)
    rl._load_queue.clear()
    rl.detail_enabled = False
    for i in range(500):
        with rl._stale_lock:
            rl._stale_geometry.add((i, i))
    errors = []

    def adder():
        try:
            for i in range(500, 1500):
                with rl._stale_lock:
                    rl._stale_geometry.add((i, i))
        except Exception as e:
            errors.append(e)

    t = threading.Thread(target=adder)
    t.start()
    rl.detail_enabled = True  # concurrent replay
    t.join()
    assert errors == []
    # replayed coords are in the queue; late adds are safely parked for next flip
    assert len(rl._load_queue) >= 500


def test_mark_chunk_stale_parks_when_disabled_and_pushes_when_enabled():
    rl = _make_render_level(render_distance=1)
    rl._chunk_manager = MagicMock()
    rl._chunk_manager.__contains__ = lambda self_, coords: coords == (7, 7)
    rl._load_queue.clear()
    rl.detail_enabled = False
    rl.mark_chunk_stale((7, 7))
    with rl._stale_lock:
        assert (7, 7) in rl._stale_geometry
    assert len(rl._load_queue) == 0

    rl2 = _make_render_level(render_distance=1)
    rl2._chunk_manager = MagicMock()
    rl2._chunk_manager.__contains__ = lambda self_, coords: coords == (7, 7)
    rl2._load_queue.clear()
    rl2.mark_chunk_stale((7, 7))
    coords, priority = rl2._load_queue.pop()
    assert (coords, priority) == ((7, 7), ChunkLoadQueue.PRIORITY_URGENT)


def test_mark_chunk_stale_ignores_unloaded_primary():
    # A chunk with no geometry builds fresh via LOAD when approached, so an
    # edit far outside render distance must not push/park an URGENT rebuild.
    rl = _make_render_level(render_distance=1)
    rl._chunk_manager = MagicMock()
    rl._chunk_manager.__contains__ = lambda self_, coords: False
    rl._load_queue.clear()
    rl.mark_chunk_stale((7, 7))
    assert len(rl._load_queue) == 0
    with rl._stale_lock:
        assert rl._stale_geometry == set()

    # ...even while the detail layer is suppressed: nothing is parked either.
    rl2 = _make_render_level(render_distance=1)
    rl2._chunk_manager = MagicMock()
    rl2._chunk_manager.__contains__ = lambda self_, coords: False
    rl2._load_queue.clear()
    rl2.detail_enabled = False
    rl2.mark_chunk_stale((7, 7))
    assert len(rl2._load_queue) == 0
    with rl2._stale_lock:
        assert rl2._stale_geometry == set()
