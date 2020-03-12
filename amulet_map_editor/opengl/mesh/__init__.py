import numpy


def new_empty_verts() -> numpy.ndarray:
    return numpy.zeros(0, dtype=numpy.float32)


from .tri_mesh import TriMesh
