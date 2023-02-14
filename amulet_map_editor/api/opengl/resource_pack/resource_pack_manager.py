from amulet_map_editor.api.opengl.resource_pack import OpenGLResourcePack


class OpenGLResourcePackManagerStatic:
    """A class to hold an opengl resource pack.
    All classes wanting to access block geometry or textures should subclass this class.
    """

    def __init__(
        self,
        resource_pack: OpenGLResourcePack,
    ):
        self._resource_pack = resource_pack

    @property
    def resource_pack(self) -> OpenGLResourcePack:
        return self._resource_pack


class OpenGLResourcePackManager(OpenGLResourcePackManagerStatic):
    """A class to hold and enable switching of an opengl resource pack.
    All classes wanting to access block geometry or textures should subclass this class.
    """

    @property
    def resource_pack(self) -> OpenGLResourcePack:
        return self._resource_pack

    @resource_pack.setter
    def resource_pack(self, resource_pack: OpenGLResourcePack):
        assert isinstance(resource_pack, OpenGLResourcePack)
        self._resource_pack = resource_pack
        self._rebuild()

    def _rebuild(self):
        """Rebuild all geometry."""
        raise NotImplementedError
