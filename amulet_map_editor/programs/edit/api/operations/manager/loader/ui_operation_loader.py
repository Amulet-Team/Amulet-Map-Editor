from typing import Callable, Optional, Type, TYPE_CHECKING
import inspect
import os
import struct
import hashlib
import wx

from .base_operation_loader import BaseOperationLoader

from amulet_map_editor import log
from amulet.api.level import BaseLevel
from amulet_map_editor.programs.edit.api.operations.ui.fixed_pipeline import (
    FixedFunctionUI,
)
from amulet_map_editor.programs.edit.api.operations.operation_ui import (
    OperationUI,
    OperationUIType,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas
    from amulet.api.level import BaseLevel

ValidChrs = set("-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


class UIOperationLoader(BaseOperationLoader):
    def __init__(self, identifier: str, export_dict: dict):
        self._ui: Optional[
            Callable[[wx.Window, "EditCanvas", "BaseLevel"], OperationUI]
        ] = None
        super().__init__(identifier, export_dict)

    def _setup(self, export_dict: dict):
        """Parse the export dictionary and setup as required."""
        options_path = os.path.abspath(
            os.path.join(
                "config",
                "edit_plugins",
                f"""{''.join(c for c in self._name if c in ValidChrs)}_{
                struct.unpack(
                    "H",
                    hashlib.sha1(
                        self.identifier.encode('utf-8')
                    ).digest()[:2]
                )[0]
                }.config""",  # generate a file name that identifiable to the operation but "unique" to the path
            )
        )

        if "operation" in export_dict:
            if inspect.isclass(export_dict["operation"]) and issubclass(
                export_dict["operation"], (wx.Window, wx.Sizer)
            ):
                operation_ui: Type[OperationUI] = export_dict.get("operation", None)
                if issubclass(operation_ui, OperationUI):
                    self._ui = lambda parent, canvas, world: operation_ui(
                        parent, canvas, world, options_path
                    )
                    self._is_valid = True
                else:
                    log.error(
                        f'"operation" must be a subclass of edit.plugins.OperationUI. {self.identifier}'
                    )

            elif callable(export_dict["operation"]):
                operation = export_dict["operation"]
                if operation.__code__.co_argcount == 4:
                    options = export_dict.get("options", {})
                    if isinstance(options, dict):
                        self._ui = lambda parent, canvas, world: FixedFunctionUI(
                            parent, canvas, world, options_path, operation, options
                        )
                        self._is_valid = True
                    else:
                        log.error(
                            f'"operation" in export must be a dictionary if defined. {self.identifier}'
                        )
                else:
                    log.error(
                        f'"operation" function in export must have 4 inputs. {self.identifier}'
                    )
            else:
                log.error(
                    f'"operation" in export must be a callable, or a subclass of wx.Window or wx.Sizer. {self.identifier}'
                )
        else:
            log.error(f'"operation" is not present in export. {self.identifier}')

    def __call__(
        self, parent: wx.Window, canvas: "EditCanvas", world: "BaseLevel"
    ) -> OperationUIType:
        return self._ui(parent, canvas, world)
