from typing import TYPE_CHECKING, Optional
import wx
from OpenGL.GL import (
    glClear,
    GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT,
)

from amulet.api.data_types import Dimension

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.api.opengl.mesh.level import RenderLevel
from amulet_map_editor.api.opengl.mesh.level_group import LevelGroup
from amulet_map_editor.api.opengl.mesh.sky_box import SkyBox
from amulet_map_editor.api.opengl.resource_pack.resource_pack import OpenGLResourcePack

from .chunk_generator import ThreadingEnabled, ChunkGenerator
from .edit_canvas_container import EditCanvasContainer
from .events import (
    DimensionChangeEvent,
    CameraMovedEvent,
    EVT_CAMERA_MOVED,
    PreDrawEvent,
    DrawEvent,
    PostDrawEvent,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class Renderer(EditCanvasContainer):
    """This class holds the drawable objects and has methods to draw them."""

    __slots__ = (
        "_render_distance",
        "_chunk_generator",
        "_opengl_resource_pack",
        "_render_world",
        "_chunk_generator",
        "_fake_levels",
        "_sky_box",
        "_draw_timer",
        "_gc_timer",
    )

    _sky_box: Optional[SkyBox]
    _fake_levels: Optional[LevelGroup]

    def __init__(
        self,
        canvas: "EditCanvas",
        world,
        context_identifier: str,
        opengl_resource_pack: OpenGLResourcePack,
    ):
        super().__init__(canvas)
        self._render_distance = 5

        self._chunk_generator = ChunkGenerator()
        self._opengl_resource_pack = opengl_resource_pack

        self._render_world = RenderLevel(
            context_identifier,
            opengl_resource_pack,
            world,
            draw_floor=True,
            draw_ceil=True,
        )
        self._chunk_generator.register(self._render_world)

        self._fake_levels = None
        self._sky_box = None

        self._draw_timer = wx.Timer(self.canvas)
        self._gc_timer = wx.Timer(self.canvas)

    def bind_events(self):
        """Set up all events required to run."""
        self.canvas.Bind(wx.EVT_TIMER, self._gc, self._gc_timer)
        self.canvas.Bind(
            wx.EVT_TIMER,
            self._do_draw,
            self._draw_timer,
        )
        self.canvas.Bind(EVT_CAMERA_MOVED, self._on_camera_moved)
        self.canvas.Bind(wx.EVT_WINDOW_DESTROY, self._on_destroy, self.canvas)

    def enable(self):
        """Enable and start working."""
        self.enable_threads()

    def disable(self):
        """Disable and unload all geometry."""
        self.disable_threads()
        self.render_world.unload()
        self.fake_levels.unload()

    def _on_destroy(self, evt):
        self.disable()
        evt.Skip()

    def is_closeable(self):
        """Check that the data is safe to be closed."""
        return self.render_world.is_closeable()

    def close(self):
        """Close and destroy all data."""
        self.render_world.close()
        self.fake_levels.clear()
        self.sky_box.unload()

    def disable_threads(self):
        """Stop the generation of new chunk geometry.
        Makes it safe to modify the world data."""
        self._draw_timer.Stop()
        self._gc_timer.Stop()
        self._chunk_generator.stop()

    def enable_threads(self):
        """Start the generation of new chunk geometry."""
        self.render_world.enable()
        self.fake_levels.enable()
        self._chunk_generator.start()
        self._draw_timer.Start(15)
        self._gc_timer.Start(10000)

    # TODO: move this logic into a resource pack reload method
    # def _load_resource_pack(self, *resource_packs: JavaResourcePack):
    #     self._resource_pack = JavaResourcePackManager(resource_packs)
    #     for _ in self._create_atlas():
    #         pass

    @property
    def opengl_resource_pack(self) -> OpenGLResourcePack:
        return self._opengl_resource_pack

    @property
    def render_world(self) -> RenderLevel:
        return self._render_world

    @property
    def fake_levels(self) -> LevelGroup:
        """Floating levels that are not the main level."""
        if self._fake_levels is None:
            self._fake_levels: LevelGroup = LevelGroup(
                self.canvas.context_identifier,
                self.opengl_resource_pack,
            )
            self._chunk_generator.register(self._fake_levels)
        return self._fake_levels

    @property
    def sky_box(self) -> SkyBox:
        """The cube in the distance displaying the sky."""
        if self._sky_box is None:
            self._sky_box = SkyBox(
                self._render_world.context_identifier,
                self._opengl_resource_pack,
            )
        return self._sky_box

    @property
    def dimension(self) -> Dimension:
        """The currently loaded dimension in the renderer."""
        return self.render_world.dimension

    @dimension.setter
    def dimension(self, dimension: Dimension):
        """Set the currently loaded dimension in the renderer."""
        if dimension != self.dimension:
            self.disable_threads()
            self.render_world.dimension = dimension
            wx.PostEvent(self.canvas, DimensionChangeEvent(dimension=dimension))
            self.enable_threads()

    @property
    def render_distance(self) -> int:
        """The distance from the camera in chunks that should be drawn"""
        return self._render_distance

    @render_distance.setter
    def render_distance(self, render_distance: int):
        """Set the distance from the camera in chunks that should be drawn"""
        self._render_distance = render_distance
        self.render_world.render_distance = render_distance
        # self.fake_levels.render_distance = render_distance  # TODO

    def _on_camera_moved(self, evt: CameraMovedEvent):
        """The camera has moved. Update each class's camera state."""
        self.move_camera(evt.camera_location, evt.camera_rotation)
        evt.Skip()

    def move_camera(self, location, rotation):
        # TODO: add combined methods
        self.render_world.camera_location = location
        self.render_world.camera_rotation = rotation

        self.fake_levels.set_camera_location(*location)
        self.fake_levels.set_camera_rotation(*rotation)

        self.sky_box.set_camera_location(location)

    def _do_draw(self, evt):
        wx.PostEvent(self.canvas, PreDrawEvent())
        wx.PostEvent(self.canvas, DrawEvent())
        wx.PostEvent(self.canvas, PostDrawEvent())

    def default_draw(self):
        """The default draw logic."""
        self.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.draw_level()
        self.end_draw()

    def start_draw(self):
        """Run commands before drawing."""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def draw_sky_box(self):
        """Draw the skybox."""
        self.sky_box.draw(self.canvas.camera.transformation_matrix)

    def draw_level(self):
        """Draw the main level."""
        self.render_world.draw(self.canvas.camera.transformation_matrix)

    def draw_fake_levels(self):
        """Draw the floating structure levels."""
        self.fake_levels.draw(self.canvas.camera.transformation_matrix)

    if ThreadingEnabled:

        def end_draw(self):
            """Run commands after drawing."""
            self.canvas.SwapBuffers()

    else:

        def end_draw(self):
            """Run commands after drawing."""
            self.canvas.SwapBuffers()
            self._chunk_generator.thread_action()

    def _gc(self, event):
        """Unload data to limit memory usage."""
        self.render_world.run_garbage_collector()
        self.fake_levels.run_garbage_collector()
        event.Skip()
