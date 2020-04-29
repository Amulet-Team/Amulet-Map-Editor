import wx
import weakref
from typing import TYPE_CHECKING, Callable, Dict

from amulet_map_editor import log
from amulet_map_editor.amulet_wx.simple import SimplePanel, SimpleChoiceAny
from amulet_map_editor import plugins

if TYPE_CHECKING:
    from amulet.api.world import World


class BaseSelectOperationUI(SimplePanel):
    def __init__(self, parent, world: 'World', run_operation: Callable):
        super().__init__(parent)
        self._world = weakref.ref(world)
        self._operation_choice = SimpleChoiceAny(self)
        self._operation_choice.SetItems({key: value["name"] for key, value in self._operations.items()})
        self._operation_choice.Bind(wx.EVT_CHOICE, self._operation_selection_change)
        self.add_object(self._operation_choice, 0, wx.ALL | wx.EXPAND)
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
        self.add_object(self._options_button, 0, wx.ALL | wx.EXPAND)
        self.add_object(run_button, 0, wx.ALL | wx.EXPAND)
        self._operation_selection_change_()

    @property
    def _operations(self) -> Dict[str, dict]:
        raise NotImplementedError

    @property
    def operation(self) -> str:
        return self._operation_choice.GetAny()

    def _operation_selection_change(self, evt):
        self._operation_selection_change_()
        evt.Skip()

    def _operation_selection_change_(self):
        operation_path = self._operation_choice.GetAny()
        if operation_path:
            operation = self._operations[operation_path]
            if "options" in operation.get("features", []) or "wxoptions" in operation.get("features", []):
                self._options_button.Enable()
            else:
                self._options_button.Disable()
        else:
            self._options_button.Disable()

    def _change_options(self, evt):
        operation_path = self._operation_choice.GetAny()
        if operation_path:
            operation = self._operations[operation_path]
            if "options" in operation.get("features", []):
                pass  # TODO: implement this
            elif "wxoptions" in operation.get("features", []):
                options = operation["wxoptions"](self, self._world(), plugins.options.get(operation_path, {}))
                if isinstance(options, dict):
                    plugins.options[operation_path] = options
                else:
                    log.error(f"Plugin {operation['name']} at {operation_path} did not return options in a valid format")
        evt.Skip()


class SelectOperationUI(BaseSelectOperationUI):
    @property
    def _operations(self) -> Dict[str, dict]:
        return plugins.operations
