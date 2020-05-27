import wx
from typing import TYPE_CHECKING, Callable, Any
from types import GeneratorType
import time

from amulet.api.data_types import OperationReturnType

from amulet_map_editor import CONFIG
from amulet_map_editor.programs.edit.edit import EDIT_CONFIG_ID
from amulet_map_editor.programs.edit.key_config import DefaultKeys, DefaultKeybindGroupId, PresetKeybinds
from amulet_map_editor.programs.edit.canvas.ui.goto import show_goto

from amulet_map_editor.programs.edit.canvas.events import (
    EVT_SELECT_TOOL_ENABLED,
    EVT_OPERATION_TOOL_ENABLED,
    EVT_EXPORT_TOOL_ENABLED,
    EVT_IMPORT_TOOL_ENABLED,
    EVT_CAMERA_MOVE,
)
from amulet_map_editor.programs.edit.canvas.controllable_edit_canvas import ControllableEditCanvas
from amulet_map_editor.programs.edit.canvas.ui.file import FilePanel
from amulet_map_editor.programs.edit.canvas.ui.tool_options.operation import OperationUI
from amulet_map_editor.programs.edit.canvas.ui.tool_options.select import SelectOptions
from amulet_map_editor.programs.edit.canvas.ui.tool import ToolSelect

if TYPE_CHECKING:
    from amulet.api.world import World


def show_loading_dialog(
    run: Callable[[], OperationReturnType], title: str, message: str, parent: wx.Window
) -> Any:
    dialog = wx.ProgressDialog(
        title,
        message,
        parent=parent,
        style=wx.PD_APP_MODAL
        | wx.PD_ELAPSED_TIME
        | wx.PD_REMAINING_TIME
        | wx.PD_AUTO_HIDE,
    )
    t = time.time()
    try:
        obj = run()
        if isinstance(obj, GeneratorType):
            try:
                while True:
                    progress = next(obj)
                    if isinstance(progress, (list, tuple)):
                        if len(progress) >= 2:
                            message = progress[1]
                        if len(progress) >= 1:
                            progress = progress[0]
                    if isinstance(progress, (int, float)) and isinstance(message, str):
                        dialog.Update(min(99.99, max(0, progress)), message)
            except StopIteration as e:
                obj = e.value
    except Exception as e:
        dialog.Destroy()
        raise e
    time.sleep(max(0.2 - time.time() + t, 0))
    dialog.Destroy()
    return obj


class EditCanvas(ControllableEditCanvas):
    """Adds embedded UI elements to the canvas."""
    def __init__(self, parent: wx.Window, world: World):
        super().__init__(parent, world)
        config = CONFIG.get(EDIT_CONFIG_ID, {})
        user_keybinds = config.get("user_keybinds", {})
        group = config.get("keybind_group", DefaultKeybindGroupId)
        if group in user_keybinds:
            keybinds = user_keybinds[group]
        elif group in PresetKeybinds:
            keybinds = PresetKeybinds[group]
        else:
            keybinds = DefaultKeys
        self.set_key_binds(
            keybinds
        )

        self._file_panel = FilePanel(self)
        self._select_options = SelectOptions(self)
        self._operation_options = OperationUI(
            self, self._world, self._run_operation_event, self._run_main_operation
        )
        self._tool_panel = ToolSelect(self)

        self.Bind(EVT_CAMERA_MOVE, self._file_panel.move_event)
        self._tool_panel.Bind(EVT_SELECT_TOOL_ENABLED, self.show_select_options)
        self._tool_panel.Bind(
            EVT_OPERATION_TOOL_ENABLED, self.show_operation_options
        )
        self._tool_panel.Bind(EVT_IMPORT_TOOL_ENABLED, self.show_import_options)
        self._tool_panel.Bind(EVT_EXPORT_TOOL_ENABLED, self.show_export_options)

        self._file_panel.Hide()
        self._select_options.Hide()
        self._operation_options.Hide()
        self._tool_panel.Hide()

        canvas_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(canvas_sizer)
        bottom_sizer0 = wx.BoxSizer(wx.HORIZONTAL)
        middle_sizer0 = wx.BoxSizer(wx.VERTICAL)
        top_sizer0 = wx.BoxSizer(wx.HORIZONTAL)
        top_sizer0.AddStretchSpacer(1)
        top_sizer0.Add(self._file_panel, 0, wx.EXPAND, 0)
        canvas_sizer.Add(top_sizer0, 0, wx.EXPAND, 0)
        middle_sizer0.AddStretchSpacer(1)
        middle_sizer0.Add(self._select_options, 0, 0, 0)
        middle_sizer0.Add(self._operation_options, 0, 0, 0)
        middle_sizer0.AddStretchSpacer(1)
        canvas_sizer.Add(middle_sizer0, 1, wx.EXPAND, 0)
        bottom_sizer0.AddStretchSpacer(1)
        bottom_sizer0.Add(self._tool_panel, 0, wx.EXPAND, 0)
        bottom_sizer0.AddStretchSpacer(1)
        canvas_sizer.Add(bottom_sizer0, 0, wx.EXPAND, 0)

        self._file_panel.Show()
        self._select_options.Show()
        self._tool_panel.Show()

    def run_operation(self, operation: Callable[[], None], title="", msg="") -> Any:
        self._canvas.disable_threads()
        try:
            out = show_loading_dialog(
                operation,
                title,
                msg,
                self,
            )
            self._world.create_undo_point()
            self._file_panel.update_buttons()
        except Exception as e:
            self._canvas.enable_threads()
            raise e
        self._canvas.enable_threads()
        return out

    def undo(self):
        self.world.undo()
        self._file_panel.update_buttons()

    def redo(self):
        self.world.redo()
        self._file_panel.update_buttons()

    def cut(self):
        pass

    def copy(self):
        pass

    def paste(self):
        pass

    def delete(self):
        pass

    def goto(self):
        location = show_goto(self, *self.camera_location)
        if location:
            self.camera_location = location

    def save(self):
        self.disable_threads()

        def save():
            for chunk_index, chunk_count in self._world.save_iter():
                yield chunk_index / chunk_count

        show_loading_dialog(lambda: save(), f"Saving world.", "Please wait.", self)
        self._file_panel.update_buttons()
        self.enable_threads()

    def close(self):
        pass
