import wx
from OpenGL.GL import *
import os
from typing import TYPE_CHECKING, Optional, Any, Dict, Tuple, List, Generator
import numpy
import weakref

import minecraft_model_reader
from amulet.api.chunk import Chunk
from amulet.api.structure import Structure
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import PointCoordinatesNDArray, Dimension
from amulet.api.selection import SelectionGroup

from amulet_map_editor.opengl.data_types import CameraLocationType, CameraRotationType
from amulet_map_editor.opengl.mesh.world_renderer.world import RenderWorld, cos, tan, atan
from amulet_map_editor.opengl.mesh.selection import RenderSelection, RenderSelectionGroup
from amulet_map_editor.opengl.mesh.structure import RenderStructure
from amulet_map_editor.opengl import textureatlas
from amulet_map_editor.opengl.canvas.base import BaseCanvas
from amulet_map_editor import log
from amulet_map_editor.programs.edit.canvas.events import (
    CameraMoveEvent,
    CameraRotateEvent,
    DimensionChangeEvent,
)

if TYPE_CHECKING:
    from amulet.api.world import World

MODE_NORMAL = 0  # normal selection
MODE_DISABLED = 1  # non-interactive selection boxes
MODE_STRUCTURE = 2  # MODE_DISABLED and draw structure if exists


class BaseEditCanvas(BaseCanvas):
    """Adds base logic for drawing everything related to the edit program to the BaseCanvas.
    All the user interaction code is implemented in ControllableEditCanvas to make them easier to read."""
    def __init__(self, parent: wx.Window, world: 'World'):
        super().__init__(parent)
        self.Hide()
        self._world = weakref.ref(world)
        self._mouse_delta_x = 0
        self._mouse_delta_y = 0
        self._mouse_lock = False

        # load the resource packs
        os.makedirs('resource_packs', exist_ok=True)
        if not os.path.isfile('resource_packs/readme.txt'):
            with open('resource_packs/readme.txt', 'w') as f:
                f.write('Put the Java resource pack you want loaded in here.')

        self._texture_bounds: Optional[Dict[Any, Tuple[float, float, float, float]]] = None
        self._resource_pack: Optional[minecraft_model_reader.JavaRPHandler] = None

        self._load_resource_pack(
            minecraft_model_reader.JavaRP(os.path.join(os.path.dirname(__file__), '..', 'amulet_resource_pack')),
            minecraft_model_reader.java_vanilla_latest,
            *[minecraft_model_reader.JavaRP(rp) for rp in os.listdir('resource_packs') if os.path.isdir(rp)],
            minecraft_model_reader.java_vanilla_fix
        )

        self._resource_pack_translator = world.world_wrapper.translation_manager.get_version('java', (1, 15, 2))

        self._render_world = RenderWorld(
            self.context_identifier,
            world,
            self._resource_pack,
            self._gl_texture_atlas,
            self._texture_bounds,
            self._resource_pack_translator
        )

        self._camera_location: CameraLocationType = (0.0, 100.0, 0.0)
        self._camera_rotation: CameraRotationType = (45.0, 45.0)
        self._camera_move_speed = 2
        self._camera_rotate_speed = 2
        self._select_distance = 10
        self._select_distance2 = 10
        self._select_mode = MODE_NORMAL

        self._selection_moved = True  # has the selection point moved and does the box need rebuilding
        self._selection_group = RenderSelectionGroup(
            self.context_identifier,
            self._texture_bounds,
            self._gl_texture_atlas
        )
        self._structure: Optional[RenderStructure] = None
        self._structure_locations: List[numpy.ndarray] = []

        self._draw_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._on_draw, self._draw_timer)

        self._gc_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._gc, self._gc_timer)

        self._rebuild_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._rebuild, self._rebuild_timer)

    @property
    def world(self) -> "World":
        return self._world()

    @property
    def selection_group(self) -> SelectionGroup:
        """Create a SelectionGroup class from the selected boxes."""
        return self._selection_group.create_selection_group()

    @property
    def active_selection(self) -> Optional[RenderSelection]:
        """Get the selection box that is currently active.
        May be None if no selection box exists."""
        return self._selection_group.active_selection

    def enable(self):
        """Enable the canvas and start it working."""
        self.SetCurrent(self._context)
        self._render_world.enable()
        self._draw_timer.Start(33)
        self._gc_timer.Start(10000)
        self._rebuild_timer.Start(1000)

    def disable(self):
        """Disable the canvas and unload all geometry."""
        self._draw_timer.Stop()
        self._gc_timer.Stop()
        self._rebuild_timer.Stop()
        self._render_world.disable()

    def disable_threads(self):
        """Stop the generation of new chunk geometry.
        Makes it safe to modify the world data."""
        self._render_world.chunk_generator.stop()

    def enable_threads(self):
        """Start the generation of new chunk geometry."""
        self._render_world.chunk_generator.start()

    def close(self):
        """Close and destroy the canvas and all contained data."""
        self._render_world.close()
        super()._close()

    def is_closeable(self):
        """Check that the canvas and contained data is safe to be closed."""
        return self._render_world.is_closeable()

    def _load_resource_pack(self, *resource_packs: minecraft_model_reader.JavaRP):
        self._resource_pack = minecraft_model_reader.JavaRPHandler(resource_packs)
        self._create_atlas()

    def _create_atlas(self):
        """Create and bind the atlas texture."""
        texture_atlas, self._texture_bounds, width, height = textureatlas.create_atlas(
            self._resource_pack.textures
        )
        glBindTexture(GL_TEXTURE_2D, self._gl_texture_atlas)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_atlas)
        glBindTexture(GL_TEXTURE_2D, 0)
        log.info('Finished setting up texture atlas in OpenGL')

    @property
    def structure(self) -> Optional[RenderStructure]:
        return self._structure

    @structure.setter
    def structure(self, structure: Structure):
        self._structure = RenderStructure(
            self.context_identifier,
            structure,
            self._resource_pack,
            self._gl_texture_atlas,
            self._texture_bounds,
            self._resource_pack_translator
        )

    @property
    def structure_locations(self) -> List[numpy.ndarray]:
        return self._structure_locations

    @property
    def select_distance(self) -> int:
        return self._select_distance

    @select_distance.setter
    def select_distance(self, distance: int):
        self._select_distance = distance
        self._selection_moved = True

    @property
    def select_distance2(self) -> int:
        return self._select_distance2

    @select_distance2.setter
    def select_distance2(self, distance: int):
        self._select_distance2 = distance
        self._selection_moved = True

    @property
    def select_mode(self) -> int:
        return self._select_mode

    @select_mode.setter
    def select_mode(self, select_mode: int):
        self._select_mode = select_mode
        self._selection_moved = True

    @property
    def dimension(self) -> Dimension:
        return self._render_world.dimension

    @dimension.setter
    def dimension(self, dimension: Dimension):
        self._render_world.dimension = dimension
        wx.PostEvent(self, DimensionChangeEvent(dimension=dimension))

    @property
    def camera_location(self) -> CameraLocationType:
        return self._camera_location

    @camera_location.setter
    def camera_location(self, location: CameraLocationType):
        assert len(location) == 3 and all(isinstance(v, (int, float)) for v in location), "format for camera_location is invalid"
        self._camera_location = location
        self._transformation_matrix = None
        self._selection_moved = True
        wx.PostEvent(self, CameraMoveEvent(location=self.camera_location))

    @property
    def camera_rotation(self) -> CameraRotationType:
        return self._camera_rotation

    @camera_rotation.setter
    def camera_rotation(self, rotation: CameraRotationType):
        assert len(rotation) == 2 and all(isinstance(v, (int, float)) for v in rotation), "format for camera_rotation is invalid"
        self._camera_rotation = rotation
        self._transformation_matrix = None
        self._selection_moved = True
        wx.PostEvent(self, CameraRotateEvent(rotation=self.camera_rotation))

    @property
    def camera_move_speed(self) -> float:
        """The speed that the camera moves at"""
        return self._camera_move_speed

    @camera_move_speed.setter
    def camera_move_speed(self, val: float):
        self._camera_move_speed = val

    @property
    def camera_rotate_speed(self) -> float:
        """The speed that the camera rotates at"""
        return self._camera_rotate_speed

    @camera_rotate_speed.setter
    def camera_rotate_speed(self, val: float):
        self._camera_rotate_speed = val

    def _change_box_location(self):
        if self._selection_group.active_selection and self._selection_group.active_selection.being_resized:
            position, box_index = self._box_location_distance(self.select_distance2)
        elif self._mouse_lock:
            position, box_index = self._box_location_distance(self.select_distance)
        else:
            position, box_index = self._box_location_closest()

        self._selection_group.update_position(position, box_index)

    def ray_collision(self):
        vector_start = self.camera_location
        direction_vector = self._look_vector()
        min_point = self.active_selection.min
        max_point = self.active_selection.max

        point_array = max_point.copy()
        numpy.putmask(point_array, direction_vector > 0, min_point)

        t = (point_array - vector_start) / direction_vector

        t_max = numpy.where(t == t.max())[0][0]
        return t_max

    def _box_location_closest(self) -> Tuple[PointCoordinatesNDArray, Optional[int]]:
        """Find the location of the closests non-air block or selection box"""
        cx: Optional[int] = None
        cz: Optional[int] = None
        chunk: Optional[Chunk] = None

        box_index, nearest_selection_box = self._selection_group.closest_intersection(self.camera_location, self._look_vector())

        location = numpy.array([0, 0, 0], dtype=numpy.int32)
        for location in self._collision_locations():
            if nearest_selection_box and nearest_selection_box.in_boundary(location):
                return location, box_index

            x, y, z = location
            cx_ = x >> 4
            cz_ = z >> 4
            if cx is None or cx != cx_ or cz != cz_:
                cx = cx_
                cz = cz_
                try:
                    chunk = self._render_world.world.get_chunk(cx, cz, self.dimension)
                except ChunkLoadError:
                    chunk = None

            if chunk is not None and self._render_world.world.palette[chunk.blocks[x % 16, y, z % 16]].namespaced_name != 'universal_minecraft:air':
                return location, None
        return location, None

    def _box_location_distance(self, distance: int) -> Tuple[PointCoordinatesNDArray, Optional[int]]:
        """
        The first block location along the camera's look vector that is further away than `distance`.
        :param distance: The distance between the block and the camera.
        :return: (x, y, z) numpy array, selection box index
        """
        look_vector = self._look_vector()
        position = numpy.array(self.camera_location, dtype=numpy.int) + numpy.floor(look_vector*distance).astype(numpy.int)
        box = next((index for index, box in enumerate(self._selection_group) if box.in_boundary(position)), None)
        return position, box

    def _look_vector(self) -> numpy.ndarray:
        """
        The x,y,z vector for the direction the camera is facing
        :return: (x, y, z) numpy float array ranging from -1 to 1
        """
        look_vector = numpy.array([0, 0, -1, 0])
        if not self._mouse_lock:
            screen_x, screen_y = numpy.array(self.GetSize(), numpy.int) / 2
            screen_dx = atan(self.aspect_ratio * tan(self.fov / 2) * self._mouse_delta_x / screen_x)
            screen_dy = atan(cos(screen_dx) * tan(self.fov / 2) * self._mouse_delta_y / screen_y)
            look_vector = numpy.matmul(self.rotation_matrix(screen_dy, screen_dx), look_vector)
        look_vector = numpy.matmul(self.rotation_matrix(*self.camera_rotation), look_vector)[:3]
        look_vector[abs(look_vector) < 0.000001] = 0.000001
        return look_vector

    def _collision_locations(self, max_distance=100) -> Generator[numpy.ndarray, None, None]:
        """
        The block locations that the camera's look vector passes through.
        :param max_distance: The maximum distance along the look vector to traverse.
        :return: A generator of (x, y, z) numpy arrays
        """
        # TODO: optimise this

        look_vector = self._look_vector()
        dx, dy, dz = look_vector

        vectors = numpy.array(
            [
                look_vector / abs(dx),
                look_vector / abs(dy),
                look_vector / abs(dz)
            ]
        )
        offsets = -numpy.eye(3)

        locations = set()
        start: numpy.ndarray = numpy.array(self.camera_location, numpy.float32) % 1

        for axis in range(3):
            location: numpy.ndarray = start.copy()
            vector = vectors[axis]
            offset = offsets[axis]
            if vector[axis] > 0:
                location = location + vector * (1 - location[axis])
            else:
                location = location + vector * location[axis]
            while numpy.all(abs(location) < max_distance):
                locations.add(tuple(numpy.floor(location).astype(numpy.int)))
                locations.add(tuple(numpy.floor(location + offset).astype(numpy.int)))
                location += vector
        if locations:
            collision_locations = numpy.array(
                sorted(list(locations), key=lambda loc: sum(abs(loc_) for loc_ in loc))
            ) + numpy.floor(self.camera_location).astype(numpy.int)
        else:
            collision_locations = start.astype(numpy.int)

        for location in collision_locations:
            yield location

    def set_size(self, width, height):
        glViewport(0, 0, width, height)
        if height > 0:
            self.aspect_ratio = width / height
        else:
            self.aspect_ratio = 1
        self.DoSetSize(0, 0, width, height, 0)  # I don't know if this is how you are supposed to do this

    def _on_draw(self, event):
        self.draw()
        event.Skip()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self._render_world.draw(self.transformation_matrix)
        if self._select_mode == MODE_STRUCTURE and self._structure is not None:
            transform = numpy.eye(4, dtype=numpy.float32)
            for location in self.structure_locations:
                transform[3, 0:3] = location
                self._structure.draw(numpy.matmul(transform, self.transformation_matrix), 0, 0)
        if self._selection_moved:
            self._selection_moved = False
            self._change_box_location()
        self._selection_group.draw(self.transformation_matrix, tuple(self.camera_location), self._select_mode == MODE_NORMAL)
        self.SwapBuffers()

    def _gc(self, event):
        self._render_world.run_garbage_collector()
        event.Skip()

    def _rebuild(self, evt):
        self._render_world.chunk_manager.rebuild()
        evt.Skip()
