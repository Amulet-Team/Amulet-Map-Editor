from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .loader import OperationLoader

PathType = str
OperationStorageType = Dict[PathType, "OperationLoader"]
