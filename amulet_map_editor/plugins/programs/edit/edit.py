import wx
import weakref
import numpy
from typing import TYPE_CHECKING, Optional, List, Callable, Type, Any

from amulet.api.selection import Selection, SubSelectionBox
from amulet.api.structure import Structure, structure_buffer
from amulet.operations.paste import paste

from amulet_map_editor import log
from amulet_map_editor.plugins.programs import BaseWorldProgram, MenuData
from amulet_map_editor.amulet_wx.simple import SimplePanel, SimpleChoiceAny, SimpleText
from amulet_map_editor.plugins import operations

from .controllable_canvas import ControllableEditCanvas

if TYPE_CHECKING:
    from amulet.api.world import World


class OperationUI(SimplePanel):
    def __init__(self, parent, world: 'World', run_operation: Callable):
        super().__init__(parent)
        self._world = weakref.ref(world)
        self._operation_choice = SimpleChoiceAny(self)
        self._operation_choice.SetItems({key: value["name"] for key, value in operations.operations.items()})
        self._operation_choice.Bind(wx.EVT_CHOICE, self._operation_selection_change)
        self.add_object(self._operation_choice, 0)
        self._options_button = wx.Button(
            self,
            label="Change Options"
        )
        run_button = wx.Button(
            self,
            label="Run Operation"
        )
        self._options_button.Bind(wx.EVT_BUTTON, self._change_options)
        run_button.Bind(wx.EVT_BUTTON, run_operation)
        self.add_object(self._options_button, 0)
        self.add_object(run_button, 0)
        self._operation_selection_change_()

    @property
    def operation(self) -> str:
        return self._operation_choice.GetAny()

    def _operation_selection_change(self, evt):
        self._operation_selection_change_()
        evt.Skip()

    def _operation_selection_change_(self):
        operation_path = self._operation_choice.GetAny()
        operation = operations.operations[operation_path]
        if "options" in operation.get("features", []) or "wxoptions" in operation.get("features", []):
            self._options_button.Enable()
        else:
            self._options_button.Disable()

    def _change_options(self, evt):
        operation_path = self._operation_choice.GetAny()
        operation = operations.operations[operation_path]
        if "options" in operation.get("features", []):
            pass  # TODO: implement this
        elif "wxoptions" in operation.get("features", []):
            options = operation["wxoptions"](self, self._world(), operations.options.get(operation_path, {}))
            if isinstance(options, dict):
                operations.options[operation_path] = options
            else:
                log.error(f"Plugin {operation['name']} at {operation_path} did not return options in a valid format")
        evt.Skip()


class SelectDestinationUI(SimplePanel):
    def __init__(self, parent, cancel_callback, confirm_callback, locations: List[numpy.ndarray]):
        super().__init__(parent)
        self._cancel_callback = cancel_callback
        self._confirm_callback = confirm_callback
        self._locations = locations

        self._operation_path: Optional[str] = None
        self._operation: Optional[Callable] = None
        self._operation_input_definitions: Optional[List[str]] = None
        self._structure: Optional[Structure] = None
        self._options: Optional[dict] = None

        self._x: wx.SpinCtrl = self._add_row('x', wx.SpinCtrl, min=-30000000, max=30000000)
        self._y: wx.SpinCtrl = self._add_row('y', wx.SpinCtrl, min=-30000000, max=30000000)
        self._z: wx.SpinCtrl = self._add_row('z', wx.SpinCtrl, min=-30000000, max=30000000)
        self._copy_air: wx.CheckBox = self._add_row('Copy Air', wx.CheckBox)
        self._x.Bind(wx.EVT_SPINCTRL, self._on_location_change)
        self._y.Bind(wx.EVT_SPINCTRL, self._on_location_change)
        self._z.Bind(wx.EVT_SPINCTRL, self._on_location_change)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.add_object(sizer, 0, 0)
        self._cancel = wx.Button(self, label="Cancel")
        sizer.Add(self._cancel, flag=wx.CENTER, border=5)
        self._confirm = wx.Button(self, label="Confirm")
        sizer.Add(self._confirm, flag=wx.CENTER, border=5)

        self._cancel.Bind(wx.EVT_BUTTON, self._on_cancel)
        self._confirm.Bind(wx.EVT_BUTTON, self._on_confirm)

    def setup(self, operation_path: Any, operation: Callable, operation_input_definitions: List[str], structure: Structure, options: dict):
        self._operation_path = operation_path
        self._operation = operation
        self._operation_input_definitions = operation_input_definitions
        self._structure = structure
        self._locations.clear()
        self._locations.append(structure.selection.min)
        self._x.SetValue(structure.selection.min[0])
        self._y.SetValue(structure.selection.min[1])
        self._z.SetValue(structure.selection.min[2])
        self._copy_air.SetValue(options.get('copy_air', False))
        self._options = options

    def _add_row(self, label: str, wx_object: Type[wx.Object], **kwargs) -> Any:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.add_object(sizer, 0, 0)
        name_text = wx.StaticText(self, label=label)
        sizer.Add(name_text, flag=wx.CENTER | wx.ALL, border=5)
        obj = wx_object(self, **kwargs)
        sizer.Add(obj, flag=wx.CENTER | wx.ALL, border=5)
        return obj

    def _on_location_change(self, evt):
        self._locations[-1] = numpy.array([self._x.GetValue(), self._y.GetValue(), self._z.GetValue()])

    def _on_cancel(self, evt):
        self._cancel_callback()

    def _on_confirm(self, evt):
        self._options['location'] = (self._x.GetValue(), self._y.GetValue(), self._z.GetValue())
        self._options['copy_air'] = self._copy_air.GetValue()
        self._confirm_callback(
            self._operation_path,
            self._operation,
            self._operation_input_definitions,
            options=self._options,
            structure=self._structure
        )


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
        self._temp.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        self.Bind(wx.EVT_SIZE, self._on_resize)

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Undo\tCtrl+z', lambda evt: self._world.undo())
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Redo\tCtrl+y', lambda evt: self._world.redo())
        # menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Cut', lambda evt: self.world.save())
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Copy\tCtrl+c', lambda evt: self._copy())
        menu.setdefault('&Edit', {}).setdefault('control', {}).setdefault('Paste\tCtrl+v', lambda evt: self._paste())
        return menu

    def _on_resize(self, event):
        if self._canvas is not None:
            self._canvas.SetSize(self.GetSize()[0], self.GetSize()[1])
        event.Skip()

    def _undo_event(self, evt):
        self._world.undo()

    def _redo_event(self, evt):
        self._world.redo()

    def _save_event(self, evt):
        self._canvas.disable_threads()
        self._world.save()
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

            for text, operation in [
                ['Undo', self._undo_event],
                ['Redo', self._redo_event],
                ['Save', self._save_event],
                ['Close', self._close_world]
            ]:
                button = wx.Button(
                    self._menu,
                    wx.ID_ANY,
                    text,
                    wx.DefaultPosition,
                    wx.DefaultSize,
                    0,
                )
                button.Bind(wx.EVT_BUTTON, operation)
                self._menu.add_object(button, 0)
                self._menu_buttons.append(
                    button
                )

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
            return self._canvas.is_closeable()
        return True

    def _close_world(self, _):
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
