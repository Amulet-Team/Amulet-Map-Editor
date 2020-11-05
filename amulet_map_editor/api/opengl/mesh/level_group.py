from typing import List, Optional, Tuple, Any
import numpy

from amulet.api.level import BaseLevel
from amulet.api.data_types import FloatTriplet, PointCoordinates, Dimension

from amulet_map_editor.api.opengl.mesh.base.tri_mesh import Drawable, ContextManager
from amulet_map_editor.api.opengl.mesh.level import RenderLevel
from amulet_map_editor.api.opengl.matrix import transform_matrix, displacement_matrix
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePackManager,
    OpenGLResourcePack,
)

LocationType = PointCoordinates
ScaleType = FloatTriplet
RotationType = FloatTriplet
TransformType = Tuple[LocationType, ScaleType, RotationType]


class LevelGroup(OpenGLResourcePackManager, Drawable, ContextManager):
    """A group of RenderLevel classes with transforms"""

    def __init__(
        self, context_identifier: Any, resource_pack: OpenGLResourcePack,
    ):
        OpenGLResourcePackManager.__init__(self, resource_pack)
        ContextManager.__init__(self, context_identifier)
        self._structures: List[RenderLevel] = []
        self._transforms: List[TransformType] = []
        self._world_translation: List[LocationType] = []
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
        level: BaseLevel,
        dimension: Dimension,
        location: LocationType,
        scale: ScaleType,
        rotation: RotationType,
    ):
        """Append a structure to the list and activate it."""
        # TODO: update this to support multiple structures
        self.clear()
        render_level = RenderLevel(
            self.context_identifier,
            self._resource_pack,
            level,
            draw_floor=False,
            draw_box=True,
        )
        render_level.dimension = dimension
        # the structure objects to be drawn
        self._structures.append(render_level)
        # the transforms (tuple) applied by the user
        self._transforms.append((location, scale, rotation))
        self._world_translation.append(
            (
                -(
                    (level.selection_bounds.min + level.selection_bounds.max) // 2
                ).astype(int)
            ).tolist()
        )
        # the matrix of the transform applied by the user
        self._transformation_matrices.append(
            numpy.matmul(
                transform_matrix(scale, rotation, location),
                displacement_matrix(*self._world_translation[-1]),
            )
        )
        if self._active_structure is None:
            self._active_structure = 0
        else:
            self._active_structure += 1

    def disable(self):
        for s in self._structures:
            s.disable()

    def clear(self):
        self.disable()
        self._structures.clear()
        self._transforms.clear()
        self._world_translation.clear()
        self._transformation_matrices.clear()
        self._active_structure = None

    def set_active_transform(
        self, location: LocationType, scale: ScaleType, rotation: RotationType
    ):
        if self._active_structure is not None:
            self._transforms[self._active_structure] = (location, scale, rotation)
            self._transformation_matrices[self._active_structure] = numpy.matmul(
                transform_matrix(scale, rotation, location),
                displacement_matrix(*self._world_translation[self._active_structure]),
            )

    def draw(self, camera_matrix: numpy.ndarray):
        for structure, transform in zip(
            self._structures, self._transformation_matrices
        ):
            structure.draw(numpy.matmul(camera_matrix, transform))
