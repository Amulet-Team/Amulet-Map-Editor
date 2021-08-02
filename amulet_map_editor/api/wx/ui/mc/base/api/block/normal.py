from typing import Optional

import PyMCTranslate
import amulet_nbt
from amulet.api.data_types import VersionNumberTuple
from amulet.api.block import PropertyType, Block, PropertyDataTypes

# from amulet.api.block_entity import BlockEntity

from .identifier import BaseMCBlockIdentifierAPI, BaseMCBlockIdentifier


class NormalMCBlockAPI(BaseMCBlockIdentifierAPI):
    @property
    def properties(self) -> PropertyType:
        """The active properties."""
        raise NotImplementedError

    @properties.setter
    def properties(self, properties: PropertyType):
        """
        Set the active properties.
        Changes will propagate to the end of this UI.
        No events will be created.

        :param properties: The properties to set.
        """
        raise NotImplementedError

    @property
    def block(self) -> Block:
        """The active block."""
        raise NotImplementedError

    @block.setter
    def block(self, block: Block):
        """
        Set the active block.
        Namespace, base name and properties will be pulled from this.
        Changes will propagate to the end of this UI.
        No events will be created.

        :param block: The block to set.
        """
        raise NotImplementedError


class NormalMCBlock(BaseMCBlockIdentifier, NormalMCBlockAPI):
    def __init__(
        self,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = False,
        namespace: str = None,
        base_name: str = None,
        properties: PropertyType = None,
    ):
        super().__init__(
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
        )
        self._properties = None
        self._set_properties(properties)

    @property
    def properties(self) -> PropertyType:
        return self._properties

    @properties.setter
    def properties(self, properties: PropertyType):
        self._set_properties(properties)
        self._schedule_push()

    def _set_properties(self, properties: Optional[PropertyType]):
        """
        Set the active properties.
        Changes will not propagate.
        :meth:`push` must be called once all desired states are set.

        :param properties: A dictionary mapping the property name to the property value.
        """
        self._properties = {}
        block_manager = self._translation_manager.get_version(
            self.platform, self.version_number
        ).block
        if self.namespace in block_manager.namespaces(
            self.force_blockstate
        ) and self.base_name in block_manager.base_names(
            self.namespace, self.force_blockstate
        ):
            # Vanilla block. Make sure the property is valid
            block_spec = block_manager.get_specification(
                self.namespace, self.base_name, self.force_blockstate
            )
            props = block_spec.get("properties", {})
            defaults = block_spec.get("defaults", {})
            if isinstance(properties, dict):
                for name, ps in props.items():
                    if (
                        name in properties
                        and isinstance(properties[name], PropertyDataTypes)
                        and properties[name].to_snbt() in ps
                    ):
                        self._properties[name] = properties[name]
                    else:
                        self._properties[name] = amulet_nbt.from_snbt(defaults[name])
            else:
                for name, snbt in defaults.items():
                    self._properties[name] = amulet_nbt.from_snbt(snbt)
        elif isinstance(properties, dict):
            for name, nbt in properties.items():
                if isinstance(nbt, PropertyDataTypes):
                    self._properties[name] = nbt

    @property
    def block(self) -> Block:
        return Block(self.namespace, self.base_name, self.properties)

    @block.setter
    def block(self, block: Block):
        self._set_block(block)
        self._schedule_push()

    def _set_block(self, block: Optional[Block]):
        """
        Set the active block.
        Namespace, base name and properties will be pulled from this.
        Changes will not propagate.
        :meth:`push` must be called once all desired states are set.

        :param block: The block to set.
        """
        self._set_namespace(block.namespace)
        self._set_base_name(block.base_name)
        self._set_properties(block.properties)
