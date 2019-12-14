#!/usr/bin/env python
#
# Copyright (c) 2014 Matthew Borgerson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""Texture Atlas and Map File Generation Utility Classes"""

from PIL import Image
import struct

DESCRIPTION = """Packs many smaller images into one larger image, a Texture
Atlas. A companion file (.map), is created that defines where each texture is
mapped in the atlas."""


class AtlasTooSmall(Exception):
    pass


class Packable(object):
    """A two-dimensional object with position information."""

    def __init__(self, width, height):
        self._x = 0
        self._y = 0
        self._width = width
        self._height = height

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def perimeter(self):
        return 2*self._width + 2*self._height


class PackRegion(object):
    """A region that two-dimensional Packable objects can be packed into."""

    def __init__(self, x, y, width, height):
        """Constructor."""
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._sub1 = None
        self._sub2 = None
        self._packable = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def packable(self):
        return self._packable

    def get_all_packables(self):
        """Returns a list of all Packables in this region and sub-regions."""
        if self._packable:
            return [self._packable] + self._sub1.get_all_packables() + \
                                      self._sub2.get_all_packables()
        return []

    def pack(self, packable):
        """Pack 2D packable into this region."""
        if not self._packable:
            # Is there room to pack this?
            if (packable.width > self._width) or \
               (packable.height > self._height):
                return False

            # Pack
            self._packable = packable

            # Set x, y on Packable
            self._packable.x = self._x
            self._packable.y = self._y

            # Create sub-regions
            self._sub1 = PackRegion(self._x,
                                    self._y+self._packable.height,
                                    self._packable.width,
                                    self._height-self._packable.height)
            self._sub2 = PackRegion(self._x+self._packable.width,
                                    self._y,
                                    self._width-self._packable.width,
                                    self._height)
            return True

        # Pack into sub-region
        return self._sub1.pack(packable) or self._sub2.pack(packable)


class Frame(Packable):
    """An image file that can be packed into a PackRegion."""

    def __init__(self, filename):
        self._filename = filename

        # Determine frame dimensions
        image = Image.open(filename)
        width, height = image.size
        del image

        super(Frame, self).__init__(width, height)

    @property
    def filename(self):
        return self._filename

    def draw(self, image):
        """Draw this frame into another Image."""
        i = Image.open(self._filename)
        image.paste(i, (self.x, self.y))
        del i


class Texture(object):
    """A collection of one or more frames."""

    def __init__(self, name, frames):
        self._name = name
        self._frames = frames

    @property
    def name(self):
        return self._name

    @property
    def frames(self):
        return self._frames


class TextureAtlas(PackRegion):
    """Texture Atlas generator."""

    def __init__(self, width, height):
        super(TextureAtlas, self).__init__(0, 0, width, height)
        self._textures = []

    @property
    def textures(self):
        return self._textures

    def pack(self, texture):
        """Pack a Texture into this atlas."""
        self._textures.append(texture)
        for frame in texture.frames:
            if not super(TextureAtlas, self).pack(frame):
                raise AtlasTooSmall('Failed to pack frame %s' % frame.filename)

    def write(self, filename, mode):
        """Generates the final texture atlas."""
        out = Image.new(mode, (self.width, self.height))
        for t in self._textures:
            for f in t.frames:
                f.draw(out)
        out.save(filename)


class TextureAtlasMap(object):
    """Texture Atlas Map file generator."""

    def __init__(self, atlas):
        self._atlas = atlas

    def write(self, fd):
        """Writes the texture atlas map file into file object fd."""
        raise Exception('Not Implemented')


class BinaryTextureAtlasMap(TextureAtlasMap):
    """Binary Texture Atlas Map file generator.

    The binary atlas map is composed of four sections. The first section is the
    header. The second section contains the details of each texture (name,
    number of frames, etc.). The third section contains all null-terminated
    strings referenced by other sections. The fourth section contains the
    coordinates and dimensions of all texture frames.

    HEADER FORMAT

    Offset Size Description
    ------ ---- -----------
    0      4    Magic ('TEXA' = 0x41584554)
    4      4    Texture Atlas Width
    8      4    Texture Atlas Height
    12     4    Number of Textures
    16     4    Texture Section Offset
    20     4    Texture Section Size
    24     4    String Section Offset
    28     4    String Section Size
    32     4    Frame Section Offset
    36     4    Frame Section Size

    TEXTURE FORMAT

    Offset Size Description
    ------ ---- -----------
    0      4    Offset to Texture Name in String Section
    4      4    Number of Frames
    8      4    Offset to first Frame

    FRAME FORMAT

    Offset Size Description
    ------ ---- -----------
    0      4    X-Coordinate of Frame
    4      4    Y-Coordinate of Frame
    8      4    Frame Width
    12     4    Frame Height
    """

    def __init__(self, atlas):
        super(BinaryTextureAtlasMap, self).__init__(atlas)

    def write(self, fd):
        """Writes the binary texture atlas map file into file object fd."""
        # Calculate offset and size of each section
        hdr_fmt = 'IIIIIIIII'
        hdr_fmt_len = struct.calcsize(hdr_fmt)
        hdr_section_len = hdr_fmt_len+4  # Header + Magic

        tex_fmt = 'III'
        tex_fmt_len = struct.calcsize(tex_fmt)
        tex_section_off = hdr_section_len
        tex_section_len = len(self._atlas.textures)*tex_fmt_len

        str_section_off = tex_section_off+tex_section_len
        str_section_len = sum(map(lambda t_: len(t_.name)+1, self._atlas.textures))

        frm_fmt = 'IIII'
        frm_fmt_len = struct.calcsize(frm_fmt)
        frm_section_off = str_section_off + str_section_len
        frm_section_len = sum(map(lambda t_: len(t_.frames), self._atlas.textures))
        frm_section_len *= frm_fmt_len

        # Write Header
        fd.write(b'TEXA')
        fd.write(
            struct.pack(
                hdr_fmt,
                self._atlas.width,
                self._atlas.height,
                len(self._atlas.textures),
                tex_section_off,
                tex_section_len,
                str_section_off,
                str_section_len,
                frm_section_off,
                frm_section_len
            )
        )

        # Write Texture Section
        str_offset = 0
        frm_offset = 0
        for t in self._atlas.textures:
            fd.write(
                struct.pack(
                    tex_fmt,
                    str_offset,
                    len(t.frames),
                    frm_offset
                )
            )
            str_offset += len(t.name) + 1  # +1 for sentinel byte
            frm_offset += len(t.frames)*frm_fmt_len

        # Write String Section
        for t in self._atlas.textures:
            fd.write((t.name + '\x00').encode('utf-8'))

        # Write Frame Section
        for t in self._atlas.textures:
            for f in t.frames:
                fd.write(
                    struct.pack(
                        frm_fmt,
                        f.x,
                        f.y,
                        f.width,
                        f.height
                    )
                )
