import wx
from typing import Set, Dict, Tuple

from .window_container import WindowContainer
from .key_config import KeyType, serialise_key

ActionIDType = str


_InputPressEventType = wx.NewEventType()
EVT_INPUT_PRESS = wx.PyEventBinder(_InputPressEventType)


class InputPressEvent(wx.PyEvent):
    """An action run by a button being pressed."""

    def __init__(self, action_id: ActionIDType):
        wx.PyEvent.__init__(self, eventType=_InputPressEventType)
        self._action_id = action_id

    @property
    def action_id(self) -> ActionIDType:
        """The string id of the action triggered by the keypress"""
        return self._action_id


_InputReleaseEventType = wx.NewEventType()
EVT_INPUT_RELEASE = wx.PyEventBinder(_InputReleaseEventType)


class InputReleaseEvent(wx.PyEvent):
    """An action run by a button being released."""

    def __init__(self, action_id: ActionIDType):
        wx.PyEvent.__init__(self, eventType=_InputReleaseEventType)
        self._action_id = action_id

    @property
    def action_id(self) -> ActionIDType:
        """The string id of the action triggered by the key release"""
        return self._action_id


_InputHeldEventType = wx.NewEventType()
EVT_INPUT_HELD = wx.PyEventBinder(_InputHeldEventType)


class InputHeldEvent(wx.PyEvent):
    """An action run by a button being held.
    This action will run frequently."""

    def __init__(self, action_ids: Set[ActionIDType]):
        wx.PyEvent.__init__(self, eventType=_InputHeldEventType)
        self._action_ids = action_ids

    @property
    def action_ids(self) -> Set[ActionIDType]:
        """The string ids of the actions that have been held."""
        return self._action_ids


class Action:
    """A private class for helping with key management for an action."""

    def __init__(self, trigger_key: KeyType, modifier_keys: Tuple[KeyType, ...]):
        self._required_keys = set(modifier_keys + (trigger_key,))
        self._trigger_key = trigger_key
        self._modifier_keys = set(modifier_keys)

    @property
    def required_keys(self) -> Set[KeyType]:
        """The keys that need to remain pressed for this action to stay active."""
        return self._required_keys

    @property
    def trigger_key(self) -> KeyType:
        """The key that needs pressing for this action to start."""
        return self._trigger_key

    @property
    def modifier_keys(self) -> Set[KeyType]:
        """Additional keys that must already be pressed for this action to start."""
        return self._modifier_keys


class ButtonInput(WindowContainer):
    """A class to detect and store user inputs."""

    def __init__(self, window: wx.Window):
        super().__init__(window)

        self._registered_actions: Dict[ActionIDType, Action] = {}

        self._pressed_keys: Set[KeyType] = set()

        # The actions that have been started but not stopped.
        self._continuous_actions: Set[ActionIDType] = set()

        # timer to deal with persistent actions
        self._input_timer = wx.Timer(self.window)

    def bind_events(self):
        """Set up all events required to run."""

        # key press actions
        self.window.Bind(wx.EVT_LEFT_DOWN, self._press)
        self.window.Bind(wx.EVT_LEFT_UP, self._release)
        self.window.Bind(wx.EVT_MIDDLE_DOWN, self._press)
        self.window.Bind(wx.EVT_MIDDLE_UP, self._release)
        self.window.Bind(wx.EVT_RIGHT_DOWN, self._press)
        self.window.Bind(wx.EVT_RIGHT_UP, self._release)
        self.window.Bind(wx.EVT_KEY_DOWN, self._press)
        self.window.Bind(wx.EVT_KEY_UP, self._release)
        self.window.Bind(wx.EVT_NAVIGATION_KEY, self._release)
        self.window.Bind(wx.EVT_NAVIGATION_KEY, self._press)
        self.window.Bind(wx.EVT_MOUSEWHEEL, self._release)
        self.window.Bind(wx.EVT_MOUSEWHEEL, self._press)
        self.window.Bind(wx.EVT_MOUSE_AUX1_DOWN, self._press)
        self.window.Bind(wx.EVT_MOUSE_AUX1_UP, self._release)
        self.window.Bind(wx.EVT_MOUSE_AUX2_DOWN, self._press)
        self.window.Bind(wx.EVT_MOUSE_AUX2_UP, self._release)

        self.window.Bind(
            wx.EVT_TIMER, self._process_continuous_inputs, self._input_timer
        )

    def enable(self):
        self._input_timer.Start(33)

    def disable(self):
        self._input_timer.Stop()

    @property
    def pressed_keys(self) -> Set[KeyType]:
        """A tuple of all the keys that are currently pressed."""
        return self._pressed_keys.copy()

    @property
    def pressed_actions(self) -> Set[ActionIDType]:
        return self._continuous_actions.copy()

    def is_key_pressed(self, key: KeyType):
        """Is the requested key currently in the pressed state."""
        return key in self._pressed_keys

    def unpress_all(self):
        """Unpress all keys.
        This is useful if the window focus is lost because key release events will not be detected."""
        self._pressed_keys.clear()
        self._clean_up_actions()

    def clear_registered_actions(self):
        """Clear the previously registered actions so that they can be repopulated."""
        self._registered_actions.clear()
        self._continuous_actions.clear()

    def action_id_registered(self, action_id: ActionIDType):
        """Has the action id already been registered."""
        return action_id in self._registered_actions

    def register_action(
        self,
        action_id: ActionIDType,
        trigger_key: KeyType,
        modifier_keys: Tuple[KeyType, ...],
    ):
        """Register a new action for the given trigger key and optional modifier keys.
        This action will be fired when the trigger key is pressed providing all the modifier keys are already pressed.

        :param action_id: The unique action id. Will raise a ValueError if it is already taken.
        :param trigger_key: The key that when pressed will start the action provided the modifier keys are pressed.
        :param modifier_keys: Other keys that need to be pressed for the action to happen.
        :return:
        """
        if type(action_id) is not str:
            raise TypeError("action_id must be a string.")
        if (
            type(trigger_key) not in (str, int)
            or type(modifier_keys) is not tuple
            or not all(type(k) in (str, int) for k in modifier_keys)
        ):
            raise TypeError(
                "The key inputs are not of the correct format. Expected Union[str, int], Tuple[Union[str, int], ...]"
            )
        if self.action_id_registered(action_id):
            raise ValueError(f"{action_id} has already been registered.")
        self._registered_actions[action_id] = Action(
            trigger_key,
            modifier_keys,
        )

    def _find_actions(self, key: KeyType) -> Tuple[ActionIDType, ...]:
        """A method to find all actions triggered by `key` with the modifier keys also pressed."""
        return tuple(
            action_id
            for action_id, action in self._registered_actions.items()
            if action.trigger_key == key
            and action.modifier_keys.issubset(self._pressed_keys)
        )

    def _press(self, evt):
        """Event to handle a number of different key presses"""
        key = serialise_key(evt)
        if key is None:
            return
        if not self.is_key_pressed(key):
            action_ids = self._find_actions(key)
            self._continuous_actions.update(action_ids)
            for action_id in action_ids:
                wx.PostEvent(
                    self.window,
                    InputPressEvent(action_id),
                )

            self._pressed_keys.add(key)
        evt.Skip()

    def _release(self, evt):
        """Event to handle a number of different key releases"""
        key = serialise_key(evt)
        if key is None:
            return
        if self.is_key_pressed(key):
            # remove the pressed key
            self._pressed_keys.remove(key)

        self._clean_up_actions()
        evt.Skip()

    def _clean_up_actions(self):
        # find all actions that are now not valid and remove them
        for action_id in list(self._continuous_actions):
            if not self._registered_actions[action_id].required_keys.issubset(
                self._pressed_keys
            ):
                self._continuous_actions.remove(action_id)
                wx.PostEvent(
                    self.window,
                    InputReleaseEvent(action_id),
                )

    def _process_continuous_inputs(self, evt):
        wx.PostEvent(
            self.window,
            InputHeldEvent(self._continuous_actions.copy()),
        )
