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
from typing import TYPE_CHECKING, Optional, Any, Dict, Tuple, List, Generator
import numpy
import weakref
import math
from concurrent.futures import ThreadPoolExecutor, Future
import time

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
from amulet.api.selection import SelectionGroup

from amulet_map_editor import experimental_bedrock_resources
from amulet_map_editor.api.opengl.data_types import (
    CameraLocationType,
    CameraRotationType,
)
from amulet_map_editor.api.opengl.mesh.level import RenderLevel
from amulet_map_editor.api.opengl.mesh.level_group import LevelGroup
from amulet_map_editor.api.opengl.mesh.sky_box import SkyBox
from amulet_map_editor.api.opengl import textureatlas, ThreadedObjectContainer
from amulet_map_editor.api.opengl.canvas import BaseCanvas, Perspective, Orthographic
from amulet_map_editor.api.opengl.resource_pack.resource_pack import OpenGLResourcePack
from amulet_map_editor.api.opengl.matrix import rotation_matrix_xy
from amulet_map_editor.api.logging import log
from .render_selection import (
    EditProgramRenderSelectionGroup,
    RenderSelectionHistoryManager,
)
from amulet_map_editor.programs.edit.api.ui.canvas.events import (
    CameraMoveEvent,
    CameraRotateEvent,
    DimensionChangeEvent,
    SelectionPointChangeEvent,
)
import amulet_map_editor.programs.edit as amulet_edit

if TYPE_CHECKING:
    from amulet.api.level import World


ThreadingEnabled = True


if ThreadingEnabled:

    class ChunkGenerator(ThreadedObjectContainer, ThreadPoolExecutor):
        def __init__(self):
            ThreadedObjectContainer.__init__(self)
            ThreadPoolExecutor.__init__(self, max_workers=1)
            self._enabled = False
            self._generator: Optional[Future] = None

        def start(self):
            if not self._enabled:
                self._enabled = True
                self._generator = self.submit(self._generate_chunks)

        def stop(self):
            if self._enabled:
                self._enabled = False
                self._generator.result()

        def _generate_chunks(self):
            while self._enabled:
                start_time = time.time()
                while time.time() - start_time < 1 / 120:
                    self.thread_action()
                time.sleep(1 / 60)


else:

    class ChunkGenerator(ThreadedObjectContainer):
        def start(self):
            pass

        def stop(self):
            pass


class BaseEditCanvas(BaseCanvas):
    """Adds base logic for drawing everything related to the edit program to the BaseCanvas.
    All the user interaction code is implemented in ControllableEditCanvas to make them easier to read."""

    background_colour = (0.61, 0.70, 0.85)

    def __init__(self, parent: wx.Window, world: "World", auto_setup=True):
        super().__init__(parent)
        glClearColor(*self.background_colour, 1.0)
        self.Hide()

        self._bound_events: List[Tuple[wx.PyEventBinder, Any, Any]] = []

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

        self._camera_location: CameraLocationType = (0.0, 100.0, 0.0)
        self._camera_rotation: CameraRotationType = (
            45.0,
            45.0,
        )  # yaw (-180 to 180), pitch (-90 to 90)
        self._camera_move_speed = 2.0
        self._camera_rotate_speed = 2.0
        self._selection_location: BlockCoordinates = (0, 0, 0)
        self._select_distance = 10
        self._select_distance2 = 10

        # has the selection point moved and does the box need rebuilding
        self._selection_moved = True

        self._draw_selection = True
        self._selection_group: Optional[RenderSelectionHistoryManager] = None

        self._draw_structure = False
        self._structure: Optional[LevelGroup] = None

        self._sky_box: Optional[SkyBox] = None

        self._chunk_generator = ChunkGenerator()

        self._draw_timer = wx.Timer(self)
        self._gc_timer = wx.Timer(self)
        self._rebuild_timer = wx.Timer(self)

        if auto_setup:
            for _ in self.setup():
                pass

    def setup(self) -> Generator[OperationYieldType, None, None]:
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
                    os.path.dirname(amulet_edit.__file__), "amulet_resource_pack", "bedrock"
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
                    os.path.dirname(amulet_edit.__file__), "amulet_resource_pack", "java"
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
        self._chunk_generator.register(self._render_world)

        self._selection_group = RenderSelectionHistoryManager(
            EditProgramRenderSelectionGroup(
                self, self.context_identifier, self._opengl_resource_pack
            )
        )
        self.world.history_manager.register(self._selection_group, False)

        self._structure: LevelGroup = LevelGroup(
            self.context_identifier,
            self._opengl_resource_pack,
        )
        self._chunk_generator.register(self._structure)

        self._sky_box: Optional[SkyBox] = SkyBox(
            self.context_identifier,
            self._opengl_resource_pack,
        )

        self._bind_base_events()

    def reset_bound_events(self):
        """Unbind all events and re-bind the default events.
        We are allowing users to bind custom events so we should have a way to reset what is bound."""
        handled_events = set()
        for event, handler, source in self._bound_events:
            if source is None:
                if event not in handled_events:
                    handled_events.add(event)
                    super().Unbind(event)
            else:
                if not self.Unbind(event, source, handler=handler):
                    log.error(f"Failed to unbind {event}, {handler}, {source}")
        self._bind_base_events()

    def _bind_base_events(self):
        self.Bind(wx.EVT_TIMER, self._on_draw, self._draw_timer)
        self.Bind(wx.EVT_TIMER, self._gc, self._gc_timer)
        self.Bind(wx.EVT_TIMER, self._rebuild, self._rebuild_timer)

    def Bind(self, event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY):
        """Bind an event to the canvas."""
        self._bound_events.append((event, handler, source))
        super().Bind(event, handler, source, id, id2)

    def Unbind(
        self, event, source=None, id=wx.ID_ANY, id2=wx.ID_ANY, handler=None
    ) -> bool:
        """Unbind an event from the canvas."""
        key = (event, handler, source)
        if key in self._bound_events:
            self._bound_events.remove(key)
        return super().Unbind(event, source=source, id=id, id2=id2, handler=handler)

    @property
    def world(self) -> "World":
        return self._world()

    @property
    def render_distance(self) -> int:
        return self._render_world.render_distance

    @render_distance.setter
    def render_distance(self, render_distance: int):
        self._render_world.render_distance = render_distance

    @property
    def selection_location(self) -> BlockCoordinates:
        return self._selection_location

    @property
    def selection(self) -> EditProgramRenderSelectionGroup:
        return self._selection_group.value

    @property
    def selection_group(self) -> SelectionGroup:
        """Create a SelectionGroup class from the selected boxes."""
        return self.selection.create_selection_group()

    @property
    def active_selection_corners(self) -> Tuple[BlockCoordinates, BlockCoordinates]:
        """Get the bounds of the selection box that is currently active.
        Will be all 0 if no selection box exists.
        The second value will be one less than the actual top edge.
        This is the same as box selection in game works and solves some other issues."""
        return self.selection.active_selection_corners

    @active_selection_corners.setter
    def active_selection_corners(
        self, box_corners: Tuple[BlockCoordinates, BlockCoordinates]
    ):
        self.selection.active_selection_corners = box_corners

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
        self._chunk_generator.stop()

    def _enable_threads(self):
        """Start the generation of new chunk geometry."""
        self._chunk_generator.start()

    def close(self):
        """Close and destroy the canvas and all contained data."""
        self._render_world.close()
        self._structure.clear()
        super()._close()

    def is_closeable(self):
        """Check that the canvas and contained data is safe to be closed."""
        return self._render_world.is_closeable()

    def _load_resource_pack(self, *resource_packs: JavaResourcePack):
        self._resource_pack = JavaResourcePackManager(resource_packs)
        for _ in self._create_atlas():
            pass

    def _create_atlas(self) -> Generator[float, None, None]:
        """Create and bind the atlas texture."""
        atlas_iter = textureatlas.create_atlas(self._resource_pack.textures)
        try:
            while True:
                yield next(atlas_iter)
        except StopIteration as e:
            texture_atlas, self._texture_bounds, width, height = e.value
        glBindTexture(GL_TEXTURE_2D, self._gl_texture_atlas)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGBA,
            width,
            height,
            0,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            texture_atlas,
        )
        glBindTexture(GL_TEXTURE_2D, 0)
        log.info("Finished setting up texture atlas in OpenGL")

    @property
    def structure(self) -> LevelGroup:
        return self._structure

    @property
    def draw_structure(self) -> bool:
        """Should the moveable structure be drawn"""
        return self._draw_structure

    @draw_structure.setter
    def draw_structure(self, draw_structure: bool):
        self._draw_structure = bool(draw_structure)

    @property
    def draw_selection(self) -> bool:
        """Should the selection box(es) be drawn"""
        return self._draw_selection

    @draw_selection.setter
    def draw_selection(self, draw_selection: bool):
        self._draw_selection = bool(draw_selection)

    @property
    def selection_editable(self) -> bool:
        """Should the selection box(es) be editable"""
        return self.selection.editable

    @selection_editable.setter
    def selection_editable(self, selection_editable: bool):
        self.selection.editable = bool(selection_editable)

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

    @property
    def camera_location(self) -> CameraLocationType:
        return self._camera_location

    @camera_location.setter
    def camera_location(self, location: CameraLocationType):
        assert len(location) == 3 and all(
            isinstance(v, (int, float)) for v in location
        ), "format for camera_location is invalid"
        self._camera_location = self._render_world.camera_location = location
        self._structure.set_camera_location(*location)
        self._sky_box.set_camera_location(location)
        self._transformation_matrix = None
        self._selection_moved = True
        wx.PostEvent(self, CameraMoveEvent(location=self.camera_location))

    @property
    def camera_rotation(self) -> CameraRotationType:
        """The rotation of the camera. (yaw, pitch).
        This should behave the same as how Minecraft handles it.
        """
        return self._camera_rotation

    @camera_rotation.setter
    def camera_rotation(self, rotation: CameraRotationType):
        """Set the rotation of the camera. (yaw, pitch).
        This should behave the same as how Minecraft handles it.
        """
        assert len(rotation) == 2 and all(
            isinstance(v, (int, float)) for v in rotation
        ), "format for camera_rotation is invalid"
        self._camera_rotation = self._render_world.camera_rotation = rotation
        self._structure.set_camera_rotation(*rotation)
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

    @property
    def cursor_location(self) -> BlockCoordinates:
        """The location of the cursor box in the world."""
        return self.selection.cursor_position

    def _change_box_location(self):
        if self.projection_mode == Orthographic:
            position, box_index = self._box_location_closest_2d()
        else:
            if self.selection.reediting:
                position, box_index = self._box_location_distance(self.select_distance2)
            elif self._mouse_lock:
                position, box_index = self._box_location_distance(self.select_distance)
            else:
                position, box_index = self._box_location_closest()
        position = numpy.floor(position).astype(numpy.int64)
        self._selection_location = position.tolist()
        wx.PostEvent(self, SelectionPointChangeEvent(location=self._selection_location))
        self.selection.update_cursor_position(position, box_index)

    def ray_collision(self):
        vector_start = self.camera_location
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
            self.camera_location, self._look_vector()
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
        x, _, z = self.camera_location
        width, height = self.GetSize()
        z += 2 * self.fov * self._mouse_delta_y / height
        x += 2 * self.fov * self.aspect_ratio * self._mouse_delta_x / width
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
        position = numpy.array(self.camera_location, dtype=numpy.int) + numpy.floor(
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
                    self.aspect_ratio
                    * math.tan(math.radians(self.fov / 2))
                    * self._mouse_delta_x
                    / screen_x
                )
            )
            screen_dy = math.degrees(
                math.atan(
                    math.cos(math.radians(screen_dx))
                    * math.tan(math.radians(self.fov / 2))
                    * self._mouse_delta_y
                    / screen_y
                )
            )
            look_vector = numpy.matmul(
                rotation_matrix_xy(math.radians(screen_dy), -math.radians(screen_dx)),
                look_vector,
            )
        ry, rx = self.camera_rotation
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
        self.DoSetSize(
            0, 0, width, height, 0
        )  # I don't know if this is how you are supposed to do this

    def _on_draw(self, event):
        self.draw()
        event.Skip()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if self.projection_mode == Perspective:
            self._sky_box.draw(self.transformation_matrix)
        self._render_world.draw(self.transformation_matrix)
        if self._draw_structure:
            self._structure.draw(self.transformation_matrix)
        if self._selection_moved:
            self._selection_moved = False
            self._change_box_location()
        self.selection.draw(
            self.transformation_matrix, tuple(self.camera_location), self.draw_selection
        )
        self.SwapBuffers()
        if not ThreadingEnabled:
            self._chunk_generator.thread_action()

    def _gc(self, event):
        self._render_world.run_garbage_collector()
        self._structure.run_garbage_collector()
        event.Skip()

    def _rebuild(self, evt):
        self._render_world.chunk_manager.rebuild()
        self._structure.rebuild()
        evt.Skip()
