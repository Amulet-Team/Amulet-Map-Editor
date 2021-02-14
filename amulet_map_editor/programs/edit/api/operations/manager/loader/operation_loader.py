from typing import Callable, Any, Optional

from .base_operation_loader import BaseOperationLoader

from amulet_map_editor import log
from amulet.api.level import BaseLevel
from amulet.api.data_types import Dimension
from amulet.api.selection import SelectionGroup


class OperationLoader(BaseOperationLoader):
    def __init__(self, identifier: str, export_dict: dict):
        self._operation: Optional[
            Callable[[BaseLevel, Dimension, SelectionGroup], Any]
        ] = None
        super().__init__(identifier, export_dict)

    def _setup(self, export_dict: dict):
        """Parse the export dictionary and setup as required."""
        if "operation" in export_dict:
            if callable(export_dict["operation"]):
                operation = export_dict["operation"]
                if operation.__code__.co_argcount == 3:
                    self._operation = operation
                    self._is_valid = True
                else:
                    log.error(
                        f'"operation" function in export must have 3 inputs. {self.identifier}'
                    )
            else:
                log.error(
                    f'"operation" in export must be a callable. {self.identifier}'
                )
        else:
            log.error(f'"operation" is not present in export. {self.identifier}')

    def __call__(
        self, world: BaseLevel, dimension: Dimension, selection: SelectionGroup
    ):
        """Run the actual operation."""
        self._operation(world, dimension, selection)
