import wx
from typing import Callable, Dict, Any, TYPE_CHECKING, Sequence

from amulet_map_editor.api.wx.util.validators import IntValidator

from amulet.api.data_types import OperationReturnType
from amulet_map_editor.programs.edit.api.operations.operation_ui import OperationUI

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas
    from amulet.api.level import BaseLevel

FixedOperationType = Callable[
    ["BaseLevel", "Dimension", "SelectionGroup", Dict[str, Any]], OperationReturnType
]


class FixedFunctionUI(wx.Panel, OperationUI):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
        operation: FixedOperationType,
        options: Dict[str, Any],
    ):
        wx.Panel.__init__(self, parent)
        OperationUI.__init__(self, parent, canvas, world, options_path)
        self._operation = operation

        self.Hide()
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)
        self._options_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(self._options_sizer)
        self._run_button = wx.Button(self, label="Run Operation")
        self._run_button.Bind(wx.EVT_BUTTON, self._run_operation)
        self._sizer.Add(self._run_button, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self._options: Dict[str, wx.Window] = {}
        self._create_options(options)

        self.Layout()
        self.Show()

    def unload(self):
        pass

    def _create_options(self, options: Dict[str, Sequence]):
        create_functions: Dict[str, Callable[[str, Sequence], None]] = {
            "label": self._create_label,
            "bool": self._create_bool,
            "int": self._create_int,
            "float": self._create_float,
            "str": self._create_string,
            "str_choice": self._create_str_choice,
            "file_open": self._create_file_open_picker,
            "file_save": self._create_file_save_picker,
            "directory": self._create_directory_picker,
        }
        for option_name, option in options.items():
            if not (isinstance(option, (list, tuple)) and option):
                continue
            option_type, option = option[0], option[1:]
            if option_type not in create_functions:
                continue
            create_functions[option_type](option_name, option)

    def _create_label(self, option_name: str, options: Sequence):
        label = wx.StaticText(self, label=option_name)
        self._options_sizer.Add(label, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

    def _create_horizontal_options_sizer(self, label) -> wx.BoxSizer:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, label=label)
        sizer.Add(label, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        self._options_sizer.Add(sizer, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)
        return sizer

    def _create_bool(self, option_name: str, options: Sequence):
        if options and not isinstance(options[0], bool):
            return
        sizer = self._create_horizontal_options_sizer(option_name)
        option = wx.CheckBox(self)
        sizer.Add(option)
        if options:
            option.SetValue(options[0])
        self._options[option_name] = option

    def _create_int(self, option_name: str, options: Sequence):
        if len(options) in {0, 1, 3} and all(isinstance(o, int) for o in options):
            sizer = self._create_horizontal_options_sizer(option_name)
            if len(options) == 0:
                option = wx.SpinCtrl(
                    self,
                    min=-30_000_000,
                    max=30_000_000,
                    initial=0,
                )
            elif len(options) == 1:
                option = wx.SpinCtrl(
                    self,
                    min=-30_000_000,
                    max=30_000_000,
                    initial=options[0],
                )
            elif len(options) == 3:
                option = wx.SpinCtrl(
                    self,
                    min=min(options[1:3]),
                    max=max(options[1:3]),
                    initial=options[0],
                )
            else:
                return  # should not get here
            option.SetValidator(IntValidator())
            sizer.Add(option)
            self._options[option_name] = option

    def _create_float(self, option_name: str, options: Sequence):
        if len(options) in {0, 1, 3} and all(
            isinstance(o, (int, float)) for o in options
        ):
            sizer = self._create_horizontal_options_sizer(option_name)
            if len(options) == 0:
                option = wx.SpinCtrlDouble(
                    self,
                    min=-30_000_000,
                    max=30_000_000,
                    initial=0,
                )
            elif len(options) == 1:
                option = wx.SpinCtrlDouble(
                    self,
                    min=-30_000_000,
                    max=30_000_000,
                    initial=options[0],
                )
            elif len(options) == 3:
                option = wx.SpinCtrlDouble(
                    self,
                    min=min(options[1:3]),
                    max=max(options[1:3]),
                    initial=options[0],
                )
            else:
                return  # should not get here
            sizer.Add(option)
            self._options[option_name] = option

    def _create_string(self, option_name: str, options: Sequence):
        if options and not isinstance(options[0], str):
            return
        sizer = self._create_horizontal_options_sizer(option_name)
        option = wx.TextCtrl(self)
        sizer.Add(option)
        if options:
            option.SetValue(options[0])
        self._options[option_name] = option

    def _create_str_choice(self, option_name: str, options: Sequence):
        if not (options and all(isinstance(o, str) for o in options)):
            return
        sizer = self._create_horizontal_options_sizer(option_name)
        option = wx.Choice(self, choices=options)
        option.SetSelection(0)
        sizer.Add(option)
        self._options[option_name] = option

    def _create_file_save_picker(self, option_name: str, options: Sequence):
        sizer = self._create_horizontal_options_sizer(option_name)
        option = wx.FilePickerCtrl(self, style=wx.FLP_SAVE | wx.FLP_USE_TEXTCTRL)
        sizer.Add(option)
        self._options[option_name] = option

    def _create_file_open_picker(self, option_name: str, options: Sequence):
        sizer = self._create_horizontal_options_sizer(option_name)
        option = wx.FilePickerCtrl(self, style=wx.FLP_OPEN | wx.FLP_USE_TEXTCTRL)
        sizer.Add(option)
        self._options[option_name] = option

    def _create_directory_picker(self, option_name: str, options: Sequence):
        sizer = self._create_horizontal_options_sizer(option_name)
        option = wx.DirPickerCtrl(self, style=wx.DIRP_USE_TEXTCTRL)
        sizer.Add(option)
        self._options[option_name] = option

    def _get_values(self) -> Dict[str, Any]:
        options = {}
        for key, window in self._options.items():
            if isinstance(
                window,
                (
                    wx.CheckBox,
                    wx.SpinCtrl,
                    wx.SpinCtrlDouble,
                    wx.TextCtrl,
                ),
            ):
                options[key] = window.GetValue()
            elif isinstance(window, wx.Choice):
                options[key] = window.GetString(window.GetSelection())
            elif isinstance(window, (wx.FilePickerCtrl, wx.DirPickerCtrl)):
                options[key] = window.GetPath()
        return options

    def _run_operation(self, evt):
        self.canvas.run_operation(
            lambda: self._operation(
                self.world,
                self.canvas.dimension,
                self.canvas.selection.selection_group,
                self._get_values(),
            )
        )
