import wx
from typing import TYPE_CHECKING, Optional
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)

from amulet.operations.paste import paste_iter

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.api.opengl.mesh.level import RenderLevel

from amulet_map_editor.programs.edit.api.ui.tool import CameraToolUI
from amulet_map_editor.programs.edit.api.events import EVT_PASTE
from amulet_map_editor.programs.edit.api.ui.select_location import SelectTransformUI, TransformChangeEvent, EVT_TRANSFORM_CHANGE

from amulet_map_editor.programs.edit.api.behaviour import StaticSelectionBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class PasteTool(wx.BoxSizer, CameraToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        CameraToolUI.__init__(self, canvas)

        self._selection = StaticSelectionBehaviour(self.canvas)

        self._button_panel = wx.Panel(canvas)
        self._button_sizer = wx.BoxSizer(wx.VERTICAL)
        self._button_panel.SetSizer(self._button_sizer)
        self.Add(self._button_panel, 0, wx.ALIGN_CENTER_VERTICAL)

        self._paste_panel = SelectTransformUI(self._button_panel)
        self._paste_panel.Bind(EVT_TRANSFORM_CHANGE, self._on_transform_change)
        self._button_sizer.Add(self._paste_panel, 0, wx.EXPAND)

        confirm_button = wx.Button(self._button_panel, label="Confirm")
        self._button_sizer.Add(confirm_button, 0, wx.ALL | wx.EXPAND, 5)
        confirm_button.Bind(wx.EVT_BUTTON, self._paste_confirm)

        self._button_panel.Disable()
        self.Layout()

    @property
    def name(self) -> str:
        return "Paste"

    def bind_events(self):
        super().bind_events()
        self._selection.bind_events()
        self.canvas.Bind(EVT_PASTE, self._paste)

    def enable(self):
        super().enable()
        self._selection.update_selection()

    def disable(self):
        super().disable()
        self._button_panel.Disable()
        self.canvas.renderer.fake_levels.clear()

    def _on_transform_change(self, evt: TransformChangeEvent):
        self.canvas.renderer.fake_levels.active_transform = (
            evt.location,
            evt.scale,
            evt.rotation_radians,
        )
        evt.Skip()

    def _paste(self, evt):
        self._button_panel.Enable()
        structure = evt.structure
        dimension = evt.dimension
        self.canvas.renderer.fake_levels.clear()
        self.canvas.renderer.fake_levels.append(
            structure, dimension, (0, 0, 0), (1, 1, 1), (0, 0, 0)
        )

    def _paste_confirm(self, evt):
        fake_levels = self.canvas.renderer.fake_levels
        level_index: int = fake_levels.active_level_index
        if level_index is not None:
            render_level: RenderLevel = fake_levels.render_levels[level_index]
            self.canvas.run_operation(
                lambda: paste_iter(
                    self.canvas.world,
                    self.canvas.dimension,
                    render_level.level,
                    render_level.dimension,
                    self._paste_panel.location,
                    self._paste_panel.scale,
                    self._paste_panel.rotation,
                    self._paste_panel.copy_air,
                    self._paste_panel.copy_water,
                    self._paste_panel.copy_lava,
                )
            )

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self.canvas.renderer.draw_fake_levels()
        self._selection.draw()
        self.canvas.renderer.end_draw()
