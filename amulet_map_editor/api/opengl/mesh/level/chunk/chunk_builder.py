import numpy
from typing import Tuple, List

from amulet.api.chunk import Chunk

from amulet_map_editor.api.opengl.mesh import TriMesh
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePackManagerStatic,
    OpenGLResourcePack,
)


try:
    from .chunk_builder_cy import create_lod0_chunk
except:
    raise Exception(
        "Could not import cython chunk mesher. The cython code must be compiled first."
    )


class RenderChunkBuilder(TriMesh, OpenGLResourcePackManagerStatic):
    """A class to define the logic to generate geometry from a block array"""

    def __init__(self, context_identifier: str, resource_pack: OpenGLResourcePack):
        texture = resource_pack.get_atlas_id(context_identifier)
        TriMesh.__init__(self, context_identifier, texture)
        OpenGLResourcePackManagerStatic.__init__(self, resource_pack)

    @property
    def chunk(self) -> Chunk:
        raise NotImplementedError

    @property
    def offset(self) -> numpy.ndarray:
        raise NotImplementedError

    @staticmethod
    def _get_block_data(blocks: numpy.ndarray) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Given a Chunk object will return the chunk arrays needed to generate geometry
        :returns: block array of the chunk, block array one block larger than the chunk, array of unique blocks"""
        larger_blocks = numpy.zeros(blocks.shape + numpy.array((2, 2, 2)), blocks.dtype)
        larger_blocks[1:-1, 1:-1, 1:-1] = blocks
        unique_blocks = numpy.unique(larger_blocks)
        return larger_blocks, unique_blocks

    def create_geometry(self):
        raise NotImplementedError

    def _set_verts(
        self,
        chunk_verts: List[numpy.ndarray],
        chunk_verts_translucent: List[numpy.ndarray],
    ):
        if chunk_verts:
            self.verts = numpy.concatenate(chunk_verts, None)
            self.verts_translucent = self.verts.size
        else:
            self.verts = self.new_empty_verts()

        if chunk_verts_translucent:
            chunk_verts_translucent.insert(0, self.verts)
            self.verts = numpy.concatenate(chunk_verts_translucent, None)

        self.draw_count = int(self.verts.size // self._vert_len)

    def _create_lod0_multi(
        self, blocks: List[Tuple[numpy.ndarray, int]]
    ) -> Tuple[List[numpy.ndarray], List[numpy.ndarray]]:
        """Create LOD0 geometry data for every sub-chunk in a given chunk.

        :param blocks: A list of tuples containing block arrays extending one block outside the sub-chunk in each direction.
        :return: Opaque block vertices, translucent block vertices.
        """
        return create_lod0_chunk(
            self.resource_pack,
            self.offset,
            blocks,
            self.chunk.block_palette,
            self._vert_len,
        )
