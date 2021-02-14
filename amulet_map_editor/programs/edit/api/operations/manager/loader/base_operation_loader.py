from amulet_map_editor import log


class BaseOperationLoader:
    """A class to load and wrap an operation"""

    def __init__(self, identifier: str, export_dict: dict):
        """
        Set up the OperationLoader.
        :param identifier: The path to the operation file. This may be a file or directory depending on if it is a module or package.
        """
        self._identifier = identifier
        self._name = ""
        self._is_valid = False
        self._load(export_dict)

    def _load(self, export_dict: dict):
        """load the operation."""
        if not isinstance(export_dict, dict):
            log.error(f"The export for {self.identifier} is not a dictionary.")
            return
        if "name" in export_dict and isinstance(export_dict["name"], str):
            self._name = export_dict["name"]
            self._setup(export_dict)
        else:
            log.error(f"Missing or invalid name in {self.identifier}")

    def _setup(self, export_dict: dict):
        """Parse the export dictionary and setup as required."""
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        """Run the actual operation."""
        raise NotImplementedError

    @property
    def is_valid(self) -> bool:
        """Is the module/package a valid operation."""
        return self._is_valid

    @property
    def identifier(self) -> str:
        """The identifier for this operation.
        This is formed of the path and optionally a number if there are multiple operations in the file."""
        return self._identifier

    @property
    def name(self) -> str:
        """The name of the operation."""
        return self._name
