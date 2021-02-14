from typing import List
from amulet_map_editor.api.wx.util.key_config import (
    KeybindContainer,
    KeybindGroup,
    KeybindGroupIdType,
    KeyActionType,
    Space,
    Shift,
    MouseLeft,
    MouseRight,
    MouseWheelScrollUp,
    MouseWheelScrollDown,
    Control,
    Alt,
    Tab,
)

ACT_MOVE_UP = "ACT_MOVE_UP"
ACT_MOVE_DOWN = "ACT_MOVE_DOWN"
ACT_MOVE_FORWARDS = "ACT_MOVE_FORWARDS"
ACT_MOVE_BACKWARDS = "ACT_MOVE_BACKWARDS"
ACT_MOVE_LEFT = "ACT_MOVE_LEFT"
ACT_MOVE_RIGHT = "ACT_MOVE_RIGHT"
ACT_BOX_CLICK = "ACT_BOX_CLICK"
ACT_BOX_CLICK_ADD = "ACT_BOX_CLICK_ADD"
ACT_CHANGE_MOUSE_MODE = "ACT_CHANGE_MOUSE_MODE"
ACT_INCR_SPEED = "ACT_INCR_SPEED"
ACT_DECR_SPEED = "ACT_DECR_SPEED"
ACT_INCR_SELECT_DISTANCE = "ACT_INCR_SELECT_DISTANCE"
ACT_DECR_SELECT_DISTANCE = "ACT_DECR_SELECT_DISTANCE"
ACT_DESELECT_ALL_BOXES = "ACT_DESELECT_ALL_BOXES"
ACT_DELESECT_BOX = "ACT_DELESECT_BOX"
ACT_INSPECT_BLOCK = "ACT_INSPECT_BLOCK"
ACT_CHANGE_PROJECTION = "ACT_CHANGE_PROJECTION"

KeybindKeys: List[KeyActionType] = [
    ACT_MOVE_UP,
    ACT_MOVE_DOWN,
    ACT_MOVE_FORWARDS,
    ACT_MOVE_BACKWARDS,
    ACT_MOVE_LEFT,
    ACT_MOVE_RIGHT,
    ACT_BOX_CLICK,
    ACT_BOX_CLICK_ADD,
    ACT_CHANGE_MOUSE_MODE,
    ACT_INCR_SPEED,
    ACT_DECR_SPEED,
    ACT_INCR_SELECT_DISTANCE,
    ACT_DECR_SELECT_DISTANCE,
    ACT_DESELECT_ALL_BOXES,
    ACT_DELESECT_BOX,
    ACT_INSPECT_BLOCK,
    ACT_CHANGE_PROJECTION,
]

PresetKeybinds: KeybindContainer = {
    "right": {
        ACT_MOVE_UP: ((), Space),
        ACT_MOVE_DOWN: ((), Shift),
        ACT_MOVE_FORWARDS: ((), "W"),
        ACT_MOVE_BACKWARDS: ((), "S"),
        ACT_MOVE_LEFT: ((), "A"),
        ACT_MOVE_RIGHT: ((), "D"),
        ACT_BOX_CLICK: ((), MouseLeft),
        ACT_BOX_CLICK_ADD: ((Control,), MouseLeft),
        ACT_CHANGE_MOUSE_MODE: ((), MouseRight),
        ACT_INCR_SPEED: ((), MouseWheelScrollUp),
        ACT_DECR_SPEED: ((), MouseWheelScrollDown),
        ACT_INCR_SELECT_DISTANCE: ((), "R"),
        ACT_DECR_SELECT_DISTANCE: ((), "F"),
        ACT_DESELECT_ALL_BOXES: ((Control, Shift), "D"),
        ACT_DELESECT_BOX: ((Control,), "D"),
        ACT_INSPECT_BLOCK: ((), Alt),
        ACT_CHANGE_PROJECTION: ((), Tab),
    },
    "right_laptop": {
        ACT_MOVE_UP: ((), Space),
        ACT_MOVE_DOWN: ((), Shift),
        ACT_MOVE_FORWARDS: ((), "W"),
        ACT_MOVE_BACKWARDS: ((), "S"),
        ACT_MOVE_LEFT: ((), "A"),
        ACT_MOVE_RIGHT: ((), "D"),
        ACT_BOX_CLICK: ((), MouseLeft),
        ACT_BOX_CLICK_ADD: ((Control,), MouseLeft),
        ACT_CHANGE_MOUSE_MODE: ((), MouseRight),
        ACT_INCR_SPEED: ((), "."),
        ACT_DECR_SPEED: ((), ","),
        ACT_INCR_SELECT_DISTANCE: ((), "R"),
        ACT_DECR_SELECT_DISTANCE: ((), "F"),
        ACT_DESELECT_ALL_BOXES: ((Control, Shift), "D"),
        ACT_DELESECT_BOX: ((Control,), "D"),
        ACT_INSPECT_BLOCK: ((), Alt),
        ACT_CHANGE_PROJECTION: ((), Tab),
    },
    "left": {
        ACT_MOVE_UP: ((), Space),
        ACT_MOVE_DOWN: ((), ";"),
        ACT_MOVE_FORWARDS: ((), "I"),
        ACT_MOVE_BACKWARDS: ((), "K"),
        ACT_MOVE_LEFT: ((), "J"),
        ACT_MOVE_RIGHT: ((), "L"),
        ACT_BOX_CLICK: ((), MouseLeft),
        ACT_BOX_CLICK_ADD: ((Control,), MouseLeft),
        ACT_CHANGE_MOUSE_MODE: ((), MouseRight),
        ACT_INCR_SPEED: ((), MouseWheelScrollUp),
        ACT_DECR_SPEED: ((), MouseWheelScrollDown),
        ACT_INCR_SELECT_DISTANCE: ((), "Y"),
        ACT_DECR_SELECT_DISTANCE: ((), "H"),
        ACT_DESELECT_ALL_BOXES: ((Control, Shift), "D"),
        ACT_DELESECT_BOX: ((Control,), "D"),
        ACT_INSPECT_BLOCK: ((), Alt),
        ACT_CHANGE_PROJECTION: ((), Tab),
    },
    "left_laptop": {
        ACT_MOVE_UP: ((), Space),
        ACT_MOVE_DOWN: ((), ";"),
        ACT_MOVE_FORWARDS: ((), "I"),
        ACT_MOVE_BACKWARDS: ((), "K"),
        ACT_MOVE_LEFT: ((), "J"),
        ACT_MOVE_RIGHT: ((), "L"),
        ACT_BOX_CLICK: ((), MouseLeft),
        ACT_BOX_CLICK_ADD: ((Control,), MouseLeft),
        ACT_CHANGE_MOUSE_MODE: ((), MouseRight),
        ACT_INCR_SPEED: ((), "."),
        ACT_DECR_SPEED: ((), ","),
        ACT_INCR_SELECT_DISTANCE: ((), "Y"),
        ACT_DECR_SELECT_DISTANCE: ((), "H"),
        ACT_DESELECT_ALL_BOXES: ((Control, Shift), "D"),
        ACT_DELESECT_BOX: ((Control,), "D"),
        ACT_INSPECT_BLOCK: ((), Alt),
        ACT_CHANGE_PROJECTION: ((), Tab),
    },
}

DefaultKeybindGroupId: KeybindGroupIdType = "right"
DefaultKeys: KeybindGroup = PresetKeybinds[DefaultKeybindGroupId]
