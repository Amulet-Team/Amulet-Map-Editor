from __future__ import annotations

from typing import Dict, Union, Type, Iterable
import os


class ResourceItem:
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


class MissingResourceItem(ResourceItem):
    __slots__ = ("_path", "_factory")

    def __init__(self, path, factory):
        super(MissingResourceItem, self).__init__(path)
        self._factory = factory

    def __getattr__(self, item):
        return MissingResourceItem(os.path.join(self._path, item), self._factory)

    def __call__(self, *args, **kwargs):
        return self._factory.default_object()


class ResourceDirectory(ResourceItem):
    __slots__ = ("_path", "_factory", "_entries")
    ALLOWED_EXTS = ()

    def __init__(
        self, directory_name: str, factory_class: Type[ResourceItem], parent: str
    ):
        super(ResourceDirectory, self).__init__(os.path.join(parent, directory_name))
        self._factory = factory_class

        self._entries: Dict[str, Union[ResourceDirectory, ResourceItem, str]] = {}
        self.scan()

    def scan(self):
        self._entries.clear()
        for entry in os.listdir(self._path):
            path = os.path.join(self._path, entry)
            if os.path.isdir(path):
                self._entries[entry] = self.__class__(entry, self._factory, self._path)
            else:
                filename, ext = os.path.splitext(entry)
                ext = ext.lower()
                if ext in self.ALLOWED_EXTS:
                    self._entries[filename] = ext

    def __repr__(self):
        return f"ResourceDirectory({self._path})"

    def __getattr__(
        self, item
    ) -> Union["ResourceDirectory", ResourceItem, MissingResourceItem]:
        if item in self._entries:
            if isinstance(self._entries[item], str):
                ext = self._entries[item]
                self._entries[item] = self._factory(
                    os.path.join(self._path, f"{item}{ext}")
                )
            return self._entries[item]
        else:
            return MissingResourceItem(os.path.join(self._path, item), self._factory)

    def __dir__(self) -> Iterable[str]:
        return [k for k in self._entries.keys() if k != "__pycache__"]


# legacy support
from . import image as img

# class TextResourceItem(_ResourceItem):
#     def text(self):
#         with open(self._path) as fp:
#             return fp.read()
#
#     @classmethod
#     def default_object(cls):
#         return ""
#
#
# class JSONResourceItem(_ResourceItem):
#     def json(self):
#         with open(self._path) as fp:
#             return json.load(fp)
#
#     @classmethod
#     def default_object(cls):
#         return dict()
