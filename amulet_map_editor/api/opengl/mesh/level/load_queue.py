import heapq
import itertools
from threading import Lock
from typing import Dict, List, Optional, Tuple

ChunkCoords = Tuple[int, int]


class ChunkLoadQueue:
    """A thread safe priority queue of chunk coordinates to build.

    Ordering: priority class first (urgent rebuilds, then never-loaded
    chunks, then verify sweeps), then Chebyshev distance to the camera
    chunk. Moving the camera re-prioritises pending entries instead of
    restarting anything. LOAD entries that fall outside the render
    distance after a camera move are dropped lazily at pop time.
    """

    PRIORITY_URGENT = 0  # a chunk known to have changed (and its neighbours)
    PRIORITY_LOAD = 1  # a chunk in render distance with no geometry yet
    PRIORITY_VERIFY = 2  # check if a loaded chunk has changed

    def __init__(self, render_distance: int = 5):
        self._lock = Lock()
        self._render_distance = render_distance
        self._camera: ChunkCoords = (0, 0)
        # coords -> priority for all live entries (dedupe + upgrade)
        self._entries: Dict[ChunkCoords, int] = {}
        # heap of (priority, distance, seq, coords). Entries whose
        # priority no longer matches self._entries are stale.
        self._heap: List[Tuple[int, int, int, ChunkCoords]] = []
        self._seq = itertools.count()

    def _distance(self, coords: ChunkCoords) -> int:
        return max(abs(coords[0] - self._camera[0]), abs(coords[1] - self._camera[1]))

    def set_render_distance(self, render_distance: int):
        with self._lock:
            self._render_distance = render_distance

    def set_camera_chunk(self, cx: int, cz: int):
        """Move the camera and re-prioritise all pending entries."""
        with self._lock:
            if (cx, cz) == self._camera:
                return
            self._camera = (cx, cz)
            self._heap = [
                (priority, self._distance(coords), next(self._seq), coords)
                for coords, priority in self._entries.items()
            ]
            heapq.heapify(self._heap)

    def push(self, coords: ChunkCoords, priority: int):
        with self._lock:
            existing = self._entries.get(coords)
            if existing is not None and existing <= priority:
                return  # already queued at the same or better priority
            self._entries[coords] = priority
            heapq.heappush(
                self._heap,
                (priority, self._distance(coords), next(self._seq), coords),
            )

    def pop(self) -> Optional[Tuple[ChunkCoords, int]]:
        with self._lock:
            while self._heap:
                priority, _, _, coords = heapq.heappop(self._heap)
                if self._entries.get(coords) != priority:
                    continue  # stale entry (upgraded or discarded)
                del self._entries[coords]
                if (
                    priority == self.PRIORITY_LOAD
                    and self._distance(coords) > self._render_distance
                ):
                    continue  # camera moved away before we got to it
                return coords, priority
            return None

    def discard(self, coords: ChunkCoords):
        with self._lock:
            self._entries.pop(coords, None)

    def clear(self):
        with self._lock:
            self._entries.clear()
            self._heap.clear()

    def __len__(self) -> int:
        with self._lock:
            return len(self._entries)

    def __contains__(self, coords: ChunkCoords) -> bool:
        with self._lock:
            return coords in self._entries
