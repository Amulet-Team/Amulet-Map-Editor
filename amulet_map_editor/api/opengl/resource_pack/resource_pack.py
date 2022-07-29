from OpenGL.GL import (
    glBindTexture,
    GL_TEXTURE_2D,
    glTexImage2D,
    GL_RGBA,
    GL_UNSIGNED_BYTE,
    glGenTextures,
    glTexParameteri,
    GL_TEXTURE_MIN_FILTER,
    GL_NEAREST,
    GL_CLAMP_TO_EDGE,
    GL_TEXTURE_MAG_FILTER,
    GL_TEXTURE_WRAP_S,
    GL_TEXTURE_WRAP_T,
)
from typing import Generator, Any, Tuple, Dict, Optional
import struct
import hashlib
import os
import json
from PIL import Image
import numpy
import glob
import logging

from minecraft_model_reader.api.resource_pack.base import BaseResourcePackManager
from minecraft_model_reader import BlockMesh
import PyMCTranslate
from amulet.api.block import Block

from amulet_map_editor.api.opengl import textureatlas

log = logging.getLogger(__name__)


class OpenGLResourcePack:
    """This class will take a minecraft_model_reader resource pack and
    load all of the textures into a texture atlas."""

    _translator: PyMCTranslate.Version
    _block_models: Dict[Block, BlockMesh]
    _texture_bounds: Dict[Any, Tuple[float, float, float, float]]
    _image: Optional[numpy.ndarray]
    _image_width: int
    _image_height: int
    _gl_textures: Dict[str, int]

    def __init__(
        self, resource_pack: BaseResourcePackManager, translator: PyMCTranslate.Version
    ):
        self._resource_pack = resource_pack
        self._translator = translator
        self._block_models: Dict[Block, BlockMesh] = {}

        self._texture_bounds: Dict[str, Tuple[float, float, float, float]] = {}
        self._image: Optional[Image.Image] = None
        self._image_width: int = 0
        self._image_height: int = 0

        self._gl_textures: Dict[str, int] = {}

    def get_atlas_id(self, context_id: str) -> int:
        """Get the opengl texture id of the atlas for a given context."""
        if context_id not in self._gl_textures:
            if self._image is None:
                raise Exception(
                    "OpenGLResourcePack.setup() needs to be run before accessing a texture."
                )
            self._setup_texture(context_id)
        return self._gl_textures[context_id]

    def get_texture_path(self, namespace: Optional[str], relative_path: str):
        """Get the absolute path of the image from the relative components.
        Useful for getting the id of textures for hard coded textures not connected to a resource pack."""
        return self._resource_pack.get_texture_path(namespace, relative_path)

    def texture_bounds(self, texture_path: str) -> Tuple[float, float, float, float]:
        """Get the bounding box of a given texture path."""
        if texture_path in self._texture_bounds:
            return self._texture_bounds[texture_path]
        else:
            return self._texture_bounds[self._resource_pack.missing_no]

    @property
    def translator(self) -> PyMCTranslate.Version:
        """The translator used to convert the universal blocks into the required version for the resource pack."""
        return self._translator

    def setup(self) -> Generator[float, None, None]:
        """Create and bind the atlas texture."""
        if self._image is None:
            cache_id = struct.unpack(
                "H",
                hashlib.sha1(
                    "".join(self._resource_pack.pack_paths).encode("utf-8")
                ).digest()[:2],
            )[0]

            atlas: Image.Image

            if not self._resource_pack.pack_paths:
                log.warning("There are no resource packs to load.")

            mod_time = max(
                (
                    os.stat(path).st_mtime
                    for pack in self._resource_pack.pack_paths
                    for path in glob.glob(
                        os.path.join(pack, "**", "*.*"), recursive=True
                    )
                ),
                default=0,
            )

            cache_dir = os.path.join(".", "cache", "resource_pack")
            img_path = os.path.join(cache_dir, f"{cache_id}.png")
            bounds_path = os.path.join(cache_dir, f"{cache_id}.json")
            try:
                with open(bounds_path) as f:
                    cache_mod_time, bounds = json.load(f)
                if mod_time != cache_mod_time:
                    raise Exception(
                        "The resource packs have changed since last merging."
                    )
                atlas = Image.open(img_path)
            except:
                atlas_iter = textureatlas.create_atlas_iter(
                    self._resource_pack.textures
                )
                try:
                    while True:
                        yield next(atlas_iter)
                except StopIteration as e:
                    (
                        atlas,
                        bounds,
                    ) = e.value
                    os.makedirs(cache_dir, exist_ok=True)
                    atlas.save(img_path)
                    with open(bounds_path, "w") as f:
                        json.dump((mod_time, bounds), f)

            self._image_width, self._image_height = atlas.size
            self._image = numpy.asarray(atlas, numpy.uint8).ravel()
            self._texture_bounds = bounds

    def _setup_texture(self, context_id: str):
        """Set up the texture for a given context"""
        gl_texture = self._gl_textures[context_id] = glGenTextures(
            1
        )  # Create the texture location
        glBindTexture(GL_TEXTURE_2D, gl_texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

        glBindTexture(GL_TEXTURE_2D, gl_texture)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGBA,
            self._image_width,
            self._image_height,
            0,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            self._image,
        )
        glBindTexture(GL_TEXTURE_2D, 0)
        log.info("Finished setting up texture atlas in OpenGL")

    def get_block_model(self, universal_block: Block) -> BlockMesh:
        """Get the BlockMesh class for a given universal Block.
        The Block will be translated to the version format using the
        previously specified translator."""
        if universal_block not in self._block_models:
            version_block = self._translator.block.from_universal(
                universal_block.base_block
            )[0]
            if universal_block.extra_blocks:
                for block_ in universal_block.extra_blocks:
                    version_block += self._translator.block.from_universal(block_)[0]

            self._block_models[universal_block] = self._resource_pack.get_block_model(
                version_block
            )

        return self._block_models[universal_block]
