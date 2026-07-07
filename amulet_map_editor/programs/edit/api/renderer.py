from typing import TYPE_CHECKING, Optional, Dict, Tuple, Any
import math
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

from amulet_map_editor.programs.edit.api.overview.scanner import OverviewScanner
from amulet_map_editor.programs.edit.api.overview.gl_layer import OverviewLayer

from .chunk_generator import ChunkGenerator
from .edit_canvas_container import EditCanvasContainer
from .events import (
    DimensionChangeEvent,
    CameraMovedEvent,
    EVT_CAMERA_MOVED,
    PreDrawEvent,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


# In top-down mode, suppress the 3D detail layer when zoomed out beyond this
# orthographic half-height (in blocks): at ~256 a block is ~2 screen pixels
# on a 1080p display, so the overview tiles carry all visible information.
DETAIL_MAX_ORTHO_FOV = 256.0

# valid values for Renderer.topdown_detail_mode
TOPDOWN_DETAIL_MODES = ("never", "zoomed_in", "always")


class Renderer(EditCanvasContainer):
    """This class holds the drawable objects and has methods to draw them."""

    __slots__ = (
        "_render_distance",
        "_chunk_generator",
        "_opengl_resource_pack",
        "_render_world",
        "_fake_levels",
        "_sky_box",
        "_draw_timer",
        "_gc_timer",
        "_overview_scanner",
        "_overview_layer",
        "_overview_enabled",
        "_topdown_detail_mode",
        "_notified_changes",
        "_world_change_pending",
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

        # Importing EDIT_CONFIG_ID from amulet_map_editor.programs.edit.edit here
        # would be fragile: edit.py imports EditCanvas, which imports
        # BaseEditCanvas, which imports this module, so a module-level import
        # back into edit.py only works because of import ordering within
        # edit.py. To avoid relying on that, use the literal config id.
        # EDIT_CONFIG_ID is defined in
        # amulet_map_editor/programs/edit/edit.py as "amulet_edit".
        from amulet_map_editor.api import config as config_api

        worker_count = (
            config_api.get("amulet_edit", {})
            .get("options", {})
            .get("chunk_worker_count")
        )
        self._chunk_generator = ChunkGenerator(worker_count=worker_count)
        self._opengl_resource_pack = opengl_resource_pack

        self._render_world = RenderLevel(
            context_identifier,
            opengl_resource_pack,
            world,
            draw_floor=True,
            draw_ceil=True,
        )
        self._chunk_generator.register_parallel(self._render_world.thread_action)

        self._overview_enabled = True
        self._topdown_detail_mode = "never"
        #: last-seen changed_time per changed chunk, so world_changed does
        #: not re-notify unchanged chunks. Cleared on dimension change.
        self._notified_changes: Dict[Tuple[int, int], Any] = {}
        #: set by world_changed() (UI thread); drained by
        #: _process_world_changes() on the worker pool.
        self._world_change_pending = False
        dimension = self._render_world.dimension
        self._overview_scanner = OverviewScanner(world, dimension, opengl_resource_pack)
        self._overview_layer = OverviewLayer(
            context_identifier,
            opengl_resource_pack,
            self._overview_scanner,
            world.bounds(dimension).min_y,
        )
        # Registration order sets pool priority: process pending edits after
        # the render world's own work but ahead of the overview scanner.
        self._chunk_generator.register_parallel(self._process_world_changes)
        self._chunk_generator.register_parallel(self._overview_scanner.scan_next)
        self._render_world.on_chunk_changed = self._overview_scanner.mark_chunk_changed

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
        self._overview_scanner.flush()
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
        self._overview_layer.unload()
        self._overview_scanner.flush()
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
        self._gc_timer.Start(2000)

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
    def overview_scanner(self) -> OverviewScanner:
        return self._overview_scanner

    @property
    def overview_enabled(self) -> bool:
        """Should the whole-world overview draw in top-down mode."""
        return self._overview_enabled

    @overview_enabled.setter
    def overview_enabled(self, enabled: bool):
        self._overview_enabled = bool(enabled)

    @property
    def topdown_detail_mode(self) -> str:
        """When the 3D detail layer is drawn on top of the overview in
        top-down mode. One of "never" (map only, the default), "zoomed_in"
        (only below the ortho zoom threshold) or "always"."""
        return self._topdown_detail_mode

    @topdown_detail_mode.setter
    def topdown_detail_mode(self, mode: str):
        if mode not in TOPDOWN_DETAIL_MODES:
            raise ValueError(
                f"topdown_detail_mode must be one of {TOPDOWN_DETAIL_MODES}, "
                f"got {mode!r}"
            )
        self._topdown_detail_mode = mode

    @property
    def detail_ortho_threshold(self) -> float:
        """The orthographic half-height below which the 3D detail layer is
        shown in top-down mode (compared against camera.orthographic_fov).

        "never" -> -1.0 (fov is always > -1, so detail is always suppressed),
        "zoomed_in" -> DETAIL_MAX_ORTHO_FOV, "always" -> +inf.
        """
        mode = self._topdown_detail_mode
        if mode == "never":
            return -1.0
        elif mode == "always":
            return float("inf")
        return DETAIL_MAX_ORTHO_FOV

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
            # changed-chunk coords are per-dimension; drop the dedupe cache.
            # Rebind (GIL-atomic) rather than .clear() so a worker mid-read of
            # _process_world_changes never sees a dict mutating under it.
            self._notified_changes = {}
            self.render_world.dimension = dimension
            self._overview_scanner.set_dimension(dimension)
            self._overview_layer.set_min_y(
                self.render_world.level.bounds(dimension).min_y
            )
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

        self._overview_scanner.set_camera_chunk(
            math.floor(location[0]) >> 4, math.floor(location[2]) >> 4
        )

    def _do_draw(self, evt):
        wx.PostEvent(self.canvas, PreDrawEvent())
        self.canvas.Refresh(False)

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
        camera = self.canvas.camera
        if camera.projection_mode == Projection.TOP_DOWN:
            detail_visible = (
                not self._overview_enabled
                or camera.orthographic_fov <= self.detail_ortho_threshold
            )
            self._render_world.detail_enabled = detail_visible
            half_z = camera.orthographic_fov * 1.1 + 16
            half_x = half_z * camera.aspect_ratio + 16
            if self._overview_enabled:
                self._overview_layer.draw(
                    camera.transformation_matrix,
                    camera.location,
                    half_x,
                    half_z,
                )
            if detail_visible:
                cam_cx, cam_cz = (
                    math.floor(camera.location[0]) >> 4,
                    math.floor(camera.location[2]) >> 4,
                )
                margin = (int(half_x) >> 4) + 1, (int(half_z) >> 4) + 1
                visible_rect = (
                    cam_cx - margin[0],
                    cam_cz - margin[1],
                    cam_cx + margin[0],
                    cam_cz + margin[1],
                )
                self.render_world.draw(camera.transformation_matrix, visible_rect)
        else:
            self._render_world.detail_enabled = True
            cam_cx = math.floor(camera.location[0]) >> 4
            cam_cz = math.floor(camera.location[2]) >> 4
            margin = self._render_distance + 5
            visible_rect = (
                cam_cx - margin,
                cam_cz - margin,
                cam_cx + margin,
                cam_cz + margin,
            )
            self.render_world.draw(camera.transformation_matrix, visible_rect)

    def draw_fake_levels(self):
        """Draw the floating structure levels."""
        self.fake_levels.draw(self.canvas.camera.transformation_matrix)

    def end_draw(self):
        """Run commands after drawing."""
        self.canvas.SwapBuffers()

    def world_changed(self):
        """Notify the renderer that world data changed (operation/undo/redo).

        Called from the UI thread; only sets a flag. The actual scan over
        level.chunks.changed_chunks() runs on the worker pool via
        _process_world_changes, so a large unsaved-edit backlog never hitches
        the UI thread or re-inflates GC-unloaded chunks synchronously.
        """
        self._world_change_pending = True

    def _process_world_changes(self) -> bool:
        """Drain a pending world_changed() notification on the worker pool.

        Feeds precisely-known changed chunks to both the overview scanner
        and the 3D detail layer. Chunks stay in level.chunks.changed_chunks()
        until the world is saved, so re-notification is deduplicated by the
        chunk's changed_time.

        Returns True if a pending notification was processed, False if there
        was nothing to do. The flag read/clear is GIL-atomic; a re-set during
        processing simply triggers another pass on the next pool cycle.
        """
        if not self._world_change_pending:
            return False
        self._world_change_pending = False

        from amulet.api.errors import ChunkDoesNotExist, ChunkLoadError

        dimension = self.render_world.dimension
        for dim, cx, cz in self.render_world.level.chunks.changed_chunks():
            if dim != dimension:
                continue
            try:
                changed_time = self.render_world.level.get_chunk(
                    cx, cz, dim
                ).changed_time
            except ChunkDoesNotExist:
                changed_time = None  # deleted chunk: cheap to rescan every wave
            except ChunkLoadError:
                continue
            key = (cx, cz)
            if (
                changed_time is not None
                and self._notified_changes.get(key) == changed_time
            ):
                continue
            self._notified_changes[key] = changed_time
            self._overview_scanner.mark_chunk_changed(key)
            self.render_world.mark_chunk_stale(key)
        return True

    def _gc(self, event):
        """Unload data to limit memory usage."""
        self.render_world.run_garbage_collector()
        self.fake_levels.run_garbage_collector()
        event.Skip()
