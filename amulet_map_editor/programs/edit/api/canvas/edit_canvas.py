import wx
from typing import Callable

from amulet.api.level.world import World
from amulet_map_editor import CONFIG

from .base_edit_canvas import BaseEditCanvas
from ...edit import EDIT_CONFIG_ID
from ..key_config import (
    DefaultKeys,
    DefaultKeybindGroupId,
    PresetKeybinds,
)


class EditCanvas(BaseEditCanvas):
    def __init__(self, parent: wx.Window, world: "World", close_callback: Callable):
        super().__init__(parent, world)
        self._close_callback = close_callback

        config_ = CONFIG.get(EDIT_CONFIG_ID, {})
        user_keybinds = config_.get("user_keybinds", {})
        group = config_.get("keybind_group", DefaultKeybindGroupId)
        if group in user_keybinds:
            keybinds = user_keybinds[group]
        elif group in PresetKeybinds:
            keybinds = PresetKeybinds[group]
        else:
            keybinds = DefaultKeys
        for action_id, (modifier_keys, trigger_key) in keybinds.items():
            self.buttons.register_action(action_id, trigger_key, modifier_keys)
