import os
import pickle
import gzip
from typing import Any

_path = os.path.abspath(os.path.join(os.environ["CONFIG_DIR"]))


def get(identifier: str, default: Any = None) -> Any:
    """
    Get the config data for a given identifier. Use an identifier unique to your program.
    :param identifier: An identifier unique to your program
    :param default: The value to return if one could not be loaded
    :return: config data
    """
    path = os.path.join(_path, identifier + ".config")
    if os.path.isfile(path):
        try:
            with gzip.open(path, "rb") as fp:
                val = pickle.load(fp)
            return val
        except:
            pass
    return default


def put(identifier: str, data: Any):
    """
    Add data to the config file and save to disk.
    :param identifier: An identifier unique to your program
    :param data: The data to be saved. Must be JSON serialisable
    :return:
    """
    if not os.path.isdir(_path):
        os.makedirs(_path)
    path = os.path.join(_path, identifier + ".config")
    with gzip.open(path, "wb") as fp:
        pickle.dump(data, fp)
