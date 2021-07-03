from typing import Optional, Tuple
from amulet.api.block import PropertyType, PropertyTypeMultiple, Block
from amulet.api.block_entity import BlockEntity
from amulet_map_editor.api.wx.ui.mc.base.base_define import BaseDefineAPI


class BaseBlockDefineAPI(BaseDefineAPI):
    @property
    def force_blockstate(self) -> bool:
        raise NotImplementedError

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        raise NotImplementedError

    @property
    def block_name(self) -> str:
        raise NotImplementedError

    @block_name.setter
    def block_name(self, block_name: str):
        raise NotImplementedError


class NormalBlockDefineAPI(BaseBlockDefineAPI):
    @property
    def properties(self) -> PropertyType:
        raise NotImplementedError

    @properties.setter
    def properties(self, properties: PropertyType):
        raise NotImplementedError

    @property
    def block(self) -> Block:
        raise NotImplementedError

    @block.setter
    def block(self, block: Block):
        raise NotImplementedError

    @property
    def block_entity(self) -> Optional[BlockEntity]:
        raise NotImplementedError

    @block_entity.setter
    def block_entity(self, block_entity: Optional[BlockEntity]):
        raise NotImplementedError

    @property
    def universal_block(self) -> Tuple[Block, Optional[BlockEntity]]:
        raise NotImplementedError

    @universal_block.setter
    def universal_block(self, universal_block: Tuple[Block, Optional[BlockEntity]]):
        raise NotImplementedError


class WildcardBlockDefineAPI(BaseBlockDefineAPI):
    @property
    def extra_properties(self) -> PropertyTypeMultiple:
        raise NotImplementedError

    @extra_properties.setter
    def extra_properties(self, properties: PropertyTypeMultiple):
        raise NotImplementedError
