import os
import json
from typing import Any


class Config:
    def __init__(self):
        """A container for accessing the config file"""
        self._config = None
        if os.path.isfile('config.json'):
            try:
                with open('config.json') as fc:
                    self._config = json.load(fc)
            except:
                pass
        if not isinstance(self._config, dict):
            self._config = {}

        if "recent_worlds" in self._config:  # convert from the old config format
            self._config = {
                "meta": self._config
            }

    def get(self, identifier: str, default: Any = None) -> Any:
        """
        Get the config data for a given identifier. Use an identifier unique to your program.
        :param identifier: An identifier unique to your program
        :param default: The value to return if one could not be loaded
        :return: config data
        """
        if identifier in self._config:
            try:
                val = json.loads(self._config[identifier])
                return val
            except json.JSONDecodeError:
                pass
        return default

    def put(self, identifier: str, data: Any):
        """
        Add data to the config file and save to disk.
        :param identifier: An identifier unique to your program
        :param data: The data to be saved. Must be JSON serialisable
        :return:
        """
        data_str = json.dumps(data, skipkeys=True)
        self._config[identifier] = data_str
        with open('config.json', 'w') as f:
            json.dump(self._config, f)


config = Config()
