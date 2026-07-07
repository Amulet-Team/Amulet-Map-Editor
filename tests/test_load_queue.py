import threading

from amulet_map_editor.api.opengl.mesh.level.load_queue import ChunkLoadQueue


def test_pop_orders_by_distance():
    q = ChunkLoadQueue(render_distance=10)
    q.set_camera_chunk(0, 0)
    q.push((5, 5), ChunkLoadQueue.PRIORITY_LOAD)
    q.push((1, 0), ChunkLoadQueue.PRIORITY_LOAD)
    q.push((3, 0), ChunkLoadQueue.PRIORITY_LOAD)
    assert q.pop() == ((1, 0), ChunkLoadQueue.PRIORITY_LOAD)
    assert q.pop() == ((3, 0), ChunkLoadQueue.PRIORITY_LOAD)
    assert q.pop() == ((5, 5), ChunkLoadQueue.PRIORITY_LOAD)
    assert q.pop() is None


def test_urgent_before_load_regardless_of_distance():
    q = ChunkLoadQueue(render_distance=20)
    q.set_camera_chunk(0, 0)
    q.push((1, 0), ChunkLoadQueue.PRIORITY_LOAD)
    q.push((15, 15), ChunkLoadQueue.PRIORITY_URGENT)
    assert q.pop() == ((15, 15), ChunkLoadQueue.PRIORITY_URGENT)


def test_load_before_verify():
    q = ChunkLoadQueue(render_distance=20)
    q.set_camera_chunk(0, 0)
    q.push((1, 0), ChunkLoadQueue.PRIORITY_VERIFY)
    q.push((15, 15), ChunkLoadQueue.PRIORITY_LOAD)
    assert q.pop() == ((15, 15), ChunkLoadQueue.PRIORITY_LOAD)
    assert q.pop() == ((1, 0), ChunkLoadQueue.PRIORITY_VERIFY)


def test_camera_move_reorders():
    q = ChunkLoadQueue(render_distance=100)
    q.set_camera_chunk(0, 0)
    q.push((90, 0), ChunkLoadQueue.PRIORITY_LOAD)
    q.push((10, 0), ChunkLoadQueue.PRIORITY_LOAD)
    q.set_camera_chunk(80, 0)
    assert q.pop() == ((90, 0), ChunkLoadQueue.PRIORITY_LOAD)


def test_stale_load_items_dropped():
    q = ChunkLoadQueue(render_distance=5)
    q.set_camera_chunk(0, 0)
    q.push((3, 0), ChunkLoadQueue.PRIORITY_LOAD)
    q.set_camera_chunk(100, 100)
    assert q.pop() is None  # (3, 0) is now out of render distance


def test_verify_items_never_dropped_by_distance():
    q = ChunkLoadQueue(render_distance=5)
    q.set_camera_chunk(0, 0)
    q.push((300, 300), ChunkLoadQueue.PRIORITY_VERIFY)
    assert q.pop() == ((300, 300), ChunkLoadQueue.PRIORITY_VERIFY)


def test_push_dedupes_and_upgrades_priority():
    q = ChunkLoadQueue(render_distance=10)
    q.set_camera_chunk(0, 0)
    q.push((2, 0), ChunkLoadQueue.PRIORITY_VERIFY)
    q.push((2, 0), ChunkLoadQueue.PRIORITY_URGENT)
    q.push((2, 0), ChunkLoadQueue.PRIORITY_VERIFY)  # downgrade attempt ignored
    assert len(q) == 1
    assert q.pop() == ((2, 0), ChunkLoadQueue.PRIORITY_URGENT)
    assert q.pop() is None


def test_contains_discard_clear():
    q = ChunkLoadQueue(render_distance=10)
    q.set_camera_chunk(0, 0)
    q.push((1, 1), ChunkLoadQueue.PRIORITY_LOAD)
    assert (1, 1) in q
    q.discard((1, 1))
    assert (1, 1) not in q
    assert q.pop() is None
    q.push((2, 2), ChunkLoadQueue.PRIORITY_LOAD)
    q.clear()
    assert len(q) == 0
    assert q.pop() is None


def test_thread_safety_smoke():
    q = ChunkLoadQueue(render_distance=10_000)
    q.set_camera_chunk(0, 0)
    popped = []

    def pusher(offset):
        for i in range(500):
            q.push((offset + i, 0), ChunkLoadQueue.PRIORITY_LOAD)

    def popper():
        for _ in range(400):
            item = q.pop()
            if item is not None:
                popped.append(item[0])

    threads = [
        threading.Thread(target=pusher, args=(0,)),
        threading.Thread(target=pusher, args=(1000,)),
        threading.Thread(target=popper),
        threading.Thread(target=popper),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    remaining = []
    while True:
        item = q.pop()
        if item is None:
            break
        remaining.append(item[0])
    assert len(popped) + len(remaining) == 1000
    assert len(set(popped) | set(remaining)) == 1000
