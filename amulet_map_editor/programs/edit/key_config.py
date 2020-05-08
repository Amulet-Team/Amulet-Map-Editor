from typing import List
from amulet_map_editor.amulet_wx.key_config import (
    KeybindContainer,
    KeybindGroup,
    KeybindGroupIdType,
    KeybindIdType,
    Space,
    Shift,
    MouseLeft,
    MouseRight,
    MouseMiddle,
    MouseWheelScrollUp,
    MouseWheelScrollDown,
)


KeybindKeys: List[KeybindIdType] = [
    "up",
    "down",
    "forwards",
    "backwards",
    "left",
    "right",
    "box click",
    "toggle selection mode",
    "toggle mouse lock",
    "speed+",
    "speed-",
]


PresetKeybinds: KeybindContainer = {
    "right": {
        "up": ((), Space),
        "down": ((), Shift),
        "forwards": ((), "W"),
        "backwards": ((), "S"),
        "left": ((), "A"),
        "right": ((), "D"),
        "box click": ((), MouseLeft),
        "toggle selection mode": ((), MouseRight),
        "toggle mouse lock": ((), MouseMiddle),
        "speed+": ((), MouseWheelScrollUp),
        "speed-": ((), MouseWheelScrollDown)
    },
    "right_laptop": {
        "up": ((), Space),
        "down": ((), Shift),
        "forwards": ((), "W"),
        "backwards": ((), "S"),
        "left": ((), "A"),
        "right": ((), "D"),
        "box click": ((), MouseLeft),
        "toggle selection mode": ((), MouseRight),
        "toggle mouse lock": ((), "F"),
        "speed+": ((), "."),
        "speed-": ((), ",")
    },
    "left": {
        "up": ((), Space),
        "down": ((), ';'),
        "forwards": ((), "I"),
        "backwards": ((), "K"),
        "left": ((), "J"),
        "right": ((), "L"),
        "box click": ((), MouseLeft),
        "toggle selection mode": ((), MouseRight),
        "toggle mouse lock": ((), MouseMiddle),
        "speed+": ((), MouseWheelScrollUp),
        "speed-": ((), MouseWheelScrollDown)
    },
    "left_laptop": {
        "up": ((), Space),
        "down": ((), ';'),
        "forwards": ((), "I"),
        "backwards": ((), "K"),
        "left": ((), "J"),
        "right": ((), "L"),
        "box click": ((), MouseLeft),
        "toggle selection mode": ((), MouseRight),
        "toggle mouse lock": ((), "H"),
        "speed+": ((), "."),
        "speed-": ((), ",")
    }
}

DefaultKeybindGroupId: KeybindGroupIdType = "right"
DefaultKeys: KeybindGroup = PresetKeybinds[DefaultKeybindGroupId]
