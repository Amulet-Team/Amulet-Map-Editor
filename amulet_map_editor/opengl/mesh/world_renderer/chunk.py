import numpy
from typing import TYPE_CHECKING, Tuple, List, Union
import weakref
import itertools

import minecraft_model_reader
from amulet.api.errors import ChunkLoadError, ChunkDoesNotExist
from amulet.api.chunk.blocks import Blocks

from amulet_map_editor.opengl.mesh import new_empty_verts
from amulet_map_editor.opengl.mesh.base.chunk_builder import RenderChunkBuilder

if TYPE_CHECKING:
    from .world import RenderWorld
    from amulet.api.chunk import Chunk


class RenderChunk(RenderChunkBuilder):
    def __init__(self, render_world: 'RenderWorld', region_size: int, chunk_coords: Tuple[int, int], dimension: int):
        # the chunk geometry is stored in chunk space (floating point)
        # at shader time it is transformed by the players transform
        super().__init__(render_world.context_identifier)
        self._render_world_ = weakref.ref(render_world)
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

    @property
    def _render_world(self) -> 'RenderWorld':
        return self._render_world_()

    def _get_model(self, block_temp_id: int) -> minecraft_model_reader.MinecraftMesh:
        return self._render_world.get_block_model(block_temp_id)

    def _texture_bounds(self, texture):
        return self._render_world.get_texture_bounds(texture)

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
        return self._render_world.world.get_chunk(*self._coords, self._dimension)

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

    def _sub_chunks(self, blocks: Blocks) -> List[Tuple[numpy.ndarray, numpy.ndarray, Tuple[int, int, int]]]:
        sub_chunks = []
        neighbour_chunks = {}
        for dx, dz in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            try:
                neighbour_chunks[(dx, dz)] = self._render_world.world.get_chunk(self.cx + dx, self.cz + dz, self.dimension).blocks
            except ChunkLoadError:
                continue

        for cy in blocks.sub_chunks:
            sub_chunk = blocks.get_sub_chunk(cy)
            larger_blocks = numpy.zeros(sub_chunk.shape + numpy.array((2, 2, 2)), sub_chunk.dtype)
            larger_blocks[1:-1, 1:-1, 1:-1] = sub_chunk
            for chunk_offset, neighbour_blocks in neighbour_chunks.items():
                if cy not in neighbour_blocks:
                    continue
                if chunk_offset == (-1, 0):
                    larger_blocks[0, 1:-1, 1:-1] = neighbour_blocks.get_sub_chunk(cy)[-1, :, :]
                elif chunk_offset == (1, 0):
                    larger_blocks[-1, 1:-1, 1:-1] = neighbour_blocks.get_sub_chunk(cy)[0, :, :]
                elif chunk_offset == (0, -1):
                    larger_blocks[1:-1, 1:-1, 0] = neighbour_blocks.get_sub_chunk(cy)[:, :, -1]
                elif chunk_offset == (0, 1):
                    larger_blocks[1:-1, 1:-1, -1] = neighbour_blocks.get_sub_chunk(cy)[:, :, 0]
            if cy - 1 in blocks:
                larger_blocks[1:-1, 0, 1:-1] = blocks.get_sub_chunk(cy-1)[:, -1, :]
            if cy + 1 in blocks:
                larger_blocks[1:-1, -1, 1:-1] = blocks.get_sub_chunk(cy+1)[:, 0, :]
            unique_blocks = numpy.unique(larger_blocks)
            sub_chunks.append((larger_blocks, unique_blocks, (0, cy*16, 0)))
        return sub_chunks

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
            self._create_lod0_multi(self._sub_chunks(chunk.blocks))
            plane: numpy.ndarray = numpy.ones((self._vert_len*12), dtype=numpy.float32).reshape((-1, self._vert_len))
            plane[:, :3], plane[:, 3:5] = self._create_chunk_plane(-0.01)
            plane[:, 5:9] = self._texture_bounds(('amulet', 'ui/translucent_white'))
            if (self.cx+self.cz) % 2:
                plane[:, 9:12] = [0.55, 0.5, 0.9]
            else:
                plane[:, 9:12] = [0.4, 0.4, 0.85]
            self.verts = numpy.concatenate([self.verts, plane.ravel()], 0)
            self.draw_count += 12
        self._rebuild = True

    def _create_empty_geometry(self):
        plane: numpy.ndarray = numpy.ones((self._vert_len * 12), dtype=numpy.float32).reshape((-1, self._vert_len))
        plane[:, :3], plane[:, 3:5] = self._create_chunk_plane(0)
        plane[:, 5:9] = self._texture_bounds(('amulet', 'ui/translucent_white'))
        if (self.cx + self.cz) % 2:
            plane[:, 9:12] = [0.3, 0.3, 0.3]
        else:
            plane[:, 9:12] = [0.2, 0.2, 0.2]
        self.verts = plane.ravel()
        self.draw_count = 12

    def _create_chunk_plane(self, height: Union[int, float]) -> Tuple[numpy.ndarray, numpy.ndarray]:
        box = numpy.array([(0, height, 0), (16, height, 16)]) + self.offset
        _box_coordinates = numpy.array(
            list(
                itertools.product(
                    *box.T.tolist()
                )
            )
        )
        _cube_face_lut = numpy.array([  # This maps to the verticies used (defined in cube_vert_lut)
            0, 4, 5, 1,
            3, 7, 6, 2
        ])
        box = box.ravel()
        _texture_index = numpy.array([
            0, 2, 3, 5,
            0, 2, 3, 5
        ], numpy.uint32)
        _uv_slice = numpy.array([0, 1, 2, 1, 2, 3, 0, 3] * 2, dtype=numpy.uint32).reshape((-1, 8)) + numpy.arange(0, 8, 4).reshape((-1, 1))

        _tri_face = numpy.array([0, 1, 2, 0, 2, 3] * 2, numpy.uint32).reshape((-1, 6)) + numpy.arange(0, 8, 4).reshape((-1, 1))
        return _box_coordinates[_cube_face_lut[_tri_face]].reshape((-1, 3)), box[_texture_index[_uv_slice]].reshape(-1, 2)[_tri_face, :].reshape((-1, 2))

    def _create_error_geometry(self):
        plane: numpy.ndarray = numpy.ones((self._vert_len*12), dtype=numpy.float32).reshape((-1, self._vert_len))
        plane[:, :3], plane[:, 3:5] = self._create_chunk_plane(0)
        plane[:, 5:9] = self._texture_bounds(('amulet', 'ui/translucent_white'))
        if (self.cx + self.cz) % 2:
            plane[:, 9:12] = [1, 0.2, 0.2]
        else:
            plane[:, 9:12] = [0.75, 0.2, 0.2]
        self.verts = plane.ravel()
        self.draw_count = 12

    def _create_lod1(self, blocks: numpy.ndarray, larger_blocks: numpy.ndarray, unique_blocks: numpy.ndarray):
        # TODO
        self.verts: numpy.ndarray = new_empty_verts()
        # self.chunk_lod1: numpy.ndarray = new_empty_verts()
