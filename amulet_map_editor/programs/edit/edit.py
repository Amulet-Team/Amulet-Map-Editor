import wx
from typing import TYPE_CHECKING, Optional, List, Callable, Any
from types import GeneratorType
import webbrowser
import time

from amulet.api.block import Block
from amulet.api.selection import Selection, SubSelectionBox
from amulet.api.structure import Structure, structure_buffer
from amulet.api.data_types import OperationType, OperationReturnType
from amulet.operations.paste import paste
from amulet.operations.fill import fill

from amulet_map_editor.programs import BaseWorldProgram, MenuData
from amulet_map_editor.plugins import operations
from .canvas.controllable_canvas import ControllableEditCanvas

from .ui.file import FilePanel
from amulet_map_editor.programs.edit.ui.tool_options.operation import OperationUI
from amulet_map_editor.programs.edit.ui.tool_options.select import SelectOptions
from amulet_map_editor.programs.edit.ui.tool import ToolSelect
from amulet_map_editor import log

from .events import (
    EVT_CAMERA_MOVE,
    EVT_SELECT_TOOL_ENABLED,
    EVT_OPERATION_TOOL_ENABLED,
    EVT_IMPORT_TOOL_ENABLED,
    EVT_EXPORT_TOOL_ENABLED,
)

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
                        dialog.Update(min(max(0, progress), 99.99), message)
            except StopIteration as e:
                obj = e.value
    except Exception as e:
        dialog.Destroy()
        raise e
    time.sleep(max(0.2 - time.time() + t, 0))
    dialog.Destroy()
    return obj


class EditExtension(wx.Panel, BaseWorldProgram):
    def __init__(self, parent, world: "World"):
        wx.Panel.__init__(self, parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)
        self._world = world
        self._canvas: Optional[ControllableEditCanvas] = None
        self._temp = wx.StaticText(self, label="Please wait while the renderer loads")
        self._temp.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        self._sizer.Add(self._temp)

        self._file_panel: Optional[FilePanel] = None
        self._select_options: Optional[SelectOptions] = None
        self._operation_options: Optional[OperationUI] = None
        self._tool_panel: Optional[ToolSelect] = None

        self.Bind(wx.EVT_SIZE, self._on_resize)

    def enable(self):
        if self._canvas is None:
            self.Update()

            self._canvas = ControllableEditCanvas(self, self._world)

            self._file_panel = FilePanel(
                self._canvas,
                self._world,
                self._undo_event,
                self._redo_event,
                self._save_event,
                self._close_world,
            )
            self._select_options = SelectOptions(self._canvas)
            self._operation_options = OperationUI(
                self._canvas, self._world, self._run_operation, self._run_main_operation
            )
            self._tool_panel = ToolSelect(self._canvas)

            self._canvas.Bind(EVT_CAMERA_MOVE, self._file_panel.move_event)
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

            self._sizer.Add(self._canvas, 1, wx.EXPAND)

            canvas_sizer = wx.BoxSizer(wx.VERTICAL)
            self._canvas.SetSizer(canvas_sizer)
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

            self._temp.Destroy()
            self._file_panel.Show()
            self._select_options.Show()
            self._tool_panel.Show()

            self.Layout()
        self._canvas.Update()
        self._canvas.enable()
        self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        self._canvas.draw()
        self._file_panel.change_dimension()

    def disable(self):
        if self._canvas is not None:
            self._canvas.disable()

    def close(self):
        self.disable()
        if self._canvas is not None:
            self._canvas.close()

    def is_closeable(self):
        if self._canvas is not None:
            return self._canvas.is_closeable() and not bool(
                self._world.chunk_history_manager.unsaved_changes
            )
        return not bool(self._world.chunk_history_manager.unsaved_changes)

    def _close_world(self, _):
        unsaved_changes = self._world.chunk_history_manager.unsaved_changes
        if unsaved_changes:
            msg = wx.MessageDialog(
                self,
                f"There {'is' if unsaved_changes == 1 else 'are'} {unsaved_changes} unsaved change{'s' if unsaved_changes >= 2 else ''}. Would you like to save?",
                style=wx.YES_NO | wx.CANCEL | wx.CANCEL_DEFAULT,
            )
            response = msg.ShowModal()
            if response == wx.ID_YES:
                self._save_world()
            elif response == wx.ID_CANCEL:
                return
        self.GetGrandParent().GetParent().close_world(self._world.world_path)

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault("&File", {}).setdefault("system", {}).setdefault(
            "Save\tCtrl+s", lambda evt: self._save_world()
        )
        # menu.setdefault('&File', {}).setdefault('system', {}).setdefault('Save As', lambda evt: self.GetGrandParent().close_world(self.world.world_path))
        menu.setdefault("&Edit", {}).setdefault("control", {}).setdefault(
            "Undo\tCtrl+z", lambda evt: self._world.undo()
        )
        menu.setdefault("&Edit", {}).setdefault("control", {}).setdefault(
            "Redo\tCtrl+y", lambda evt: self._world.redo()
        )
        menu.setdefault("&Edit", {}).setdefault("control", {}).setdefault(
            "Cut\tCtrl+x", lambda evt: self._cut()
        )
        menu.setdefault("&Edit", {}).setdefault("control", {}).setdefault(
            "Copy\tCtrl+c", lambda evt: self._copy()
        )
        menu.setdefault("&Edit", {}).setdefault("control", {}).setdefault(
            "Paste\tCtrl+v", lambda evt: self._paste()
        )
        menu.setdefault("&Edit", {}).setdefault("control", {}).setdefault(
            "Delete\tDelete", lambda evt: self._delete()
        )
        menu.setdefault("&Edit", {}).setdefault("control", {}).setdefault(
            "Goto\tCtrl+g", lambda evt: self._file_panel.show_goto()
        )
        menu.setdefault("&Help", {}).setdefault("control", {}).setdefault(
            "Controls", lambda evt: self._help_controls()
        )
        return menu

    @staticmethod
    def _help_controls():
        webbrowser.open(
            "https://github.com/Amulet-Team/Amulet-Map-Editor/tree/master/amulet_map_editor/plugins/programs/edit/readme.md"
        )

    def _on_resize(self, event):
        if self._canvas is not None:
            self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        event.Skip()

    def _undo_event(self, _):
        self._world.undo()
        self._file_panel.update_buttons()

    def _redo_event(self, _):
        self._world.redo()
        self._file_panel.update_buttons()

    def _save_event(self, _):
        self._save_world()

    def _save_world(self):
        self._canvas.disable_threads()

        def save():
            for chunk_index, chunk_count in self._world.save_iter():
                yield 100 * chunk_index / chunk_count

        show_loading_dialog(lambda: save(), f"Saving world.", "Please wait.", self)
        self._file_panel.update_buttons()
        self._canvas.enable_threads()

    def _get_box(self) -> Optional[Selection]:
        box = self._canvas.selection_box
        if box.select_state == 2:
            return Selection((SubSelectionBox(box.min, box.max),))
        else:
            wx.MessageBox(
                "You must select an area of the world before running this operation"
            )
            return None

    def _run_operation(self, evt):
        operation_path = self._operation_options.operation
        operation = operations.operations[operation_path]
        features = operation.get("features", [])
        operation_input_definitions = operation.get("inputs", [])
        if any(feature in features for feature in ("dst_location_absolute",)):
            if "structure_callable" in operation:
                operation_inputs = []
                for inp in operation.get("structure_callable_inputs", []):
                    if inp == "src_selection":
                        selection = self._get_box()
                        if selection is None:
                            return
                        operation_inputs.append(selection)

                    elif inp == "options":
                        operation_inputs.append(
                            operations.options.get(operation_path, {})
                        )

                self._operation_options.Disable()

                self._canvas.disable_threads()
                try:
                    structure = show_loading_dialog(
                        lambda: operation["structure_callable"](
                            self._world, self._canvas.dimension, *operation_inputs
                        ),
                        f'Running structure operation for {operation["name"]}.',
                        "Please wait for the operation to finish.",
                        self,
                    )
                except Exception as e:
                    wx.MessageBox(f"Error running structure operation: {e}")
                    self._world.restore_last_undo_point()
                    self._canvas.enable_threads()
                    return
                self._canvas.enable_threads()

                self._operation_options.Enable()
                if not isinstance(structure, Structure):
                    wx.MessageBox(
                        "Object returned from structure_callable was not a Structure. Aborting."
                    )
                    return
            else:
                selection = self._get_box()
                if selection is None:
                    return
                self._operation_options.Disable()
                structure = show_loading_dialog(
                    lambda: Structure.from_world(
                        self._world, selection, self._canvas.dimension
                    ),
                    f'Running structure operation for {operation["name"]}.',
                    "Copying structure from world.",
                    self,
                )
                self._operation_options.Enable()

            if "dst_location_absolute" in features:
                # trigger UI to show select box UI
                self._operation_options.enable_select_destination_ui(
                    operation_path,
                    operation["operation"],
                    operation_input_definitions,
                    structure,
                    operations.options.get(operation_path, {}),
                )
            else:
                # trigger UI to show select box multiple UI
                raise NotImplementedError

        else:
            self._operation_options.Disable()
            self._run_main_operation(
                operation_path, operation["operation"], operation_input_definitions
            )
            self._operation_options.Enable()
        evt.Skip()

    def _run_main_operation(
        self,
        operation_path: str,
        operation: OperationType,
        operation_input_definitions: List[str],
        options=None,
        structure=None,
    ):
        operation_inputs = []
        for inp in operation_input_definitions:
            if inp == "src_selection":
                selection = self._get_box()
                if selection is None:
                    return
                operation_inputs.append(selection)
            elif inp == "structure":
                operation_inputs.append(structure)
            elif inp == "options":
                if options:
                    operations.options[operation_path] = options
                    operation_inputs.append(options)
                else:
                    operation_inputs.append(operations.options.get(operation_path, {}))

        self._canvas.disable_threads()
        try:
            show_loading_dialog(
                lambda: operation(
                    self._world, self._canvas.dimension, *operation_inputs
                ),
                f"Running Operation ?.",
                "Please wait for the operation to finish.",
                self,
            )
            self._world.create_undo_point()
            self._file_panel.update_buttons()
        except Exception as e:
            operation_info = operations.operations[operation_path]
            log.exception(
                f'Error occurred while running operation: {operation_info["name"]} v{operation_info["v"]}'
            )
            wx.MessageBox(f"Error running operation: {e}")
            self._world.restore_last_undo_point()
        self._canvas.enable_threads()

    def _cut(self) -> bool:
        if self._copy():
            return self._delete()
        return False

    def _copy(self) -> bool:
        selection = self._get_box()
        if selection is None:
            return False
        structure = show_loading_dialog(
            lambda: Structure.from_world(
                self._world, selection, self._canvas.dimension
            ),
            f"Copying selection.",
            "",
            self,
        )
        structure_buffer.append(structure)
        return True

    def _paste(self) -> bool:
        if structure_buffer:
            self.show_operation_options(None)
            structure = structure_buffer[-1]
            self._operation_options.enable_select_destination_ui(
                None, paste, ["structure", "options"], structure, {}
            )
            return True
        return False

    def _delete(self) -> bool:
        selection = self._get_box()
        if selection is None:
            return False
        show_loading_dialog(
            lambda: fill(
                self._world,
                self._canvas.dimension,
                selection,
                {"fill_block": Block("universal_minecraft", "air")},
            ),
            f"Deleting selection.",
            "",
            self,
        )
        self._world.create_undo_point()
        self._file_panel.update_buttons()
        return True

    def show_select_options(self, _):
        self._operation_options.Hide()
        self._select_options.enable()
        self.Layout()

    def _show_operation_options(self, enable: Callable):
        self._select_options.Hide()
        enable()
        self.Layout()

    def show_operation_options(self, _):
        self._show_operation_options(self._operation_options.enable_operation_ui)

    def show_import_options(self, _):
        self._show_operation_options(self._operation_options.enable_import_ui)

    def show_export_options(self, _):
        self._show_operation_options(self._operation_options.enable_export_ui)
