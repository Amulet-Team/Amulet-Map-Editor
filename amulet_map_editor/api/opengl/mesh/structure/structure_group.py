from typing import List, Optional, Tuple, Any
import numpy

from amulet.api.structure import Structure
from amulet.api.data_types import FloatTriplet, PointCoordinates

from .structure import RenderStructure
from amulet_map_editor.api.opengl.mesh.base.tri_mesh import Drawable, ContextManager
from amulet_map_editor.api.opengl.matrix import transform_matrix
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePackManager,
    OpenGLResourcePack,
)

LocationType = PointCoordinates
ScaleType = FloatTriplet
RotationType = FloatTriplet
TransformType = Tuple[LocationType, ScaleType, RotationType]


class StructureGroup(OpenGLResourcePackManager, Drawable, ContextManager):
    """A group of RenderStructure classes with transforms"""

    def __init__(
        self, context_identifier: Any, resource_pack: OpenGLResourcePack,
    ):
        OpenGLResourcePackManager.__init__(self, resource_pack)
        ContextManager.__init__(self, context_identifier)
        self._structures: List[RenderStructure] = []
        self._transforms: List[TransformType] = []
        self._transformation_matrices: List[numpy.ndarray] = []
        self._active_structure: Optional[int] = None

    @property
    def active_structure(self) -> Optional[int]:
        """The index of the active structure. None if no structure is active."""
        return self._active_structure

    @property
    def active_transform(self) -> TransformType:
        if self._active_structure is None:
            return (0, 0, 0), (0, 0, 0), (0, 0, 0)
        return self._transforms[self._active_structure]

    def append(
        self,
        structure: Structure,
        location: LocationType,
        scale: ScaleType,
        rotation: RotationType,
    ):
        """Append a structure to the list and activate it."""
        # TODO: update this to support multiple structures
        self.clear()
        self._structures.append(
            RenderStructure(self.context_identifier, self._resource_pack, structure)
        )
        self._transforms.append((location, scale, rotation))
        self._transformation_matrices.append(
            transform_matrix(location, scale, rotation)
        )
        if self._active_structure is None:
            self._active_structure = 0
        else:
            self._active_structure += 1

    def clear(self):
        self._structures.clear()
        self._transforms.clear()
        self._transformation_matrices.clear()
        self._active_structure = None

    def set_active_transform(
        self, location: LocationType, scale: ScaleType, rotation: RotationType
    ):
        if self._active_structure is not None:
            self._transforms[self._active_structure] = (location, scale, rotation)
            self._transformation_matrices[self._active_structure] = transform_matrix(
                location, scale, rotation
            )

    def draw(self, camera_matrix: numpy.ndarray):
        for structure, transform in zip(
            self._structures, self._transformation_matrices
        ):
            structure.draw(numpy.matmul(transform, camera_matrix), 0, 0)
