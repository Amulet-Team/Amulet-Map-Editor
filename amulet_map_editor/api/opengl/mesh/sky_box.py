import numpy

from minecraft_model_reader.api.mesh.block.cube import get_cube

from .tri_mesh import TriMesh
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePackManager,
    OpenGLResourcePack,
)
from amulet_map_editor.api.opengl.data_types import CameraLocationType
from amulet_map_editor.api.opengl.matrix import displacement_matrix

Radius = 2000


class SkyBox(TriMesh, OpenGLResourcePackManager):
    """A class to define the logic to generate geometry from a block array"""

    def __init__(self, context_identifier: str, resource_pack: OpenGLResourcePack):
        TriMesh.__init__(self, context_identifier, resource_pack)
        OpenGLResourcePackManager.__init__(self, resource_pack)
        self._camera_location: CameraLocationType = (0, 0, 0)
        self._rebuild()

    def _rebuild(self):
        model = get_cube(
            self.resource_pack.get_texture_path("amulet", "amulet_ui/cubemap/down"),
            self.resource_pack.get_texture_path("amulet", "amulet_ui/cubemap/up"),
            self.resource_pack.get_texture_path("amulet", "amulet_ui/cubemap/north"),
            self.resource_pack.get_texture_path("amulet", "amulet_ui/cubemap/west"),
            self.resource_pack.get_texture_path("amulet", "amulet_ui/cubemap/south"),
            self.resource_pack.get_texture_path("amulet", "amulet_ui/cubemap/east"),
            bounds=((Radius, -Radius), (-Radius, Radius), (-Radius, Radius)),
            do_not_cull=(True,) * 6,
        )

        verts = model.verts[None].reshape((-1, 3))
        tverts = model.texture_coords[None].reshape((-1, 2))
        faces = model.faces[None]

        # each slice in the first axis is a new block, each slice in the second is a new vertex
        vert_table = numpy.zeros((faces.size, self._vert_len), dtype=numpy.float32)
        vert_table[:, :3] = verts[faces]
        vert_table[:, 3:5] = tverts[faces]

        vert_index = 0
        for texture_index in model.texture_index[None]:
            tex_bounds = self.resource_pack.texture_bounds(
                model.textures[texture_index]
            )

            vert_table[vert_index : vert_index + 3, 5:9] = tex_bounds
            vert_index += 3

        vert_table[:, 9:12] = model.tint_verts[None].reshape((-1, 3))[faces]
        self.verts = numpy.ravel(vert_table)
        self.draw_count = int(self.verts.size // self._vert_len)

    def set_camera_location(self, camera_location: CameraLocationType):
        self._camera_location = (numpy.asarray(camera_location)).tolist()

    def draw(self, transformation_matrix: numpy.ndarray):
        super().draw(
            numpy.matmul(
                transformation_matrix, displacement_matrix(*self._camera_location)
            )
        )
