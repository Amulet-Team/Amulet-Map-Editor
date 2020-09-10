from typing import Tuple, Any
import weakref
import numpy

from amulet.api.structure import Structure
from amulet.api.chunk import Chunk

from amulet_map_editor.api.opengl.mesh.base.chunk_builder import RenderChunkBuilder
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePackManager,
    OpenGLResourcePack,
)
from amulet_map_editor.api.opengl.mesh.selection import (
    RenderSelectionGroup,
    RenderSelection,
)
from amulet_map_editor.api.opengl.mesh.base.tri_mesh import Drawable, ContextManager
from amulet_map_editor.api.opengl.matrix import displacement_matrix


class GreenRenderSelection(RenderSelection):
    @property
    def box_tint(self) -> Tuple[float, float, float]:
        return 0.7, 1.0, 0.7


class GreenRenderSelectionGroup(RenderSelectionGroup):
    def _new_render_selection(self):
        return GreenRenderSelection(self._context_identifier, self.resource_pack)


class RenderStructureChunk(RenderChunkBuilder):
    """A class to create geometry for a chunk in the structure and render it."""

    def __init__(
        self,
        context_identifier: str,
        resource_pack: OpenGLResourcePack,
        chunk: Chunk,
        slices: Tuple[slice, slice, slice],
        offset: numpy.ndarray,
    ):
        super().__init__(context_identifier, resource_pack)
        self._chunk = weakref.ref(chunk)
        self._cx = chunk.cx
        self._cz = chunk.cz
        self._slices = slices
        self._offset = (offset + tuple(s.start for s in slices)) + (
            chunk.cx * 16,
            0,
            chunk.cz * 16,
        )

    @property
    def chunk(self) -> Chunk:
        return self._chunk()

    @property
    def cx(self):
        return self._cx

    @property
    def cz(self):
        return self._cz

    def create_geometry(self):
        larger_blocks, unique_blocks = self._get_block_data(
            self._chunk().blocks[self._slices]
        )
        self._create_lod0(larger_blocks, unique_blocks)

    @property
    def offset(self) -> numpy.ndarray:
        return self._offset


class RenderStructure(OpenGLResourcePackManager, Drawable, ContextManager):
    """A class to create geometry for a Structure and render it."""

    def __init__(
        self,
        context_identifier: Any,
        resource_pack: OpenGLResourcePack,
        structure: Structure,
    ):
        OpenGLResourcePackManager.__init__(self, resource_pack)
        ContextManager.__init__(self, context_identifier)
        self._structure = structure
        self._sub_structures = []
        self._selection = GreenRenderSelectionGroup(
            context_identifier, self.resource_pack, structure.selection
        )
        self._selection_transform = displacement_matrix(
            *(
                (self._structure.selection.min - self._structure.selection.max) / 2
            ).astype(int)
        )
        self._create_geometry()  # TODO: move this to a different thread

    def _create_geometry(self):
        offset = -numpy.floor(
            (self._structure.selection.min + self._structure.selection.max) / 2
        ).astype(int)
        sections = []
        for chunk, slices, _ in self._structure.get_chunk_slices():
            section = RenderStructureChunk(
                self.context_identifier, self.resource_pack, chunk, slices, offset
            )
            section.create_geometry()
            sections.append(section)
        self._sub_structures = sections

    def draw(self, camera_matrix: numpy.ndarray, cam_cx, cam_cz):
        for chunk in sorted(
            self._sub_structures,
            key=lambda x: abs(x.cx - cam_cx) + abs(x.cz - cam_cz),
            reverse=True,
        ):
            chunk.draw(camera_matrix)
        self._selection.draw(numpy.matmul(self._selection_transform, camera_matrix))
