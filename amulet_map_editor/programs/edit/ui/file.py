from typing import TYPE_CHECKING, Optional
import wx
import weakref

from .goto import show_goto
from amulet_map_editor.amulet_wx.simple import SimpleChoiceAny

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas.controllable_canvas import ControllableEditCanvas


class FilePanel(wx.Panel):
    def __init__(self, canvas: 'ControllableEditCanvas', world, undo_evt, redo_evt, save_evt, close_evt):
        wx.Panel.__init__(self, canvas)
        self._canvas = weakref.ref(canvas)
        self._world = weakref.ref(world)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self._location_button = wx.Button(self, label=', '.join([f'{s:.2f}' for s in self._canvas().camera_location]))
        self._location_button.Bind(wx.EVT_BUTTON, lambda evt: self.show_goto())

        top_sizer.Add(self._location_button, 0, wx.ALL | wx.CENTER, 5)

        dim_label = wx.StaticText(self, label="Dimension:")
        self._dim_options = SimpleChoiceAny(self)
        self._dim_options.SetItems(dict(zip(self._world().world_wrapper.dimensions.values(), self._world().world_wrapper.dimensions.keys())))
        self._dim_options.SetValue("overworld")
        self._dim_options.Bind(wx.EVT_CHOICE, self._on_dimension_change)

        top_sizer.Add(dim_label, 0, wx.ALL | wx.CENTER, 5)
        top_sizer.Add(self._dim_options, 0, wx.ALL | wx.CENTER, 5)

        def create_button(text, operation):
            button = wx.Button(self, label=text)
            button.Bind(wx.EVT_BUTTON, operation)
            top_sizer.Add(button, 0, wx.ALL, 5)
            return button

        self._undo_button: Optional[wx.Button] = create_button('Undo', undo_evt)
        self._redo_button: Optional[wx.Button] = create_button('Redo', redo_evt)
        self._save_button: Optional[wx.Button] = create_button('Save', save_evt)
        create_button('Close', close_evt)
        self.update_buttons()

        self.SetSizer(top_sizer)
        top_sizer.Fit(self)
        self.Layout()

    def update_buttons(self):
        self._undo_button.SetLabel(f"Undo | {self._world().chunk_history_manager.undo_count}")
        self._redo_button.SetLabel(f"Redo | {self._world().chunk_history_manager.redo_count}")
        self._save_button.SetLabel(f"Save | {self._world().chunk_history_manager.unsaved_changes}")

    def _on_dimension_change(self, evt):
        self.change_dimension()
        evt.Skip()

    def change_dimension(self):
        dimension = self._dim_options.GetAny()
        if dimension is not None:
            self._canvas().dimension = dimension

    def move_event(self, evt):
        self._location_button.SetLabel(f'{evt.x:.2f}, {evt.y:.2f}, {evt.z:.2f}')
        self.Layout()
        self.GetParent().Layout()

    def show_goto(self):
        location = show_goto(self, *self._canvas().camera_location)
        if location:
            self._canvas().camera_location = location
