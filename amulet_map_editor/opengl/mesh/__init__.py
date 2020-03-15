import numpy


def new_empty_verts() -> numpy.ndarray:
    return numpy.zeros(0, dtype=numpy.float32)


from amulet_map_editor.opengl.mesh.base.tri_mesh import TriMesh
