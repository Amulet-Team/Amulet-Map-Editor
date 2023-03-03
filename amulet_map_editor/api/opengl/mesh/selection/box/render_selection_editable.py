import numpy
from OpenGL.GL import (
    GL_TRIANGLES,
    glCullFace,
    GL_FRONT,
    GL_BACK,
    glDisable,
    GL_DEPTH_TEST,
    GL_LINE_STRIP,
    glEnable,
    glGetBooleanv,
    glGetIntegerv,
    GL_CULL_FACE_MODE,
)

from amulet.api.data_types import PointCoordinatesAny
from .render_selection_highlightable import RenderSelectionHighlightable
from amulet_map_editor.api.opengl.resource_pack import OpenGLResourcePack
from amulet_map_editor.api.opengl.data_types import RGBColour
from .colours import colours


class RenderSelectionEditable(RenderSelectionHighlightable):
    """A drawable selection box with additional editing controls"""

    def __init__(self, context_identifier: str, resource_pack: OpenGLResourcePack):
        super().__init__(context_identifier, resource_pack)
        # is the locked or is it being modified. Changes the colour of the faces.
        self._locked = True

    def _init_verts(self):
        # the first 36 verts are used for the full box which is used for lines
        # the next 36 verts are used for the inset faces
        # the next 144 verts are used for the edges
        # the next 144 verts are used for the corners

        verts_per_quad = 2 * 3  # triangles * verts
        self.verts = numpy.zeros(
            (
                6 * verts_per_quad
                + 6  # original box verts (used for the lines)
                * 9
                * verts_per_quad,  # new verts
                self._vert_len,
            ),
            dtype=numpy.float32,
        )
        self.verts[:, 5:9] = self.resource_pack.texture_bounds(
            self.resource_pack.get_texture_path("amulet", "amulet_ui/selection")
        )

        self.verts[verts_per_quad * 6 :, 9:12] = self.box_tint
        self.verts[verts_per_quad * 12 : verts_per_quad * 36, 9:12] = self.edge_colour

    @property
    def highlight_colour(self) -> RGBColour:
        if self.locked:
            return colours.get("box_highlight", (0.5, 0.5, 1.0))
        else:
            return colours.get("box_highlight_move", (1.0, 0.7, 0.3))

    @property
    def edge_colour(self) -> RGBColour:
        return colours.get("box_edge", (0.5, 1.0, 1.0))

    @property
    def corner_colour(self) -> RGBColour:
        return colours.get("box_corner", (1.0, 1.0, 0.5))

    @property
    def point1_colour(self) -> RGBColour:
        return colours.get("box_point1", (0.0, 1.0, 0.0))

    @property
    def point2_colour(self) -> RGBColour:
        return colours.get("box_point2", (0.0, 0.0, 1.0))

    @property
    def locked(self) -> bool:
        """Is the selection locked or not.
        If locked (True) the highlight colour will be used, if unlocked (False) the moving colour will be used.
        """
        return self._locked

    @locked.setter
    def locked(self, lock: bool):
        """Set if the selection locked or not.
        If locked (True) the highlight colour will be used, if unlocked (False) the moving colour will be used.
        """
        self._locked = bool(lock)

    def _create_geometry_(self):
        super()._create_geometry_()

        point1, point2 = self._points - self.min + (self.min % 16)
        size = numpy.abs(point2 - point1)
        verts_per_face = 2 * 3  # triangles * verts
        # the edges of the box
        min_point, max_point = numpy.sort([point1, point2], 0).astype(numpy.float64)
        min_point -= 0.01
        max_point += 0.01
        # the edge points offset by the boundary amount.
        min_point_1 = min_point + numpy.min([numpy.ones(3), size / 4], 0)
        max_point_1 = max_point - numpy.min([numpy.ones(3), size / 4], 0)

        # down, up
        # west, east
        # north, south

        face_offset = verts_per_face * 6

        # inset faces
        for axis in ("y", "z", "x"):
            (
                self.verts[face_offset : face_offset + verts_per_face * 2, :3],
                self.verts[face_offset : face_offset + verts_per_face * 2, 3:5],
            ) = self._create_box_faces(
                (
                    min_point[0] if axis == "x" else min_point_1[0],
                    min_point[1] if axis == "y" else min_point_1[1],
                    min_point[2] if axis == "z" else min_point_1[2],
                ),
                (
                    max_point[0] if axis == "x" else max_point_1[0],
                    max_point[1] if axis == "y" else max_point_1[1],
                    max_point[2] if axis == "z" else max_point_1[2],
                ),
                up=axis == "y",
                down=axis == "y",
                north=axis == "z",
                south=axis == "z",
                west=axis == "x",
                east=axis == "x",
            )
            face_offset += verts_per_face * 2

        for y in (False, True):
            for x in (False, True):
                (
                    self.verts[face_offset : face_offset + verts_per_face * 2, :3],
                    self.verts[face_offset : face_offset + verts_per_face * 2, 3:5],
                ) = self._create_box_faces(
                    (
                        max_point_1[0] if x else min_point[0],
                        max_point_1[1] if y else min_point[1],
                        min_point_1[2],
                    ),
                    (
                        max_point[0] if x else min_point_1[0],
                        max_point[1] if y else min_point_1[1],
                        max_point_1[2],
                    ),
                    up=y,
                    down=not y,
                    west=not x,
                    east=x,
                )
                face_offset += verts_per_face * 2

        for y in (False, True):
            for z in (False, True):
                (
                    self.verts[face_offset : face_offset + verts_per_face * 2, :3],
                    self.verts[face_offset : face_offset + verts_per_face * 2, 3:5],
                ) = self._create_box_faces(
                    (
                        min_point_1[0],
                        max_point_1[1] if y else min_point[1],
                        max_point_1[2] if z else min_point[2],
                    ),
                    (
                        max_point_1[0],
                        max_point[1] if y else min_point_1[1],
                        max_point[2] if z else min_point_1[2],
                    ),
                    up=y,
                    down=not y,
                    north=not z,
                    south=z,
                )
                face_offset += verts_per_face * 2

        for x in (False, True):
            for z in (False, True):
                (
                    self.verts[face_offset : face_offset + verts_per_face * 2, :3],
                    self.verts[face_offset : face_offset + verts_per_face * 2, 3:5],
                ) = self._create_box_faces(
                    (
                        max_point_1[0] if x else min_point[0],
                        min_point_1[1],
                        max_point_1[2] if z else min_point[2],
                    ),
                    (
                        max_point[0] if x else min_point_1[0],
                        max_point_1[1],
                        max_point[2] if z else min_point_1[2],
                    ),
                    north=not z,
                    south=z,
                    west=not x,
                    east=x,
                )
                face_offset += verts_per_face * 2

        self.verts[216:360, 9:12] = self.corner_colour
        corners = point2 >= point1
        not_corners = numpy.invert(corners)
        # corners
        for y in (False, True):
            for z in (False, True):
                for x in (False, True):
                    (
                        self.verts[face_offset : face_offset + verts_per_face * 3, :3],
                        self.verts[face_offset : face_offset + verts_per_face * 3, 3:5],
                    ) = self._create_box_faces(
                        (
                            max_point_1[0] if x else min_point[0],
                            max_point_1[1] if y else min_point[1],
                            max_point_1[2] if z else min_point[2],
                        ),
                        (
                            max_point[0] if x else min_point_1[0],
                            max_point[1] if y else min_point_1[1],
                            max_point[2] if z else min_point_1[2],
                        ),
                        up=y,
                        down=not y,
                        north=not z,
                        south=z,
                        west=not x,
                        east=x,
                    )
                    if numpy.array_equal(corners, (x, y, z)):
                        self.verts[
                            face_offset : face_offset + verts_per_face * 3, 9:12
                        ] = self.point2_colour
                    elif numpy.array_equal(not_corners, (x, y, z)):
                        self.verts[
                            face_offset : face_offset + verts_per_face * 3, 9:12
                        ] = self.point1_colour
                    face_offset += verts_per_face * 3

        self.verts[:, 3:5] /= 16

        self.verts[36:72, 9:12] = self.box_tint

        indexes = numpy.zeros(6, numpy.uint8)
        if self.point2[0] > self.point1[0]:
            indexes[[4, 5]] = 0, 3
        else:
            indexes[[4, 5]] = 3, 0

        if self.point2[1] > self.point1[1]:
            indexes[[0, 1]] = 1, 4
        else:
            indexes[[0, 1]] = 4, 1

        if self.point2[2] > self.point1[2]:
            indexes[[2, 3]] = 2, 5
        else:
            indexes[[2, 3]] = 5, 2

        self.verts[36:72][
            numpy.repeat(self._highlight_edges.ravel()[indexes], 6), 9:12
        ] = self.highlight_colour

    def draw(
        self, camera_matrix: numpy.ndarray, camera_position: PointCoordinatesAny = None
    ):
        """
        Draw the selection box
        :param camera_matrix: 4x4 transformation matrix for the camera
        :param camera_position: The position of the camera. Used to flip draw direction if camera inside box.
        :return:
        """
        self._setup()
        if self._needs_rebuild:
            self._create_geometry()

        transformation_matrix = numpy.matmul(camera_matrix, self.transformation_matrix)

        depth_state = glGetBooleanv(GL_DEPTH_TEST)
        cull_state = glGetIntegerv(GL_CULL_FACE_MODE)

        # draw the lines around the boxes
        self.draw_start = 0
        self.draw_count = 36

        if depth_state:
            glDisable(GL_DEPTH_TEST)
        self._draw_mode = GL_LINE_STRIP
        super()._draw(transformation_matrix)
        if depth_state:
            glEnable(GL_DEPTH_TEST)

        if camera_position is not None:
            if camera_position in self:
                glCullFace(GL_FRONT)
            else:
                glCullFace(GL_BACK)
        self._draw_mode = GL_TRIANGLES
        self.draw_start = 36
        # 6 faces, 9 quads/face, 2 triangles/quad, 3 verts/triangle
        self.draw_count = 324
        super()._draw(transformation_matrix)

        glCullFace(cull_state)
