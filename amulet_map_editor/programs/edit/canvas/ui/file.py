from typing import TYPE_CHECKING, Optional
import wx

from .base_ui import BaseUI
from amulet_map_editor.amulet_wx.simple import SimpleChoiceAny

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class FilePanel(wx.BoxSizer, BaseUI):
    def __init__(self, canvas: 'EditCanvas'):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        BaseUI.__init__(self, canvas)

        self._location_button = wx.Button(canvas, label=', '.join([f'{s:.2f}' for s in self._canvas().camera_location]))
        self._location_button.Bind(wx.EVT_BUTTON, lambda evt: self.canvas.goto())

        self.Add(self._location_button, 0, wx.TOP | wx.BOTTOM | wx.RIGHT | wx.CENTER, 5)

        self._dim_options = SimpleChoiceAny(canvas)
        self._dim_options.SetItems(self.canvas.world.world_wrapper.dimensions)
        self._dim_options.SetValue("overworld")
        self._dim_options.Bind(wx.EVT_CHOICE, self._on_dimension_change)

        self.Add(self._dim_options, 0, wx.TOP | wx.BOTTOM | wx.RIGHT | wx.CENTER, 5)

        def create_button(text, operation):
            button = wx.Button(canvas, label=text)
            button.Bind(wx.EVT_BUTTON, operation)
            self.Add(button, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)
            return button

        self._undo_button: Optional[wx.Button] = create_button('Undo', lambda evt: self.canvas.undo())
        self._redo_button: Optional[wx.Button] = create_button('Redo', lambda evt: self.canvas.redo())
        self._save_button: Optional[wx.Button] = create_button('Save', lambda evt: self.canvas.save())
        create_button('Close', lambda evt: self.canvas.close())
        self.update_buttons()

        # self.Fit(self)
        self.Layout()

    def update_buttons(self):
        self._undo_button.SetLabel(f"Undo | {self.canvas.world.chunk_history_manager.undo_count}")
        self._redo_button.SetLabel(f"Redo | {self.canvas.world.chunk_history_manager.redo_count}")
        self._save_button.SetLabel(f"Save | {self.canvas.world.chunk_history_manager.unsaved_changes}")

    def _on_dimension_change(self, evt):
        self.change_dimension()
        evt.Skip()

    def change_dimension(self):
        dimension = self._dim_options.GetAny()
        if dimension is not None:
            self.canvas.dimension = dimension

    def move_event(self, evt):
        x, y, z = evt.location
        self._location_button.SetLabel(f'{x:.2f}, {y:.2f}, {z:.2f}')
        self.Layout()
        self.canvas.Layout()
