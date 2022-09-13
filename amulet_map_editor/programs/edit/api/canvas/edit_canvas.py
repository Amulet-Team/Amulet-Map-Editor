import logging
import warnings
import wx
from typing import Callable, TYPE_CHECKING, Any, Generator, Optional
from types import GeneratorType
from threading import RLock, Thread

from .base_edit_canvas import BaseEditCanvas
from ...edit import EDIT_CONFIG_ID
from ..key_config import (
    DefaultKeys,
    DefaultKeybindGroupId,
    PresetKeybinds,
    KeybindGroup,
)

import time
import traceback

from amulet.api.data_types import OperationReturnType, OperationYieldType, Dimension
from amulet.api.structure import structure_cache
from amulet.api.level import BaseLevel

from amulet_map_editor import CONFIG
from amulet_map_editor import close_level
from amulet_map_editor.api.wx.ui.traceback_dialog import TracebackDialog
from amulet_map_editor.programs.edit.api.ui.goto import show_goto
from amulet_map_editor.programs.edit.api.ui.tool_manager import ToolManagerSizer
from amulet_map_editor.programs.edit.api.operations.errors import (
    OperationError,
    OperationSilentAbort,
    BaseLoudException,
    BaseSilentException,
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
    ToolChangeEvent,
    EVT_EDIT_CLOSE,
)
from amulet_map_editor.programs.edit.api.ui.file import FilePanel

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel

log = logging.getLogger(__name__)
OperationType = Callable[[], OperationReturnType]


def show_loading_dialog(
    run: OperationType, title: str, message: str, parent: wx.Window
) -> Any:
    warnings.warn("show_loading_dialog is depreciated.", DeprecationWarning)
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
                        dialog.Update(
                            min(9999, max(0, int(progress * 10_000))), message
                        )
                    wx.Yield()
            except StopIteration as e:
                obj = e.value
    except Exception as e:
        dialog.Update(10_000)
        raise e
    time.sleep(max(0.2 - time.time() + t, 0))
    dialog.Update(10_000)
    return obj


class OperationThread(Thread):
    # The operation to run
    _operation: OperationType

    # Should the operation be stopped. Set externally
    stop: bool
    # The starting message for the progress dialog
    message: str
    # The operation progress (from 0-1)
    progress: float
    # The return value from the operation
    out: Any
    # The error raised if any
    error: Optional[BaseException]

    def __init__(self, operation: OperationType, message: str):
        super().__init__()
        self._operation = operation
        self.stop = False
        self.message = message
        self.progress = 0.0
        self.out = None
        self.error = None

    def run(self) -> None:
        t = time.time()
        try:
            obj = self._operation()
            if isinstance(obj, GeneratorType):
                try:
                    while True:
                        if self.stop:
                            raise OperationSilentAbort
                        progress = next(obj)
                        if isinstance(progress, (list, tuple)):
                            if len(progress) >= 2:
                                self.message = progress[1]
                            if len(progress) >= 1:
                                self.progress = progress[0]
                        elif isinstance(progress, (int, float)):
                            self.progress = progress
                except StopIteration as e:
                    self.out = e.value
        except BaseException as e:
            self.error = e
        time.sleep(max(0.2 - time.time() + t, 0))


class EditCanvas(BaseEditCanvas):
    def __init__(self, parent: wx.Window, world: "BaseLevel"):
        super().__init__(parent, world)
        self._file_panel: Optional[FilePanel] = None
        self._tool_sizer: Optional[ToolManagerSizer] = None
        self.buttons.register_actions(self.key_binds)

        self._canvas_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._canvas_sizer)

        # Tracks if an operation has been started and not finished.
        self._operation_running = False
        # This lock stops two threads from editing the world simultaneously
        # call run_operation to acquire it.
        self._edit_lock = RLock()

    def _init_opengl(self):
        super()._init_opengl()
        self._file_panel = FilePanel(self)
        self._canvas_sizer.Add(self._file_panel, 0, wx.EXPAND, 0)
        self._tool_sizer = ToolManagerSizer(self)
        self._canvas_sizer.Add(self._tool_sizer, 1, wx.EXPAND, 0)

    def bind_events(self):
        """Set up all events required to run.
        Note this will also bind subclass events."""
        self._tool_sizer.bind_events()
        # binding the tool events first will run them last so they can't accidentally block UI events.
        super().bind_events()
        self._file_panel.bind_events()
        self.Bind(EVT_EDIT_CLOSE, self._on_close)

    def enable(self):
        super().enable()
        self._tool_sizer.enable()

    def disable(self):
        super().disable()
        self._tool_sizer.disable()

    def _on_close(self, _):
        close_level(self.world.level_path)

    @property
    def tools(self):
        return self._tool_sizer.tools

    @property
    def key_binds(self) -> KeybindGroup:
        config_ = CONFIG.get(EDIT_CONFIG_ID, {})
        user_keybinds = config_.get("user_keybinds", {})
        group = config_.get("keybind_group", DefaultKeybindGroupId)
        if group in user_keybinds:
            return user_keybinds[group]
        elif group in PresetKeybinds:
            return PresetKeybinds[group]
        else:
            return DefaultKeys

    def _deselect(self):
        # TODO: Re-implement this
        self._tool_sizer.enable_default_tool()

    def run_operation(
        self,
        operation: OperationType,
        title="Amulet",
        msg="Running Operation",
        throw_exceptions=False,
    ) -> Any:
        try:
            out = self._run_operation(operation, title, msg, True)
        except Exception as e:
            if throw_exceptions:
                raise e
        else:
            # If there were no errors create an undo point
            def create_undo():
                yield 0, "Creating Undo Point"
                yield from self.create_undo_point_iter()

            self._run_operation(create_undo, title, msg, False)

            return out

    def _run_operation(
        self,
        operation: OperationType,
        title: str,
        msg: str,
        cancelable: bool,
    ) -> Any:
        with self._edit_lock:
            if self._operation_running:
                raise Exception(
                    "run_operation cannot be called from within itself. "
                    "This function has already been called by parent code so you cannot run it again"
                )
            self._operation_running = True

            self.renderer.disable_threads()

            style = (
                wx.PD_APP_MODAL
                | wx.PD_ELAPSED_TIME
                | wx.PD_REMAINING_TIME
                | wx.PD_AUTO_HIDE
                | (wx.PD_CAN_ABORT * cancelable)
            )
            dialog = wx.ProgressDialog(
                title,
                msg,
                maximum=10_000,
                parent=self,
                style=style,
            )
            dialog.Fit()

            # Set up a thread to run the actual operation
            op = OperationThread(operation, msg)
            # run the operation
            op.start()
            while op.is_alive():
                op.join(0.1)
                dialog.Update(max(0, min(int(op.progress * 10_000), 9999)), op.message)
                wx.Yield()
                if dialog.WasCancelled():
                    op.stop = True

            dialog.Destroy()
            wx.Yield()

            if op.error is not None:
                # If there is any kind of error restore the last undo point
                self.world.restore_last_undo_point()

                if isinstance(op.error, BaseLoudException):
                    msg = str(op.error)
                    if isinstance(op.error, OperationError):
                        msg = f"Error running operation: {msg}"
                    log.info(msg)
                    wx.MessageDialog(self, msg, style=wx.OK).ShowModal()
                elif isinstance(op.error, BaseSilentException):
                    pass
                elif isinstance(op.error, BaseException):
                    log.error(traceback.format_exc())
                    dialog = TracebackDialog(
                        self,
                        "Exception while running operation",
                        str(op.error),
                        traceback.format_exc(),
                    )
                    dialog.ShowModal()
                    dialog.Destroy()
                    self.world.restore_last_undo_point()

            self.renderer.enable_threads()
            self.renderer.render_world.rebuild_changed()
            self._operation_running = False
            if op.error is not None:
                raise op.error
            return op.out

    def create_undo_point(self, world=True, non_world=True):
        self.world.create_undo_point(world, non_world)
        wx.PostEvent(self, CreateUndoEvent())

    def create_undo_point_iter(
        self, world=True, non_world=True
    ) -> Generator[float, None, bool]:
        result = yield from self.world.create_undo_point_iter(world, non_world)
        wx.PostEvent(self, CreateUndoEvent())
        return result

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
        wx.PostEvent(
            self,
            ToolChangeEvent(
                tool="Paste", state={"structure": structure, "dimension": dimension}
            ),
        )

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
                        self.world.bounds(self.dimension).min[1],
                        min_z * self.world.sub_chunk_size,
                    ),
                    (
                        (max_x + 1) * self.world.sub_chunk_size,
                        self.world.bounds(self.dimension).max[1],
                        (max_z + 1) * self.world.sub_chunk_size,
                    ),
                )
            ]

        else:
            self.selection.selection_corners = []

    def save(self):
        def save():
            yield 0, "Running Pre-Save Operations."
            pre_save_op = self.world.pre_save_operation()
            try:
                while True:
                    yield next(pre_save_op)
            except StopIteration as e:
                if e.value:
                    yield from self.create_undo_point_iter()
                else:
                    self.world.restore_last_undo_point()

            yield 0, "Saving Chunks."
            for chunk_index, chunk_count in self.world.save_iter():
                yield chunk_index / chunk_count

        self._run_operation(save, "Saving world.", "Please wait.", False)
        wx.PostEvent(self, SaveEvent())
