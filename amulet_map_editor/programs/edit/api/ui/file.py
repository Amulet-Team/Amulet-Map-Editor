from typing import TYPE_CHECKING
from math import floor, log10
import logging

import wx

from amulet_map_editor.programs.edit.api.edit_canvas_container import (
    EditCanvasContainer,
)
from amulet_map_editor.api.wx.ui.simple import SimpleChoiceAny
from amulet_map_editor.programs.edit.api.events import (
    EVT_CAMERA_MOVED,
    EVT_SPEED_CHANGED,
    EVT_UNDO,
    EVT_REDO,
    EVT_CREATE_UNDO,
    EVT_SAVE,
    EVT_PROJECTION_CHANGED,
    EVT_DIMENSION_CHANGE,
    DimensionChangeEvent,
    EditCloseEvent,
)
from amulet_map_editor.api import image, lang
from amulet_map_editor.api.opengl.camera import Projection

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

log = logging.getLogger(__name__)


def _format_float(num: float) -> str:
    if num < 100:
        return f"{num:.0{max(0, 2 - floor(log10(num)))}f}".rstrip("0").rstrip(".")
    else:
        return f"{num:.0f}"


class FilePanel(EditCanvasContainer):
    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)

        level = self.canvas.world

        self._version_panel = wx.Panel(canvas.GetParent())
        self._version_panel.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)
        )
        self._version_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._version_panel.SetSizer(self._version_sizer)
        self._version_text = wx.StaticText(
            self._version_panel,
            label=f"{level.level_wrapper.platform}, {level.level_wrapper.version}",
        )
        self._version_sizer.Add(self._version_text)
        self._version_text.SetToolTip(
            lang.get("program_3d_edit.file_ui.version_tooltip")
        )

        self._button_window = wx.Panel(canvas.GetParent())
        self._button_window.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)
        )
        self._button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._button_window.SetSizer(self._button_sizer)

        self._projection_button = wx.Button(self._button_window, label="3D")
        self._projection_button.SetToolTip(
            lang.get("program_3d_edit.file_ui.projection_tooltip")
        )
        self._projection_button.Bind(wx.EVT_BUTTON, self._on_projection_button)
        self._button_sizer.Add(self._projection_button)
        self._location_button = wx.Button(
            self._button_window,
            label=", ".join([f"{s:.2f}" for s in self.canvas.camera.location]),
        )
        self._location_button.SetToolTip(
            lang.get("program_3d_edit.file_ui.location_tooltip")
        )
        self._location_button.Bind(wx.EVT_BUTTON, lambda evt: self.canvas.goto())
        self._button_sizer.Add(self._location_button)

        def set_speed(evt):
            dialog = SpeedSelectDialog(
                canvas, self.canvas.camera.move_speed * 1000 / 33
            )
            log.debug(f"Showing SpeedSelectDialog at {dialog.GetRect()}")
            if dialog.ShowModal() == wx.ID_OK:
                self.canvas.camera.move_speed = dialog.speed * 33 / 1000

        self._speed_button = wx.Button(
            self._button_window,
            label=f"{_format_float(self.canvas.camera.move_speed * 1000 / 33)} {lang.get('program_3d_edit.file_ui.speed_blocks_per_second')}",
        )
        self._speed_button.SetToolTip(lang.get("program_3d_edit.file_ui.speed_tooltip"))
        self._speed_button.Bind(wx.EVT_BUTTON, set_speed)
        self._button_sizer.Add(self._speed_button)

        self._dim_options = SimpleChoiceAny(self._button_window)
        self._dim_options.SetToolTip(lang.get("program_3d_edit.file_ui.dim_tooltip"))
        self._dim_options.SetItems(level.level_wrapper.dimensions)
        self._set_dimension(canvas.dimension)
        self._dim_options.Bind(wx.EVT_CHOICE, self._on_dimension_change)

        self._button_sizer.Add(self._dim_options)

        def create_button(text, operation):
            button = wx.Button(self._button_window, label=text)
            button.Bind(wx.EVT_BUTTON, operation)
            self._button_sizer.Add(button)
            return button

        self._undo_button = create_button("0", lambda evt: self.canvas.undo())
        self._undo_button.SetBitmap(image.icon.tablericons.arrow_back_up.bitmap(20, 20))
        self._undo_button.SetToolTip(lang.get("program_3d_edit.file_ui.undo_tooltip"))

        self._redo_button = create_button("0", lambda evt: self.canvas.redo())
        self._redo_button.SetBitmap(
            image.icon.tablericons.arrow_forward_up.bitmap(20, 20)
        )
        self._redo_button.SetToolTip(lang.get("program_3d_edit.file_ui.redo_tooltip"))

        self._save_button = create_button("0", lambda evt: self.canvas.save())
        self._save_button.SetBitmap(image.icon.tablericons.device_floppy.bitmap(20, 20))
        self._save_button.SetToolTip(lang.get("program_3d_edit.file_ui.save_tooltip"))

        self._close_button = create_button(
            "", lambda evt: wx.PostEvent(self.canvas, EditCloseEvent())
        )
        self._close_button.SetBitmap(image.icon.tablericons.square_x.bitmap(20, 20))
        self._close_button.SetToolTip(lang.get("program_3d_edit.file_ui.close_tooltip"))
        size = self._close_button.GetSize()
        self._close_button.SetSize(wx.Size(size.GetHeight(), size.GetHeight()))
        self._close_button.SetMinSize(wx.Size(size.GetHeight(), size.GetHeight()))

        self._update_buttons()

        self._resize()

    def bind_events(self):
        self.canvas.Bind(EVT_CAMERA_MOVED, self._on_camera_move)
        self.canvas.Bind(EVT_SPEED_CHANGED, self._on_speed_change)
        self.canvas.Bind(EVT_UNDO, self._on_update_buttons)
        self.canvas.Bind(EVT_REDO, self._on_update_buttons)
        self.canvas.Bind(EVT_SAVE, self._on_update_buttons)
        self.canvas.Bind(EVT_CREATE_UNDO, self._on_update_buttons)
        self.canvas.Bind(EVT_PROJECTION_CHANGED, self._on_projection_change)
        self.canvas.Bind(EVT_DIMENSION_CHANGE, self._change_dimension)
        self.canvas.Bind(wx.EVT_SIZE, self._on_resize)

    def _on_update_buttons(self, evt):
        self._update_buttons()
        evt.Skip()

    def _update_buttons(self):
        self._undo_button.SetLabel(f"{self.canvas.world.history_manager.undo_count}")
        self._redo_button.SetLabel(f"{self.canvas.world.history_manager.redo_count}")
        self._save_button.SetLabel(
            f"{self.canvas.world.history_manager.unsaved_changes}"
        )

    def _on_dimension_change(self, evt):
        """Run when the dimension selection is changed by the user."""
        dimension = self._dim_options.GetCurrentObject()
        if dimension is not None:
            self.canvas.dimension = dimension
        evt.Skip()

    def _on_projection_change(self, evt):
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self._projection_button.SetLabel("3D")
        elif self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            self._projection_button.SetLabel("2D")
        evt.Skip()

    def _on_projection_button(self, evt):
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.camera.projection_mode = Projection.TOP_DOWN
        else:
            self.canvas.camera.projection_mode = Projection.PERSPECTIVE
        evt.Skip()

    def _change_dimension(self, evt: DimensionChangeEvent):
        """Run when the dimension attribute in the canvas is changed.
        This is run when the user changes the attribute and when it is changed manually in code.
        """
        self._set_dimension(evt.dimension)

    def _set_dimension(self, dimension: str) -> None:
        index = self._dim_options.FindString(dimension)
        if not (index == wx.NOT_FOUND or index == self._dim_options.GetSelection()):
            self._dim_options.SetSelection(index)

    def _on_camera_move(self, evt):
        x, y, z = evt.camera_location
        label = f"{x:.2f}, {y:.2f}, {z:.2f}"
        old_label = self._location_button.GetLabel()
        self._location_button.SetLabel(label)
        if len(label) != len(old_label):
            self._resize()
        evt.Skip()

    def _on_speed_change(self, evt):
        label = f"{_format_float(self.canvas.camera.move_speed * 1000 / 33)} {lang.get('program_3d_edit.file_ui.speed_blocks_per_second')}"
        old_label = self._speed_button.GetLabel()
        self._speed_button.SetLabel(label)
        if len(label) != len(old_label):
            self._resize()
        evt.Skip()

    def _on_resize(self, evt) -> None:
        self._resize()
        evt.Skip()

    def _resize(self) -> None:
        version_text_size = self._version_panel.GetBestSize()
        self._version_panel.SetSize(
            wx.Rect(0, 0, version_text_size.GetWidth(), version_text_size.GetHeight())
        )
        self._version_panel.Raise()

        self._button_window.Layout()
        window_size = self._button_window.GetBestSize()
        canvas_size = self.canvas.GetSize()
        self._button_window.SetSize(
            wx.Rect(
                max(0, canvas_size.GetWidth() - window_size.GetWidth()),
                0,
                window_size.GetWidth(),
                window_size.GetHeight(),
            )
        )
        self._button_window.Raise()
        self._button_window.Refresh(False)


class SpeedSelectDialog(wx.Dialog):
    def __init__(self, parent: wx.Window, speed: float):
        wx.Dialog.__init__(self, parent)
        self.SetTitle(lang.get("program_3d_edit.file_ui.speed_dialog_name"))

        sizer = wx.BoxSizer(wx.VERTICAL)

        self._speed_spin_ctrl_double = wx.SpinCtrlDouble(
            self, wx.ID_ANY, initial=speed, min=0.0, max=1_000_000_000.0
        )
        self._speed_spin_ctrl_double.SetToolTip(
            lang.get("program_3d_edit.file_ui.speed_tooltip")
        )

        def on_mouse_wheel(evt: wx.MouseEvent):
            if evt.GetWheelRotation() > 0:
                self._speed_spin_ctrl_double.SetValue(
                    self._speed_spin_ctrl_double.GetValue()
                    + self._speed_spin_ctrl_double.GetIncrement()
                )
            else:
                self._speed_spin_ctrl_double.SetValue(
                    self._speed_spin_ctrl_double.GetValue()
                    - self._speed_spin_ctrl_double.GetIncrement()
                )

        self._speed_spin_ctrl_double.Bind(wx.EVT_MOUSEWHEEL, on_mouse_wheel)
        self._speed_spin_ctrl_double.SetIncrement(1.0)
        self._speed_spin_ctrl_double.SetDigits(4)
        sizer.Add(self._speed_spin_ctrl_double)

        button_sizer = wx.StdDialogButtonSizer()
        sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self._button_ok = wx.Button(self, wx.ID_OK, "")
        self._button_ok.SetDefault()
        button_sizer.AddButton(self._button_ok)

        self._button_cancel = wx.Button(self, wx.ID_CANCEL, "")
        button_sizer.AddButton(self._button_cancel)

        button_sizer.Realize()

        self.SetSizer(sizer)
        sizer.Fit(self)

        self.SetAffirmativeId(self._button_ok.GetId())
        self.SetEscapeId(self._button_cancel.GetId())

        self.Layout()

    @property
    def speed(self) -> float:
        return self._speed_spin_ctrl_double.GetValue()
