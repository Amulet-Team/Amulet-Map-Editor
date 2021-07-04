from typing import Optional

from ..version import BaseMCVersionAPI


class BaseMCBlockAPI(BaseMCVersionAPI):
    @property
    def namespace(self) -> str:
        raise NotImplementedError

    @namespace.setter
    def namespace(self, namespace: str):
        raise NotImplementedError

    def set_namespace(self, namespace: str):
        raise NotImplementedError

    @property
    def block_name(self) -> str:
        raise NotImplementedError

    @block_name.setter
    def block_name(self, block_name: str):
        raise NotImplementedError

    def set_block_name(self, block_name: str):
        raise NotImplementedError
