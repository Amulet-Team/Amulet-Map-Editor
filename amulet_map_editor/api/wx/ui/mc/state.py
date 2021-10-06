from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable, List, Dict, Any, Union, Tuple, Optional
import copy

from PyMCTranslate import TranslationManager, Version
from PyMCTranslate.py3.api.version.translators.block import BlockSpecification
from amulet.api.data_types import PlatformType, VersionNumberTuple, VersionNumberAny
from amulet.api.block import (
    PropertyType,
    PropertyTypeMultiple,
    Block,
    PropertyDataTypes,
)
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
    ValidProperties = "valid_properties"

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

    @property
    def translation_manager(self) -> TranslationManager:
        return self._translation_manager

    def __deepcopy__(self, memodict=None):
        new_state = self.__class__(self.translation_manager)
        new_state._state = copy.deepcopy(self._state)
        new_state._changed_state = copy.deepcopy(self._state)
        return new_state


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
        return self.valid_version_numbers[-1]

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
        if self.is_changed(State.ForceBlockstate) or self.is_changed(State.Namespace):
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
        if self.is_changed(State.Namespace) or self.is_changed(State.BaseName):
            self._changed_state[State.BaseName] = self._sanitise_base_name(
                self.base_name
            )

    def _sanitise_base_name(self, base_name: str = None) -> str:
        if isinstance(base_name, str) and base_name:
            return base_name
        else:
            valid = self.valid_base_names
            if valid:
                return valid[0]
            else:
                return ""

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

    @property
    def is_supported(self):
        return self.base_name in self.valid_base_names


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

    def _fix_version_change(self):
        if not self.is_changed(State.Namespace) or self.is_changed(State.BaseName):
            universal_biome = self._translation_manager.get_version(
                self._state[State.Platform], self._state[State.VersionNumber]
            ).biome.to_universal(f"{self.namespace}:{self.base_name}")
            version_biome = self._translation_manager.get_version(
                self.platform, self.version_number
            ).biome.from_universal(universal_biome)
            namespace, base_name = version_biome.split(":")
            self._changed_state[State.Namespace] = self._sanitise_namespace(namespace)
            self._changed_state[State.BaseName] = self._sanitise_base_name(base_name)


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
    """
    A class to store the state of a block id and properties.
    Supports a single value per property and a sequence of values.
    """

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
        valid_properties: PropertyTypeMultiple = None,
    ):
        super().__init__(
            translation_manager,
            platform=platform,
            version_number=version_number,
            force_blockstate=force_blockstate,
            namespace=namespace,
            base_name=base_name,
        )
        (
            self._state[State.Properties],
            self._state[State.PropertiesMultiple],
            self._state[State.ValidProperties],
        ) = self._sync_properties(
            self._sanitise_properties(properties),
            self._sanitise_properties_multiple(properties_multiple),
            self._sanitise_properties_multiple(valid_properties),
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
        validate = self.is_changed(State.BaseName)
        if self.is_changed(State.Properties):
            self._changed_state[State.Properties] = self._sanitise_properties(
                self.properties
            )
            validate = True
        if self.is_changed(State.PropertiesMultiple):
            self._changed_state[
                State.PropertiesMultiple
            ] = self._sanitise_properties_multiple(self.properties_multiple)
            validate = True
        if self.is_changed(State.ValidProperties) and self.is_supported:
            self._changed_state[
                State.ValidProperties
            ] = self._sanitise_properties_multiple(self.valid_properties)

        if validate:
            (
                self._changed_state[State.Properties],
                self._changed_state[State.PropertiesMultiple],
                self._changed_state[State.ValidProperties],
            ) = self._sync_properties()

    def _get_block_spec(self):
        if self.is_supported:
            return self._get_version().block.get_specification(
                self.namespace, self.base_name, self.force_blockstate
            )
        else:
            return BlockSpecification({})

    @property
    def default_properties(self) -> PropertyType:
        """The default properties for this block."""
        if self.is_supported:
            return self._get_block_spec().default_properties
        else:
            return {}

    @property
    def valid_properties(self) -> PropertyTypeMultiple:
        """The properties that are valid for this block."""
        if self.is_supported:
            return self._get_block_spec().valid_properties
        else:
            return self._get_state(State.ValidProperties)

    @valid_properties.setter
    def valid_properties(self, valid_properties: PropertyTypeMultiple):
        self._set_state(State.ValidProperties, valid_properties)

    def _sanitise_properties(self, properties: PropertyType = None) -> PropertyType:
        if isinstance(properties, dict):
            return {
                key: val
                for key, val in properties.items()
                if isinstance(val, PropertyDataTypes)
            }
        else:
            return {}

    def _sync_properties(
        self,
        properties: PropertyType = None,
        properties_multiple: PropertyTypeMultiple = None,
        valid_properties: PropertyTypeMultiple = None,
    ) -> Tuple[PropertyType, PropertyTypeMultiple, Optional[PropertyTypeMultiple]]:
        """Make sure that all the properties states are in sync."""
        if properties is None:
            properties = self.properties
        if properties_multiple is None:
            properties_multiple = self.properties_multiple
        if valid_properties is None or self.is_supported:
            valid_properties = self.valid_properties
        if not self.is_supported:
            # Nothing is known. Populate/extend valid from the filled out.
            valid_properties = {
                prop: tuple(
                    set(
                        valid_properties.get(prop, ())
                        + properties_multiple.get(prop, ())
                        + ((properties[prop],) if prop in properties else ())
                    )
                )
                for prop in set(
                    list(valid_properties)
                    + list(properties)
                    + list(properties_multiple)
                )
            }
            # Make sure there are valid properties.
            valid_properties = {
                key: val for key, val in valid_properties.items() if val
            }
            default_properties = {key: val[0] for key, val in valid_properties.items()}
        else:
            default_properties = self.default_properties

        # Make sure all the properties are defined and are a subset of valid properties
        properties = {
            name: properties[name]
            if name in properties
            and isinstance(properties[name], PropertyDataTypes)
            and properties[name] in valid_properties[name]
            else default_properties[name]
            for name in valid_properties
        }

        # Make sure all the multiple properties are defined and are a subset of valid properties
        properties_multiple = {
            name: tuple(
                val
                for val in properties_multiple[name]
                if isinstance(val, PropertyDataTypes) and val in valid_properties[name]
            )
            if name in properties_multiple
            and isinstance(properties_multiple[name], (list, tuple))
            else valid_properties[name]
            for name in valid_properties
        }
        if self.is_supported:
            return properties, properties_multiple, {}
        else:
            return properties, properties_multiple, valid_properties

    @property
    def properties(self) -> PropertyType:
        """The value for each property that is currently active for this block."""
        return self._get_state(State.Properties)

    @properties.setter
    def properties(self, properties: PropertyType):
        self._set_state(State.Properties, properties)

    def _sanitise_properties_multiple(
        self, properties: PropertyTypeMultiple = None
    ) -> PropertyTypeMultiple:
        if isinstance(properties, dict):
            return {
                name: tuple(
                    val
                    for val in properties[name]
                    if isinstance(val, PropertyDataTypes)
                )
                for name in properties
            }
        else:
            return {}

    @property
    def properties_multiple(self) -> PropertyTypeMultiple:
        """The values for each property that are currently active for this block."""
        return self._get_state(State.PropertiesMultiple)

    @properties_multiple.setter
    def properties_multiple(self, properties_multiple: PropertyTypeMultiple):
        self._set_state(State.PropertiesMultiple, properties_multiple)
