import wx
from typing import TYPE_CHECKING, Callable, Any
from types import GeneratorType
import time

from amulet.api.data_types import OperationReturnType

from amulet_map_editor import CONFIG
from amulet_map_editor.programs.edit.edit import EDIT_CONFIG_ID
from amulet_map_editor.programs.edit.key_config import DefaultKeys, DefaultKeybindGroupId, PresetKeybinds
from amulet_map_editor.programs.edit.canvas.ui.goto import show_goto
from amulet_map_editor.programs.edit.canvas.ui.tool import Tool

from amulet_map_editor.programs.edit.canvas.events import (
    UndoEvent,
    RedoEvent,
    CreateUndoEvent,
    SaveEvent,
    EditCloseEvent,
)
from amulet_map_editor.programs.edit.canvas.controllable_edit_canvas import ControllableEditCanvas
from amulet_map_editor.programs.edit.canvas.ui.file import FilePanel

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
    def __init__(self, parent: wx.Window, world: "World"):
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

        canvas_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(canvas_sizer)

        file_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_sizer.AddStretchSpacer(1)
        self._file_panel = FilePanel(self)
        file_sizer.Add(self._file_panel, 0, wx.EXPAND, 0)
        canvas_sizer.Add(file_sizer, 0, wx.EXPAND, 0)

        tool_sizer = Tool(self)
        canvas_sizer.Add(tool_sizer, 1, wx.EXPAND, 0)

    def run_operation(self, operation: Callable[[], None], title="", msg="") -> Any:
        self.disable_threads()
        try:
            out = show_loading_dialog(
                operation,
                title,
                msg,
                self,
            )
            self.world.create_undo_point()
            wx.PostEvent(self, CreateUndoEvent())
        except Exception as e:
            self.enable_threads()
            raise e
        self.enable_threads()
        return out

    def undo(self):
        self.world.undo()
        wx.PostEvent(self, UndoEvent())

    def redo(self):
        self.world.redo()
        wx.PostEvent(self, RedoEvent())

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
            for chunk_index, chunk_count in self.world.save_iter():
                yield chunk_index / chunk_count

        show_loading_dialog(lambda: save(), f"Saving world.", "Please wait.", self)
        wx.PostEvent(self, SaveEvent())
        self.enable_threads()

    def close(self):
        wx.PostEvent(self, EditCloseEvent())
