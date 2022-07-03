from typing import TYPE_CHECKING, Optional, Tuple, Generator, List
import numpy
import math

from amulet.api.chunk import Chunk
from amulet.api.block import UniversalAirLikeBlocks
from amulet.api.errors import ChunkLoadError

from amulet_map_editor.api.opengl.matrix import rotation_matrix_xy

from amulet.api.data_types import PointCoordinatesNDArray

from .base_behaviour import BaseBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class RaycastBehaviour(BaseBehaviour):
    """Adds the base behaviour for behaviours that needs to do ray casting."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)

    def look_vector(self) -> numpy.ndarray:
        """
        The x,y,z vector for the direction the camera is facing
        :return: (x, y, z) numpy float array ranging from -1 to 1
        """
        look_vector = numpy.array([0, 0, 1, 0])

        if self.canvas.mouse.delta_xy != (0, 0):
            screen_width, screen_height = numpy.array(self.canvas.GetSize(), int) / 2
            screen_width = max(1, screen_width)
            screen_height = max(1, screen_height)
            screen_dx = math.atan(
                self.canvas.mouse.delta_x
                * self.canvas.camera.aspect_ratio
                * math.tan(math.radians(self.canvas.camera.fov / 2))
                / screen_width
            )
            screen_dy = math.atan(
                self.canvas.mouse.delta_y
                * math.cos(screen_dx)
                * math.tan(math.radians(self.canvas.camera.fov / 2))
                / screen_height
            )
            look_vector = numpy.matmul(
                rotation_matrix_xy(screen_dy, -screen_dx),
                look_vector,
            )
        ry, rx = self.canvas.camera.rotation
        look_vector = numpy.matmul(
            rotation_matrix_xy(*numpy.radians([rx, -ry])), look_vector
        )[:3]
        look_vector[abs(look_vector) < 0.000001] = 0.000001
        return look_vector

    def closest_block_3d(
        self, max_distance: float = 100
    ) -> Tuple[PointCoordinatesNDArray, bool]:
        """Find the location of the closest non-air block.

        If the end is reached an a non-air block was not found the end location will be returned.
        :param max_distance: The distance to search up to.
        :return: Tuple[The block coordinate, was a non-air block found in the range]
        """
        cx: Optional[int] = None
        cz: Optional[int] = None
        chunk: Optional[Chunk] = None
        in_air = False

        location = numpy.array([0, 0, 0], dtype=numpy.int32)
        for location in self.collision_locations(max_distance):
            x, y, z = location
            cx_ = x >> 4
            cz_ = z >> 4
            if cx is None or cx != cx_ or cz != cz_:
                cx = cx_
                cz = cz_
                try:
                    chunk = self.canvas.world.get_chunk(cx, cz, self.canvas.dimension)
                except ChunkLoadError:
                    chunk = None

            if (
                chunk is not None
                and chunk.block_palette[chunk.blocks[x % 16, y, z % 16]]
                not in UniversalAirLikeBlocks
            ):
                # the block is not air
                if in_air:  # if we have previously found an air block
                    return location, True
            elif not in_air:
                in_air = True
        return location, False

    def get_2d_mouse_location(self) -> Tuple[float, float]:
        """Get the x and z location of the cursor when in 2D mode."""
        x, _, z = self.canvas.camera.location
        width, height = self.canvas.GetSize()
        width = max(1, width)
        height = max(1, height)
        z += 2 * self.canvas.camera.fov * self.canvas.mouse.delta_y / height
        x += (
            2
            * self.canvas.camera.fov
            * self.canvas.camera.aspect_ratio
            * self.canvas.mouse.delta_x
            / width
        )
        x, z = numpy.floor([x, z]) + 0.5
        return x, z

    def closest_block_2d(self, min_y: int = 0) -> Tuple[PointCoordinatesNDArray, bool]:
        """Find the first non-air block above a given y axis.
        Note if there are no non-air blocks above the given axis it will return the min_y value

        :param min_y: The minimum y coordinate to look to.
        :return: Tuple[The block coordinate, was a non-air block found in the range]
        """
        x, z = self.get_2d_mouse_location()
        sub_chunk_size = self.canvas.world.sub_chunk_size
        y = min_y
        try:
            chunk = self.canvas.world.get_chunk(
                int(x // sub_chunk_size),
                int(z // sub_chunk_size),
                self.canvas.dimension,
            )
        except ChunkLoadError:
            pass
        else:
            box_max_chunk = int(min_y // sub_chunk_size)
            sub_chunks = sorted(
                [cy for cy in chunk.blocks.sub_chunks if cy >= box_max_chunk],
                reverse=True,
            )
            if sub_chunks:
                dx, dz = (numpy.floor([x, z]) % sub_chunk_size).astype(numpy.int64)
                for sy in sub_chunks:
                    blocks = numpy.invert(
                        numpy.isin(
                            chunk.blocks.get_section(sy)[dx, ::-1, dz],
                            UniversalAirLikeBlocks,
                        )
                    )
                    if numpy.any(blocks):
                        y = (
                            sub_chunk_size
                            - 1
                            - numpy.argmax(blocks)
                            + sy * sub_chunk_size
                        )
                        y = max(min_y, y)
                        return numpy.asarray((x, y, z)), True
        return numpy.asarray((x, y, z)), False

    def distance_block_3d(
        self,
        distance: float,
        start_location: Optional[numpy.ndarray] = None,
        look_vector: Optional[numpy.ndarray] = None,
    ) -> PointCoordinatesNDArray:
        """The first block location along the camera's look vector that is further away than `distance`.
        :param distance: The distance between the block and the camera.
        :param start_location: The start location. Defaults to the camera location.
        :param look_vector: The unit look vector. Defaults to the camera look vector.
        :return: (x, y, z) numpy array, selection box index
        """
        if look_vector is None:
            look_vector = self.look_vector()
        if start_location is None:
            start_location = self.canvas.camera.location
        position = numpy.array(start_location, dtype=int) + numpy.floor(
            look_vector * distance
        ).astype(int)
        return position

    def collision_locations(
        self,
        max_distance: float = 100,
        start_location: Optional[numpy.ndarray] = None,
        look_vector: Optional[numpy.ndarray] = None,
    ) -> Generator[numpy.ndarray, None, None]:
        """
        The block locations that the camera's look vector passes through.
        :param max_distance: The maximum distance along the look vector to traverse.
        :param start_location: The start location. Defaults to the camera location.
        :param look_vector: The unit look vector. Defaults to the camera look vector.
        :return: A generator of (x, y, z) numpy arrays
        """
        if look_vector is None:
            look_vector = self.look_vector()
        if start_location is None:
            start_location = self.canvas.camera.location
        dx, dy, dz = look_vector

        vectors = numpy.array(
            [look_vector / abs(dx), look_vector / abs(dy), look_vector / abs(dz)]
        )

        locations: List[numpy.ndarray] = []
        # the location within the block
        start: numpy.ndarray = numpy.array(start_location, numpy.float32) % 1

        for axis in range(3):
            vector = vectors[axis]
            vector_size = numpy.sum(vector**2) ** 0.5
            # move the start position to the block edge behind the vector
            if vector[axis] > 0:
                initial_offset = -vector * start[axis]
            else:
                initial_offset = -vector * (1 - start[axis])

            block_count = (
                max_distance + numpy.sum(initial_offset**2) ** 0.5 - 0.001
            ) // vector_size

            if block_count:
                blocks = numpy.arange(block_count + 1).reshape(-1, 1)
                offsets = blocks * vector + initial_offset
                locations_ = numpy.floor(offsets + start).astype(int)
                if vector[axis] < 0:
                    locations_[:, axis] -= 1

                locations.append(locations_)

        if locations:
            collision_locations = numpy.floor(start_location).astype(int) + numpy.array(
                sorted(
                    numpy.concatenate(locations),
                    key=lambda loc: sum(abs(loc_) for loc_ in loc),
                )
            )
        else:
            collision_locations = start.astype(int).reshape(1, 3)

        for location in collision_locations:
            yield location
