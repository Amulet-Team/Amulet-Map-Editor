from typing import TYPE_CHECKING, Tuple
import weakref
import numpy

from amulet.api.structure import Structure
from amulet.api.chunk import Chunk
from amulet.api.block import BlockManager
from amulet_map_editor.opengl.mesh.base_chunk import BaseRenderChunk
import minecraft_model_reader

if TYPE_CHECKING:
    from amulet_map_editor.opengl.mesh.world_renderer.world import RenderWorld


class SubRenderStructure(BaseRenderChunk):
    def __init__(self, render_world: 'RenderWorld', structure_palette: BlockManager, chunk: Chunk, slices: Tuple[slice, slice, slice], offset: numpy.ndarray):
        super().__init__(render_world.identifier)
        self._render_world = weakref.ref(render_world)
        self._structure_palette = structure_palette
        self._chunk = weakref.ref(chunk)
        self._slices = slices
        self._offset = (offset + (s.start for s in slices)) + (chunk.cx*16, 0, chunk.cz*16)

    def create_geometry(self):
        blocks, larger_blocks, unique_blocks = self._get_block_data(self._chunk().blocks[self._slices])
        self._create_lod0(blocks, larger_blocks, unique_blocks)

    def _get_model(self, block_temp_id: int) -> minecraft_model_reader.MinecraftMesh:
        # The structure and world may have different block palettes so need to convert from one to the other
        block = self._structure_palette[block_temp_id]
        world_block_temp_id = self._render_world().palette.get_add_block(block)
        return self._render_world().get_model(world_block_temp_id)

    def _texture_bounds(self, texture):
        return self._render_world().get_texture_bounds(texture)

    @property
    def offset(self) -> numpy.ndarray:
        return self._offset


class RenderStructure:
    def __init__(self, render_world: 'RenderWorld', structure: Structure):
        self._render_world = weakref.ref(render_world)
        self._structure = structure
        self._sub_structures = []
        self._create_geometry()  # TODO: move this to a different thread

    def _create_geometry(self):
        offset = -self._structure.selection.min
        sections = []
        for chunk, slices in self._structure.get_chunk_slices():
            section = SubRenderStructure(self._render_world(), self._structure.palette, chunk, slices, offset)
            section.create_geometry()
            sections.append(section)
