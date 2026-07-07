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
import threading

from minecraft_model_reader.api.resource_pack.base import BaseResourcePackManager
from minecraft_model_reader import BlockMesh
import PyMCTranslate
from amulet.api.block import Block

from amulet_map_editor.api.opengl import textureatlas

log = logging.getLogger(__name__)

# The block model caches (_block_models, block_model_manager) are shared
# mutable state used by the Cython mesher and the overview scanner.
# Every call into create_lod0_chunk / get_block_model / colour lookups
# from a worker thread must hold this lock.
model_lock = threading.Lock()


def mean_texture_colour(
    image: numpy.ndarray, bounds: Tuple[float, float, float, float]
) -> numpy.ndarray:
    """Alpha-weighted mean RGBA colour of an atlas sub-region.

    :param image: the atlas as a (height, width, 4) uint8 array.
    :param bounds: (u0, v0, u1, v1) texture bounds in 0-1 UV space.
    :return: shape (4,) uint8 RGBA.
    """
    height, width = image.shape[:2]
    u0, v0, u1, v1 = bounds
    x0 = int(u0 * width)
    x1 = max(x0 + 1, int(round(u1 * width)))
    y0 = int(v0 * height)
    y1 = max(y0 + 1, int(round(v1 * height)))
    region = image[y0:y1, x0:x1].astype(numpy.float32)
    alpha = region[:, :, 3:4]
    total_alpha = float(alpha.sum())
    if total_alpha < 1:
        return numpy.zeros(4, numpy.uint8)
    rgb = (region[:, :, :3] * alpha).sum((0, 1)) / total_alpha
    return (
        numpy.concatenate([rgb, [alpha.mean()]])
        .round()
        .clip(0, 255)
        .astype(numpy.uint8)
    )


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
    _block_top_colours: Dict[Block, numpy.ndarray]

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
        self._block_top_colours: Dict[Block, numpy.ndarray] = {}

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
        Useful for getting the id of textures for hard coded textures not connected to a resource pack.
        """
        return self._resource_pack.get_texture_path(namespace, relative_path)

    def texture_bounds(self, texture_path: str) -> Tuple[float, float, float, float]:
        """Get the bounding box of a given texture path."""
        if texture_path in self._texture_bounds:
            return self._texture_bounds[texture_path]
        else:
            return self._texture_bounds[self._resource_pack.missing_no]

    def get_block_top_colour(self, block: Block) -> numpy.ndarray:
        """Approximate map colour of a block seen from above.

        Returns a shape (4,) uint8 RGBA array. Invisible blocks (air)
        return alpha 0. The caller must hold model_lock because this
        touches the shared block model cache.
        """
        if block not in self._block_top_colours:
            if self._image is None:
                raise Exception(
                    "OpenGLResourcePack.setup() needs to be run before accessing a texture."
                )
            colour = numpy.zeros(4, numpy.uint8)
            model = self.get_block_model(block)
            image = self._image.reshape((self._image_height, self._image_width, 4))
            preferred = ("up", None, "north", "east", "south", "west", "down")
            remaining = sorted(
                (face for face in model.faces if face not in preferred), key=str
            )
            for face_dir in (*preferred, *remaining):
                if face_dir not in model.faces:
                    continue
                texture_indexes = model.texture_index[face_dir]
                if not len(texture_indexes):
                    continue
                texture_path = model.textures[texture_indexes[0]]
                colour = mean_texture_colour(
                    image, self.texture_bounds(texture_path)
                ).astype(numpy.float32)
                tint = numpy.asarray(model.tint_verts[face_dir]).reshape((-1, 3))
                if tint.size:
                    colour[:3] *= tint.mean(0)
                colour = colour.round().clip(0, 255).astype(numpy.uint8)
                break
            colour.setflags(write=False)
            self._block_top_colours[block] = colour
        return self._block_top_colours[block]

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
                        os.path.join(glob.escape(pack), "**", "*.*"), recursive=True
                    )
                ),
                default=0,
            )

            cache_dir = os.path.join(os.environ["CACHE_DIR"], "resource_packs", "atlas")
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
            self._image = numpy.array(atlas, numpy.uint8).ravel()
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
