import threading
import time

from amulet_map_editor.programs.edit.api.chunk_generator import ChunkGenerator


def test_default_worker_count_is_capped():
    from amulet_map_editor.programs.edit.api.chunk_generator import (
        default_worker_count,
    )

    assert 2 <= default_worker_count() <= 4


def test_parallel_action_called_from_multiple_threads():
    gen = ChunkGenerator(worker_count=3)
    seen_threads = set()
    lock = threading.Lock()

    def action() -> bool:
        with lock:
            seen_threads.add(threading.get_ident())
        time.sleep(0.001)
        return True

    gen.register_parallel(action)
    gen.start()
    time.sleep(0.5)
    gen.stop()
    assert len(seen_threads) >= 2


def test_serial_object_never_called_concurrently():
    gen = ChunkGenerator(worker_count=4)
    active = 0
    max_active = 0
    lock = threading.Lock()

    class Serial:
        thread_weighting = 1

        def thread_action(self):
            nonlocal active, max_active
            with lock:
                active += 1
                max_active = max(max_active, active)
            time.sleep(0.002)
            with lock:
                active -= 1

    gen.register(Serial())
    gen.start()
    time.sleep(0.3)
    gen.stop()
    assert max_active == 1


def test_stop_joins_workers():
    gen = ChunkGenerator(worker_count=2)
    gen.register_parallel(lambda: False)
    gen.start()
    threads = list(gen._threads)
    gen.stop()
    assert threads
    assert all(not t.is_alive() for t in threads)


def test_parallel_priority_chaining():
    gen = ChunkGenerator(worker_count=1)
    calls = []
    budget = [3]

    def high() -> bool:
        if budget[0] > 0:
            budget[0] -= 1
            calls.append("high")
            return True
        return False

    def low() -> bool:
        calls.append("low")
        return False

    gen.register_parallel(high)
    gen.register_parallel(low)
    gen.start()
    time.sleep(0.3)
    gen.stop()
    first_low = calls.index("low")
    assert calls[:first_low] == ["high"] * 3  # all high-priority work drained first


def test_serial_exception_does_not_kill_worker():
    gen = ChunkGenerator(worker_count=1)
    calls = []

    class Exploding:
        thread_weighting = 1

        def thread_action(self):
            calls.append(1)
            raise RuntimeError("boom")

    gen.register(Exploding())
    gen.start()
    time.sleep(0.3)
    gen.stop()
    assert len(calls) >= 2  # worker survived the first exception and retried


def test_idle_serial_objects_are_not_busy_polled():
    gen = ChunkGenerator(worker_count=1)
    calls = []

    class Idle:
        thread_weighting = 0

        def thread_action(self):
            calls.append(1)

    gen.register(Idle())
    gen.start()
    time.sleep(0.2)
    gen.stop()
    assert calls == []  # weighting 0 means never serviced (and workers sleep)
