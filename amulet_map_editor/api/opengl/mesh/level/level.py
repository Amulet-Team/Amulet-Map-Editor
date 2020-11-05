from typing import TYPE_CHECKING, Tuple, Generator, Optional, Any, Set
from concurrent.futures import ThreadPoolExecutor, Future
import time
import weakref
import numpy

from amulet.api.data_types import Dimension

from amulet_map_editor.api.logging import log
from .chunk import RenderChunk
from .region import ChunkManager
from .selection import GreenRenderSelectionGroup
from amulet_map_editor.api.opengl.data_types import (
    CameraLocationType,
    CameraRotationType,
    TransformationMatrix,
)
from amulet_map_editor.api.opengl.matrix import displacement_matrix
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePackManager,
    OpenGLResourcePack,
)
from amulet_map_editor.api.opengl.mesh.base.tri_mesh import Drawable, ContextManager

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel


class ChunkGenerator(ThreadPoolExecutor):
    def __init__(self, render_level: "RenderLevel"):
        super().__init__(max_workers=1)
        self._render_level_ = weakref.ref(render_level)
        self._region_size = render_level.chunk_manager.region_size
        self._enabled = False
        self._generator: Optional[Future] = None
        self._chunk_rebuilds: Set[Tuple[int, int]] = set()

    @property
    def _render_level(self) -> "RenderLevel":
        return self._render_level_()

    def start(self):
        if not self._enabled:
            self._enabled = True
            self._generator = self.submit(self._generate_chunks)

    def stop(self):
        if self._enabled:
            self._enabled = False
            self._generator.result()

    def _generate_chunks(self):
        while self._enabled:
            start_time = time.time()
            # first check if there is a chunk that exists and needs rebuilding
            chunk_coords = next(
                (
                    c
                    for c in self._render_level.chunk_coords()
                    if self._render_level.chunk_manager.render_chunk_needs_rebuild(c)
                ),
                None,
            )
            if chunk_coords is not None:
                # if there was a chunk found that needs rebuilding then add the surrounding chunks for rebuilding
                # (this deals with if the chunk was deleted or the blocks up to the chunk boundary were deleted)
                for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    chunk_coords_ = (
                        chunk_coords[0] + offset[0],
                        chunk_coords[1] + offset[1],
                    )
                    if chunk_coords_ in self._render_level.chunk_manager:
                        self._chunk_rebuilds.add(chunk_coords_)
            elif self._chunk_rebuilds:
                # if a chunk was not found that needs rebuilding due to it changing but a previously
                # identified neighbour chunk needs rebuilding do that.
                chunk_coords = self._chunk_rebuilds.pop()
            else:
                # if no chunks need rebuilding then find a new chunk to load.
                chunk_coords = next(
                    (
                        c
                        for c in self._render_level.chunk_coords()
                        if c not in self._render_level.chunk_manager
                    ),
                    None,
                )
            if chunk_coords is not None:
                # if chunk coords is in here then remove it so it doesn't get generated twice.
                if chunk_coords in self._chunk_rebuilds:
                    self._chunk_rebuilds.remove(chunk_coords)

                # generate the chunk
                chunk = RenderChunk(
                    self._render_level.context_identifier,
                    self._render_level.resource_pack,
                    self._render_level.level,
                    self._region_size,
                    chunk_coords,
                    self._render_level.dimension,
                    self._render_level.draw_floor,
                )

                try:
                    chunk.create_geometry()
                except:
                    log.error(
                        f"Failed generating chunk geometry for chunk {chunk_coords}",
                        exc_info=True,
                    )

                self._render_level.chunk_manager.add_render_chunk(chunk)
            delta_time = time.time() - start_time
            if delta_time < 1 / 60:
                # go to sleep so this thread doesn't lock up the main thread.
                time.sleep(1 / 60 - delta_time)


class RenderLevel(OpenGLResourcePackManager, Drawable, ContextManager):
    def __init__(
        self,
        context_identifier: Any,
        opengl_resource_pack: OpenGLResourcePack,
        level: "BaseLevel",
        draw_floor=True,
        draw_box=False,
    ):
        OpenGLResourcePackManager.__init__(self, opengl_resource_pack)
        ContextManager.__init__(self, context_identifier)
        self._level = level
        self._camera_location: CameraLocationType = (0, 150, 0)
        # yaw (-180 to 180), pitch (-90 to 90)
        self._camera_rotation: CameraRotationType = (0, 90)
        self._dimension: Dimension = "overworld"
        self._render_distance = 5
        self._garbage_distance = 10
        self._draw_box = draw_box
        self._draw_floor = draw_floor
        self._selection = GreenRenderSelectionGroup(
            context_identifier, self.resource_pack, self.level.selection_bounds
        )
        # self._selection_displacement = numpy.matmul(
        #     displacement_matrix(*(
        #         (
        #             self.level.selection_bounds.min
        #             + self.level.selection_bounds.max
        #         )
        #         / 2
        #     ).astype(int)),
        #     displacement_matrix(
        #         *(
        #                 (
        #                         self.level.selection_bounds.min
        #                         - self.level.selection_bounds.max
        #                 )
        #                 / 2
        #         ).astype(int)
        #     )
        # )
        self._selection_displacement = displacement_matrix(
            *(self.level.selection_bounds.min).astype(int)
        )
        self._chunk_manager = ChunkManager(self.context_identifier, self.resource_pack)
        self._chunk_generator = ChunkGenerator(self)

    @property
    def level(self) -> "BaseLevel":
        return self._level

    @property
    def chunk_manager(self) -> ChunkManager:
        return self._chunk_manager

    @property
    def chunk_generator(self) -> ChunkGenerator:
        return self._chunk_generator

    def is_closeable(self):
        return True

    def enable(self):
        self._chunk_generator.start()

    def disable(self):
        self._chunk_generator.stop()
        self.run_garbage_collector(True)

    def close(self):
        self.disable()

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
        self._chunk_generator.stop()
        self._dimension = dimension
        self.run_garbage_collector(True)
        self._chunk_generator.start()

    @property
    def render_distance(self) -> int:
        """The radius around the camera within which to load chunks."""
        return self._render_distance

    @render_distance.setter
    def render_distance(self, val: int):
        assert isinstance(val, int), "Render distance must be an int"
        self._render_distance = val
        self._garbage_distance = val + 5

    @property
    def draw_box(self):
        """Should the selection box around the level be drawn."""
        return self._draw_box

    @property
    def draw_floor(self):
        """Should the floor under the level be drawn."""
        return self._draw_floor

    def chunk_coords(self) -> Generator[Tuple[int, int], None, None]:
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
            self._selection.draw(
                numpy.matmul(camera_matrix, self._selection_displacement),
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
