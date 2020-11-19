from typing import List, Optional, Tuple, Any
import numpy

from amulet.api.level import BaseLevel
from amulet.api.data_types import FloatTriplet, PointCoordinates, Dimension

from amulet_map_editor.api.opengl import Drawable, ContextManager
from amulet_map_editor.api.opengl.mesh.level import RenderLevel
from amulet_map_editor.api.opengl.matrix import (
    transform_matrix,
    displacement_matrix,
    inverse_transform_matrix,
)
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePackManager,
    OpenGLResourcePack,
)

numpy.seterr(all="raise")

LocationType = PointCoordinates
ScaleType = FloatTriplet
RotationType = FloatTriplet
TransformType = Tuple[LocationType, ScaleType, RotationType]


class LevelGroup(OpenGLResourcePackManager, Drawable, ContextManager):
    """A group of RenderLevel classes with transforms"""

    def __init__(
        self,
        context_identifier: Any,
        resource_pack: OpenGLResourcePack,
    ):
        OpenGLResourcePackManager.__init__(self, resource_pack)
        ContextManager.__init__(self, context_identifier)
        self._levels: List[RenderLevel] = []
        self._transforms: List[TransformType] = []
        self._world_translation: List[LocationType] = []
        self._transformation_matrices: List[numpy.ndarray] = []
        self._active_level: Optional[int] = None

    @property
    def active_level(self) -> Optional[int]:
        """The index of the active level. None if no level is active."""
        return self._active_level

    @property
    def active_transform(self) -> TransformType:
        """Get the transform of the active level.
        If no level is selected will return zeros."""
        if self._active_level is None:
            return (0, 0, 0), (0, 0, 0), (0, 0, 0)
        return self._transforms[self._active_level]

    @active_transform.setter
    def active_transform(self, location_scale_rotation: TransformType):
        """Set the transform for the active object.
        Has no effect if there is no active object.
        :param location_scale_rotation: The location, scale and rotation
        :return:
        """
        if self._active_level is not None:
            location, scale, rotation = location_scale_rotation
            self._transforms[self._active_level] = (location, scale, rotation)
            self._transformation_matrices[self._active_level] = numpy.matmul(
                transform_matrix(scale, rotation, location),
                displacement_matrix(*self._world_translation[self._active_level]),
            )

    def set_camera_location(self, x: float, y: float, z: float):
        """Set the location of the camera for each of the levels."""
        for level, (displacement, scale, rotation) in zip(
            self._levels, self._transforms
        ):
            level.camera_location = numpy.matmul(
                inverse_transform_matrix(scale, rotation, displacement), (x, y, z, 1)
            ).tolist()[:-1]

    def set_camera_rotation(self, yaw: float, pitch: float):
        """Set the rotation of the camera for each of the levels."""
        for level in self._levels:
            level.camera_rotation = yaw, pitch

    def append(
        self,
        level: BaseLevel,
        dimension: Dimension,
        location: LocationType,
        scale: ScaleType,
        rotation: RotationType,
    ):
        """Append a level to the list and activate it."""
        # TODO: update this to support multiple levels
        self.clear()
        render_level = RenderLevel(
            self.context_identifier,
            self._resource_pack,
            level,
            draw_floor=False,
            draw_box=True,
        )
        render_level.dimension = dimension
        # the level objects to be drawn
        self._levels.append(render_level)
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
        if self._active_level is None:
            self._active_level = 0
        else:
            self._active_level += 1

    def enable(self):
        """Enable chunk generation in a new thread."""
        for level in self._levels:
            level.enable()

    def disable(self, unload_data: bool = False):
        """Disable the chunk generation thread.
        This makes it safe to access and modify world data.
        :param unload_data: Unload the data stored in the world
        :return:
        """
        for level in self._levels:
            level.disable(unload_data)

    def clear(self):
        """Destroy and unload all level objects."""
        self.disable(True)
        self._levels.clear()
        self._transforms.clear()
        self._world_translation.clear()
        self._transformation_matrices.clear()
        self._active_level = None

    def run_garbage_collector(self):
        for level in self._levels:
            level.run_garbage_collector()

    def rebuild(self):
        """Rebuild a single region which was last rebuild the longest ago.
        Put this on a semi-fast clock to rebuild all regions."""
        for level in self._levels:
            level.chunk_manager.rebuild()

    def draw(self, camera_matrix: numpy.ndarray):
        """Draw all of the levels."""
        for level, transform in zip(self._levels, self._transformation_matrices):
            level.draw(numpy.matmul(camera_matrix, transform))
