import wx
from amulet_map_editor.amulet_wx.simple import SimpleDialog, SimpleScrollablePanel, SimpleChoice
from typing import Dict, Tuple, Optional, Union

ModifierKeyType = int
KeyType = Union[int, str]
ModifierType = Tuple[ModifierKeyType, ...]
SerialisedKeyType = Tuple[ModifierType, KeyType]
KeybindDict = Dict[str, SerialisedKeyType]

MouseLeft = "ML"
MouseMiddle = "MM"
MouseRight = "MR"
MouseWheelScrollUp = "MWSU"
MouseWheelScrollDown = "MWSD"

_presets: Dict[str, KeybindDict] = {
    "right": {
        "up": ((), wx.WXK_SPACE),
        "down": ((), wx.WXK_SHIFT),
        "forwards": ((), ord("W")),
        "backwards": ((), ord("S")),
        "left": ((), ord("A")),
        "right": ((), ord("D")),
        "box click": ((), MouseLeft),
        "toggle selection mode": ((), MouseRight),
        "toggle mouse lock": ((), MouseMiddle),
        "speed+": ((), MouseWheelScrollUp),
        "speed-": ((), MouseWheelScrollDown)
    },
    "right_laptop": {
        "up": ((), wx.WXK_SPACE),
        "down": ((), wx.WXK_SHIFT),
        "forwards": ((), ord("W")),
        "backwards": ((), ord("S")),
        "left": ((), ord("A")),
        "right": ((), ord("D")),
        "box click": ((), MouseLeft),
        "toggle selection mode": ((), MouseRight),
        "toggle mouse lock": ((), ord("F")),
        "speed+": ((), wx.WXK_PAGEUP),
        "speed-": ((), wx.WXK_PAGEDOWN)
    },
    "left": {
        "up": ((), wx.WXK_SPACE),
        "down": ((), ord(';')),
        "forwards": ((), ord("I")),
        "backwards": ((), ord("K")),
        "left": ((), ord("J")),
        "right": ((), ord("L")),
        "box click": ((), MouseLeft),
        "toggle selection mode": ((), MouseRight),
        "toggle mouse lock": ((), MouseMiddle),
        "speed+": ((), MouseWheelScrollUp),
        "speed-": ((), MouseWheelScrollDown)
    },
    "left_laptop": {
        "up": ((), wx.WXK_SPACE),
        "down": ((), ord(';')),
        "forwards": ((), ord("I")),
        "backwards": ((), ord("K")),
        "left": ((), ord("J")),
        "right": ((), ord("L")),
        "box click": ((), MouseLeft),
        "toggle selection mode": ((), MouseRight),
        "toggle mouse lock": ((), ord("H")),
        "speed+": ((), wx.WXK_PAGEUP),
        "speed-": ((), wx.WXK_PAGEDOWN)
    }
}

DefaultKeys = _presets["right"]


_mouse_events = {
    wx.EVT_LEFT_DOWN.evtType[0]: "ML",
    wx.EVT_LEFT_UP.evtType[0]: "ML",
    wx.EVT_MIDDLE_DOWN.evtType[0]: "MM",
    wx.EVT_MIDDLE_UP.evtType[0]: "MM",
    wx.EVT_RIGHT_DOWN.evtType[0]: "MR",
    wx.EVT_RIGHT_UP.evtType[0]: "MR"
}


def serialise_key_event(evt: Union[wx.KeyEvent, wx.MouseEvent]) -> Optional[SerialisedKeyType]:
    if isinstance(evt, wx.KeyEvent):
        modifier = []
        key = evt.GetUnicodeKey() or evt.GetKeyCode()
        if key == wx.WXK_CONTROL:
            print('key == ctrl')
            return
        if evt.ControlDown():
            if key in (wx.WXK_SHIFT, wx.WXK_ALT):
                print('key == shift | alt')
                return  # if control is pressed the real key must not be a modifier

            modifier.append(wx.WXK_CONTROL)
            if evt.ShiftDown():
                modifier.append(wx.WXK_SHIFT)
            if evt.AltDown():
                modifier.append(wx.WXK_ALT)
        return tuple(modifier), int(key)
    elif isinstance(evt, wx.MouseEvent):
        key = evt.GetEventType()
        if key in wx.EVT_MOUSEWHEEL.evtType:
            if evt.GetWheelRotation() < 0:
                return (), "MWSD"
            elif evt.GetWheelRotation() > 0:
                return (), "MWSU"
        elif key in _mouse_events:
            return (), _mouse_events[key]


class KeyConfigModal(SimpleDialog):
    def __init__(self, parent: wx.Window):
        super().__init__(parent, 'Key Select')
        self._key_config = KeyConfig(self)
        self.sizer.Add(
            self._key_config,
            0,
            wx.EXPAND
        )
        self.Layout()

    @property
    def options(self) -> Dict[str, SerialisedKeyType]:
        return self._key_config.options


class KeyConfig(wx.BoxSizer):
    def __init__(self, parent: wx.Window):
        super().__init__(wx.VERTICAL)
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.Add(top_sizer, 0, wx.EXPAND)
        self._choice = SimpleChoice(parent, list(_presets.keys()))
        top_sizer.Add(self._choice, 1, wx.ALL | wx.EXPAND, 5)
        # some other buttons

        self._options = SimpleScrollablePanel(parent)
        self.Add(self._options, 1, wx.EXPAND)


    @property
    def options(self) -> Dict[str, SerialisedKeyType]:
        return _presets[self._choice.GetCurrentString()]


