import wx
from OpenGL.GL import (
    glClearColor,
    glBindTexture,
    GL_TEXTURE_2D,
    glTexImage2D,
    GL_RGBA,
    GL_UNSIGNED_BYTE,
    glViewport,
    glClear,
    GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT,
)
import os
import warnings
from typing import Optional, Any, Dict, Tuple, Generator
import numpy
import weakref
import math

from minecraft_model_reader.api.resource_pack.java.download_resources import (
    get_java_vanilla_latest_iter,
    get_java_vanilla_fix,
)
from minecraft_model_reader.api.resource_pack.java import (
    JavaResourcePackManager,
    JavaResourcePack,
)
from minecraft_model_reader.api.resource_pack.bedrock.download_resources import (
    get_bedrock_vanilla_latest_iter,
    get_bedrock_vanilla_fix,
)
from minecraft_model_reader.api.resource_pack.bedrock import BedrockResourcePack
from minecraft_model_reader.api.resource_pack import (
    load_resource_pack,
    load_resource_pack_manager,
)
from amulet.api.chunk import Chunk
from amulet.api.block import UniversalAirBlock
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import (
    PointCoordinatesNDArray,
    Dimension,
    BlockCoordinates,
    OperationYieldType,
)

from amulet_map_editor import experimental_bedrock_resources
from amulet_map_editor.api.opengl.mesh.level import RenderLevel
from amulet_map_editor.api.opengl.mesh.level_group import LevelGroup
from amulet_map_editor.api.opengl.mesh.sky_box import SkyBox
from amulet_map_editor.api.opengl import textureatlas
from amulet_map_editor.api.opengl.canvas import EventCanvas
from amulet_map_editor.api.opengl.resource_pack.resource_pack import OpenGLResourcePack
from amulet_map_editor.api.opengl.matrix import rotation_matrix_xy
from amulet_map_editor.api.logging import log
from amulet_map_editor.programs.edit.api.selection import (
    SelectionManager,
    SelectionHistoryManager,
)
from amulet_map_editor.programs.edit.api.events import (
    CameraMovedEvent,
    EVT_CAMERA_MOVED,
    DimensionChangeEvent,
    DrawEvent,
    EVT_DRAW,
    CursorMoveEvent,
    EVT_CURSOR_MOVE,
)
import amulet_map_editor.programs.edit as amulet_edit
from ..chunk_generator import ThreadingEnabled, ChunkGenerator

from amulet_map_editor.api.opengl.camera import Projection, ControllableCamera

from amulet.api.level import World


class BaseEditCanvas(EventCanvas):
    """Adds base logic for drawing everything related to the edit program to the canvas.
    All the user interaction code is implemented in ControllableEditCanvas to make them easier to read."""

    background_colour = (0.61, 0.70, 0.85)

    def __init__(self, parent: wx.Window, world: World):
        super().__init__(parent)
        glClearColor(*self.background_colour, 1.0)
        self.Hide()

        self._camera: ControllableCamera = ControllableCamera(self)
        self._camera.location_rotation = (0.0, 100.0, 0.0), (45.0, 45.0)
        self._world = weakref.ref(world)

        self._mouse_delta_x = 0
        self._mouse_delta_y = 0
        self._mouse_lock = False

        # load the resource packs
        os.makedirs("resource_packs", exist_ok=True)
        if not os.path.isfile("resource_packs/readme.txt"):
            with open("resource_packs/readme.txt", "w") as f:
                f.write("Put the Java resource pack you want loaded in here.")

        self._texture_bounds: Optional[
            Dict[Any, Tuple[float, float, float, float]]
        ] = None
        self._opengl_resource_pack: Optional[OpenGLResourcePack] = None

        self._render_world: Optional[RenderLevel] = None

        self._camera_move_speed = 2.0
        self._camera_rotate_speed = 2.0
        self._select_distance = 10
        self._select_distance2 = 10

        # has the selection point moved and does the box need rebuilding
        self._selection_moved = True

        self._selection: Optional[SelectionHistoryManager] = None

        self._structure: Optional[LevelGroup] = None

        self._sky_box: Optional[SkyBox] = None

        self.chunk_generator = ChunkGenerator()

        self._draw_timer = wx.Timer(self)
        self._gc_timer = wx.Timer(self)
        self._rebuild_timer = wx.Timer(self)

    def setup(self) -> Generator[OperationYieldType, None, None]:
        """Set up objects that take a while to set up.
        If you want to extend setup subclass the _setup method not this method."""
        yield from self._setup()
        self._finalise()

    def _setup(self) -> Generator[OperationYieldType, None, None]:
        """Set up objects that take a while to set up."""
        user_packs = [
            load_resource_pack(os.path.join("resource_packs", rp))
            for rp in os.listdir("resource_packs")
            if os.path.isdir(os.path.join("resource_packs", rp))
        ]
        if (
            self.world.level_wrapper.platform == "bedrock"
            and experimental_bedrock_resources
        ):
            yield 0.1, "Downloading Bedrock vanilla resource pack"
            gen = get_bedrock_vanilla_latest_iter()
            try:
                while True:
                    yield next(gen) * 0.4 + 0.1
            except StopIteration as e:
                latest_pack = e.value
            yield 0.5, "Loading resource packs"
            fix_pack = get_bedrock_vanilla_fix()
            amulet_pack = load_resource_pack(
                os.path.join(
                    os.path.dirname(amulet_edit.__file__),
                    "amulet_resource_pack",
                    "bedrock",
                )
            )

            user_packs = [
                pack for pack in user_packs if isinstance(pack, BedrockResourcePack)
            ]

            translator = self.world.translation_manager.get_version(
                "bedrock", (999, 0, 0)
            )
        else:
            yield 0.1, "Downloading Java vanilla resource pack"
            gen = get_java_vanilla_latest_iter()
            try:
                while True:
                    yield next(gen) * 0.4 + 0.1
            except StopIteration as e:
                latest_pack = e.value
            yield 0.5, "Loading resource packs"
            fix_pack = get_java_vanilla_fix()
            amulet_pack = load_resource_pack(
                os.path.join(
                    os.path.dirname(amulet_edit.__file__),
                    "amulet_resource_pack",
                    "java",
                )
            )

            user_packs = [
                pack for pack in user_packs if isinstance(pack, JavaResourcePack)
            ]

            translator = self.world.translation_manager.get_version("java", (999, 0, 0))

        resource_pack = load_resource_pack_manager(
            (amulet_pack, latest_pack, *user_packs, fix_pack), load=False
        )
        for i in resource_pack.reload():
            yield i / 4 + 0.5

        self._opengl_resource_pack = OpenGLResourcePack(resource_pack, translator)

        yield 0.75, "Creating texture atlas"
        for i in self._opengl_resource_pack.setup():
            yield i / 4 + 0.75

        yield 1.0, "Setting up renderer"

        self._render_world = RenderLevel(
            self.context_identifier,
            self._opengl_resource_pack,
            self.world,
        )
        self.chunk_generator.register(self._render_world)

        self._selection = SelectionHistoryManager(SelectionManager(self))
        self.world.history_manager.register(self._selection, False)

        self._structure: LevelGroup = LevelGroup(
            self.context_identifier,
            self._opengl_resource_pack,
        )
        self.chunk_generator.register(self._structure)

        self._sky_box: Optional[SkyBox] = SkyBox(
            self.context_identifier,
            self._opengl_resource_pack,
        )

    def _finalise(self):
        """Any logic that needs to be run after everything has been set up."""
        self.reset_bound_events()

    def set_up_events(self):
        """Set up all events required to run.
        Note this will also bind subclass events."""
        self.Bind(wx.EVT_SIZE, self._on_size)
        self.Bind(
            wx.EVT_TIMER, lambda evt: wx.PostEvent(self, DrawEvent()), self._draw_timer
        )
        self.Bind(wx.EVT_TIMER, self._gc, self._gc_timer)
        self.Bind(wx.EVT_TIMER, self._rebuild, self._rebuild_timer)
        self.Bind(EVT_CURSOR_MOVE, lambda evt: self._change_box_location())
        self._selection.value.set_up_events()  # TODO: clean this up a bit
        self.Bind(EVT_DRAW, self.on_draw)
        self.Bind(EVT_CAMERA_MOVED, self._on_camera_move)

    def enable(self):
        """Enable the canvas and start it working."""
        self.SetCurrent(self._context)
        self._render_world.enable()
        self._structure.enable()
        self._enable_threads()
        self._draw_timer.Start(15)
        self._gc_timer.Start(10000)
        self._rebuild_timer.Start(1000)

    def disable(self):
        """Disable the canvas and unload all geometry."""
        self._draw_timer.Stop()
        self._gc_timer.Stop()
        self._rebuild_timer.Stop()
        self._disable_threads()
        self._render_world.unload()
        self._structure.unload()

    def _disable_threads(self):
        """Stop the generation of new chunk geometry.
        Makes it safe to modify the world data."""
        self.chunk_generator.stop()

    def _enable_threads(self):
        """Start the generation of new chunk geometry."""
        self.chunk_generator.start()

    def close(self):
        """Close and destroy the canvas and all contained data."""
        self._render_world.close()
        self._structure.clear()
        super()._close()

    def is_closeable(self):
        """Check that the canvas and contained data is safe to be closed."""
        return self._render_world.is_closeable()

    @property
    def camera(self) -> ControllableCamera:
        """A class holding the state of the camera with methods to access and modify the state."""
        return self._camera

    @property
    def world(self) -> World:
        """The amulet-core `World` class representing the "world" that is open."""
        return self._world()

    @property
    def render_distance(self) -> int:
        """The distance from the camera in chunks that should be drawn"""
        return self._render_world.render_distance

    @render_distance.setter
    def render_distance(self, render_distance: int):
        """Set the distance from the camera in chunks that should be drawn"""
        self._render_world.render_distance = render_distance

    @property
    def selection_(self) -> SelectionManager:  # TODO: rename this to selection
        """A simple class for storing the selection state."""
        return self._selection.value

    # TODO: move this logic into a resource pack reload method
    # def _load_resource_pack(self, *resource_packs: JavaResourcePack):
    #     self._resource_pack = JavaResourcePackManager(resource_packs)
    #     for _ in self._create_atlas():
    #         pass
    #
    # def _create_atlas(self) -> Generator[float, None, None]:
    #     """Create and bind the atlas texture."""
    #     atlas_iter = textureatlas.create_atlas(self._resource_pack.textures)
    #     try:
    #         while True:
    #             yield next(atlas_iter)
    #     except StopIteration as e:
    #         texture_atlas, self._texture_bounds, width, height = e.value
    #     glBindTexture(GL_TEXTURE_2D, self._gl_texture_atlas)
    #     glTexImage2D(
    #         GL_TEXTURE_2D,
    #         0,
    #         GL_RGBA,
    #         width,
    #         height,
    #         0,
    #         GL_RGBA,
    #         GL_UNSIGNED_BYTE,
    #         texture_atlas,
    #     )
    #     glBindTexture(GL_TEXTURE_2D, 0)
    #     log.info("Finished setting up texture atlas in OpenGL")

    @property
    def structure(self) -> LevelGroup:
        """Floating levels that are not the main level."""
        warnings.warn(
            "EditCanvas.structure is depreciated and will be removed in the future. Please used EditCanvas.fake_levels instead",
            DeprecationWarning,
        )
        return self._structure

    @property
    def fake_levels(self) -> LevelGroup:
        """Floating levels that are not the main level."""
        return self._structure

    @property
    def dimension(self) -> Dimension:
        """The currently loaded dimension in the renderer."""
        return self._render_world.dimension

    @dimension.setter
    def dimension(self, dimension: Dimension):
        """Set the currently loaded dimension in the renderer."""
        if dimension != self.dimension:
            self._disable_threads()
            self._render_world.dimension = dimension
            wx.PostEvent(self, DimensionChangeEvent(dimension=dimension))
            self._enable_threads()

    def _on_camera_move(self, evt: CameraMovedEvent):
        """The camera has moved. Update each class's camera state."""
        location = evt.camera_location
        rotation = evt.camera_rotation

        # TODO: add combined methods
        self._render_world.camera_location = location
        self._render_world.camera_rotation = rotation

        self._structure.set_camera_location(*location)
        self._structure.set_camera_rotation(*rotation)

        self._sky_box.set_camera_location(location)

        # self._selection_moved = True
        evt.Skip()

    @property
    def cursor_location(self) -> BlockCoordinates:
        """The location of the cursor box in the world."""
        return self.selection.cursor_position

    def _change_box_location(self):
        if self.camera.projection_mode == Projection.TOP_DOWN:
            position, box_index = self._box_location_closest_2d()
        else:
            if self.selection.reediting:
                position, box_index = self._box_location_distance(self.select_distance2)
            elif self._mouse_lock:
                position, box_index = self._box_location_distance(self.select_distance)
            else:
                position, box_index = self._box_location_closest()
        position = numpy.floor(position).astype(numpy.int64)
        self.selection_location = position.tolist()
        self.selection.set_box_index(box_index)

    def ray_collision(self):
        vector_start = self.camera.location
        direction_vector = self._look_vector()
        min_point, max_point = numpy.sort(self.active_selection_corners, 0)
        max_point += 1

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
        in_air = False

        box_index, nearest_selection_box = self.selection.closest_intersection(
            self.camera.location, self._look_vector()
        )

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
                    chunk = self._render_world.level.get_chunk(cx, cz, self.dimension)
                except ChunkLoadError:
                    chunk = None

            if (
                chunk is not None
                and self._render_world.level.block_palette[
                    chunk.blocks[x % 16, y, z % 16]
                ]
                != UniversalAirBlock
            ):
                # the block is not air
                if in_air:  # if we have previously found an air block
                    return location, None
            elif not in_air:
                in_air = True
        return location, None

    def _box_location_closest_2d(self) -> Tuple[PointCoordinatesNDArray, Optional[int]]:
        x, _, z = self.camera.location
        width, height = self.GetSize()
        z += 2 * self.camera.fov * self._mouse_delta_y / height
        x += (
            2 * self.camera.fov * self.camera.aspect_ratio * self._mouse_delta_x / width
        )
        x, z = numpy.floor([x, z]) + 0.5
        box_index, nearest_selection_box = self.selection.closest_intersection(
            (x, 2 * 32, z), (0, -1, 0)
        )

        sub_chunk_size = self.world.sub_chunk_size
        y = 0
        try:
            chunk = self.world.get_chunk(
                int(x // sub_chunk_size), int(z // sub_chunk_size), self.dimension
            )
        except ChunkLoadError:
            if nearest_selection_box is not None:
                y = nearest_selection_box.max[1] - 1
        else:
            if nearest_selection_box is None:
                box_max = -2 * 32
            else:
                box_max: int = nearest_selection_box.max[1] - 1
            box_max_chunk = int(box_max // sub_chunk_size)
            sub_chunks = sorted(
                [cy for cy in chunk.blocks.sub_chunks if cy >= box_max_chunk],
                reverse=True,
            )
            if sub_chunks:
                dx, dz = (numpy.floor([x, z]) % sub_chunk_size).astype(numpy.int64)
                for sy in sub_chunks:
                    blocks = chunk.blocks.get_section(sy)[
                        dx, ::-1, dz
                    ] != chunk.block_palette.get_add_block(UniversalAirBlock)
                    if numpy.any(blocks):
                        y = (
                            sub_chunk_size
                            - 1
                            - numpy.argmax(blocks)
                            + sy * sub_chunk_size
                        )
                        break
                else:
                    if nearest_selection_box is not None:
                        y = nearest_selection_box.max[1] - 1
                y = max(box_max, y)
            elif nearest_selection_box is not None:
                y = nearest_selection_box.max[1] - 1

        return numpy.asarray((x, y, z)), box_index

    def _box_location_distance(
        self, distance: int
    ) -> Tuple[PointCoordinatesNDArray, Optional[int]]:
        """
        The first block location along the camera's look vector that is further away than `distance`.
        :param distance: The distance between the block and the camera.
        :return: (x, y, z) numpy array, selection box index
        """
        look_vector = self._look_vector()
        position = numpy.array(self.camera.location, dtype=numpy.int) + numpy.floor(
            look_vector * distance
        ).astype(numpy.int)
        box = next(
            (
                index
                for index, box in enumerate(self.selection)
                if box.in_boundary(position)
            ),
            None,
        )
        return position, box

    def _look_vector(self) -> numpy.ndarray:
        """
        The x,y,z vector for the direction the camera is facing
        :return: (x, y, z) numpy float array ranging from -1 to 1
        """
        look_vector = numpy.array([0, 0, 1, 0])
        if not self._mouse_lock:
            screen_x, screen_y = numpy.array(self.GetSize(), numpy.int) / 2
            screen_dx = math.degrees(
                math.atan(
                    self.camera.aspect_ratio
                    * math.tan(math.radians(self.camera.fov / 2))
                    * self._mouse_delta_x
                    / screen_x
                )
            )
            screen_dy = math.degrees(
                math.atan(
                    math.cos(math.radians(screen_dx))
                    * math.tan(math.radians(self.camera.fov / 2))
                    * self._mouse_delta_y
                    / screen_y
                )
            )
            look_vector = numpy.matmul(
                rotation_matrix_xy(math.radians(screen_dy), -math.radians(screen_dx)),
                look_vector,
            )
        ry, rx = self.camera.rotation
        look_vector = numpy.matmul(
            rotation_matrix_xy(*numpy.radians([rx, -ry])), look_vector
        )[:3]
        look_vector[abs(look_vector) < 0.000001] = 0.000001
        return look_vector

    def _collision_locations(
        self, max_distance=100
    ) -> Generator[numpy.ndarray, None, None]:
        """
        The block locations that the camera's look vector passes through.
        :param max_distance: The maximum distance along the look vector to traverse.
        :return: A generator of (x, y, z) numpy arrays
        """
        # TODO: optimise this

        look_vector = self._look_vector()
        dx, dy, dz = look_vector

        vectors = numpy.array(
            [look_vector / abs(dx), look_vector / abs(dy), look_vector / abs(dz)]
        )
        offsets = -numpy.eye(3)

        locations = set()
        start: numpy.ndarray = numpy.array(self.camera.location, numpy.float32) % 1

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
            ) + numpy.floor(self.camera.location).astype(numpy.int)
        else:
            collision_locations = start.astype(numpy.int)

        for location in collision_locations:
            yield location

    def _on_size(self, evt):
        wx.CallAfter(self._set_size)
        evt.Skip()

    def _set_size(self):
        size = self.GetClientSize() * self.GetContentScaleFactor()
        width = size.width
        height = size.height
        self.SetCurrent(self._context)
        glViewport(0, 0, width, height)
        if height > 0:
            self.camera.aspect_ratio = width / height
        else:
            self.camera.aspect_ratio = 1

    def on_draw(self, evt):
        """The default draw logic."""
        self.start_draw()
        if self.camera.projection_mode == Projection.PERSPECTIVE:
            self.draw_sky_box()
        self.draw_level()
        # self.draw_selection()
        self.end_draw()
        # do not call evt.Skip() otherwise the default draw logic will run as well.

    def start_draw(self):
        """Run commands before drawing."""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if self._selection_moved:
            self._selection_moved = False
            self.GetEventHandler().ProcessEvent(CursorMoveEvent())

    def draw_sky_box(self):
        """Draw the skybox."""
        self._sky_box.draw(self.camera.transformation_matrix)

    def draw_level(self):
        """Draw the main level."""
        self._render_world.draw(self.camera.transformation_matrix)

    def draw_fake_levels(self):
        """Draw the floating structure levels."""
        self._structure.draw(self.camera.transformation_matrix)

    def draw_selection(self, draw_selection: bool = True, draw_cursor: bool = True):
        """Draw the selection box."""
        self.selection.draw(
            self.camera.transformation_matrix,
            tuple(self.camera.location),
            draw_selection,
            draw_cursor,
        )

    if ThreadingEnabled:

        def end_draw(self):
            """Run commands after drawing."""
            self.SwapBuffers()

    else:

        def end_draw(self):
            """Run commands after drawing."""
            self.SwapBuffers()
            self.chunk_generator.thread_action()

    def _gc(self, event):
        """Unload data to limit memory usage."""
        self._render_world.run_garbage_collector()
        self._structure.run_garbage_collector()
        event.Skip()

    def _rebuild(self, evt):
        """Rebuild the geometry to reduce draw calls."""
        self._render_world.chunk_manager.rebuild()
        self._structure.rebuild()
        evt.Skip()
