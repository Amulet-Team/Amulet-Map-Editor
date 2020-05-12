import wx
from typing import TYPE_CHECKING, Optional, List, Callable, Any
from types import GeneratorType
import webbrowser
import time
import traceback
import os

from amulet.api.selection import SelectionGroup, SelectionBox
from amulet.api.structure import Structure
from amulet.api.data_types import OperationType, OperationReturnType

from amulet_map_editor import log, CONFIG
from amulet_map_editor.programs import BaseWorldProgram, MenuData
from amulet_map_editor import plugins
from amulet_map_editor.amulet_wx.key_config import KeyConfigDialog


from .canvas.controllable_canvas import ControllableEditCanvas
from .ui.file import FilePanel
from .ui.tool_options.operation import OperationUI
from .ui.tool_options.select import SelectOptions
from .ui.tool import ToolSelect
from .key_config import DefaultKeys, DefaultKeybindGroupId, PresetKeybinds, KeybindKeys

from .events import (
    EVT_CAMERA_MOVE,
    EVT_SELECT_TOOL_ENABLED,
    EVT_OPERATION_TOOL_ENABLED,
    EVT_IMPORT_TOOL_ENABLED,
    EVT_EXPORT_TOOL_ENABLED,
)

if TYPE_CHECKING:
    from amulet.api.world import World

EDIT_CONFIG_ID = "amulet_edit"


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

            config = CONFIG.get(EDIT_CONFIG_ID, {})
            user_keybinds = config.get("user_keybinds", {})
            group = config.get("keybind_group", DefaultKeybindGroupId)
            if group in user_keybinds:
                keybinds = user_keybinds[group]
            elif group in PresetKeybinds:
                keybinds = PresetKeybinds[group]
            else:
                keybinds = DefaultKeys
            self._canvas.set_key_binds(
                keybinds
            )

            self._file_panel = FilePanel(
                self._canvas,
                self._world,
                self._undo,
                self._redo,
                self._save_world,
                self._close_world,
            )
            self._select_options = SelectOptions(self._canvas)
            self._operation_options = OperationUI(
                self._canvas, self._world, self._run_operation_event, self._run_main_operation
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
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Undo\tCtrl+z", lambda evt: self._undo()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Redo\tCtrl+y", lambda evt: self._redo()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Cut\tCtrl+x", lambda evt: self._cut()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Copy\tCtrl+c", lambda evt: self._copy()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Paste\tCtrl+v", lambda evt: self._paste()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Delete\tDelete", lambda evt: self._delete()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Goto\tCtrl+g", lambda evt: self._file_panel.show_goto()
        )
        menu.setdefault("&Options", {}).setdefault("options", {}).setdefault(
            "Controls...", lambda evt: self._edit_controls()
        )
        menu.setdefault("&Help", {}).setdefault("help", {}).setdefault(
            "Controls", lambda evt: self._help_controls()
        )
        return menu

    def _edit_controls(self):
        edit_config = CONFIG.get(EDIT_CONFIG_ID, {})
        keybind_id = edit_config.get("keybind_group", DefaultKeybindGroupId)
        user_keybinds = edit_config.get("user_keybinds", {})
        key_config = KeyConfigDialog(self, keybind_id, KeybindKeys, PresetKeybinds, user_keybinds)
        if key_config.ShowModal() == wx.ID_OK:
            user_keybinds, keybind_id, keybinds = key_config.options
            edit_config["user_keybinds"] = user_keybinds
            edit_config["keybind_group"] = keybind_id
            CONFIG.put(EDIT_CONFIG_ID, edit_config)
            self._canvas.set_key_binds(keybinds)

    @staticmethod
    def _help_controls():
        webbrowser.open(
            "https://github.com/Amulet-Team/Amulet-Map-Editor/blob/master/amulet_map_editor/programs/edit/readme.md"
        )

    def _on_resize(self, event):
        if self._canvas is not None:
            self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        event.Skip()

    def _undo(self, *_):
        self._world.undo()
        self._file_panel.update_buttons()

    def _redo(self, *_):
        self._world.redo()
        self._file_panel.update_buttons()

    def _save_world(self, *_):
        self._canvas.disable_threads()

        def save():
            for chunk_index, chunk_count in self._world.save_iter():
                yield 100 * chunk_index / chunk_count

        show_loading_dialog(lambda: save(), f"Saving world.", "Please wait.", self)
        self._file_panel.update_buttons()
        self._canvas.enable_threads()

    def _get_box(self) -> Optional[SelectionGroup]:
        group = self._canvas.selection_group
        if group.selection_boxes:
            return group
        else:
            wx.MessageBox(
                "You must select an area of the world before running this operation"
            )
            return None

    def _run_operation_event(self, evt):
        self._run_operation()
        evt.Skip()

    def _run_operation(self, operation_path=None) -> Any:
        if operation_path is None:
            operation_path = self._operation_options.operation
        operation = plugins.all_operations[operation_path]
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
                            plugins.options.get(operation_path, {})
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
                    log.error(f"Error running structure operation: {e}\n{traceback.format_exc()}")
                    wx.MessageBox(f"Error running structure operation: {e}")
                    self._world.restore_last_undo_point()
                    self._canvas.enable_threads()
                    return
                self._canvas.enable_threads()

                self._operation_options.Enable()
                if not isinstance(structure, Structure):
                    log.error("Object returned from structure_callable was not a Structure. Aborting.")
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
                    plugins.options.get(operation_path, {}),
                )
            else:
                # trigger UI to show select box multiple UI
                raise NotImplementedError

        else:
            self._operation_options.Disable()
            out = self._run_main_operation(
                operation_path, operation["operation"], operation_input_definitions
            )
            self._operation_options.Enable()
            return out

    def _run_main_operation(
        self,
        operation_path: str,
        operation: OperationType,
        operation_input_definitions: List[str],
        options=None,
        structure=None,
    ) -> Any:
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
                    plugins.options[operation_path] = options
                    operation_inputs.append(options)
                else:
                    operation_inputs.append(plugins.options.get(operation_path, {}))

        self._canvas.disable_threads()
        try:
            out = show_loading_dialog(
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
            operation_info = plugins.all_operations[operation_path]
            log.error(
                f'Error occurred while running operation: {operation_info["name"]} v{operation_info["v"]}'
            )
            log.error(f"{e}\n{traceback.format_exc()}")
            wx.MessageBox(f"Error running operation: {e}")
            self._world.restore_last_undo_point()
            out = None
        self._canvas.enable_threads()
        return out

    def _cut(self) -> bool:
        return self._run_operation(os.path.join(os.path.dirname(plugins.__file__), 'internal_operations', 'cut.py'))

    def _copy(self) -> bool:
        return self._run_operation(os.path.join(os.path.dirname(plugins.__file__), 'internal_operations', 'copy.py'))

    def _paste(self) -> bool:
        self.show_operation_options(None)
        return self._run_operation(os.path.join(os.path.dirname(plugins.__file__), 'internal_operations', 'paste.py'))

    def _delete(self) -> bool:
        return self._run_operation(os.path.join(os.path.dirname(plugins.__file__), 'internal_operations', 'delete.py'))

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
