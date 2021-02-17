import wx
from typing import TYPE_CHECKING, Optional
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)

from amulet.operations.paste import paste_iter

from amulet_map_editor.api.opengl.camera import Projection

from amulet_map_editor.programs.edit.api.ui.tool import CameraToolUI
from amulet_map_editor.programs.edit.api.events import EVT_PASTE
from amulet_map_editor.programs.edit.api.ui.select_location import SelectTransformUI

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
        paste_button = wx.Button(self._button_panel, label="Paste")
        self._button_sizer.Add(paste_button, 0, wx.ALL | wx.EXPAND, 5)
        paste_button.Bind(wx.EVT_BUTTON, lambda evt: self.canvas.paste_from_cache())
        self.Add(self._button_panel, 0, wx.ALIGN_CENTER_VERTICAL)

        self._paste_panel: Optional[SelectTransformUI] = None
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
        self.canvas.renderer.fake_levels.unload()

    def _remove_paste(self):
        if self._paste_panel is not None:
            self._paste_panel.Destroy()
            self._paste_panel = None

    def _paste(self, evt):
        structure = evt.structure
        dimension = evt.dimension
        self._remove_paste()
        self._paste_panel = SelectTransformUI(
            self._button_panel, self.canvas, structure, dimension, self._paste_confirm
        )
        self._button_sizer.Add(self._paste_panel, 0, wx.EXPAND)
        self.Layout()

    def _paste_confirm(self):
        self.canvas.run_operation(
            lambda: paste_iter(
                self.canvas.world,
                self.canvas.dimension,
                self._paste_panel.structure,
                self._paste_panel.dimension,
                self._paste_panel.location,
                (1, 1, 1),
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
