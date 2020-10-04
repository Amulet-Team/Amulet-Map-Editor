from typing import TYPE_CHECKING, Optional
import wx

from .base_ui import BaseUI
from amulet_map_editor.api.wx.ui.simple import SimpleChoiceAny
from amulet_map_editor.programs.edit.canvas.events import (
    EVT_CAMERA_MOVE,
    EVT_UNDO,
    EVT_REDO,
    EVT_CREATE_UNDO,
    EVT_SAVE,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class FilePanel(wx.BoxSizer, BaseUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        BaseUI.__init__(self, canvas)

        self._location_button = wx.Button(
            canvas, label=", ".join([f"{s:.2f}" for s in self.canvas.camera_location])
        )
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

        self._undo_button: Optional[wx.Button] = create_button(
            "Undo", lambda evt: self.canvas.undo()
        )
        self._redo_button: Optional[wx.Button] = create_button(
            "Redo", lambda evt: self.canvas.redo()
        )
        self._save_button: Optional[wx.Button] = create_button(
            "Save", lambda evt: self.canvas.save()
        )
        create_button("Close", lambda evt: self.canvas.close())
        self._update_buttons()

        # self.Fit(self)
        self.Layout()

    def bind_events(self):
        self.canvas.Bind(EVT_CAMERA_MOVE, self._on_camera_move)
        self.canvas.Bind(EVT_UNDO, self._on_update_buttons)
        self.canvas.Bind(EVT_REDO, self._on_update_buttons)
        self.canvas.Bind(EVT_SAVE, self._on_update_buttons)
        self.canvas.Bind(EVT_CREATE_UNDO, self._on_update_buttons)

    def _on_update_buttons(self, evt):
        self._update_buttons()
        evt.Skip()

    def _update_buttons(self):
        self._undo_button.SetLabel(
            f"Undo | {self.canvas.world.history_manager.undo_count}"
        )
        self._redo_button.SetLabel(
            f"Redo | {self.canvas.world.history_manager.redo_count}"
        )
        self._save_button.SetLabel(
            f"Save | {self.canvas.world.history_manager.unsaved_changes}"
        )

    def _on_dimension_change(self, evt):
        """Run when the dimension selection is changed by the user."""
        dimension = self._dim_options.GetCurrentObject()
        if dimension is not None:
            self.canvas.dimension = dimension
        evt.Skip()

    def _change_dimension(self, evt):
        """Run when the dimension attribute in the canvas is changed.
        This is run when the user changes the attribute and when it is changed manually in code."""
        dimension = evt.dimension
        index = self._dim_options.FindString(dimension)
        if not (index == wx.NOT_FOUND or index == self._dim_options.GetSelection()):
            self._dim_options.SetSelection(index)

    def _on_camera_move(self, evt):
        x, y, z = evt.location
        label = f"{x:.2f}, {y:.2f}, {z:.2f}"
        old_label = self._location_button.GetLabel()
        self._location_button.SetLabel(label)
        if len(label) != len(old_label):
            self.canvas.Layout()
