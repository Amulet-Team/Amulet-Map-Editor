from typing import Tuple, Any, Dict
import weakref
import numpy

import minecraft_model_reader
import PyMCTranslate

from amulet.api.structure import Structure
from amulet.api.chunk import Chunk
from amulet.api.block import BlockManager

from amulet_map_editor.opengl.mesh.base.chunk_builder import RenderChunkBuilder
from amulet_map_editor.opengl.resource_pack import ResourcePackManager
from amulet_map_editor.opengl.mesh.selection import RenderSelectionGroup


class SubRenderStructure(RenderChunkBuilder):
    def __init__(
        self,
        render_structure: 'RenderStructure',
        structure_palette: BlockManager,
        chunk: Chunk,
        slices: Tuple[slice, slice, slice],
        offset: numpy.ndarray,
        texture: int
    ):
        super().__init__(render_structure.context_identifier, texture)
        self._render_structure = weakref.ref(render_structure)
        self._structure_palette = structure_palette
        self._chunk = weakref.ref(chunk)
        self._cx = chunk.cx
        self._cz = chunk.cz
        self._slices = slices
        self._offset = (offset + tuple(s.start for s in slices)) + (chunk.cx*16, 0, chunk.cz*16)

    @property
    def cx(self):
        return self._cx

    @property
    def cz(self):
        return self._cz

    def create_geometry(self):
        larger_blocks, unique_blocks = self._get_block_data(self._chunk().blocks[self._slices])
        self._create_lod0(larger_blocks, unique_blocks)

    def _get_model(self, block_temp_id: int) -> minecraft_model_reader.MinecraftMesh:
        return self._render_structure().get_block_model(block_temp_id)

    def _texture_bounds(self, texture):
        return self._render_structure().get_texture_bounds(texture)

    @property
    def offset(self) -> numpy.ndarray:
        return self._offset


class RenderStructure(ResourcePackManager):
    def __init__(
        self,
        context_identifier: Any,
        structure: Structure,
        resource_pack: minecraft_model_reader.JavaRPHandler,
        texture: Any,
        texture_bounds: Dict[Any, Tuple[float, float, float, float]],
        translator: PyMCTranslate.Version
    ):
        super().__init__(context_identifier, resource_pack, texture, texture_bounds, translator)
        self._structure = structure
        self._sub_structures = []
        self._selection = RenderSelectionGroup(context_identifier, texture_bounds, texture, structure.selection)
        self._create_geometry()  # TODO: move this to a different thread

    @property
    def _palette(self) -> BlockManager:
        return self._structure.palette

    def _create_geometry(self):
        offset = -self._structure.selection.min
        sections = []
        for chunk, slices, _ in self._structure.get_chunk_slices():
            section = SubRenderStructure(self, self._structure.palette, chunk, slices, offset, self.texture)
            section.create_geometry()
            sections.append(section)
        self._sub_structures = sections

    def draw(self, transformation_matrix: numpy.ndarray, cam_cx, cam_cz):
        for chunk in sorted(
            self._sub_structures, key=lambda x: abs(x.cx - cam_cx) + abs(x.cz - cam_cz),
            reverse=True
        ):
            chunk.draw(transformation_matrix)
        self._selection.draw(transformation_matrix)
