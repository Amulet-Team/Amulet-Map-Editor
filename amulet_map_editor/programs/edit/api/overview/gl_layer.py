import logging
from typing import Dict, Optional, Tuple

import numpy
from OpenGL.GL import (
    GL_LINEAR,
    GL_LINEAR_MIPMAP_LINEAR,
    GL_RGBA,
    GL_TEXTURE_2D,
    GL_TEXTURE_MAG_FILTER,
    GL_TEXTURE_MIN_FILTER,
    GL_TEXTURE_WRAP_S,
    GL_TEXTURE_WRAP_T,
    GL_CLAMP_TO_EDGE,
    GL_UNSIGNED_BYTE,
    glBindTexture,
    glDeleteTextures,
    glDepthMask,
    glGenTextures,
    glGenerateMipmap,
    glTexImage2D,
    glTexParameteri,
    glTexSubImage2D,
    GL_FALSE,
    GL_TRUE,
)

from amulet_map_editor.api.opengl.mesh.tri_mesh import TriMesh
from .cache import TILE_PIXELS
from .scanner import OverviewScanner

log = logging.getLogger(__name__)

MAX_UPLOADS_PER_FRAME = 2
_TILE_BYTES = TILE_PIXELS * TILE_PIXELS * 4 * 4 // 3  # pixels + mipmaps


class OverviewTileMesh(TriMesh):
    """One 512x512-block textured quad using the render_chunk shader."""

    def __init__(self, context_identifier, resource_pack, tx, tz, min_y):
        super().__init__(context_identifier, resource_pack)
        self._pending_pixels: Optional[numpy.ndarray] = None
        self.last_drawn = 0
        x0, z0 = tx * TILE_PIXELS, tz * TILE_PIXELS
        x1, z1 = x0 + TILE_PIXELS, z0 + TILE_PIXELS
        u0, v0, u1, v1 = 0.0, 0.0, 0.9995, 0.9995
        y = min_y - 0.5
        corners = {
            "a": ((x0, y, z0), (u0, v0)),
            "b": ((x1, y, z0), (u1, v0)),
            "c": ((x1, y, z1), (u1, v1)),
            "d": ((x0, y, z1), (u0, v1)),
        }
        # both windings so GL_CULL_FACE cannot hide the quad
        order = ("a", "b", "c", "a", "c", "d", "a", "c", "b", "a", "d", "c")
        verts = numpy.zeros((12, 12), numpy.float32)
        for row, key in enumerate(order):
            position, uv = corners[key]
            verts[row, :3] = position
            verts[row, 3:5] = uv
        verts[:, 5:9] = (0.0, 0.0, 1.0, 1.0)  # sample the whole tile texture
        verts[:, 9:12] = 1.0 / 0.85  # cancel the shader's 0.85 darkening
        self.verts = verts.ravel()
        self.draw_count = 12

    def _setup(self):
        """Create the tile's own texture instead of the atlas texture."""
        if self._vao is None:
            texture = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texture)
            glTexParameteri(
                GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR
            )
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
            glTexImage2D(
                GL_TEXTURE_2D,
                0,
                GL_RGBA,
                TILE_PIXELS,
                TILE_PIXELS,
                0,
                GL_RGBA,
                GL_UNSIGNED_BYTE,
                numpy.zeros((TILE_PIXELS, TILE_PIXELS, 4), numpy.uint8),
            )
            glGenerateMipmap(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, 0)
            self._own_texture = texture
            super()._setup()
            # super()._setup set self._texture to the atlas; override it
            self._texture = texture

    def set_pixels(self, pixels: numpy.ndarray):
        """Store pixels to upload at the next draw (main thread does GL)."""
        self._pending_pixels = pixels

    @property
    def has_pending_pixels(self) -> bool:
        return self._pending_pixels is not None

    def upload_pending(self):
        """Upload pending pixel data. Main thread only, needs _setup done."""
        if self._pending_pixels is None:
            return
        self._setup()
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glTexSubImage2D(
            GL_TEXTURE_2D,
            0,
            0,
            0,
            TILE_PIXELS,
            TILE_PIXELS,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            numpy.ascontiguousarray(self._pending_pixels),
        )
        glGenerateMipmap(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, 0)
        self._pending_pixels = None

    def unload(self):
        super().unload()
        if getattr(self, "_own_texture", None) is not None:
            glDeleteTextures([self._own_texture])
            self._own_texture = None
            self._texture = None


class OverviewLayer:
    """Draws the scanner's tiles as flat textured quads. Main thread only."""

    def __init__(
        self,
        context_identifier: str,
        resource_pack,
        scanner: OverviewScanner,
        min_y: float,
    ):
        self._context_identifier = context_identifier
        self._resource_pack = resource_pack
        self._scanner = scanner
        self._min_y = min_y
        self._meshes: Dict[Tuple[int, int], OverviewTileMesh] = {}
        self._draw_counter = 0
        self.texture_budget_bytes = 512 * 2**20

    def set_min_y(self, min_y: float):
        self._min_y = min_y
        self.unload()

    def draw(self, camera_matrix, camera_location, half_extent_x, half_extent_z):
        self._draw_counter += 1
        # consume freshly scanned tiles
        for tx, tz, pixels in self._scanner.take_dirty_tiles():
            mesh = self._meshes.get((tx, tz))
            if mesh is not None:
                mesh.set_pixels(pixels)
        cam_x, _, cam_z = camera_location
        min_tx = int((cam_x - half_extent_x) // TILE_PIXELS)
        max_tx = int((cam_x + half_extent_x) // TILE_PIXELS)
        min_tz = int((cam_z - half_extent_z) // TILE_PIXELS)
        max_tz = int((cam_z + half_extent_z) // TILE_PIXELS)
        uploads = 0
        glDepthMask(GL_FALSE)
        try:
            for tx, tz in self._scanner.list_tiles():
                if not (min_tx <= tx <= max_tx and min_tz <= tz <= max_tz):
                    continue
                mesh = self._meshes.get((tx, tz))
                if mesh is None:
                    pixels = self._scanner.tile_pixels(tx, tz)
                    if pixels is None:
                        continue
                    mesh = OverviewTileMesh(
                        self._context_identifier,
                        self._resource_pack,
                        tx,
                        tz,
                        self._min_y,
                    )
                    mesh.set_pixels(pixels)
                    self._meshes[(tx, tz)] = mesh
                if mesh.has_pending_pixels and uploads < MAX_UPLOADS_PER_FRAME:
                    mesh.upload_pending()
                    uploads += 1
                mesh.last_drawn = self._draw_counter
                mesh.draw(camera_matrix)
        finally:
            glDepthMask(GL_TRUE)
        self._evict_over_budget()

    def _evict_over_budget(self):
        over = len(self._meshes) * _TILE_BYTES - self.texture_budget_bytes
        if over <= 0:
            return
        victims = sorted(self._meshes.items(), key=lambda kv: kv[1].last_drawn)
        while over > 0 and victims:
            coords, mesh = victims.pop(0)
            if mesh.last_drawn == self._draw_counter:
                break  # everything left was just drawn
            mesh.unload()
            del self._meshes[coords]
            over -= _TILE_BYTES

    def unload(self):
        for mesh in self._meshes.values():
            mesh.unload()
        self._meshes.clear()
