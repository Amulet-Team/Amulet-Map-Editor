from typing import Any, Dict, Tuple

import minecraft_model_reader
import PyMCTranslate
from amulet.api.block import BlockManager


class ResourcePackManager:
    def __init__(
        self,
        context_identifier: Any,
        resource_pack: minecraft_model_reader.BaseRPHandler,
        texture: int,
        texture_bounds: Dict[Any, Tuple[float, float, float, float]],
        translator: PyMCTranslate.Version
    ):
        self.context_identifier = context_identifier
        self._texture = texture
        self._resource_pack = resource_pack
        self._texture_bounds: Dict[Any, Tuple[float, float, float, float]] = texture_bounds
        self._resource_pack_translator = translator

        self._block_models: Dict[int, minecraft_model_reader.MinecraftMesh] = {}

    def set_resource_pack(
        self,
        resource_pack: minecraft_model_reader.BaseRPHandler,
        texture_bounds: Dict[Any, Tuple[float, float, float, float]]
    ):
        self._resource_pack = resource_pack
        self._texture_bounds = texture_bounds
        self._block_models.clear()

    @property
    def texture(self) -> int:
        return self._texture

    def get_texture_bounds(self, texture):
        if texture not in self._texture_bounds:
            texture = ('minecraft', 'missing_no')
        return self._texture_bounds[texture]

    @property
    def _palette(self) -> BlockManager:
        raise NotImplementedError

    @property
    def translator(self) -> PyMCTranslate.Version:
        return self._resource_pack_translator

    @translator.setter
    def translator(self, translator: PyMCTranslate.Version):
        self._resource_pack_translator = translator

    def get_block_model(self, pallete_index: int) -> minecraft_model_reader.MinecraftMesh:
        if pallete_index not in self._block_models:
            block = self._palette[pallete_index]
            extra_blocks = tuple()
            if block.extra_blocks:
                extra_blocks = tuple(
                    self._resource_pack_translator.block.from_universal(
                        block_
                    )[0] for block_ in block.extra_blocks
                )
            block = self._resource_pack_translator.block.from_universal(
                block.base_block
            )[0]
            for block_ in extra_blocks:
                block += block_
            self._block_models[pallete_index] = self._resource_pack.get_model(
                block
            )

        return self._block_models[pallete_index]
