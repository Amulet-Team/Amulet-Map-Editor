import wx
from typing import Callable, TYPE_CHECKING, Any, Generator, Optional
from types import GeneratorType

from .base_edit_canvas import BaseEditCanvas
from ...edit import EDIT_CONFIG_ID
from ..key_config import (
    DefaultKeys,
    DefaultKeybindGroupId,
    PresetKeybinds,
)

import time
import traceback

from amulet.api.data_types import OperationReturnType, OperationYieldType, Dimension
from amulet.api.structure import structure_cache
from amulet.api.level import BaseLevel

from amulet_map_editor import CONFIG, log
from amulet_map_editor.programs.edit.api.ui.goto import show_goto
from amulet_map_editor.programs.edit.api.ui.tool_manager import ToolManagerSizer
from amulet_map_editor.programs.edit.api.operations import (
    OperationError,
    OperationSuccessful,
    OperationSilentAbort,
)
from amulet_map_editor.programs.edit.plugins.operations.stock_plugins.internal_operations import (
    cut,
    copy,
    delete,
)

from amulet_map_editor.programs.edit.api.events import (
    UndoEvent,
    RedoEvent,
    CreateUndoEvent,
    SaveEvent,
    EditCloseEvent,
    PasteEvent,
    ToolChangeEvent,
    EVT_EDIT_CLOSE,
)
from amulet_map_editor.programs.edit.api.ui.file import FilePanel

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel


def show_loading_dialog(
    run: Callable[[], OperationReturnType], title: str, message: str, parent: wx.Window
) -> Any:
    dialog = wx.ProgressDialog(
        title,
        message,
        maximum=10_000,
        parent=parent,
        style=wx.PD_APP_MODAL
        | wx.PD_ELAPSED_TIME
        | wx.PD_REMAINING_TIME
        | wx.PD_AUTO_HIDE,
    )
    dialog.Fit()
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
                        dialog.Update(min(9999, max(0, progress * 10_000)), message)
                    wx.Yield()
            except StopIteration as e:
                obj = e.value
    except Exception as e:
        dialog.Destroy()
        raise e
    time.sleep(max(0.2 - time.time() + t, 0))
    dialog.Destroy()
    return obj


class EditCanvas(BaseEditCanvas):
    def __init__(self, parent: wx.Window, world: "BaseLevel", close_callback: Callable):
        super().__init__(parent, world)
        self._close_callback = close_callback
        self._file_panel: Optional[FilePanel] = None
        self._tool_sizer: Optional[ToolManagerSizer] = None
        config_ = CONFIG.get(EDIT_CONFIG_ID, {})
        user_keybinds = config_.get("user_keybinds", {})
        group = config_.get("keybind_group", DefaultKeybindGroupId)
        if group in user_keybinds:
            keybinds = user_keybinds[group]
        elif group in PresetKeybinds:
            keybinds = PresetKeybinds[group]
        else:
            keybinds = DefaultKeys
        for action_id, (modifier_keys, trigger_key) in keybinds.items():
            self.buttons.register_action(action_id, trigger_key, modifier_keys)

    def _setup(self) -> Generator[OperationYieldType, None, None]:
        yield from super()._setup()
        canvas_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(canvas_sizer)

        self._file_panel = FilePanel(self)
        canvas_sizer.Add(self._file_panel, 0, wx.EXPAND, 0)

        self._tool_sizer = ToolManagerSizer(self)
        canvas_sizer.Add(self._tool_sizer, 1, wx.EXPAND, 0)

    def _finalise(self):
        super()._finalise()
        self._tool_sizer.enable_default_tool()

    def bind_events(self):
        """Set up all events required to run.
        Note this will also bind subclass events."""
        self._tool_sizer.bind_events()
        # binding the tool events first will run them last so they can't accidentally block UI events.
        super().bind_events()
        self._file_panel.bind_events()
        self.Bind(EVT_EDIT_CLOSE, self._on_close)

    def _on_close(self, _):
        self._close_callback()

    @property
    def tools(self):
        return self._tool_sizer.tools

    def _deselect(self) -> bool:
        return self._tool_sizer.enable_default_tool()

    def run_operation(
        self,
        operation: Callable[[], OperationReturnType],
        title="Amulet",
        msg="Running Operation",
        throw_exceptions=False,
    ) -> Any:
        def operation_wrapper():
            yield 0, "Disabling Threads"
            self.renderer.disable_threads()
            yield 0, msg
            op = operation()
            if isinstance(op, GeneratorType):
                yield from op
            return op

        err = None
        out = None
        try:
            out = show_loading_dialog(
                operation_wrapper,
                title,
                msg,
                self,
            )
            self.create_undo_point()
        except OperationError as e:
            msg = f"Error running operation: {e}"
            log.info(msg)
            self.world.restore_last_undo_point()
            wx.MessageDialog(self, msg, style=wx.OK).ShowModal()
            err = e
        except OperationSuccessful as e:
            msg = str(e)
            log.info(msg)
            self.world.restore_last_undo_point()
            wx.MessageDialog(self, msg, style=wx.OK).ShowModal()
            err = e
        except OperationSilentAbort as e:
            self.world.restore_last_undo_point()
            err = e
        except Exception as e:
            self.world.restore_last_undo_point()
            log.error(traceback.format_exc())
            wx.MessageDialog(
                self,
                f"Exception running operation: {e}\nSee the console for more details",
                style=wx.OK,
            ).ShowModal()
            err = e

        self.renderer.enable_threads()
        self.renderer.render_world.rebuild_changed()
        if err is not None and throw_exceptions:
            raise err
        return out

    def create_undo_point(self, world=True, non_world=True):
        self.world.create_undo_point(world, non_world)
        wx.PostEvent(self, CreateUndoEvent())

    def undo(self):
        self.world.undo()
        self.renderer.render_world.rebuild_changed()
        wx.PostEvent(self, UndoEvent())

    def redo(self):
        self.world.redo()
        self.renderer.render_world.rebuild_changed()
        wx.PostEvent(self, RedoEvent())

    def cut(self):
        self.run_operation(
            lambda: cut(self.world, self.dimension, self.selection.selection_group)
        )

    def copy(self):
        self.run_operation(
            lambda: copy(self.world, self.dimension, self.selection.selection_group)
        )

    def paste(self, structure: BaseLevel, dimension: Dimension):
        assert isinstance(
            structure, BaseLevel
        ), "Structure given is not a subclass of BaseLevel."
        assert (
            dimension in structure.dimensions
        ), "The requested dimension does not exist for this object."
        wx.PostEvent(self, ToolChangeEvent(tool="Paste"))
        wx.PostEvent(self, PasteEvent(structure=structure, dimension=dimension))

    def paste_from_cache(self):
        if structure_cache:
            self.paste(*structure_cache.get_structure())
        else:
            wx.MessageBox("A structure needs to be copied before one can be pasted.")

    def delete(self):
        self.run_operation(
            lambda: delete(self.world, self.dimension, self.selection.selection_group)
        )

    def goto(self):
        location = show_goto(self, *self.camera.location)
        if location:
            self.camera.location = location

    def select_all(self):
        all_chunk_coords = tuple(self.world.all_chunk_coords(self.dimension))
        if all_chunk_coords:
            min_x, min_z = max_x, max_z = all_chunk_coords[0]
            for x, z in all_chunk_coords:
                if x < min_x:
                    min_x = x
                elif x > max_x:
                    max_x = x
                if z < min_z:
                    min_z = z
                elif z > max_z:
                    max_z = z

            self.selection.selection_corners = [
                (
                    (
                        min_x * self.world.sub_chunk_size,
                        self.world.selection_bounds.min[1],
                        min_z * self.world.sub_chunk_size,
                    ),
                    (
                        (max_x + 1) * self.world.sub_chunk_size,
                        self.world.selection_bounds.max[1],
                        (max_z + 1) * self.world.sub_chunk_size,
                    ),
                )
            ]

        else:
            self.selection.selection_corners = []

    def save(self):
        self.renderer.disable_threads()

        def save():
            for chunk_index, chunk_count in self.world.save_iter():
                yield chunk_index / chunk_count

        show_loading_dialog(lambda: save(), f"Saving world.", "Please wait.", self)
        wx.PostEvent(self, SaveEvent())
        self.renderer.enable_threads()

    def close(self):
        wx.PostEvent(self, EditCloseEvent())
