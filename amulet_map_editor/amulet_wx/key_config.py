import wx
from amulet_map_editor.amulet_wx.simple import SimpleDialog, SimpleScrollablePanel, SimpleChoice
from typing import Dict, Tuple, Optional, Union, Sequence

from amulet_map_editor.amulet_wx.icon import ADD, SUBTRACT, EDIT

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
    wx.WXK_PAGEDOWN: PageDown,
    wx.WXK_BACK: "BACK",
    wx.WXK_TAB: "TAB",
    wx.WXK_RETURN: "RETURN",
    wx.WXK_ESCAPE: "ESCAPE",
    wx.WXK_DELETE: "DELETE",
    wx.WXK_START: "START",
    wx.WXK_MENU: "MENU",
    wx.WXK_PAUSE: "PAUSE",
    wx.WXK_CAPITAL: "CAPITAL",
    wx.WXK_END: "END",
    wx.WXK_HOME: "HOME",
    wx.WXK_LEFT: "LEFT",
    wx.WXK_UP: "UP",
    wx.WXK_RIGHT: "RIGHT",
    wx.WXK_DOWN: "DOWN",
    wx.WXK_SELECT: "SELECT",
    wx.WXK_PRINT: "PRINT",
    wx.WXK_EXECUTE: "EXECUTE",
    wx.WXK_SNAPSHOT: "SNAPSHOT",
    wx.WXK_INSERT: "INSERT",
    wx.WXK_HELP: "HELP",
    wx.WXK_NUMPAD0: "NUMPAD0",
    wx.WXK_NUMPAD1: "NUMPAD1",
    wx.WXK_NUMPAD2: "NUMPAD2",
    wx.WXK_NUMPAD3: "NUMPAD3",
    wx.WXK_NUMPAD4: "NUMPAD4",
    wx.WXK_NUMPAD5: "NUMPAD5",
    wx.WXK_NUMPAD6: "NUMPAD6",
    wx.WXK_NUMPAD7: "NUMPAD7",
    wx.WXK_NUMPAD8: "NUMPAD8",
    wx.WXK_NUMPAD9: "NUMPAD9",
    wx.WXK_MULTIPLY: "MULTIPLY",
    wx.WXK_ADD: "ADD",
    wx.WXK_SEPARATOR: "SEPARATOR",
    wx.WXK_SUBTRACT: "SUBTRACT",
    wx.WXK_DECIMAL: "DECIMAL",
    wx.WXK_DIVIDE: "DIVIDE",
    wx.WXK_F1: "F1",
    wx.WXK_F2: "F2",
    wx.WXK_F3: "F3",
    wx.WXK_F4: "F4",
    wx.WXK_F5: "F5",
    wx.WXK_F6: "F6",
    wx.WXK_F7: "F7",
    wx.WXK_F8: "F8",
    wx.WXK_F9: "F9",
    wx.WXK_F10: "F10",
    wx.WXK_F11: "F11",
    wx.WXK_F12: "F12",
    wx.WXK_F13: "F13",
    wx.WXK_F14: "F14",
    wx.WXK_F15: "F15",
    wx.WXK_F16: "F16",
    wx.WXK_F17: "F17",
    wx.WXK_F18: "F18",
    wx.WXK_F19: "F19",
    wx.WXK_F20: "F20",
    wx.WXK_F21: "F21",
    wx.WXK_F22: "F22",
    wx.WXK_F23: "F23",
    wx.WXK_F24: "F24",
    wx.WXK_NUMLOCK: "NUMLOCK",
    wx.WXK_SCROLL: "SCROLL",
    wx.WXK_NUMPAD_SPACE: "NUMPAD_SPACE",
    wx.WXK_NUMPAD_TAB: "NUMPAD_TAB",
    wx.WXK_NUMPAD_ENTER: "NUMPAD_ENTER",
    wx.WXK_NUMPAD_F1: "NUMPAD_F1",
    wx.WXK_NUMPAD_F2: "NUMPAD_F2",
    wx.WXK_NUMPAD_F3: "NUMPAD_F3",
    wx.WXK_NUMPAD_F4: "NUMPAD_F4",
    wx.WXK_NUMPAD_HOME: "NUMPAD_HOME",
    wx.WXK_NUMPAD_LEFT: "NUMPAD_LEFT",
    wx.WXK_NUMPAD_UP: "NUMPAD_UP",
    wx.WXK_NUMPAD_RIGHT: "NUMPAD_RIGHT",
    wx.WXK_NUMPAD_DOWN: "NUMPAD_DOWN",
    wx.WXK_NUMPAD_PAGEUP: "NUMPAD_PAGEUP",
    wx.WXK_NUMPAD_PAGEDOWN: "NUMPAD_PAGEDOWN",
    wx.WXK_NUMPAD_END: "NUMPAD_END",
    wx.WXK_NUMPAD_BEGIN: "NUMPAD_BEGIN",
    wx.WXK_NUMPAD_INSERT: "NUMPAD_INSERT",
    wx.WXK_NUMPAD_DELETE: "NUMPAD_DELETE",
    wx.WXK_NUMPAD_EQUAL: "NUMPAD_EQUAL",
    wx.WXK_NUMPAD_MULTIPLY: "NUMPAD_MULTIPLY",
    wx.WXK_NUMPAD_ADD: "NUMPAD_ADD",
    wx.WXK_NUMPAD_SEPARATOR: "NUMPAD_SEPARATOR",
    wx.WXK_NUMPAD_SUBTRACT: "NUMPAD_SUBTRACT",
    wx.WXK_NUMPAD_DECIMAL: "NUMPAD_DECIMAL",
    wx.WXK_NUMPAD_DIVIDE: "NUMPAD_DIVIDE",
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
        else:
            key = f"UNKNOWN KEY {key}"
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


def stringify_key(key: SerialisedKeyType) -> str:
    return " + ".join([str(s) for s in key[0] + (key[1],)])


class KeyCatcher(wx.Dialog):
    def __init__(self, parent: wx.Window, action: str):
        super().__init__(parent, title=f"Press the key you want assigned to {action}")

        self._key = ((), 'NONE')

        self.Bind(wx.EVT_LEFT_DOWN, self._on_key)
        self.Bind(wx.EVT_MIDDLE_DOWN, self._on_key)
        self.Bind(wx.EVT_RIGHT_DOWN, self._on_key)
        self.Bind(wx.EVT_KEY_DOWN, self._on_key)
        self.Bind(wx.EVT_MOUSEWHEEL, self._on_key)

    def _on_key(self, evt):
        key = serialise_key_event(evt)
        if key is not None:
            self._key = key
            self.EndModal(1)

    @property
    def key(self) -> SerialisedKeyType:
        return self._key


class KeyConfigDialog(SimpleDialog):
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
            1,
            wx.EXPAND
        )
        self.Layout()
        self.Fit()

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
        self._choice.Bind(wx.EVT_CHOICE, self._on_group_change)
        top_sizer.Add(self._choice, 1, wx.ALL | wx.EXPAND, 5)

        add = wx.BitmapButton(parent, bitmap=ADD)
        add.Bind(wx.EVT_BUTTON, lambda evt: self._create_new_group())
        top_sizer.Add(add, 0, wx.ALL, 5)

        self._delete = wx.BitmapButton(parent, bitmap=SUBTRACT)
        self._delete.Bind(wx.EVT_BUTTON, lambda evt: self._delete_group())
        top_sizer.Add(self._delete, 0, wx.ALL, 5)

        self._rename = wx.BitmapButton(parent, bitmap=EDIT)
        self._rename.Bind(wx.EVT_BUTTON, lambda evt: self._rename_group())
        top_sizer.Add(self._rename, 0, wx.ALL, 5)

        self._options = SimpleScrollablePanel(parent, size=(500, 500))
        self.Add(self._options, 1, wx.EXPAND)

        grid_sizer = wx.GridSizer(len(entries), 2, 5, 5)
        self._options.sizer.Add(grid_sizer, 0, wx.ALL | wx.EXPAND, 5)
        self._key_buttons: Dict[str, wx.Button] = {}
        for action in entries:
            grid_sizer.Add(
                wx.StaticText(self._options, label=action.title()),
                0, wx.ALIGN_CENTER
            )
            self._key_buttons[action] = button = wx.Button(self._options)
            button.Bind(wx.EVT_BUTTON, lambda evt, a=action: self._modify_button(a))
            grid_sizer.Add(button, 0, wx.EXPAND)
        self._rebuild_buttons()

    def _rebuild_buttons(self):
        group_id = self._choice.GetCurrentString()
        if group_id in self._fixed_keybinds:
            group = self._fixed_keybinds[group_id]
            self._delete.Disable()
            self._rename.Disable()
        else:
            group = self._user_keybinds[group_id]
            self._delete.Enable()
            self._rename.Enable()

        for action in self._entries:
            self._key_buttons[action].SetLabel(
                stringify_key(
                    group.get(action, ((), 'NONE'))
                )
            )

    def _rebuild_choice(self, group_name=None):
        index = self._choice.GetSelection()
        self._choice.SetItems(
            list(self._fixed_keybinds.keys()) + list(self._user_keybinds.keys())
        )
        if group_name is not None:
            self._choice.SetSelection(self._choice.FindString(group_name))
        else:
            self._choice.SetSelection(max(index-1, 0))
        self._rebuild_buttons()

    def _delete_group(self):
        group = self._choice.GetCurrentString()
        if group in self._user_keybinds:
            del self._user_keybinds[group]
            self._rebuild_choice()

    def _request_group_name(self) -> Optional[str]:
        group_name = ""
        while group_name == "":
            msg = wx.TextEntryDialog(
                self._options,
                "Enter a new group name."
            )
            if msg.ShowModal() == wx.ID_OK:
                group_name = msg.GetValue()
                if group_name in self._fixed_keybinds or group_name in self._user_keybinds:
                    group_name = ""
            else:
                return
        return group_name

    def _rename_group(self):
        old_group_name = self._choice.GetCurrentString()
        if old_group_name in self._user_keybinds:
            group_name = self._request_group_name()
            if group_name is None:
                return
            group = self._user_keybinds[old_group_name]
            del self._user_keybinds[old_group_name]
            self._user_keybinds[group_name] = group
            self._rebuild_choice(group_name)

    def _create_new_group(self):
        group_name = self._request_group_name()
        if group_name is None:
            return
        old_group_name = self._choice.GetCurrentString()
        if old_group_name in self._fixed_keybinds:
            group = self._fixed_keybinds[old_group_name]
        else:
            group = self._user_keybinds[old_group_name]
        self._user_keybinds[group_name] = group.copy()
        self._rebuild_choice(group_name)

    def _modify_button(self, action):
        if self._choice.GetCurrentString() in self._fixed_keybinds:
            msg = wx.MessageDialog(
                self._options,
                "The active key group is not editable. Would you like to create a new group to edit?",
                style=wx.YES_NO,
            )
            if msg.ShowModal() == wx.ID_YES:
                self._create_new_group()
            else:
                return
        group_name = self._choice.GetCurrentString()
        if group_name in self._user_keybinds:
            catcher = KeyCatcher(self._options, action)
            catcher.ShowModal()
            self._user_keybinds[group_name][action] = catcher.key
            self._rebuild_buttons()

    def _on_group_change(self, evt):
        self._rebuild_buttons()

    @property
    def options(self) -> Tuple[KeybindContainer, KeybindGroupIdType, KeybindGroup]:
        keybind_group = self._choice.GetCurrentString()
        if keybind_group in self._fixed_keybinds:
            keybinds = self._fixed_keybinds[keybind_group]
        else:
            keybinds = self._user_keybinds[keybind_group]
        return self._user_keybinds, keybind_group, keybinds
