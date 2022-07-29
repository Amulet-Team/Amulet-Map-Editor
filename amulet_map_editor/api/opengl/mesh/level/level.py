from typing import TYPE_CHECKING, Generator, Optional, Any
import numpy
import time
import logging

from amulet.api.data_types import Dimension, ChunkCoordinates

from .chunk import RenderChunk
from .region import ChunkManager
from .selection import GreenRenderSelectionGroup
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

        self._last_rebuild_camera_location: Optional[
            numpy.ndarray
        ] = None  # x, z camera location
        self._needs_rebuild = (
            True  # Should we go back to the beginning and re-find chunks to rebuild
        )
        self._chunk_rebuilds = self._rebuild_generator()
        self._rebuild_time = 0

    @property
    def level(self) -> "BaseLevel":
        return self._level

    @property
    def chunk_manager(self) -> ChunkManager:
        return self._chunk_manager

    def is_closeable(self):
        return True

    def _rebuild_generator(self) -> Generator[Optional[ChunkCoordinates], None, None]:
        """A generator of chunk coordinates to rebuild.
        This is an infinite length generator."""
        while True:
            if self._needs_rebuild:
                self._needs_rebuild = False
                # a set of chunks that are next to chunks that have changed but have not changed themselves
                chunk_rebuilt = set()
                chunk_not_loaded = []  # a list of chunks that have not been loaded

                for chunk_coords in self.chunk_coords():
                    # for all chunks within radius of the player
                    if self.chunk_manager.render_chunk_needs_rebuild(chunk_coords):
                        # if the render chunk exists and the state has changed
                        # rebuild that chunk
                        chunk_rebuilt.add(chunk_coords)
                        yield chunk_coords
                        for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            # for all surrounding chunks
                            chunk_coords_ = (
                                chunk_coords[0] + offset[0],
                                chunk_coords[1] + offset[1],
                            )
                            if (
                                chunk_coords_ not in chunk_rebuilt
                                and chunk_coords in self.chunk_manager
                                and not self.chunk_manager.render_chunk_needs_rebuild(
                                    chunk_coords_
                                )
                            ):
                                # if the chunk has not already been rebuilt and it exists
                                # yield it to be rebuilt
                                yield chunk_coords_
                                # store the coords so that it does not get rebuilt twice
                                chunk_rebuilt.add(
                                    chunk_coords_
                                )  # so that it doesn't get picked up again
                        # if the rebuild flag has been set go to the beginning
                        if self._needs_rebuild:
                            break
                    elif chunk_coords not in self.chunk_manager:
                        # if the chunk is not yet loaded, mark it for loading.
                        chunk_not_loaded.append(chunk_coords)
                # if the rebuild flag has been set go to the beginning
                if self._needs_rebuild:
                    continue
                for chunk_coords in chunk_not_loaded:
                    # if the rebuild flag has been set go to the beginning
                    if self._needs_rebuild:
                        break
                    yield chunk_coords
            else:
                yield None

    def thread_action(self):
        # first check if there is a chunk that exists and needs rebuilding
        camera = numpy.asarray(self.camera_location)[[0, 2]]
        if self._last_rebuild_camera_location is None or numpy.sum(
            (self._last_rebuild_camera_location - camera) ** 2
        ) > min(2048, self.render_distance * 16 - 8):
            # if the camera has moved more than 32 blocks set the rebuild flag
            self._needs_rebuild = True
            self._last_rebuild_camera_location = camera

        chunk_coords = next(self._chunk_rebuilds)
        if chunk_coords is not None:
            # generate the chunk
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

        t = time.time()
        if t > self._rebuild_time + 1:
            self._rebuild_time = t
            self.chunk_manager.rebuild()

    def enable(self):
        """Enable chunk generation in a new thread."""
        self._needs_rebuild = True

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
        self._camera_location = value

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
        self.run_garbage_collector(True)
        self._needs_rebuild = True

    @property
    def render_distance(self) -> int:
        """The radius around the camera within which to load chunks."""
        return self._render_distance

    @render_distance.setter
    def render_distance(self, val: int):
        assert isinstance(val, int), "Render distance must be an int"
        self._render_distance = val
        self._garbage_distance = val + 5
        self._needs_rebuild = True

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

    def chunk_coords(self) -> Generator[ChunkCoordinates, None, None]:
        """Get all of the chunks to draw/load"""
        # This yield chunk coordinates in a spiral around the camera
        # TODO: Perhaps redesign this to prioritise chunks in front of the camera
        cx, cz = int(self.camera_location[0]) >> 4, int(self.camera_location[2]) >> 4

        sign = 1
        length = 1
        for _ in range(self.render_distance * 2 + 1):
            for _ in range(length):
                yield cx, cz
                cx += sign
            for _ in range(length):
                yield cx, cz
                cz += sign
            sign *= -1
            length += 1

    def draw(self, camera_matrix: TransformationMatrix):
        self._chunk_manager.draw(camera_matrix, self.camera_location)
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
            safe_area = (
                self._dimension,
                int(self.camera_location[0] // 16 - self._garbage_distance),
                int(self.camera_location[2] // 16 - self._garbage_distance),
                int(self.camera_location[0] // 16 + self._garbage_distance),
                int(self.camera_location[2] // 16 + self._garbage_distance),
            )
            self._chunk_manager.unload(safe_area[1:])
            self._level.unload(safe_area)

    def _rebuild(self):
        """Unload all the chunks so they can be rebuilt."""
        self._chunk_manager.unload()
        self._needs_rebuild = True

    def rebuild_changed(self):
        """Rebuild the chunks that have changed."""
        self._needs_rebuild = True
