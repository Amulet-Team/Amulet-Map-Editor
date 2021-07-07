from amulet.api.block import PropertyTypeMultiple

from .base import BaseMCBlockAPI


class WildcardMCBlockAPI(BaseMCBlockAPI):
    @property
    def all_properties(self) -> PropertyTypeMultiple:
        """The values that exist for every property."""
        raise NotImplementedError

    @all_properties.setter
    def all_properties(self, properties: PropertyTypeMultiple):
        raise NotImplementedError

    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        """The values that are selected for every property."""
        raise NotImplementedError

    @selected_properties.setter
    def selected_properties(self, properties: PropertyTypeMultiple):
        raise NotImplementedError
