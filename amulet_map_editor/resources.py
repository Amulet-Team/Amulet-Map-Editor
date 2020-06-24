from __future__ import annotations

from typing import Dict, Union

import os.path as op

_BASE = op.dirname(__file__)

_RESOURCE_DIRS: Dict[str, _ResourceDict] = {}


class _ResourceDict:
    __slots__ = ("directory_name", "_file_cache", "_dir_cache")

    def __init__(self, dir_name: str):
        self.directory_name = dir_name
        self._file_cache: Dict[str, str] = {}
        self._dir_cache: Dict[str, _ResourceDict] = {}

    def __repr__(self):
        return f'_ResourceDict("{self.directory_name}")'

    def __getattr__(self, item: str) -> _ResourceDict:
        if item in self._dir_cache:
            return self._dir_cache[item]

        path = op.join(self.directory_name, item)
        if op.isdir(path):
            return self._dir_cache.setdefault(item, _ResourceDict(path))

        raise NotADirectoryError(
            f'Could not find directory named "{item}" in "{self.directory_name}"'
        )

    def __getitem__(self, item: str) -> Union[str, _ResourceDict]:
        if item in self._file_cache:
            return self._file_cache[item]

        if item in self._dir_cache:
            return self._dir_cache[item]

        path = op.join(self.directory_name, item)
        if op.isfile(path):
            return self._file_cache.setdefault(item, path)
        elif op.isdir(path):
            return self._dir_cache.setdefault(item, _ResourceDict(path))
        else:
            raise AttributeError(
                f'Could not find file or directory named "{item}" in "{self.directory_name}"'
            )

    def get_directory_or_file(self, name) -> Union[str, _ResourceDict]:
        return self.__getitem__(name)


def __getattr__(name) -> Union[str, _ResourceDict]:
    path = op.join(_BASE, name)
    if op.isfile(path):
        return op.join(_BASE, name)
    if name in _RESOURCE_DIRS:
        return _RESOURCE_DIRS[name]
    if not op.exists(path) or not op.isdir(path):
        raise FileNotFoundError(
            f'Could not file a file or directory with name "{name}"'
        )
    return _RESOURCE_DIRS.setdefault(name, _ResourceDict(path))


def get_directory_or_file(name) -> Union[str, _ResourceDict]:
    return __getattr__(name)
