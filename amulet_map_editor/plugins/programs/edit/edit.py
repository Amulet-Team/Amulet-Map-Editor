import wx
import weakref
from typing import TYPE_CHECKING, Optional, List, Callable, Any
import webbrowser

from amulet.api.selection import Selection, SubSelectionBox
from amulet.api.structure import Structure, structure_buffer
from amulet.operations.paste import paste

from amulet_map_editor.plugins.programs import BaseWorldProgram, MenuData
from amulet_map_editor.amulet_wx.simple import SimplePanel, SimpleChoiceAny
from amulet_map_editor.plugins import operations
from .operation_ui import SelectOperationUI, SelectDestinationUI

from .canvas.controllable_canvas import ControllableEditCanvas

if TYPE_CHECKING:
    from amulet.api.world import World


class FilePanel(wx.Panel):
    def __init__(self, parent, world, undo_evt, redo_evt, save_evt, close_evt):
        wx.Panel.__init__(self, parent)
        self._canvas = None
        self._world = weakref.ref(world)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

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

    def set_canvas(self, canvas):
        self._canvas = weakref.ref(canvas)

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


class OperationUI(wx.Panel):
    def __init__(self, parent, world, run_operation, run_main_operation):
        wx.Panel.__init__(self, parent)

        self._world = weakref.ref(world)
        self._canvas = None
        self._run_main_operation =run_main_operation

        middle_sizer = wx.BoxSizer(wx.VERTICAL)

        self._operation_ui: Optional[SelectOperationUI] = SelectOperationUI(self, world, run_operation)
        middle_sizer.Add(self._operation_ui)
        # self._operation_ui.Bind(wx.EVT_ENTER_WINDOW, self._steal_focus_operation)
        self._operation_ui.Layout()
        self._operation_ui.Fit()
        self._select_destination_ui: Optional[SelectDestinationUI] = SelectDestinationUI(
            self,
            self._destination_select_cancel,
            self._destination_select_confirm
        )
        middle_sizer.Add(self._select_destination_ui)
        # self._select_destination_ui.Bind(wx.EVT_ENTER_WINDOW, self._steal_focus_destination)
        self._select_destination_ui.Layout()
        self._select_destination_ui.Fit()
        self._select_destination_ui.Hide()

        self.SetSizer(middle_sizer)
        middle_sizer.Fit(self)
        self.Layout()

    def set_canvas(self, canvas):
        self._canvas = weakref.ref(canvas)
        self._select_destination_ui.bind_locations(canvas.structure_locations)

    def enable_select_destination_ui(self, operation_path: Any, operation: Callable, operation_input_definitions: List[str], structure: Structure, options: dict):
        self._select_destination_ui.setup(operation_path, operation, operation_input_definitions, structure, options)
        self._hide_all()
        self._select_destination_ui.Show()
        self.Fit()
        self._canvas().structure = structure
        self._canvas().select_mode = 1

    def _destination_select_cancel(self):
        self.enable_operation_ui()

    def _destination_select_confirm(self, *args, **kwargs):
        self._select_destination_ui.Disable()
        self._run_main_operation(*args, **kwargs)
        self._select_destination_ui.Enable()
        self.enable_operation_ui()

    def enable_operation_ui(self):
        self._hide_all()
        self._operation_ui.Show()
        self._canvas().select_mode = 0
        self.Fit()

    def hide(self):
        self.Hide()

    def _hide_all(self):
        self._operation_ui.Hide()
        self._select_destination_ui.Hide()

    @property
    def operation(self):
        return self._operation_ui.operation


class ToolSelect(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: toolSelect.__init__
        kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE
        wx.Panel.__init__(self, *args, **kwds)
        self.button_6 = wx.Button(self, wx.ID_ANY, "button_6")
        self.button_7 = wx.Button(self, wx.ID_ANY, "button_7")

        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bottom_sizer.Add(self.button_6, 0, 0, 0)
        bottom_sizer.Add(self.button_7, 0, 0, 0)
        self.SetSizer(bottom_sizer)
        bottom_sizer.Fit(self)
        self.Layout()


class EditExtension(BaseWorldProgram):
    def __init__(self, parent, world: 'World'):
        super().__init__(parent, wx.VERTICAL)
        self._world = world
        self._canvas: Optional[ControllableEditCanvas] = None
        self._temp = wx.StaticText(self, label='Please wait while the renderer loads')
        self._temp.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        # self.add_object(self._temp)

        self._top_panel: Optional[FilePanel] = None
        self._left_panel: Optional[OperationUI] = None
        self._bottom_panel: Optional[ToolSelect] = None

        self._options_button: Optional[wx.Button] = None

        self.Bind(wx.EVT_SIZE, self._on_resize)

    def enable(self):
        if self._canvas is None:
            self.Update()

            self._canvas = ControllableEditCanvas(self, self._world)

            self._top_panel = FilePanel(self._canvas, self._world, self._undo_event, self._redo_event, self._save_event, self._close_world)
            self._left_panel = OperationUI(self._canvas, self._world, self._run_operation, self._run_main_operation)
            self._bottom_panel = ToolSelect(self._canvas, wx.ID_ANY)

            self._top_panel.set_canvas(self._canvas)
            self._left_panel.set_canvas(self._canvas)

            self._top_panel.Hide()
            self._left_panel.Hide()
            self._bottom_panel.Hide()

            self.sizer.Add(self._canvas, 0, wx.EXPAND)

            canvas_sizer = wx.BoxSizer(wx.VERTICAL)
            self._canvas.SetSizer(canvas_sizer)
            bottom_sizer0 = wx.BoxSizer(wx.HORIZONTAL)
            middle_sizer0 = wx.BoxSizer(wx.VERTICAL)
            top_sizer0 = wx.BoxSizer(wx.HORIZONTAL)
            top_sizer0.Add((20, 20), 1, 0, 0)
            top_sizer0.Add(self._top_panel, 0, wx.EXPAND, 0)
            canvas_sizer.Add(top_sizer0, 0, wx.EXPAND, 0)
            middle_sizer0.Add((20, 20), 1, 0, 0)
            middle_sizer0.Add(self._left_panel, 0, 0, 0)
            middle_sizer0.Add((20, 20), 1, 0, 0)
            canvas_sizer.Add(middle_sizer0, 1, wx.EXPAND, 0)
            bottom_sizer0.Add((20, 20), 1, 0, 0)
            bottom_sizer0.Add(self._bottom_panel, 0, wx.EXPAND, 0)
            bottom_sizer0.Add((20, 20), 1, 0, 0)
            canvas_sizer.Add(bottom_sizer0, 0, wx.EXPAND, 0)

            self._temp.Destroy()
            self._top_panel.Show()
            self._left_panel.Show()
            self._bottom_panel.Show()

            self.Layout()
        self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        self._canvas.draw()
        self._canvas.Update()
        self._canvas.enable()
        self._top_panel.change_dimension()

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
        self._top_panel.update_buttons()

    def _redo_event(self, _):
        self._world.redo()
        self._top_panel.update_buttons()

    def _save_event(self, _):
        self._save_world()

    def _save_world(self):
        self._canvas.disable_threads()
        self._world.save()
        self._top_panel.update_buttons()
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
        operation_path = self._left_panel.operation
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

                self._left_panel.Disable()

                self._canvas.disable_threads()
                try:
                    structure = self._world.run_operation(operation["structure_callable"], self._canvas.dimension, *operation_inputs, create_undo=False)
                except Exception as e:
                    wx.MessageBox(f"Error running structure operation: {e}")
                    self._world.restore_last_undo_point()
                    self._canvas.enable_threads()
                    return
                self._canvas.enable_threads()

                self._left_panel.Enable()
                if not isinstance(structure, Structure):
                    wx.MessageBox("Object returned from structure_callable was not a Structure. Aborting.")
                    return
            else:
                selection = self._get_box()
                if selection is None:
                    return
                self._left_panel.Disable()
                structure = Structure.from_world(self._world, selection, self._canvas.dimension)
                self._left_panel.Enable()

            if "dst_location_absolute" in features:
                # trigger UI to show select box UI
                self._left_panel.enable_select_destination_ui(
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
            self._left_panel.Disable()
            self._run_main_operation(operation_path, operation["operation"], operation_input_definitions)
            self._left_panel.Enable()
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
            self._top_panel.update_buttons()
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
        self._left_panel.enable_select_destination_ui(
            None,
            paste,
            ["structure", "options"],
            structure,
            {}
        )

    # def _steal_focus_menu(self, evt):
    #     self._left_panel.SetFocus()
    #     evt.Skip()

    # def _steal_focus_operation(self, evt):
    #     self._operation_ui.SetFocus()
    #     evt.Skip()
    #
    # def _steal_focus_destination(self, evt):
    #     self._select_destination_ui.SetFocus()
    #     evt.Skip()
