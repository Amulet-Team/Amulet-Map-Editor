from typing import Optional, Tuple

from amulet.api.block import PropertyType, Block
from amulet.api.block_entity import BlockEntity

from .base import BaseMCBlockAPI


class NormalMCBlockAPI(BaseMCBlockAPI):
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
