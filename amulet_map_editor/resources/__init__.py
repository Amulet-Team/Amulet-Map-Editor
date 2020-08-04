from __future__ import annotations

from typing import Dict, Union

from os.path import (
    join as opjoin,
    splitext as opsplit,
    dirname as opdir,
    isdir,
    normpath,
)
from os import listdir
import json

import wx


_BASE = normpath(opjoin(opdir(__file__), ""))


class _ResourceItem:
    __slots__ = ("_path",)

    def __init__(self, path):
        self._path = path

    def __repr__(self):
        return f'{self.__class__.__name__}("{self._path}")'

    @property
    def path(self):
        return self._path

    def to(self, resource_item):
        return resource_item(self._path)

    @classmethod
    def default_object(cls):
        return None


class BitmapResourceItem(_ResourceItem):
    def bitmap(self, width=-1, height=-1, quality=wx.IMAGE_QUALITY_HIGH) -> wx.Bitmap:
        bm = wx.Bitmap(self._path)

        if width > 0 or height > 0:
            im: wx.Image = bm.ConvertToImage()
            im = im.Scale(
                width if width > 0 else bm.Width,
                height if height > 0 else bm.Height,
                quality,
            )
            bm = im.ConvertToBitmap()
        return bm

    @classmethod
    def default_object(cls):
        bm = wx.Bitmap()
        bm.Create(32, 32)
        return bm


class TextResourceItem(_ResourceItem):
    def text(self):
        with open(self._path) as fp:
            return fp.read()

    @classmethod
    def default_object(cls):
        return ""


class JSONResourceItem(_ResourceItem):
    def json(self):
        with open(self._path) as fp:
            return json.load(fp)

    @classmethod
    def default_object(cls):
        return dict()


class _MissingResourceItem(_ResourceItem):
    __slots__ = ("_path", "_factory")

    def __init__(self, path, factory):
        super(_MissingResourceItem, self).__init__(path)
        self._factory = factory

    def __getattr__(self, item):
        return _MissingResourceItem(opjoin(self._path, item), self._factory)

    def __call__(self, *args, **kwargs):
        return self._factory.default_object()


class _ResourceDirectory(_ResourceItem):
    __slots__ = ("_path", "_factory", "_entries")

    def __init__(self, directory_name, factory_class, parent):
        super(_ResourceDirectory, self).__init__(opjoin(parent, directory_name))
        self._factory = factory_class

        self._entries: Dict[str, Union[_ResourceDirectory, _ResourceItem, str]] = {}
        self.scan()

    def scan(self):
        self._entries.clear()
        for entry in listdir(self._path):
            path = opjoin(self._path, entry)
            if isdir(path):
                self._entries[entry] = _ResourceDirectory(
                    entry, self._factory, self._path
                )
            else:
                filename, ext = opsplit(entry)
                self._entries[filename] = ext

    def __repr__(self):
        return f"_ResourceDirectory({self._path})"

    def __getattr__(self, item) -> Union[_ResourceItem, _MissingResourceItem]:
        if item in self._entries:
            if isinstance(self._entries[item], str):
                ext = self._entries[item]
                del self._entries[item]
                self._entries[item] = self._factory(opjoin(self._path, f"{item}{ext}"))
            return self._entries[item]
        else:
            return _MissingResourceItem(opjoin(self._path, item), self._factory)


img = _ResourceDirectory("img", BitmapResourceItem, _BASE)

if __name__ == "__main__":  # Demo code
    logo_dir = img.logo
    icon64_item = logo_dir.icon64
    non_existent_item = logo_dir.icon42
    non_existent_path = img.test1.test2.test3.file_doesnt_exist

    app = wx.App()
    print(icon64_item.bitmap())
    print(non_existent_item.bitmap())
    print(non_existent_path.bitmap())
    print(icon64_item.path)
