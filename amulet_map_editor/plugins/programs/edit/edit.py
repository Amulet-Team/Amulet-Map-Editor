import wx
import weakref
import numpy
from typing import TYPE_CHECKING, Optional, List, Callable, Type, Any
import webbrowser

from amulet.api.selection import Selection, SubSelectionBox
from amulet.api.structure import Structure, structure_buffer
from amulet.operations.paste import paste

from amulet_map_editor import log
from amulet_map_editor.plugins.programs import BaseWorldProgram, MenuData
from amulet_map_editor.amulet_wx.simple import SimplePanel, SimpleChoiceAny
from amulet_map_editor.plugins import operations
from .operation_ui import SelectOperationUI, SelectDestinationUI

from .controllable_canvas import ControllableEditCanvas

if TYPE_CHECKING:
    from amulet.api.world import World


class EditExtension(BaseWorldProgram):
    def __init__(self, parent, world: 'World'):
        super().__init__(parent, wx.HORIZONTAL)
        self._world = world
        self._canvas: Optional[ControllableEditCanvas] = None
        self._temp = wx.StaticText(
            self,
            wx.ID_ANY,
            'Please wait while the renderer loads',
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self._menu: Optional[SimplePanel] = None
        self._operation_ui: Optional[OperationUI] = None
        self._select_destination_ui: Optional[SelectDestinationUI] = None
        self._menu_buttons: List[wx.Button] = []
        self._dim_options: Optional[SimpleChoiceAny] = None
        self._options_button: Optional[wx.Button] = None
        self._undo_button: Optional[wx.Button] = None
        self._redo_button: Optional[wx.Button] = None
        self._save_button: Optional[wx.Button] = None
        self._temp.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        self.Bind(wx.EVT_SIZE, self._on_resize)

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Undo\tCtrl+z', lambda evt: self._world.undo())
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Redo\tCtrl+y', lambda evt: self._world.redo())
        # menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Cut', lambda evt: self.world.save())
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Copy\tCtrl+c', lambda evt: self._copy())
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Paste\tCtrl+v', lambda evt: self._paste())
        menu.setdefault('&Help', {}).setdefault('control', {}).setdefault('Controls', lambda evt: self._help_controls())
        return menu

    def _help_controls(self):
        webbrowser.open("https://github.com/Amulet-Team/Amulet-Map-Editor/tree/master/amulet_map_editor/plugins/programs/edit/readme.md")

    def _on_resize(self, event):
        if self._canvas is not None:
            self._canvas.SetSize(self.GetSize()[0], self.GetSize()[1])
        event.Skip()

    def _undo_event(self, evt):
        self._world.undo()
        self._update_buttons()

    def _redo_event(self, evt):
        self._world.redo()
        self._update_buttons()

    def _update_buttons(self):
        self._undo_button.SetLabel(f"Undo | {self._world.chunk_history_manager.undo_count}")
        self._redo_button.SetLabel(f"Redo | {self._world.chunk_history_manager.redo_count}")
        self._save_button.SetLabel(f"Save | {self._world.chunk_history_manager.unsaved_changes}")

    def _save_event(self, evt):
        self._save_world()

    def _save_world(self):
        self._canvas.disable_threads()
        self._world.save()
        self._update_buttons()
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

    def _enable_operation_ui(self):
        self._select_destination_ui.Hide()
        self._operation_ui.Show()
        self._canvas.select_mode = 0
        self._menu.Fit()

    def _enable_select_destination_ui(self, structure: Structure):
        self._operation_ui.Hide()
        self._select_destination_ui.Show()
        self._menu.Fit()
        self._canvas.structure = structure
        self._canvas.select_mode = 1

    def _run_operation(self, evt):
        operation_path = self._operation_ui.operation
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

                self._operation_ui.Disable()

                self._canvas.disable_threads()
                try:
                    structure = self._world.run_operation(operation["structure_callable"], self._canvas.dimension, *operation_inputs, create_undo=False)
                except Exception as e:
                    wx.MessageBox(f"Error running structure operation: {e}")
                    self._world.restore_last_undo_point()
                    self._canvas.enable_threads()
                    return
                self._canvas.enable_threads()

                self._operation_ui.Enable()
                if not isinstance(structure, Structure):
                    wx.MessageBox("Object returned from structure_callable was not a Structure. Aborting.")
                    return
            else:
                selection = self._get_box()
                if selection is None:
                    return
                self._operation_ui.Disable()
                structure = Structure.from_world(self._world, selection, self._canvas.dimension)
                self._operation_ui.Enable()

            if "dst_location_absolute" in features:
                # trigger UI to show select box UI
                self._select_destination_ui.setup(
                    operation_path,
                    operation["operation"],
                    operation_input_definitions,
                    structure,
                    operations.options.get(operation_path, {})
                )
                self._enable_select_destination_ui(structure)
            else:
                # trigger UI to show select box multiple UI
                raise NotImplementedError

        else:
            self._operation_ui.Disable()
            self._run_main_operation(operation_path, operation["operation"], operation_input_definitions)
            self._operation_ui.Enable()
        evt.Skip()

    def _destination_select_cancel(self):
        self._enable_operation_ui()

    def _destination_select_confirm(self, *args, **kwargs):
        self._select_destination_ui.Disable()
        self._run_main_operation(*args, **kwargs)
        self._select_destination_ui.Enable()
        self._enable_operation_ui()

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
            self._update_buttons()
        except Exception as e:
            wx.MessageBox(f"Error running operation: {e}")
            self._world.restore_last_undo_point()
        self._canvas.enable_threads()

    def enable(self):
        if self._canvas is None:
            self.Update()
            self._menu = SimplePanel(self)
            self._menu.Hide()
            self.add_object(self._menu, 0, wx.EXPAND)
            self._menu.Bind(wx.EVT_ENTER_WINDOW, self._steal_focus_menu)

            dim_label = wx.StaticText(self._menu, label="Dimension:")
            self._dim_options = SimpleChoiceAny(self._menu)
            self._dim_options.SetItems(dict(zip(self._world.world_wrapper.dimensions.values(), self._world.world_wrapper.dimensions.keys())))
            self._dim_options.SetValue("overworld")
            self._dim_options.Bind(wx.EVT_CHOICE, self._on_dimension_change)

            sizer = wx.BoxSizer(wx.HORIZONTAL)
            sizer.Add(dim_label, 0, wx.ALL, 5)
            sizer.Add(self._dim_options, 0, wx.ALL, 5)
            self._menu.add_object(sizer, 0)

            def create_button(text, operation):
                button = wx.Button(
                    self._menu,
                    label=text
                )
                button.Bind(wx.EVT_BUTTON, operation)
                self._menu.add_object(button, 0)
                self._menu_buttons.append(
                    button
                )
                return button
            self._undo_button = create_button('Undo', self._undo_event)
            self._redo_button = create_button('Redo', self._redo_event)
            self._save_button = create_button('Save', self._save_event)
            create_button('Close', self._close_world)
            self._update_buttons()

            self._operation_ui = OperationUI(self._menu, self._world, self._run_operation)
            self._menu.add_object(self._operation_ui, options=0)
            self._operation_ui.Bind(wx.EVT_ENTER_WINDOW, self._steal_focus_operation)
            self._operation_ui.Layout()
            self._operation_ui.Fit()
            self._canvas = ControllableEditCanvas(self, self._world)
            self._select_destination_ui = SelectDestinationUI(
                self._menu,
                self._destination_select_cancel,
                self._destination_select_confirm,
                self._canvas.structure_locations
            )
            self._menu.add_object(self._select_destination_ui, options=0)
            self._select_destination_ui.Bind(wx.EVT_ENTER_WINDOW, self._steal_focus_destination)
            self._select_destination_ui.Layout()
            self._select_destination_ui.Fit()
            self._select_destination_ui.Hide()

            self.add_object(self._canvas, 0, wx.EXPAND)
            self._temp.Destroy()
            self._menu.Show()

            self.GetParent().Layout()
            self._menu.Layout()
            self._menu.Fit()
            self.Update()
        self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        self._canvas.draw()
        self._canvas.Update()
        self._canvas.enable()
        self._change_dimension()

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

    def _copy(self):
        selection = self._get_box()
        if selection is None:
            return
        structure = Structure.from_world(self._world, selection, self._canvas.dimension)
        structure_buffer.append(structure)

    def _paste(self):
        structure = structure_buffer[-1]
        self._select_destination_ui.setup(
            None,
            paste,
            ["structure", "options"],
            structure,
            {}
        )
        self._enable_select_destination_ui(structure)

    def _on_dimension_change(self, evt):
        self._change_dimension()
        evt.Skip()

    def _change_dimension(self):
        dimension = self._dim_options.GetAny()
        self._canvas.dimension = dimension

    def _steal_focus_menu(self, evt):
        self._menu.SetFocus()
        evt.Skip()

    def _steal_focus_operation(self, evt):
        self._operation_ui.SetFocus()
        evt.Skip()

    def _steal_focus_destination(self, evt):
        self._select_destination_ui.SetFocus()
        evt.Skip()
