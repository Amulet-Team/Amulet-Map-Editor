import wx
from wx import glcanvas
from OpenGL.GL import *
import os
from typing import TYPE_CHECKING, Optional, Any, Dict, Tuple, List
import uuid
import numpy
import math

import minecraft_model_reader
from amulet.api.structure import Structure
from amulet.api.errors import ChunkLoadError

from amulet_map_editor.opengl.mesh.world_renderer.world import RenderWorld, sin, cos
from amulet_map_editor.opengl.mesh.selection import RenderSelection
from amulet_map_editor.opengl.mesh.structure import RenderStructure
from amulet_map_editor.opengl import textureatlas
from amulet_map_editor import log

if TYPE_CHECKING:
    from amulet.api.world import World
    from .edit import EditExtension


class EditCanvas(glcanvas.GLCanvas):
    def __init__(self, world_panel: 'EditExtension', world: 'World'):
        self._keys_pressed = set()
        attribs = (glcanvas.WX_GL_CORE_PROFILE, glcanvas.WX_GL_RGBA, glcanvas.WX_GL_DOUBLEBUFFER, glcanvas.WX_GL_DEPTH_SIZE, 24)
        super().__init__(world_panel, -1, size=world_panel.GetClientSize(), attribList=attribs)
        self._context = glcanvas.GLContext(self)  # setup the OpenGL context
        self.SetCurrent(self._context)
        self.context_identifier = str(uuid.uuid4())  # create a UUID for the context. Used to get shaders
        self._gl_texture_atlas = glGenTextures(1)  # Create the atlas texture location
        self._setup_opengl()  # set some OpenGL states

        self._last_mouse_x = 0
        self._last_mouse_y = 0
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
            minecraft_model_reader.JavaRP(os.path.join(os.path.dirname(__file__), 'amulet_resource_pack')),
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

        self._transformation_matrix: Optional[numpy.ndarray] = None
        self._collision_locations_cache: Optional[numpy.ndarray] = None
        self._camera = [0, 150, 0, 90, 0]
        self._projection = [70.0, 4 / 3, 0.1, 1000.0]
        self._camera_move_speed = 2
        self._camera_rotate_speed = 2
        self._select_distance = 10
        self._select_mode = 0  # 0 is normal box select, 1 is selection place
        self._select_style = 1  # 0 is select at fixed distance, 1 is select closest non-air
        self._selection_box = RenderSelection(
            self.context_identifier,
            self._texture_bounds
        )
        self._selection_box2 = RenderSelection(
            self.context_identifier,
            self._texture_bounds
        )
        self._structure: Optional[RenderStructure] = None
        self._structure_locations: List[numpy.ndarray] = []

        self._draw_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._on_draw, self._draw_timer)

        self._input_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._process_inputs, self._input_timer)

        self._gc_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._gc, self._gc_timer)

        world_panel.Bind(wx.EVT_SIZE, self._on_resize)

    def enable(self):
        self.SetCurrent(self._context)
        self._render_world.enable()
        self._draw_timer.Start(33)
        self._input_timer.Start(33)
        self._gc_timer.Start(10000)

    def disable(self):
        self._draw_timer.Stop()
        self._input_timer.Stop()
        self._gc_timer.Stop()
        self._render_world.disable()

    def disable_threads(self):
        self._render_world.chunk_generator.stop()

    def enable_threads(self):
        self._render_world.chunk_generator.start()

    def close(self):
        self._render_world.close()
        glDeleteTextures([self._gl_texture_atlas])

    def is_closeable(self):
        return self._render_world.is_closeable()

    def _setup_opengl(self):
        glClearColor(0.5, 0.66, 1.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glBindTexture(GL_TEXTURE_2D, self._gl_texture_atlas)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

    def _load_resource_pack(self, *resource_packs: minecraft_model_reader.JavaRP):
        self._resource_pack = minecraft_model_reader.JavaRPHandler(resource_packs)
        self._create_atlas()

    def _create_atlas(self):
        texture_atlas, self._texture_bounds, width, height = textureatlas.create_atlas(
            self._resource_pack.textures
        )
        glBindTexture(GL_TEXTURE_2D, self._gl_texture_atlas)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_atlas)
        log.info('Finished setting up texture atlas in OpenGL')

    @property
    def structure(self) -> RenderStructure:
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
    def select_mode(self) -> int:
        return self._select_mode

    @select_mode.setter
    def select_mode(self, select_mode: int):
        self._select_mode = select_mode

    @property
    def dimension(self) -> int:
        return self._render_world.dimension

    @dimension.setter
    def dimension(self, dimension: int):
        self._render_world.dimension = dimension

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

    @property
    def fov(self) -> float:
        return self._projection[0]

    @fov.setter
    def fov(self, fov: float):
        self._projection[0] = fov
        self._transformation_matrix = None

    @property
    def aspect_ratio(self) -> float:
        return self._projection[1]

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio: float):
        self._projection[1] = aspect_ratio
        self._transformation_matrix = None

    @property
    def transformation_matrix(self) -> numpy.ndarray:
        # camera translation
        if self._transformation_matrix is None:
            transformation_matrix = numpy.eye(4, dtype=numpy.float32)
            transformation_matrix[3, :3] = numpy.array(self._camera[:3]) * -1

            c = cos(self._camera[4])
            s = sin(self._camera[4])

            y_rot = numpy.array(
                [
                    [c, 0, -s, 0],
                    [0, 1, 0, 0],
                    [s, 0, c, 0],
                    [0, 0, 0, 1]
                ],
                dtype=numpy.float32
            )

            transformation_matrix = numpy.matmul(transformation_matrix, y_rot)

            # rotations
            c = cos(self._camera[3])
            s = sin(self._camera[3])

            x_rot = numpy.array(
                [
                    [1, 0, 0, 0],
                    [0, c, s, 0],
                    [0, -s, c, 0],
                    [0, 0, 0, 1]
                ],
                dtype=numpy.float32
            )

            transformation_matrix = numpy.matmul(transformation_matrix, x_rot)

            # camera projection
            fovy, aspect, z_near, z_far = self._projection
            fovy = math.radians(fovy)
            f = 1 / math.tan(fovy / 2)
            projection = numpy.array(
                [
                    [f/aspect, 0, 0, 0],
                    [0, f, 0, 0],
                    [0, 0, (z_far+z_near)/(z_near-z_far), -1],
                    [0, 0, (2*z_far*z_near)/(z_near-z_far), 0]
                ],
                dtype=numpy.float32
            )

            self._transformation_matrix = numpy.matmul(transformation_matrix, projection)

        return self._transformation_matrix

    @property
    def selection(self) -> Optional[numpy.ndarray]:
        return numpy.array([self._selection_box.min, self._selection_box.max])

    def _collision_location_closest(self):
        """Find the location of the closests non-air block"""
        # TODO: optimise this
        for location in self._collision_locations():
            try:
                if self._render_world.world.get_block(*location, self._render_world.dimension).namespaced_name != 'universal_minecraft:air':
                    return location
            except IndexError:
                continue
            except ChunkLoadError:
                continue
        return self._collision_locations()[-1]

    def _collision_location_distance(self, distance):
        distance = distance ** 2
        locations = self._collision_locations()
        camera = numpy.array(self._camera[:3], dtype=numpy.int)
        block = next((loc for loc in locations if sum((abs(loc - camera) + 0.5) ** 2) >= distance), None)
        if block is None:
            return locations[-1]
        else:
            return block

    def _collision_locations(self):
        if self._collision_locations_cache is None:

            dx = sin(self._camera[4]) * cos(self._camera[3])
            dy = -sin(self._camera[3])
            dz = -cos(self._camera[4]) * cos(self._camera[3])
            look_vector = numpy.array([dx, dy, dz])
            look_vector[abs(look_vector) < 0.000001] = 0.000001
            dx, dy, dz = look_vector
            max_distance = 30

            vectors = numpy.array(
                [
                    look_vector / abs(dx),
                    look_vector / abs(dy),
                    look_vector / abs(dz)
                ]
            )
            offsets = -numpy.eye(3)

            locations = set()
            start: numpy.ndarray = numpy.array(self._camera[:3], numpy.float32) % 1

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
            self._collision_locations_cache = numpy.array(
                sorted(list(locations), key=lambda loc: sum(abs(loc_) for loc_ in loc))) + numpy.floor(
                self._camera[:3]).astype(numpy.int)

        return self._collision_locations_cache

    def _on_resize(self, event):
        self.set_size(*event.GetSize())

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
        if self._select_mode == 1 and self._structure is not None:
            transform = numpy.eye(4, dtype=numpy.float32)
            for location in self.structure_locations:
                transform[3, 0:3] = location
                self._structure.draw(numpy.matmul(transform, self.transformation_matrix), 0, 0)
        self._selection_box.draw(self.transformation_matrix)
        if self._selection_box.select_state == 2:
            self._selection_box2.draw(self.transformation_matrix)
        self.SwapBuffers()

    def _gc(self, event):
        self._render_world.run_garbage_collector()
        event.Skip()
