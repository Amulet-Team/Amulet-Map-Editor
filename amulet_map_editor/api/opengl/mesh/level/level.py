from typing import TYPE_CHECKING, Callable, Optional, Any, Tuple, Set
from threading import Lock
import numpy
import time
import logging
import math

from amulet.api.data_types import Dimension

from .chunk import RenderChunk
from .region import ChunkManager
from .selection import GreenRenderSelectionGroup
from .load_queue import ChunkLoadQueue
from amulet_map_editor.api.opengl.data_types import (
    CameraLocationType,
    CameraRotationType,
    TransformationMatrix,
)
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePackManager,
    OpenGLResourcePack,
)
from amulet_map_editor.api.opengl import Drawable, ThreadedObject, ContextManager
from amulet_map_editor.api.util.system_memory import total_system_memory

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel

log = logging.getLogger(__name__)


class RenderLevel(OpenGLResourcePackManager, Drawable, ThreadedObject, ContextManager):
    """A RenderLevel holds a reference to a level and manages all the geometry and drawing for that level."""

    def __init__(
        self,
        context_identifier: Any,
        opengl_resource_pack: OpenGLResourcePack,
        level: "BaseLevel",
        draw_box=False,
        draw_floor=False,
        draw_ceil=False,
        limit_bounds=False,
    ):
        """
        Create a new RenderLevel instance.

        :param context_identifier: The identifier for the opengl context.
        :param opengl_resource_pack: The resource pack to use for models and textures.
        :param level: The level to pull data from.
        :param draw_box: Should the box around the level be drawn.
        :param draw_floor: Should the floor below the level be drawn.
        :param draw_ceil: Should the ceiling above the level be drawn.
        :param limit_bounds: Should the chunks be limited to the bounds of the level.
        """
        OpenGLResourcePackManager.__init__(self, opengl_resource_pack)
        ContextManager.__init__(self, context_identifier)
        self._level = level
        self._camera_location: CameraLocationType = (0, 150, 0)
        # yaw (-180 to 180), pitch (-90 to 90)
        self._camera_rotation: CameraRotationType = (0, 90)
        self._dimension: Dimension = level.dimensions[0]
        self._render_distance = 5
        self._garbage_distance = 10
        self._draw_box = draw_box
        self._draw_floor = draw_floor
        self._draw_ceil = draw_ceil
        self._limit_bounds = limit_bounds
        self._selection = None
        self._chunk_manager = ChunkManager(self.context_identifier, self.resource_pack)

        self._load_queue = ChunkLoadQueue(self._render_distance)

        self.geometry_budget_bytes = total_system_memory() // 4

        self._rebuild_time = 0.0
        self._rebuild_clock_lock = Lock()
        #: called from worker threads with chunk coords when a verify
        #: pass discovers the chunk data has changed (used by the
        #: overview scanner to keep tiles in sync).
        self.on_chunk_changed: Optional[Callable[[Tuple[int, int]], None]] = None

        self._detail_enabled = True
        #: chunk coords whose geometry is known stale while the detail
        #: layer is suppressed (zoomed out). Replayed as URGENT pushes
        #: when the detail layer is re-enabled.
        self._stale_geometry: Set[Tuple[int, int]] = set()
        self._stale_lock = Lock()

    @property
    def level(self) -> "BaseLevel":
        return self._level

    @property
    def chunk_manager(self) -> ChunkManager:
        return self._chunk_manager

    @property
    def detail_enabled(self) -> bool:
        """Should the full 3D chunk geometry be built and enqueued.

        When disabled (eg. zoomed far out in top-down view where the
        overview map carries all visible detail) the load queue is not
        fed new work and pending LOAD items are dropped by the worker
        threads, but VERIFY items are still processed so the overview
        stays in sync with edits; the geometry rebuilds they would have
        triggered are deferred until re-enabled.
        """
        return self._detail_enabled

    @detail_enabled.setter
    def detail_enabled(self, value: bool):
        value = bool(value)
        if value == self._detail_enabled:
            return
        self._detail_enabled = value
        if value:
            with self._stale_lock:
                stale = self._stale_geometry
                self._stale_geometry = set()
            for coords in stale:
                self._load_queue.push(coords, ChunkLoadQueue.PRIORITY_URGENT)
            self.enable()

    def is_closeable(self):
        return True

    def thread_action(self) -> bool:
        """Process one queued work item.
        Returns True if work was done, False if the queue was empty.
        Safe to call concurrently from multiple worker threads."""
        item = self._load_queue.pop()
        if item is None:
            self._try_region_merge()
            return False
        chunk_coords, priority = item
        if priority == ChunkLoadQueue.PRIORITY_VERIFY:
            if self.chunk_manager.render_chunk_needs_rebuild(chunk_coords):
                self._mark_stale_or_push(chunk_coords)
                for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbour = (
                        chunk_coords[0] + offset[0],
                        chunk_coords[1] + offset[1],
                    )
                    if neighbour in self.chunk_manager:
                        self._mark_stale_or_push(neighbour)
                on_changed = self.on_chunk_changed
                if on_changed is not None:
                    on_changed(chunk_coords)
            self._try_region_merge()
        elif not self._detail_enabled:
            if priority == ChunkLoadQueue.PRIORITY_URGENT:
                with self._stale_lock:
                    self._stale_geometry.add(chunk_coords)
            # PRIORITY_LOAD is simply dropped; re-enable reseeds it.
        else:
            chunk = RenderChunk(
                self.context_identifier,
                self.resource_pack,
                self.level,
                self.chunk_manager.region_size,
                chunk_coords,
                self.dimension,
                draw_floor=self.draw_floor,
                draw_ceil=self.draw_ceil,
                limit_bounds=self._limit_bounds,
            )
            try:
                chunk.create_geometry()
            except:
                log.error(
                    f"Failed generating chunk geometry for chunk {chunk_coords}",
                    exc_info=True,
                )
            self.chunk_manager.add_render_chunk(chunk)
            self._try_region_merge()
        return True

    def _mark_stale_or_push(self, chunk_coords: Tuple[int, int]):
        """Push an URGENT rebuild, or remember it for later if the detail
        layer is currently suppressed (avoids the queue just dropping it
        again on the next pop)."""
        if self._detail_enabled:
            self._load_queue.push(chunk_coords, ChunkLoadQueue.PRIORITY_URGENT)
        else:
            with self._stale_lock:
                self._stale_geometry.add(chunk_coords)

    def mark_chunk_stale(self, coords: Tuple[int, int]):
        """External notification that a chunk's data changed: rebuild the
        geometry of the chunk and its loaded neighbours now if detail is
        enabled, or when detail is next enabled.

        Only chunks that already have geometry are touched: a chunk without a
        render chunk (eg. edited far outside render distance) has no stale
        geometry to rebuild and will build fresh via a LOAD item when the
        camera next approaches it. This avoids building 3D geometry nobody can
        see."""
        if coords in self.chunk_manager:
            self._mark_stale_or_push(coords)
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbour = (coords[0] + offset[0], coords[1] + offset[1])
            if neighbour in self.chunk_manager:
                self._mark_stale_or_push(neighbour)

    def _try_region_merge(self):
        """At most once per second, and never concurrently, merge one
        region's chunk geometry into a single VBO-sized array."""
        if not self._rebuild_clock_lock.acquire(blocking=False):
            return  # another worker is already merging
        try:
            t = time.time()
            if t <= self._rebuild_time + 1:
                return
            self._rebuild_time = t
            self.chunk_manager.rebuild()
        finally:
            self._rebuild_clock_lock.release()

    def _enqueue_missing_chunks(self):
        """Push a LOAD item for every chunk in render distance that has
        no geometry and is not already queued. Cheap: set lookups only."""
        if not self._detail_enabled:
            return
        cx = math.floor(self.camera_location[0]) >> 4
        cz = math.floor(self.camera_location[2]) >> 4
        rd = self._render_distance
        queue = self._load_queue
        chunk_manager = self.chunk_manager
        for dx in range(-rd, rd + 1):
            for dz in range(-rd, rd + 1):
                coords = (cx + dx, cz + dz)
                if coords not in queue and coords not in chunk_manager:
                    queue.push(coords, ChunkLoadQueue.PRIORITY_LOAD)

    def enable(self):
        """Seed the load queue. Chunk building happens on the worker threads."""
        self._load_queue.set_camera_chunk(
            math.floor(self.camera_location[0]) >> 4,
            math.floor(self.camera_location[2]) >> 4,
        )
        self._enqueue_missing_chunks()

    def unload(self):
        """Unload all loaded data. Can be resumed by calling enable."""
        self.run_garbage_collector(True)

    def close(self):
        self.unload()

    @property
    def camera_location(self) -> CameraLocationType:
        """The x, y, z coordinates of the camera."""
        return self._camera_location

    @camera_location.setter
    def camera_location(self, value: CameraLocationType):
        old_chunk = (
            math.floor(self._camera_location[0]) >> 4,
            math.floor(self._camera_location[2]) >> 4,
        )
        self._camera_location = value
        new_chunk = (math.floor(value[0]) >> 4, math.floor(value[2]) >> 4)
        if new_chunk != old_chunk:
            self._load_queue.set_camera_chunk(*new_chunk)
            self._enqueue_missing_chunks()

    @property
    def camera_rotation(self) -> CameraRotationType:
        """The rotation of the camera. (yaw, pitch).
        This should behave the same as how Minecraft handles it.
        """
        return self._camera_rotation

    @camera_rotation.setter
    def camera_rotation(self, value: CameraRotationType):
        """Set the rotation of the camera. (yaw, pitch).
        This should behave the same as how Minecraft handles it.
        """
        self._camera_rotation = value

    @property
    def dimension(self) -> Dimension:
        """The dimension currently being displayed."""
        return self._dimension

    @dimension.setter
    def dimension(self, dimension: Dimension):
        self._dimension = dimension
        self._load_queue.clear()
        # Drop stale coords parked for the previous dimension: their coords
        # would otherwise replay as URGENT builds in the new dimension.
        with self._stale_lock:
            self._stale_geometry = set()
        self.run_garbage_collector(True)
        self.enable()

    @property
    def render_distance(self) -> int:
        """The radius around the camera within which to load chunks."""
        return self._render_distance

    @render_distance.setter
    def render_distance(self, val: int):
        assert isinstance(val, int), "Render distance must be an int"
        self._render_distance = val
        self._garbage_distance = val + 5
        self._load_queue.set_render_distance(val)
        self._enqueue_missing_chunks()

    @property
    def draw_box(self):
        """Should the selection box around the level be drawn."""
        return self._draw_box

    @property
    def draw_floor(self):
        """Should the floor under the level be drawn."""
        return self._draw_floor

    @property
    def draw_ceil(self):
        """Should the ceiling above the level be drawn."""
        return self._draw_ceil

    def draw(self, camera_matrix: TransformationMatrix, visible_rect=None):
        self._chunk_manager.draw(camera_matrix, self.camera_location, visible_rect)
        if self._draw_box:
            if self._selection is None:
                self._selection = GreenRenderSelectionGroup(
                    self.context_identifier,
                    self.resource_pack,
                    self.level.bounds(self.dimension),
                )
            self._selection.draw(
                camera_matrix,
                self.camera_location,
            )

    def run_garbage_collector(self, remove_all=False):
        if remove_all:
            self._chunk_manager.unload()
            self._level.unload()
        else:
            cx = math.floor(self.camera_location[0]) >> 4
            cz = math.floor(self.camera_location[2]) >> 4
            region_size = self._chunk_manager.region_size
            rd = self._render_distance
            protected = {
                (rx, rz)
                for rx in range((cx - rd) // region_size, (cx + rd) // region_size + 1)
                for rz in range((cz - rd) // region_size, (cz + rd) // region_size + 1)
            }
            self._chunk_manager.enforce_budget(self.geometry_budget_bytes, protected)
            # The level's own chunk-data cache is still trimmed by distance.
            # Render geometry no longer depends on it once built.
            self._level.unload(
                (
                    self._dimension,
                    cx - self._garbage_distance,
                    cz - self._garbage_distance,
                    cx + self._garbage_distance,
                    cz + self._garbage_distance,
                )
            )

    def rebuild_changed(self):
        """Schedule a verify pass over every loaded chunk.
        Chunks found changed get rebuilt at top priority."""
        for coords in self.chunk_manager.chunk_coords():
            self._load_queue.push(coords, ChunkLoadQueue.PRIORITY_VERIFY)
