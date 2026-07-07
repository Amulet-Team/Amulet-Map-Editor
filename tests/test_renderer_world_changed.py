from unittest.mock import MagicMock

from amulet.api.errors import ChunkDoesNotExist

from amulet_map_editor.programs.edit.api.renderer import Renderer


def _bare_renderer(changed, get_chunk):
    r = Renderer.__new__(Renderer)
    r._notified_changes = {}
    r._world_change_pending = False
    r._overview_scanner = MagicMock()
    render_world = MagicMock()
    render_world.dimension = "overworld"
    render_world.level.chunks.changed_chunks = lambda: iter(changed)
    render_world.level.get_chunk = get_chunk
    object.__setattr__(r, "_render_world", render_world)
    return r


def _chunk_with_time(t):
    chunk = MagicMock()
    chunk.changed_time = t
    return chunk


def test_world_changed_notifies_scanner_and_detail():
    r = _bare_renderer([("overworld", 1, 2)], lambda cx, cz, dim: _chunk_with_time(5.0))
    r.world_changed()
    assert r._process_world_changes() is True
    r._overview_scanner.mark_chunk_changed.assert_called_once_with((1, 2))
    r.render_world.mark_chunk_stale.assert_called_once_with((1, 2))


def test_world_changed_dedupes_by_changed_time():
    r = _bare_renderer([("overworld", 1, 2)], lambda cx, cz, dim: _chunk_with_time(5.0))
    r.world_changed()
    r._process_world_changes()
    r.world_changed()
    r._process_world_changes()  # same changed_time -> no re-notify
    assert r._overview_scanner.mark_chunk_changed.call_count == 1


def test_world_changed_renotifies_on_new_edit():
    times = iter([5.0, 5.0, 9.0])
    r = _bare_renderer(
        [("overworld", 1, 2)],
        lambda cx, cz, dim: _chunk_with_time(next(times)),
    )
    for _ in range(3):
        r.world_changed()
        r._process_world_changes()  # changed_time moved on 3rd -> re-notify
    assert r._overview_scanner.mark_chunk_changed.call_count == 2


def test_world_changed_deleted_chunk_always_notifies():
    def raise_missing(cx, cz, dim):
        raise ChunkDoesNotExist()

    r = _bare_renderer([("overworld", 3, 4)], raise_missing)
    r.world_changed()
    r._process_world_changes()
    r.world_changed()
    r._process_world_changes()
    assert r._overview_scanner.mark_chunk_changed.call_count == 2


def test_world_changed_ignores_other_dimensions():
    r = _bare_renderer([("nether", 1, 2)], lambda cx, cz, dim: _chunk_with_time(1.0))
    r.world_changed()
    r._process_world_changes()
    r._overview_scanner.mark_chunk_changed.assert_not_called()


def test_process_world_changes_noop_without_flag():
    r = _bare_renderer([], lambda cx, cz, dim: None)
    assert r._process_world_changes() is False


def test_world_changed_sets_flag_only():
    r = _bare_renderer([("overworld", 1, 2)], lambda cx, cz, dim: _chunk_with_time(1.0))
    r.world_changed()
    r._overview_scanner.mark_chunk_changed.assert_not_called()  # deferred to pool
    assert r._process_world_changes() is True
    r._overview_scanner.mark_chunk_changed.assert_called_once_with((1, 2))
