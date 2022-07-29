from OpenGL.GL import (
    GL_DYNAMIC_DRAW,
    glBindVertexArray,
    glBindBuffer,
    GL_ARRAY_BUFFER,
    glBufferSubData,
)
from typing import Dict, Tuple, Optional
import numpy
import queue
from .chunk import RenderChunk
from amulet_map_editor.api.opengl.mesh.tri_mesh import TriMesh
from amulet_map_editor.api.opengl.resource_pack import OpenGLResourcePack
from amulet_map_editor.api.opengl.matrix import displacement_matrix
from amulet_map_editor.api.opengl.data_types import TransformationMatrix


class ChunkManager:
    def __init__(
        self, context_identifier: str, resource_pack: OpenGLResourcePack, region_size=16
    ):
        self.context_identifier = context_identifier
        self._resource_pack = resource_pack
        self.region_size = region_size
        self._regions: Dict[Tuple[int, int], RenderRegion] = {}
        # added chunks are put in here and then processed on the next call of draw
        # This is because add_render_chunk can be called from a different thread to draw
        # which causes issues due to dictionaries resizing
        self._chunk_temp: queue.Queue = queue.Queue()
        self._chunk_temp_set = set()
        self._rebuild_regions = []

    def add_render_chunk(self, render_chunk: RenderChunk):
        """Add a RenderChunk to the database.
        A call to _merge_chunk_temp from the main thread will be needed for them to be drawn.
        This is done after the next draw call."""
        self._chunk_temp.put(render_chunk)
        chunk_coords = (render_chunk.cx, render_chunk.cz)
        self._chunk_temp_set.add(chunk_coords)

    def render_chunk_needs_rebuild(self, chunk_coords: Tuple[int, int]) -> bool:
        return (
            chunk_coords not in self._chunk_temp_set
            and self.render_chunk_in_main_database(chunk_coords)
            and self.get_render_chunk(chunk_coords).needs_rebuild()
        )

    def get_render_chunk(self, chunk_coords: Tuple[int, int]) -> RenderChunk:
        """Get a RenderChunk from the database.
        Might throw a key error if it has not been added to the real database yet."""
        return self._regions[self.region_coords(*chunk_coords)].get_render_chunk(
            chunk_coords
        )

    def _merge_chunk_temp(self):
        for _ in range(self._chunk_temp.qsize()):
            render_chunk = self._chunk_temp.get()
            region_coords = self.region_coords(render_chunk.cx, render_chunk.cz)
            if region_coords not in self._regions:
                self._regions[region_coords] = RenderRegion(
                    region_coords[0],
                    region_coords[1],
                    self.region_size,
                    self.context_identifier,
                    self._resource_pack,
                )
            self._regions[region_coords].add_render_chunk(render_chunk)
        self._chunk_temp_set.clear()

    def __contains__(self, chunk_coords: Tuple[int, int]):
        return (
            chunk_coords in self._chunk_temp_set
            or self.render_chunk_in_main_database(chunk_coords)
        )

    def render_chunk_in_main_database(self, chunk_coords: Tuple[int, int]) -> bool:
        region_coords = self.region_coords(*chunk_coords)
        return (
            region_coords in self._regions
            and chunk_coords in self._regions[region_coords]
        )

    def region_coords(self, cx, cz):
        return cx // self.region_size, cz // self.region_size

    def draw(self, camera_matrix: TransformationMatrix, camera):
        cam_rx, cam_rz = numpy.floor(
            numpy.array(camera)[[0, 2]] / (16 * self.region_size)
        )
        cam_cx, cam_cz = numpy.floor(numpy.array(camera)[[0, 2]] / 16)
        for region in sorted(
            self._regions.values(),
            key=lambda x: abs(x.rx - cam_rx) + abs(x.rz - cam_rz),
            reverse=True,
        ):
            region.draw(camera_matrix, cam_cx, cam_cz)
        self._merge_chunk_temp()

    def unload(self, safe_area: Tuple[int, int, int, int] = None):
        if safe_area is None:
            for _ in range(self._chunk_temp.qsize()):
                self._chunk_temp.get()
            self._chunk_temp_set.clear()
            for region in self._regions.values():
                region.unload()
            self._regions.clear()
        else:
            min_rx, min_rz = self.region_coords(*safe_area[:2])
            max_rx, max_rz = self.region_coords(*safe_area[2:])
            delete_regions = []
            for region in self._regions.values():
                if not (
                    min_rx <= region.rx <= max_rx and min_rz <= region.rz <= max_rz
                ):
                    region.unload()
                    delete_regions.append((region.rx, region.rz))

            for region in delete_regions:
                del self._regions[region]

    def rebuild(self):
        """Rebuild a single region which was last rebuild the longest ago.
        Put this on a semi-fast clock to rebuild all regions."""
        if not self._rebuild_regions:
            self._rebuild_regions = list(self._regions.keys())

        if self._rebuild_regions:
            region = self._rebuild_regions.pop(0)
            if region in self._regions:
                self._regions[region].rebuild()


MergedChunkLocationsType = Dict[Tuple[int, int], Tuple[int, int, int, int]]


class RenderRegion(TriMesh):
    _merged_chunk_locations: MergedChunkLocationsType
    _temp_data: Optional[Tuple[numpy.ndarray, MergedChunkLocationsType]]

    def __init__(
        self,
        rx: int,
        rz: int,
        region_size: int,
        context_identifier: str,
        resource_pack: OpenGLResourcePack,
    ):
        """A group of RenderChunks to minimise the number of draw calls"""
        super().__init__(context_identifier, resource_pack)
        self.rx = rx
        self.rz = rz
        self._chunks: Dict[Tuple[int, int], RenderChunk] = {}
        self._merged_chunk_locations: MergedChunkLocationsType = {}
        self._manual_chunks: Dict[Tuple[int, int], RenderChunk] = {}

        # Merging is done on a new thread which can't modify the opengl state.
        # This stores the created data and the main thread loads it when drawing.
        self._temp_data = None

        self.region_transform = displacement_matrix(
            rx * region_size * 16, 0, rz * region_size * 16
        )

    @property
    def vertex_usage(self):
        return GL_DYNAMIC_DRAW

    def __repr__(self):
        return f"RenderRegion({self.rx}, {self.rz})"

    def __contains__(self, item):
        return item in self._chunks

    def add_render_chunk(self, render_chunk: RenderChunk):
        """Add a chunk to the region"""
        chunk_coords = (render_chunk.cx, render_chunk.cz)
        if chunk_coords in self._chunks:
            self._chunks[chunk_coords].unload()
        self._disable_merged_chunk(chunk_coords)
        self._chunks[chunk_coords] = render_chunk
        self._manual_chunks[chunk_coords] = render_chunk

    def get_render_chunk(self, chunk_coords: Tuple[int, int]):
        return self._chunks[chunk_coords]

    def _disable_merged_chunk(self, chunk_coords: Tuple[int, int]):
        """Zero out the region of memory in the merged chunks related to a given chunk"""
        if chunk_coords in self._merged_chunk_locations:
            (
                offset,
                size,
                translucent_offset,
                translucent_size,
            ) = self._merged_chunk_locations.pop(chunk_coords)
            glBindVertexArray(self._vao)
            glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
            glBufferSubData(
                GL_ARRAY_BUFFER,
                offset * 4,
                size * 4,
                numpy.zeros(size, dtype=numpy.float32),
            )
            glBufferSubData(
                GL_ARRAY_BUFFER,
                translucent_offset * 4,
                translucent_size * 4,
                numpy.zeros(translucent_size, dtype=numpy.float32),
            )
            glBindVertexArray(0)
            glBindBuffer(GL_ARRAY_BUFFER, 0)

    def rebuild(self):
        """Merges chunk geometry for the region into one large array.
        As each chunk is added it is drawn individually.
        After not too long the individual draw calls for each chunk will reach the bottleneck for python.
        To solve this we take the geometry for each chunk and merge them into one large array that only requires one draw call.

        :return:
        """
        if self._manual_chunks:
            region_verts = []
            region_verts_translucent = []
            merged_locations: MergedChunkLocationsType = {}
            offset = 0
            translucent_offset = 0
            for chunk_location, chunk in self._chunks.items():
                region_verts.append(chunk.verts[: chunk.verts_translucent])
                region_verts_translucent.append(chunk.verts[chunk.verts_translucent :])
                merged_locations[chunk_location] = [
                    offset,
                    chunk.verts_translucent,
                    translucent_offset,
                    chunk.verts.size - chunk.verts_translucent,
                ]
                offset += chunk.verts_translucent
                translucent_offset += chunk.verts.size - chunk.verts_translucent

            for val in merged_locations.values():
                val[2] += offset

            region_verts += region_verts_translucent

            if region_verts:
                verts = numpy.concatenate(region_verts)
            else:
                verts = self.new_empty_verts()
            self._temp_data = verts, merged_locations

    def _create_geometry(self):
        """Load the temporary vertex data into opengl."""
        if self._temp_data is not None:
            self._setup()
            verts, merged_locations = self._temp_data
            self._temp_data = None
            self.draw_count = int(verts.size // self._vert_len)
            self._merged_chunk_locations = merged_locations

            self.change_verts(verts)
            for coord in merged_locations:
                chunk = self._manual_chunks.pop(coord, None)
                if chunk is not None:
                    chunk.unload()

    def unload(self):
        """Unload all opengl data"""
        super().unload()
        for chunk in self._chunks.values():
            chunk.unload()
        self._chunks.clear()

    def draw(self, camera_matrix: TransformationMatrix, cam_cx, cam_cz):
        self._create_geometry()
        transformation_matrix = numpy.matmul(camera_matrix, self.region_transform)
        super().draw(transformation_matrix)
        for chunk in sorted(
            self._manual_chunks.values(),
            key=lambda x: abs(x.cx - cam_cx) + abs(x.cz - cam_cz),
            reverse=True,
        ):
            chunk.draw(transformation_matrix)
