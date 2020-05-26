import pickle
from typing import Any
import os


class OperationUI:
    """The base class that all operations must inherit from."""
    def __init__(self, options_path: str):
        self._options_path = options_path

    def _load_options(self, default=None) -> Any:
        """Load previously saved options from disk or return the default options."""
        try:
            with open(self._options_path, "rb") as f:
                return pickle.load(f)
        except:
            return default

    def _save_options(self, options: Any):
        """Save the given options to disk so that they persist in the next session."""
        os.makedirs(os.path.basename(self._options_path), exist_ok=True)
        with open(self._options_path, "wb") as f:
            return pickle.dump(options, f)
