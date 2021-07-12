from typing import Optional

from .resource_id import BaseMCResourceIDAPI, BaseMCResourceID


class MCBiomeIdentifierAPI(BaseMCResourceIDAPI):
    pass


class MCBiomeIdentifier(BaseMCResourceID, MCBiomeIdentifierAPI):
    def set_namespace(self, namespace: Optional[str]):
        if namespace is None:
            self._namespace = (
                self._translation_manager.get_version(
                    self.platform, self.version_number
                )
                .biome.biome_ids[0]
                .split(":", 1)[0]
            )
        else:
            self._namespace = str(namespace)

    def set_base_name(self, base_name: Optional[str]):
        if base_name is None:
            self._base_name = (
                self._translation_manager.get_version(
                    self.platform, self.version_number
                )
                .biome.biome_ids[0]
                .split(":", 1)[-1]
            )
        else:
            self._base_name = str(base_name)
