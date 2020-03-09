from OpenGL.GL import *
from typing import Dict, Tuple, List
import numpy
import queue
from .render_chunk import RenderChunk, new_empty_verts
from amulet_map_editor.opengl import shaders


class ChunkManager:
    def __init__(self, identifier: str, region_size=16):
        self.identifier = identifier
        self.region_size = region_size
        self._regions: Dict[Tuple[int, int], RenderRegion] = {}
        # added chunks are put in here and then processed on the next call of draw
        # This is because add_render_chunk can be called from a different thread to draw
        # which causes issues due to dictionaries resizing
        self._chunk_temp: queue.Queue = queue.Queue()
        self._chunk_temp_set = set()
        self.chunk_rebuilds = set()

    def add_render_chunk(self, render_chunk: RenderChunk):
        """Add a RenderChunk to the database.
        A call to _merge_chunk_temp from the main thread will be needed for them to be drawn.
        This is done after the next draw call."""
        self._chunk_temp.put(render_chunk)
        chunk_coords = (render_chunk.cx, render_chunk.cz)
        self._chunk_temp_set.add(chunk_coords)

    def render_chunk_needs_rebuild(self, chunk_coords: Tuple[int, int]) -> bool:
        return chunk_coords not in self._chunk_temp_set and self.render_chunk_in_main_database(chunk_coords) and self.get_render_chunk(chunk_coords).needs_rebuild()

    def get_render_chunk(self, chunk_coords: Tuple[int, int]) -> RenderChunk:
        """Get a RenderChunk from the database.
        Might throw a key error if it has not been added to the real database yet."""
        return self._regions[self.region_coords(*chunk_coords)].get_render_chunk(chunk_coords)

    def _merge_chunk_temp(self):
        for _ in range(self._chunk_temp.qsize()):
            render_chunk = self._chunk_temp.get()
            region_coords = self.region_coords(render_chunk.cx, render_chunk.cz)
            if region_coords not in self._regions:
                self._regions[region_coords] = RenderRegion(region_coords[0], region_coords[1], self.region_size, self.identifier)
            self._regions[region_coords].add_render_chunk(render_chunk)
        self._chunk_temp_set.clear()

    def __contains__(self, chunk_coords: Tuple[int, int]):
        return chunk_coords in self._chunk_temp_set or self.render_chunk_in_main_database(chunk_coords)

    def render_chunk_in_main_database(self, chunk_coords: Tuple[int, int]) -> bool:
        region_coords = self.region_coords(*chunk_coords)
        return region_coords in self._regions and chunk_coords in self._regions[region_coords]

    def region_coords(self, cx, cz):
        return cx // self.region_size, cz // self.region_size

    def draw(self, camera_transform, camera):
        cam_rx, cam_rz = numpy.floor(numpy.array(camera)[[0, 2]]/(16*self.region_size))
        cam_cx, cam_cz = numpy.floor(numpy.array(camera)[[0, 2]]/16)
        for region in sorted(self._regions.values(), key=lambda x: abs(x.rx-cam_rx) + abs(x.rz-cam_rz), reverse=True):
            region.draw(camera_transform, cam_cx, cam_cz)
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
                if min_rx <= region.rx <= max_rx and min_rz <= region.rz <= max_rz:
                    region.rebuild()
                else:
                    region.unload()
                    delete_regions.append((region.rx, region.rz))

            for region in delete_regions:
                del self._regions[region]

    def rebuild(self):
        """Force a rebuild of the region geometry from the chunk geometry
        Useful to force an update rather than wait for the next unload call."""
        for region in self._regions.values():
            region.rebuild()


class RenderRegion:
    def __init__(self, rx: int, rz: int, region_size: int, identifier: str):
        """A group of RenderChunks to minimise the number of draw calls"""
        self.identifier = identifier
        self.rx = rx
        self.rz = rz
        self._chunks: Dict[Tuple[int, int], RenderChunk] = {}
        self._merged_chunk_locations: Dict[Tuple[int, int], Tuple[int, int, int, int]] = {}
        self._manual_chunks: Dict[Tuple[int, int], RenderChunk] = {}
        self._shader = None
        self._trm_mat_loc = None
        self._vao = None
        self._vbo = None
        self._draw_count = 0

        self.region_transform = numpy.eye(4, dtype=numpy.float32)
        self.region_transform[3, [0, 2]] = numpy.array([rx, rz]) * region_size * 16

    def __repr__(self):
        return f'RenderRegion({self.rx}, {self.rz})'

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
            offset, size, translucent_offset, translucent_size = self._merged_chunk_locations.pop(chunk_coords)
            glBindVertexArray(self._vao)
            glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
            glBufferSubData(GL_ARRAY_BUFFER, offset*4, size*4, numpy.zeros(size, dtype=numpy.float32))
            glBufferSubData(GL_ARRAY_BUFFER, translucent_offset*4, translucent_size*4, numpy.zeros(translucent_size, dtype=numpy.float32))

    def _setup(self):
        """Set up an empty VAO"""
        if self._vao is None:
            self._vao = glGenVertexArrays(1)
            glBindVertexArray(self._vao)
            self._vbo = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
            glBufferData(GL_ARRAY_BUFFER, 0, new_empty_verts(), GL_DYNAMIC_DRAW)
            # vertex attribute pointers
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(0))
            glEnableVertexAttribArray(0)
            # texture coords attribute pointers
            glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(12))
            glEnableVertexAttribArray(1)
            # texture coords attribute pointers
            glVertexAttribPointer(2, 4, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(20))
            glEnableVertexAttribArray(2)
            # tint value
            glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(36))
            glEnableVertexAttribArray(3)

            glBindVertexArray(0)

            self._shader = shaders.get_shader(self.identifier, 'render_chunk')
            self._trm_mat_loc = glGetUniformLocation(self._shader, "transformation_matrix")

    def rebuild(self):
        """If there are any chunks that have not been merged recreate the merged vertex table"""
        self._setup()
        if self._manual_chunks and self._vao and self._vbo:
            glBindVertexArray(self._vao)
            glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
            chunks: List[Tuple[Tuple[int, int], RenderChunk]] = list(self._chunks.items())
            region_verts = []
            region_verts_translucent = []
            merged_locations: Dict[Tuple[int, int], Tuple[int, int, int, int]] = {}
            offset = 0
            translucent_offset = 0
            for chunk_location, chunk in chunks:
                region_verts.append(chunk.chunk_lod0[:chunk.chunk_lod0_translucent])
                region_verts_translucent.append(chunk.chunk_lod0[chunk.chunk_lod0_translucent:])
                merged_locations[chunk_location] = [
                    offset, chunk.chunk_lod0_translucent,
                    translucent_offset, chunk.chunk_lod0.size - chunk.chunk_lod0_translucent
                ]
                offset += chunk.chunk_lod0_translucent
                translucent_offset += chunk.chunk_lod0.size - chunk.chunk_lod0_translucent

            for val in merged_locations.values():
                val[2] += offset

            region_verts += region_verts_translucent

            if region_verts:
                verts = numpy.concatenate(region_verts)
            else:
                verts = new_empty_verts()
            self._draw_count = int(verts.size//10)
            self._merged_chunk_locations = merged_locations
            glBufferData(GL_ARRAY_BUFFER, verts.size * 4, verts, GL_DYNAMIC_DRAW)
            for chunk in self._manual_chunks.values():
                chunk.unload()
            self._manual_chunks.clear()

    def unload(self):
        """Unload all opengl data"""
        if self._vao is not None:
            glDeleteVertexArrays(1, self._vao)
            self._vao = None
        for chunk in self._chunks.values():
            chunk.unload()
        self._chunks.clear()

    def draw(self, transformation_matrix: numpy.ndarray, cam_cx, cam_cz):
        self._setup()
        if self._vao:
            glUseProgram(self._shader)
            transformation_matrix = numpy.matmul(self.region_transform, transformation_matrix)
            glUniformMatrix4fv(self._trm_mat_loc, 1, GL_FALSE, transformation_matrix)
            glBindVertexArray(self._vao)
            glDrawArrays(GL_TRIANGLES, 0, self._draw_count)
            for chunk in sorted(self._manual_chunks.values(), key=lambda x: abs(x.cx-cam_cx) + abs(x.cz-cam_cz), reverse=True):
                chunk.draw(transformation_matrix)
