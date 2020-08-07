from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    pass

PathType = str
OperationStorageType = Dict[PathType, "OperationLoader"]
