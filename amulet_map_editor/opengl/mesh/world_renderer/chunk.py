import numpy
from typing import TYPE_CHECKING, Tuple, Dict
import weakref

import minecraft_model_reader
from amulet.api.errors import ChunkLoadError, ChunkDoesNotExist
from amulet_map_editor.opengl.mesh import new_empty_verts, TriMesh
from amulet_map_editor.opengl.mesh.base_chunk import BaseRenderChunk

if TYPE_CHECKING:
    from .world import RenderWorld
    from amulet.api.chunk import Chunk


class RenderChunk(BaseRenderChunk):
    def __init__(self, render_world: 'RenderWorld', region_size: int, chunk_coords: Tuple[int, int], dimension: int):
        # the chunk geometry is stored in chunk space (floating point)
        # at shader time it is transformed by the players transform
        super().__init__(render_world.identifier)
        self._render_world = weakref.ref(render_world)
        self._region_size = region_size
        self._coords = chunk_coords
        self._dimension = dimension
        self._chunk_state = 0  # 0 = chunk does not exist, 1 = chunk exists but failed to load, 2 = chunk exists
        self._changed_time = 0
        self._rebuild = True
        self.verts_translucent = 0  # the offset into the above from which the faces can be translucent
        # self.chunk_lod1: numpy.ndarray = new_empty_verts()

    def __repr__(self):
        return f'RenderChunk({self._coords[0]}, {self._coords[1]})'

    def _setup(self):
        """Set up the opengl data which cannot be set up in another thread"""
        super()._setup()
        if self._rebuild:
            self.change_verts()
            self._rebuild = False

    def _get_model(self, block_temp_id: int) -> minecraft_model_reader.MinecraftMesh:
        return self._render_world().get_model(block_temp_id)

    def _texture_bounds(self, texture):
        return self._render_world().get_texture_bounds(texture)

    @property
    def offset(self) -> numpy.ndarray:
        return 16 * (numpy.array([self._coords[0], 0, self._coords[1]]) % self._region_size)

    @property
    def dimension(self) -> int:
        return self._dimension

    @property
    def cx(self) -> int:
        return self._coords[0]

    @property
    def cz(self) -> int:
        return self._coords[1]

    @property
    def coords(self) -> Tuple[int, int]:
        return self._coords

    @property
    def chunk(self) -> "Chunk":
        return self._render_world().world.get_chunk(*self._coords, self._dimension)

    @property
    def chunk_state(self) -> int:
        return self._chunk_state

    def needs_rebuild(self):
        """has the chunk data changed since the last rebuild"""
        try:
            chunk = self.chunk
        except ChunkDoesNotExist:
            chunk_state = 0
        except ChunkLoadError:
            chunk_state = 1
        else:
            chunk_state = 2
            if chunk.changed_time != self._changed_time:
                return True
        return chunk_state != self._chunk_state

    def _fill_boundary_block_data(self, larger_blocks):
        for dx, dz in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            try:
                blocks_temp: numpy.ndarray = self._render_world().world.get_chunk(self.cx + dx, self.cz + dz).blocks
                if (dx, dz) == (-1, 0):
                    larger_blocks[0, 1:-1, 1:-1] = blocks_temp[-1, :, :]
                elif (dx, dz) == (1, 0):
                    larger_blocks[-1, 1:-1, 1:-1] = blocks_temp[0, :, :]
                elif (dx, dz) == (0, -1):
                    larger_blocks[1:-1, 1:-1, 0] = blocks_temp[:, :, -1]
                elif (dx, dz) == (0, 1):
                    larger_blocks[1:-1, 1:-1, -1] = blocks_temp[:, :, 0]

            except ChunkLoadError:
                continue
        return larger_blocks

    def create_geometry(self):
        try:
            chunk = self.chunk
        except ChunkDoesNotExist:
            self._create_empty_geometry()
            self._chunk_state = 0
        except ChunkLoadError:
            # log.info(f'Error loading chunk {chunk_coords}', exc_info=True)
            self._create_error_geometry()
            self._chunk_state = 1
        else:
            self._changed_time = chunk.changed_time
            self._chunk_state = 2
            blocks, larger_blocks, unique_blocks = self._get_block_data(chunk.blocks)
            self._create_lod0(blocks, larger_blocks, unique_blocks)
        self._rebuild = True

    def _create_empty_geometry(self):
        self.verts: numpy.ndarray = new_empty_verts()
        # self.chunk_lod1: numpy.ndarray = new_empty_verts()

    def _create_error_geometry(self):
        # TODO
        self.verts: numpy.ndarray = new_empty_verts()
        # self.chunk_lod1: numpy.ndarray = new_empty_verts()

    def _create_lod1(self, blocks: numpy.ndarray, larger_blocks: numpy.ndarray, unique_blocks: numpy.ndarray):
        # TODO
        self.verts: numpy.ndarray = new_empty_verts()
        # self.chunk_lod1: numpy.ndarray = new_empty_verts()
