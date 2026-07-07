import os
import time
from typing import Callable, List, Optional
from threading import Thread, Lock

ThreadingEnabled = True


def default_worker_count() -> int:
    # More threads mostly fight the GIL and starve the UI thread.
    return min(4, max(2, (os.cpu_count() or 4) - 2))


class ChunkGenerator:
    """A pool of worker threads that generate chunk geometry and other
    background data.

    Two kinds of work source:
    - parallel actions (thread safe callables returning True if they did
      work) are called concurrently by every worker.
    - legacy serial ThreadedObject instances (e.g. LevelGroup for pasted
      structures) are serviced by at most one worker at a time.
    """

    def __init__(self, worker_count: Optional[int] = None):
        self._worker_count = worker_count or default_worker_count()
        self._enabled = False
        self._threads: List[Thread] = []
        self._parallel: List[Callable[[], bool]] = []
        self._serial: List = []
        self._serial_lock = Lock()

    def register(self, thread_object):
        """Register a legacy serial ThreadedObject (has .thread_action())."""
        if thread_object in self._serial:
            raise Exception("ThreadedObject object is already registered.")
        self._serial.append(thread_object)

    def unregister(self, thread_object):
        self._serial.remove(thread_object)

    def register_parallel(self, action: Callable[[], bool]):
        """Register a thread safe callable returning True if it did work."""
        if action in self._parallel:
            raise Exception("Parallel action is already registered.")
        self._parallel.append(action)

    def unregister_parallel(self, action: Callable[[], bool]):
        self._parallel.remove(action)

    def start(self):
        if not self._enabled:
            if self._threads:
                raise Exception("Thread being disabled")
            self._enabled = True
            self._threads = [
                # daemon: workers only read world data and all cache writes
                # are atomic, so if an abnormal teardown ever skips stop(),
                # they must not keep the dead process alive in memory.
                Thread(target=self._work, name=f"ChunkGenerator-{i}", daemon=True)
                for i in range(self._worker_count)
            ]
            for thread in self._threads:
                thread.start()

    def stop(self):
        if self._enabled:
            self._enabled = False
            for thread in self._threads:
                thread.join()
            self._threads = []

    def _work(self):
        while self._enabled:
            did_work = False
            for action in tuple(self._parallel):
                if not self._enabled:
                    return
                try:
                    if action():
                        did_work = True
                        break  # restart from the highest-priority action
                except Exception:
                    import logging

                    logging.getLogger(__name__).exception(
                        "Error in chunk generator worker"
                    )
            if self._serial and self._serial_lock.acquire(blocking=False):
                try:
                    for thread_object in tuple(self._serial):
                        if not self._enabled:
                            return
                        if not thread_object.thread_weighting:
                            continue  # nothing to do - don't count as work
                        try:
                            thread_object.thread_action()
                        except Exception:
                            import logging

                            logging.getLogger(__name__).exception(
                                "Error in chunk generator worker"
                            )
                        did_work = True
                finally:
                    self._serial_lock.release()
            if not did_work:
                # nothing to do - do not busy-spin
                time.sleep(0.02)
