from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable, List, Dict, Any, Union

import amulet_nbt
from PyMCTranslate import TranslationManager, Version
from amulet.api.data_types import PlatformType, VersionNumberTuple, VersionNumberAny
from amulet.api.block import PropertyType, PropertyTypeMultiple, Block
from amulet_map_editor import log


OnChangeType = Callable[[int], None]


class State(Enum):
    Platform = "platform"
    VersionNumber = "version_number"
    ForceBlockstate = "force_blockstate"
    Namespace = "namespace"
    BaseName = "base_name"
    Properties = "properties"
    PropertiesMultiple = "properties_multiple"

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        super().__eq__(other)

    def __hash__(self):
        return hash(self.value)


class BaseState(ABC):
    _translation_manager: TranslationManager
    _edit: bool
    _state: Dict[State, Any]
    _changed_state: Dict[State, Any]
    _on_change: List[OnChangeType]

    def __init__(self, translation_manager: TranslationManager):
        self._translation_manager = translation_manager
        self._edit = False  # Is the instance being edited
        self._state = {}  # The actual state
        self._changed_state = {}  # Temporary storage that new states are written to
        self._on_change = []  # Functions to call to notify of any changes.

    def __enter__(self):
        assert (
            not self._edit
        ), "State is already being set. Release the state before editing again."
        self._edit = True
        self._changed_state = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._edit = False
        self._fix_new_state()
        self._state.update(self._changed_state)
        for on_change in self._on_change:
            try:
                on_change()
            except:
                log.warning(f"Error calling {on_change}", exc_info=True)

    def is_changed(self, state: Union[State, str]):
        """Check if the state has changed."""
        return state in self._changed_state

    def _get_state(self, state: State) -> Any:
        if state in self._changed_state:
            return self._changed_state[state]
        else:
            return self._state[state]

    def _set_state(self, state: State, value: Any):
        if not self._edit:
            raise Exception("The state has not been opened for editing.")
        self._changed_state[state] = value

    @abstractmethod
    def _fix_new_state(self):
        """
        The new state may have only been partially set.
        Update the new state so that when merged with the old state is fully valid.
        Called when released in __exit__
        """
        raise NotImplementedError

    def bind_on_change(self, on_change: OnChangeType):
        self._on_change.append(on_change)

    def unbind_on_change(self, on_change: OnChangeType):
        while on_change in self._on_change:
            self._on_change.remove(on_change)


class StateHolder:
    _state: BaseState

    def __init__(self, state: BaseState):
        self._state = None
        self.state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: BaseState):
        if self._state is not None:
            self._state.unbind_on_change(self._on_state_change)
        self._state = state
        self._state.bind_on_change(self._on_state_change)

    def _on_state_change(self):
        pass


class PlatformState(BaseState):
    def __init__(
        self,
        translation_manager: TranslationManager,
        *,
        platform: str = None,
    ):
        super().__init__(translation_manager)
        self._state[State.Platform] = self._sanitise_platform(platform)

    def _fix_new_state(self):
        if self.is_changed(State.Platform):
            self._changed_state[State.Platform] = self._sanitise_platform(
                self._changed_state[State.Platform]
            )

    def _sanitise_platform(self, platform: str = None) -> PlatformType:
        if platform is not None and platform in self.valid_platforms:
            return platform
        else:
            return self.valid_platforms[0]

    @property
    def valid_platforms(self) -> List[PlatformType]:
        return self._translation_manager.platforms()

    @property
    def platform(self) -> PlatformType:
        return self._get_state(State.Platform)

    @platform.setter
    def platform(self, platform: PlatformType):
        self._set_state(State.Platform, platform)


class VersionState(PlatformState):
    def __init__(
        self,
        translation_manager: TranslationManager,
        *,
        platform: str = None,
        version_number: VersionNumberAny = None,
        force_blockstate: bool = None,
    ):
        super().__init__(translation_manager, platform=platform)
        self._state[State.VersionNumber] = self._sanitise_version(version_number)
        self._state[State.ForceBlockstate] = self._sanitise_force_blockstate(
            force_blockstate
        )

    def _fix_new_state(self):
        super()._fix_new_state()
        if self.is_changed(State.Platform) or self.is_changed(State.VersionNumber):
            self._changed_state[State.VersionNumber] = self._sanitise_version(
                self.version_number
            )
        if self.is_changed(State.VersionNumber) or self.is_changed(
            State.ForceBlockstate
        ):
            self._changed_state[
                State.ForceBlockstate
            ] = self._sanitise_force_blockstate(self.force_blockstate)
            self._fix_version_change()

    def _fix_version_change(self):
        pass

    def _get_version(self) -> Version:
        return self._translation_manager.get_version(self.platform, self.version_number)

    def _sanitise_version(
        self, version_number: VersionNumberAny = None
    ) -> VersionNumberTuple:
        if version_number is not None:
            if version_number in self.valid_version_numbers:
                return version_number
            else:
                try:
                    return self._translation_manager.get_version(
                        self.platform, version_number
                    ).version_number
                except KeyError:
                    pass
        return self.valid_version_numbers[0]

    @property
    def valid_version_numbers(self) -> List[VersionNumberTuple]:
        return self._translation_manager.version_numbers(self.platform)

    @property
    def version_number(self) -> VersionNumberTuple:
        return self._get_state(State.VersionNumber)

    @version_number.setter
    def version_number(self, version_number: VersionNumberAny):
        self._set_state(State.VersionNumber, version_number)

    def _sanitise_force_blockstate(self, force_blockstate: bool = None) -> bool:
        if self.has_abstract_format:
            return bool(force_blockstate)
        else:
            return False

    @property
    def has_abstract_format(self) -> bool:
        return self._get_version().has_abstract_format

    @property
    def force_blockstate(self) -> bool:
        return self._get_state(State.ForceBlockstate)

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        self._set_state(State.ForceBlockstate, force_blockstate)


class BaseNamespaceState(VersionState):
    def __init__(
        self,
        translation_manager: TranslationManager,
        *,
        platform: str = None,
        version_number: VersionNumberAny = None,
        force_blockstate: bool = None,
        namespace: str = None,
    ):
        super().__init__(
            translation_manager,
            platform=platform,
            version_number=version_number,
            force_blockstate=force_blockstate,
        )
        self._state[State.Namespace] = self._sanitise_namespace(namespace)

    def _fix_new_state(self):
        super()._fix_new_state()
        if self.is_changed(State.Namespace):
            self._changed_state[State.Namespace] = self._sanitise_namespace(
                self.namespace
            )

    def _sanitise_namespace(self, namespace: str = None) -> str:
        if isinstance(namespace, str) and namespace:
            return namespace
        else:
            return self.valid_namespaces[0]

    @property
    @abstractmethod
    def valid_namespaces(self) -> List[str]:
        raise NotImplementedError

    @property
    def namespace(self) -> str:
        return self._get_state(State.Namespace)

    @namespace.setter
    def namespace(self, namespace: str):
        self._set_state(State.Namespace, namespace)


class BaseResourceIDState(BaseNamespaceState):
    def __init__(
        self,
        translation_manager: TranslationManager,
        *,
        platform: str = None,
        version_number: VersionNumberAny = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
    ):
        super().__init__(
            translation_manager,
            platform=platform,
            version_number=version_number,
            force_blockstate=force_blockstate,
            namespace=namespace,
        )
        self._state[State.BaseName] = self._sanitise_base_name(base_name)

    def _fix_new_state(self):
        super()._fix_new_state()
        if self.is_changed(State.BaseName):
            self._changed_state[State.BaseName] = self._sanitise_base_name(
                self.base_name
            )

    def _sanitise_base_name(self, base_name: str = None) -> str:
        if isinstance(base_name, str) and base_name:
            return base_name
        else:
            return self.valid_base_names[0]

    @property
    @abstractmethod
    def valid_base_names(self) -> List[str]:
        raise NotImplementedError

    @property
    def base_name(self) -> str:
        return self._get_state(State.BaseName)

    @base_name.setter
    def base_name(self, base_name: str):
        self._set_state(State.BaseName, base_name)


class BiomeNamespaceState(BaseNamespaceState):
    @property
    def valid_namespaces(self) -> List[str]:
        # TODO: make the biome translator similar to the block translator
        return list(
            set(biome.split(":", 1)[0] for biome in self._get_version().biome.biome_ids)
        )


class BiomeResourceIDState(BiomeNamespaceState, BaseResourceIDState):
    @property
    def valid_base_names(self) -> List[str]:
        biomes = []
        for biome in self._get_version().biome.biome_ids:
            namespace, base_name = biome.split(":", 1)
            if namespace == self.namespace:
                biomes.append(base_name)
        return biomes


class BlockNamespaceState(BaseNamespaceState):
    @property
    def valid_namespaces(self) -> List[str]:
        return self._get_version().block.namespaces(self.force_blockstate)


class BlockResourceIDState(BlockNamespaceState, BaseResourceIDState):
    @property
    def valid_base_names(self) -> List[str]:
        return self._get_version().block.base_names(
            self.namespace, self.force_blockstate
        )


class BlockState(BlockResourceIDState):
    def __init__(
        self,
        translation_manager: TranslationManager,
        *,
        platform: str = None,
        version_number: VersionNumberAny = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        properties: PropertyType = None,
        properties_multiple: PropertyTypeMultiple = None,
    ):
        super().__init__(
            translation_manager,
            platform=platform,
            version_number=version_number,
            force_blockstate=force_blockstate,
            namespace=namespace,
            base_name=base_name,
        )
        self._state[State.Properties] = self._sanitise_properties(properties)
        self._state[State.PropertiesMultiple] = self._sanitise_properties_multiple(
            properties_multiple
        )

    def _fix_version_change(self):
        universal_block, _, _ = self._translation_manager.get_version(
            self._state[State.Platform], self._state[State.VersionNumber]
        ).block.to_universal(
            Block(self.namespace, self.base_name, self.properties),
            force_blockstate=self.force_blockstate,
        )
        version_block, _, _ = self._translation_manager.get_version(
            self.platform, self.version_number
        ).block.from_universal(universal_block)
        if isinstance(version_block, Block):
            version_block: Block
            if self.is_changed(State.Namespace) or self.is_changed(State.BaseName):
                if (
                    version_block.namespace == self.namespace
                    and version_block.base_name == self.base_name
                ):
                    if not self.is_changed(State.Properties):
                        self._changed_state[
                            State.Properties
                        ] = self._sanitise_properties(version_block.properties)
            else:
                self._changed_state[State.Namespace] = self._sanitise_namespace(
                    version_block.namespace
                )
                self._changed_state[State.BaseName] = self._sanitise_base_name(
                    version_block.base_name
                )
                if not self.is_changed(State.Properties):
                    self._changed_state[State.Properties] = self._sanitise_properties(
                        version_block.properties
                    )

    def _fix_new_state(self):
        super()._fix_new_state()
        if self.is_changed(State.Properties) or self.is_changed(
            State.PropertiesMultiple
        ):
            self._changed_state[
                State.PropertiesMultiple
            ] = self._sanitise_properties_multiple(self.properties_multiple)
            self._changed_state[State.Properties] = self._sanitise_properties(
                self.properties
            )

    def _get_block_spec(self):
        return self._get_version().block.get_specification(
            self.namespace, self.base_name, self.force_blockstate
        )

    @property
    def default_properties(self) -> PropertyType:
        return self._get_block_spec().default_properties

    @property
    def valid_properties(self) -> PropertyTypeMultiple:
        return self._get_block_spec().valid_properties

    def _sanitise_properties(self, properties: PropertyType = None) -> PropertyType:
        valid_properties = self.valid_properties
        default_properties = self.default_properties
        if isinstance(properties, dict):
            return {
                name: properties[name]
                if name in properties
                and isinstance(properties[name], amulet_nbt.BaseValueType)
                and properties[name] in valid_properties[name]
                else default_properties[name]
                for name in valid_properties
            }
        else:
            return default_properties

    @property
    def properties(self) -> PropertyType:
        return self._get_state(State.Properties)

    @properties.setter
    def properties(self, properties: PropertyType):
        self._set_state(State.Properties, properties)

    def _sanitise_properties_multiple(
        self, properties: PropertyTypeMultiple = None
    ) -> PropertyTypeMultiple:
        valid_properties = self.valid_properties
        if isinstance(properties, dict):
            return {
                name: tuple(
                    val
                    for val in properties[name]
                    if isinstance(val, amulet_nbt.BaseValueType)
                    and val in valid_properties[name]
                )
                if name in properties and isinstance(properties[name], (list, tuple))
                else valid_properties[name]
                for name in valid_properties
            }
        else:
            return valid_properties

    @property
    def properties_multiple(self) -> PropertyTypeMultiple:
        return self._get_state(State.PropertiesMultiple)

    @properties_multiple.setter
    def properties_multiple(self, properties_multiple: PropertyTypeMultiple):
        self._set_state(State.PropertiesMultiple, properties_multiple)
