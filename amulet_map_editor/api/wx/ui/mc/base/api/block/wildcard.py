from amulet.api.block import PropertyTypeMultiple

from .base import BaseMCBlockAPI


class WildcardMCBlockAPI(BaseMCBlockAPI):
    @property
    def extra_properties(self) -> PropertyTypeMultiple:
        raise NotImplementedError

    @extra_properties.setter
    def extra_properties(self, properties: PropertyTypeMultiple):
        raise NotImplementedError
