import wx
from OpenGL.GL import *
import os
from typing import TYPE_CHECKING, Optional, Any, Dict, Tuple, List, Generator
import numpy
import weakref

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
from amulet.api.block import Block
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
from amulet_map_editor.api.opengl.mesh.world_renderer.world import (
    RenderWorld,
    cos,
    tan,
    atan,
)
from amulet_map_editor.api.opengl.mesh.structure import StructureGroup
from amulet_map_editor.api.opengl import textureatlas
from amulet_map_editor.api.opengl.canvas.base import BaseCanvas
from amulet_map_editor.api.opengl.resource_pack.resource_pack import OpenGLResourcePack
from amulet_map_editor.api.logging import log
from .render_selection import (
    EditProgramRenderSelectionGroup,
    RenderSelectionHistoryManager,
)
from amulet_map_editor.programs.edit.canvas.events import (
    CameraMoveEvent,
    CameraRotateEvent,
    DimensionChangeEvent,
    SelectionPointChangeEvent,
)

if TYPE_CHECKING:
    from amulet.api.world import World


AIR = Block("universal_minecraft", "air")


class BaseEditCanvas(BaseCanvas):
    """Adds base logic for drawing everything related to the edit program to the BaseCanvas.
    All the user interaction code is implemented in ControllableEditCanvas to make them easier to read."""

    background_colour = (0.5, 0.66, 1.0)

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

        self._render_world = None

        self._camera_location: CameraLocationType = (0.0, 100.0, 0.0)
        self._camera_rotation: CameraRotationType = (45.0, 45.0)
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
        self._structure: Optional[StructureGroup] = None

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
            self.world.world_wrapper.platform == "bedrock"
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
                    os.path.dirname(__file__), "..", "amulet_resource_pack", "bedrock"
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
                    os.path.dirname(__file__), "..", "amulet_resource_pack", "java"
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

        self._render_world = RenderWorld(
            self.context_identifier, self._opengl_resource_pack, self.world,
        )

        self._selection_group = RenderSelectionHistoryManager(
            EditProgramRenderSelectionGroup(
                self, self.context_identifier, self._opengl_resource_pack
            )
        )
        self.world.history_manager.register(self._selection_group, False)

        self._structure: StructureGroup = StructureGroup(
            self.context_identifier, self._opengl_resource_pack,
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
        self._draw_timer.Start(33)
        self._gc_timer.Start(10000)
        self._rebuild_timer.Start(1000)

    def disable(self):
        """Disable the canvas and unload all geometry."""
        self._draw_timer.Stop()
        self._gc_timer.Stop()
        self._rebuild_timer.Stop()
        self._render_world.disable()

    def _disable_threads(self):
        """Stop the generation of new chunk geometry.
        Makes it safe to modify the world data."""
        self._render_world.chunk_generator.stop()

    def _enable_threads(self):
        """Start the generation of new chunk geometry."""
        self._render_world.chunk_generator.start()

    def close(self):
        """Close and destroy the canvas and all contained data."""
        self._render_world.close()
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
    def structure(self) -> StructureGroup:
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
        assert len(location) == 3 and all(
            isinstance(v, (int, float)) for v in location
        ), "format for camera_location is invalid"
        self._camera_location = self._render_world.camera_location = location
        self._transformation_matrix = None
        self._selection_moved = True
        wx.PostEvent(self, CameraMoveEvent(location=self.camera_location))

    @property
    def camera_rotation(self) -> CameraRotationType:
        return self._camera_rotation

    @camera_rotation.setter
    def camera_rotation(self, rotation: CameraRotationType):
        assert len(rotation) == 2 and all(
            isinstance(v, (int, float)) for v in rotation
        ), "format for camera_rotation is invalid"
        self._camera_rotation = self._render_world.camera_rotation = rotation
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
        if self.selection.reediting:
            position, box_index = self._box_location_distance(self.select_distance2)
        elif self._mouse_lock:
            position, box_index = self._box_location_distance(self.select_distance)
        else:
            position, box_index = self._box_location_closest()
        self._selection_location = position.tolist()
        wx.PostEvent(self, SelectionPointChangeEvent(location=position.tolist()))
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
                    chunk = self._render_world.world.get_chunk(cx, cz, self.dimension)
                except ChunkLoadError:
                    chunk = None

            if (
                chunk is not None
                and self._render_world.world.palette[chunk.blocks[x % 16, y, z % 16]]
                != AIR
            ):
                # the block is not air
                if in_air:  # if we have previously found an air block
                    return location, None
            elif not in_air:
                in_air = True
        return location, None

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
        look_vector = numpy.array([0, 0, -1, 0])
        if not self._mouse_lock:
            screen_x, screen_y = numpy.array(self.GetSize(), numpy.int) / 2
            screen_dx = atan(
                self.aspect_ratio * tan(self.fov / 2) * self._mouse_delta_x / screen_x
            )
            screen_dy = atan(
                cos(screen_dx) * tan(self.fov / 2) * self._mouse_delta_y / screen_y
            )
            look_vector = numpy.matmul(
                self.rotation_matrix(screen_dy, screen_dx), look_vector
            )
        look_vector = numpy.matmul(
            self.rotation_matrix(*self.camera_rotation), look_vector
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

    def _gc(self, event):
        self._render_world.run_garbage_collector()
        event.Skip()

    def _rebuild(self, evt):
        self._render_world.chunk_manager.rebuild()
        evt.Skip()
