import wx
from amulet_map_editor.amulet_wx.simple import SimpleDialog, SimpleScrollablePanel, SimpleChoice
from typing import Dict, Tuple, Optional, Union, Sequence

ModifierKeyType = str
KeyType = Union[int, str]
KeybindGroupIdType = str
KeybindIdType = str
ModifierType = Tuple[ModifierKeyType, ...]
SerialisedKeyType = Tuple[ModifierType, KeyType]
KeybindGroup = Dict[KeybindIdType, SerialisedKeyType]
KeybindContainer = Dict[KeybindGroupIdType, KeybindGroup]

MouseLeft = "MOUSE_LEFT"
MouseMiddle = "MOUSE_MIDDLE"
MouseRight = "MOUSE_RIGHT"
MouseWheelScrollUp = "MOUSE_WHEEL_SCROLL_UP"
MouseWheelScrollDown = "MOUSE_WHEEL_SCROLL_DOWN"
Control = "CTRL"
Shift = "SHIFT"
Alt = "ALT"

Space = "SPACE"
PageUp = "PAGE_UP"
PageDown = "PAGE_DOWN"

key_string_map = {
    wx.WXK_SHIFT: Shift,
    wx.WXK_ALT: Alt,
    wx.WXK_SPACE: Space,
    wx.WXK_PAGEUP: PageUp,
    wx.WXK_PAGEDOWN: PageDown
}


_mouse_events = {
    wx.EVT_LEFT_DOWN.evtType[0]: MouseLeft,
    wx.EVT_LEFT_UP.evtType[0]: MouseLeft,
    wx.EVT_MIDDLE_DOWN.evtType[0]: MouseMiddle,
    wx.EVT_MIDDLE_UP.evtType[0]: MouseMiddle,
    wx.EVT_RIGHT_DOWN.evtType[0]: MouseRight,
    wx.EVT_RIGHT_UP.evtType[0]: MouseRight
}


def serialise_key_event(evt: Union[wx.KeyEvent, wx.MouseEvent]) -> Optional[SerialisedKeyType]:
    if isinstance(evt, wx.KeyEvent):
        modifier = []
        key = evt.GetUnicodeKey() or evt.GetKeyCode()
        if key == wx.WXK_CONTROL:
            return
        if evt.ControlDown():
            if key in (wx.WXK_SHIFT, wx.WXK_ALT):
                return  # if control is pressed the real key must not be a modifier

            modifier.append(Control)
            if evt.ShiftDown():
                modifier.append(Shift)
            if evt.AltDown():
                modifier.append(Alt)

        if 33 <= key <= 126:
            key = chr(key).upper()
        elif key in key_string_map:
            key = key_string_map[key]
        return tuple(modifier), key
    elif isinstance(evt, wx.MouseEvent):
        key = evt.GetEventType()
        if key in wx.EVT_MOUSEWHEEL.evtType:
            if evt.GetWheelRotation() < 0:
                return (), MouseWheelScrollDown
            elif evt.GetWheelRotation() > 0:
                return (), MouseWheelScrollUp
        elif key in _mouse_events:
            return (), _mouse_events[key]


class KeyConfigModal(SimpleDialog):
    def __init__(
            self,
            parent: wx.Window,
            selected_group: KeybindGroupIdType,
            entries: Sequence[KeybindIdType],
            fixed_keybinds: KeybindContainer,
            user_keybinds: KeybindContainer
    ):
        super().__init__(parent, 'Key Select')
        self._key_config = KeyConfig(self, selected_group, entries, fixed_keybinds, user_keybinds)
        self.sizer.Add(
            self._key_config,
            0,
            wx.EXPAND
        )
        self.Layout()

    @property
    def options(self) -> Tuple[KeybindContainer, KeybindGroupIdType, KeybindGroup]:
        return self._key_config.options


class KeyConfig(wx.BoxSizer):
    def __init__(
            self,
            parent: wx.Window,
            selected_group: KeybindGroupIdType,
            entries: Sequence[KeybindIdType],
            fixed_keybinds: KeybindContainer,
            user_keybinds: KeybindContainer
    ):
        super().__init__(wx.VERTICAL)
        self._entries = entries
        self._fixed_keybinds = fixed_keybinds
        self._user_keybinds = user_keybinds

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.Add(top_sizer, 0, wx.EXPAND)
        self._choice = SimpleChoice(
            parent,
            list(self._fixed_keybinds.keys()) + list(self._user_keybinds.keys()),
            selected_group
        )
        top_sizer.Add(self._choice, 1, wx.ALL | wx.EXPAND, 5)
        # some other buttons

        self._options = SimpleScrollablePanel(parent)
        self.Add(self._options, 1, wx.EXPAND)

    @property
    def options(self) -> Tuple[KeybindContainer, KeybindGroupIdType, KeybindGroup]:
        keybind_group = self._choice.GetCurrentString()
        if keybind_group in self._fixed_keybinds:
            keybinds = self._fixed_keybinds[keybind_group]
        else:
            keybinds = self._user_keybinds[keybind_group]
        return self._user_keybinds, keybind_group, keybinds
