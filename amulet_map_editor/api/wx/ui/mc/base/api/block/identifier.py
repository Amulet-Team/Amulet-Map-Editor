from typing import Optional

from ..resource_id import BaseMCResourceIDAPI, BaseMCResourceID


class MCBlockIdentifierAPI(BaseMCResourceIDAPI):
    pass


class MCBlockIdentifier(BaseMCResourceID, MCBlockIdentifierAPI):
    def set_namespace(self, namespace: Optional[str]):
        if namespace is None:
            self._namespace = self._translation_manager.get_version(
                self.platform, self.version_number
            ).block.namespaces(self.force_blockstate)[0]
        else:
            self._namespace = str(namespace)

    def set_base_name(self, base_name: Optional[str]):
        if base_name is None:
            blocks = self._translation_manager.get_version(
                self.platform, self.version_number
            ).block.base_names(self.namespace, self.force_blockstate)
            if blocks:
                self._base_name = blocks[0]
            else:
                self._base_name = ""
        else:
            self._base_name = str(base_name)
