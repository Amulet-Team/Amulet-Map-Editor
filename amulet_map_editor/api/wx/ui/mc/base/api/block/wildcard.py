from typing import Optional
import PyMCTranslate
import amulet_nbt
from amulet.api.data_types import VersionNumberTuple
from amulet.api.block import PropertyTypeMultiple, PropertyDataTypes

from .identifier import BaseMCBlockIdentifierAPI, BaseMCBlockIdentifier


class WildcardMCBlockAPI(BaseMCBlockIdentifierAPI):
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


class WildcardMCBlock(BaseMCBlockIdentifier, WildcardMCBlockAPI):
    def __init__(
        self,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = False,
        namespace: str = None,
        base_name: str = None,
        selected_properties: PropertyTypeMultiple = None,
        all_properties: PropertyTypeMultiple = None,
    ):
        super().__init__(
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
        )
        self._all_properties = None
        self._selected_properties = None
        self._set_all_properties(all_properties)
        self._set_selected_properties(selected_properties)

    def _block_manager(self):
        return self._translation_manager.get_version(
            self.platform, self.version_number
        ).block

    @property
    def is_vanilla(self):
        block_manager = self._block_manager()
        return self.namespace in block_manager.namespaces(
            self.force_blockstate
        ) and self.base_name in block_manager.base_names(
            self.namespace, self.force_blockstate
        )

    @property
    def all_properties(self) -> PropertyTypeMultiple:
        return self._all_properties

    @all_properties.setter
    def all_properties(self, all_properties: PropertyTypeMultiple):
        self._set_all_properties(all_properties)
        self._schedule_push()

    def _clean_properties(
        self, properties: Optional[PropertyTypeMultiple]
    ) -> PropertyTypeMultiple:
        out_properties: PropertyTypeMultiple = {}
        if self.is_vanilla:
            # Vanilla block. Make sure the property is valid
            block_spec = self._block_manager().get_specification(
                self.namespace, self.base_name, self.force_blockstate
            )
            props = block_spec.get("properties", {})
            if isinstance(properties, dict):
                for name, ps in props.items():
                    if name in properties:
                        out_properties[name] = tuple(
                            nbt
                            for nbt in properties[name]
                            if isinstance(nbt, PropertyDataTypes)
                            and nbt.to_snbt() in ps
                        )
            else:
                for name, snbts in props.items():
                    out_properties[name] = tuple(
                        amulet_nbt.from_snbt(snbt) for snbt in snbts
                    )
        elif isinstance(properties, dict):
            for name, nbts in properties.items():
                out_properties[name] = tuple(
                    nbt for nbt in nbts if isinstance(nbt, PropertyDataTypes)
                )
        return out_properties

    def _set_all_properties(self, all_properties: Optional[PropertyTypeMultiple]):
        self._all_properties: PropertyTypeMultiple = self._clean_properties(
            all_properties
        )

    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        return self._selected_properties

    @selected_properties.setter
    def selected_properties(self, selected_properties: PropertyTypeMultiple):
        self._set_selected_properties(selected_properties)
        self._schedule_push()

    def _set_selected_properties(
        self, selected_properties: Optional[PropertyTypeMultiple]
    ):
        if self.is_vanilla:
            self._selected_properties = {
                name: tuple(nbt for nbt in nbts if nbt in self.all_properties[name])
                for name, nbts in self._clean_properties(selected_properties).items()
                if name in self.all_properties
            }
        else:
            selected_properties = self._clean_properties(selected_properties)
            all_properties = self.all_properties
            for name, nbts in selected_properties.items():
                if name in all_properties:
                    ap = all_properties[name]
                    all_properties[name] = ap + tuple(
                        nbt for nbt in nbts if nbt not in ap
                    )
                else:
                    all_properties[name] = nbts
            self._all_properties = all_properties
            self._selected_properties = selected_properties
