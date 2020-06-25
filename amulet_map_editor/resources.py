from __future__ import annotations

from typing import Dict, Union

import os.path as op

_BASE = op.dirname(__file__)


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


_BASE_RESOURCEDICT = _ResourceDict(_BASE)


def __getattr__(name):
    return _BASE_RESOURCEDICT[name]


def get_directory_or_file(name) -> Union[str, _ResourceDict]:
    return _BASE_RESOURCEDICT.get_directory_or_file(name)
