import wx
import weakref
from typing import TYPE_CHECKING, Optional, List, Callable
import webbrowser

from amulet.api.selection import Selection, SubSelectionBox
from amulet.api.structure import Structure, structure_buffer
from amulet.operations.paste import paste

from amulet_map_editor.plugins.programs import BaseWorldProgram, MenuData
from amulet_map_editor.amulet_wx.simple import SimpleChoiceAny
from amulet_map_editor.plugins import operations
from .operation_ui import OperationUI
from .events import EVT_CAMERA_MOVE, SelectToolEnabledEvent, OperationToolEnabledEvent, EVT_SELECT_TOOL_ENABLED, EVT_OPERATION_TOOL_ENABLED

from .canvas.controllable_canvas import ControllableEditCanvas

if TYPE_CHECKING:
    from amulet.api.world import World


class FilePanel(wx.Panel):
    def __init__(self, canvas, world, undo_evt, redo_evt, save_evt, close_evt):
        wx.Panel.__init__(self, canvas)
        self._canvas = weakref.ref(canvas)
        self._world = weakref.ref(world)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self._location_label = wx.StaticText(self, label="x, y, z")
        top_sizer.Add(self._location_label, 0, wx.ALL | wx.CENTER, 5)

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
        self._canvas().dimension = dimension

    def move_event(self, evt):
        self._location_label.SetLabel(f'{evt.x:.2f}, {evt.y:.2f}, {evt.z:.2f}')
        self.Layout()
        self.GetParent().Layout()


class SelectOptions(wx.Panel):
    def __init__(self, canvas):
        wx.Panel.__init__(self, canvas)
        self._canvas = weakref.ref(canvas)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        button = wx.Button(self, label='hi')
        sizer.Add(button)

    def enable(self):
        self._canvas().select_mode = 0
        self.Show()

"""
SelectOptions
OperationOptions
    SelectOperationOptions
    SelectAbsoluteLocationOptions
    # SelectAbsoluteLocationMultipleOptions
    # SelectCloneOptions
"""


class ToolSelect(wx.Panel):
    def __init__(self, canvas):
        wx.Panel.__init__(self, canvas)

        self.select_button = wx.Button(self, label="Select")
        self.select_button.Bind(wx.EVT_BUTTON, self._select_evt)
        self.operation_button = wx.Button(self, label="Operation")
        self.operation_button.Bind(wx.EVT_BUTTON, self._operation_evt)

        # self.import_button = wx.Button(self, label="Import")
        # self.export_button = wx.Button(self, label="Export")

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.select_button)
        sizer.Add(self.operation_button)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def _select_evt(self, evt):
        wx.PostEvent(self, SelectToolEnabledEvent())

    def _operation_evt(self, evt):
        wx.PostEvent(self, OperationToolEnabledEvent())


class EditExtension(BaseWorldProgram):
    def __init__(self, parent, world: 'World'):
        super().__init__(parent, wx.VERTICAL)
        self._world = world
        self._canvas: Optional[ControllableEditCanvas] = None
        self._temp = wx.StaticText(self, label='Please wait while the renderer loads')
        self._temp.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

        self._file_panel: Optional[FilePanel] = None
        self._select_options: Optional[SelectOptions] = None
        self._operation_options: Optional[OperationUI] = None
        self._tool_panel: Optional[ToolSelect] = None

        self.Bind(wx.EVT_SIZE, self._on_resize)

    def enable(self):
        if self._canvas is None:
            self.Update()

            self._canvas = ControllableEditCanvas(self, self._world)

            self._file_panel = FilePanel(self._canvas, self._world, self._undo_event, self._redo_event, self._save_event, self._close_world)
            self._select_options = SelectOptions(self._canvas)
            self._operation_options = OperationUI(self._canvas, self._world, self._run_operation, self._run_main_operation)
            self._tool_panel = ToolSelect(self._canvas)

            self._canvas.Bind(EVT_CAMERA_MOVE, self._file_panel.move_event)
            self._tool_panel.Bind(EVT_SELECT_TOOL_ENABLED, self.show_select_options)
            self._tool_panel.Bind(EVT_OPERATION_TOOL_ENABLED, self.show_operation_options)

            self._file_panel.Hide()
            self._select_options.Hide()
            self._operation_options.Hide()
            self._tool_panel.Hide()

            self.sizer.Add(self._canvas, 0, wx.EXPAND)

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
        self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        self._canvas.draw()
        self._canvas.Update()
        self._canvas.enable()
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
            return self._canvas.is_closeable() and not bool(self._world.chunk_history_manager.unsaved_changes)
        return not bool(self._world.chunk_history_manager.unsaved_changes)

    def _close_world(self, _):
        unsaved_changes = self._world.chunk_history_manager.unsaved_changes
        if unsaved_changes:
            msg = wx.MessageDialog(
                self,
                f"There {'is' if unsaved_changes == 1 else 'are'} {unsaved_changes} unsaved change{'s' if unsaved_changes >= 2 else ''}. Would you like to save?",
                style=wx.YES_NO | wx.CANCEL | wx.CANCEL_DEFAULT
            )
            response = msg.ShowModal()
            if response == wx.ID_YES:
                self._save_world()
            elif response == wx.ID_CANCEL:
                return
        self.GetGrandParent().GetParent().close_world(self._world.world_path)

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Undo\tCtrl+z', lambda evt: self._world.undo())
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Redo\tCtrl+y', lambda evt: self._world.redo())
        # menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Cut', lambda evt: self.world.save())
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Copy\tCtrl+c', lambda evt: self._copy())
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Paste\tCtrl+v', lambda evt: self._paste())
        menu.setdefault('&Help', {}).setdefault('control', {}).setdefault('Controls', lambda evt: self._help_controls())
        return menu

    @staticmethod
    def _help_controls():
        webbrowser.open("https://github.com/Amulet-Team/Amulet-Map-Editor/tree/master/amulet_map_editor/plugins/programs/edit/readme.md")

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
        self._world.save()
        self._file_panel.update_buttons()
        self._canvas.enable_threads()

    def _get_box(self) -> Optional[Selection]:
        box = self._canvas._selection_box  # TODO: make a way to publicly access this
        if box.select_state == 2:
            return Selection(
                (SubSelectionBox(
                    box.min,
                    box.max
                ),)
            )
        else:
            wx.MessageBox("You must select an area of the world before running this operation")
            return None

    def _run_operation(self, evt):
        operation_path = self._operation_options.operation
        operation = operations.operations[operation_path]
        features = operation.get("features", [])
        operation_input_definitions = operation.get("inputs", [])
        if any(feature in features for feature in ("dst_location_absolute", )):
            if "structure_callable" in operation:
                operation_inputs = []
                for inp in operation.get("structure_callable_inputs", []):
                    if inp == "src_selection":
                        selection = self._get_box()
                        if selection is None:
                            return
                        operation_inputs.append(selection)

                    elif inp == "options":
                        operation_inputs.append(operations.options.get(operation_path, {}))

                self._operation_options.Disable()

                self._canvas.disable_threads()
                try:
                    structure = self._world.run_operation(operation["structure_callable"], self._canvas.dimension, *operation_inputs, create_undo=False)
                except Exception as e:
                    wx.MessageBox(f"Error running structure operation: {e}")
                    self._world.restore_last_undo_point()
                    self._canvas.enable_threads()
                    return
                self._canvas.enable_threads()

                self._operation_options.Enable()
                if not isinstance(structure, Structure):
                    wx.MessageBox("Object returned from structure_callable was not a Structure. Aborting.")
                    return
            else:
                selection = self._get_box()
                if selection is None:
                    return
                self._operation_options.Disable()
                structure = Structure.from_world(self._world, selection, self._canvas.dimension)
                self._operation_options.Enable()

            if "dst_location_absolute" in features:
                # trigger UI to show select box UI
                self._operation_options.enable_select_destination_ui(
                    operation_path,
                    operation["operation"],
                    operation_input_definitions,
                    structure,
                    operations.options.get(operation_path, {})
                )
            else:
                # trigger UI to show select box multiple UI
                raise NotImplementedError

        else:
            self._operation_options.Disable()
            self._run_main_operation(operation_path, operation["operation"], operation_input_definitions)
            self._operation_options.Enable()
        evt.Skip()

    def _run_main_operation(self, operation_path: str, operation: Callable, operation_input_definitions: List[str], options=None, structure=None):
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
            self._world.run_operation(operation, self._canvas.dimension, *operation_inputs)
            self._file_panel.update_buttons()
        except Exception as e:
            wx.MessageBox(f"Error running operation: {e}")
            self._world.restore_last_undo_point()
        self._canvas.enable_threads()

    def _copy(self):
        selection = self._get_box()
        if selection is None:
            return
        structure = Structure.from_world(self._world, selection, self._canvas.dimension)
        structure_buffer.append(structure)

    def _paste(self):
        structure = structure_buffer[-1]
        self._operation_options.enable_select_destination_ui(
            None,
            paste,
            ["structure", "options"],
            structure,
            {}
        )

    def show_select_options(self, _):
        self._operation_options.Hide()
        self._select_options.enable()
        self.Layout()

    def show_operation_options(self, _):
        self._select_options.Hide()
        self._operation_options.enable_operation_ui()
        self.Layout()
