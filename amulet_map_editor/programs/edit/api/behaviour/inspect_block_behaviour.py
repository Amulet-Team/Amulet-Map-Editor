from typing import TYPE_CHECKING
import logging

import wx
from amulet.api.chunk.biomes import BiomesShape
from amulet.api.errors import ChunkDoesNotExist

from amulet_map_editor.api.wx.util.button_input import InputReleaseEvent
from amulet_map_editor import lang
from .base_behaviour import BaseBehaviour
from .pointer_behaviour import PointerBehaviour
from ..events import (
    InputPressEvent,
    EVT_INPUT_PRESS,
    EVT_INPUT_RELEASE,
)
from ..key_config import (
    ACT_INSPECT_BLOCK,
)

if TYPE_CHECKING:
    from ..canvas import EditCanvas

log = logging.getLogger(__name__)


class InspectWidget(wx.PopupWindow):
    def __init__(self, parent: wx.Window, *, wrap: int = 500) -> None:
        super().__init__(parent, wx.BORDER_SIMPLE)
        self._panel = wx.Panel(self)

        self._title = wx.StaticText(self._panel)
        self._title.SetFont(self._title.GetFont().Bold())
        self._title.SetLabel(lang.get("inspect.title"))

        self._wrap = wrap
        self._msg = wx.StaticText(self._panel)
        self._message_text = ""

        head = wx.BoxSizer(wx.HORIZONTAL)
        head.Add(self._title, 1, wx.ALIGN_CENTER_VERTICAL)
        body = wx.BoxSizer(wx.VERTICAL)
        body.Add(head, 0, wx.EXPAND | wx.BOTTOM, 4)
        body.Add(self._msg, 0, wx.EXPAND)
        outer = wx.BoxSizer(wx.VERTICAL)
        outer.Add(body, 1, wx.EXPAND | wx.ALL, 8)
        self._panel.SetSizer(outer)

    def set_message(self, msg: str) -> None:
        if msg == self._message_text:
            return
        self._message_text = msg
        self.Freeze()
        self._msg.SetLabel(msg)
        self._msg.Wrap(self._wrap)
        self._panel.Layout()
        size = self._panel.GetSizer().GetMinSize()
        self._panel.SetSize(size)
        self.SetClientSize(size)
        self.Refresh()
        self.Thaw()

    def ShowAt(self, point: wx.Point):
        """
        Show the tip intersecting the given point.
        Will adjust the position to ensure the tip is entirely on the screen.
        """
        display = wx.Display(max(wx.Display.GetFromPoint(point), 0)).GetClientArea()
        size = self.GetSize()

        if point.x + size.x <= display.GetRight():
            x = point.x + 20
        else:
            x = point.x - size.x - 20

        if point.y + size.y <= display.GetBottom():
            y = point.y + 20
        else:
            y = max(point.y - size.y - 20, display.GetTop())

        rect = wx.Rect(wx.Point(x, y), size)
        self.SetRect(rect)

        if not self.IsShown():
            self.Show()
            self.Raise()


class InspectBlockBehaviour(BaseBehaviour):
    """Adds a popup with block information."""

    def __init__(self, canvas: "EditCanvas", pointer_behaviour: PointerBehaviour):
        super().__init__(canvas)
        self._pointer_behaviour = pointer_behaviour
        self._tool_tip = InspectWidget(self.canvas)
        self._inspect_pressed = False

    def bind_events(self) -> None:
        """Set up all events required to run."""
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)
        self.canvas.Bind(EVT_INPUT_RELEASE, self._on_input_release)
        self.canvas.Bind(wx.EVT_MOTION, self._motion)
        self.canvas.Bind(wx.EVT_LEAVE_WINDOW, self._hide_gui)

    def _show_gui(self) -> None:
        msg = self._get_block_info_message()
        self._tool_tip.set_message(msg)
        if self.canvas.mouse.locked:
            rect = self.canvas.GetScreenRect()
            position = wx.Point(rect.x + rect.width // 2, rect.y + rect.height // 2)
        else:
            position = wx.GetMousePosition()
        self._tool_tip.ShowAt(position)

    def _motion(self, evt: wx.MouseEvent) -> None:
        if self._inspect_pressed:
            self._show_gui()
        elif self._tool_tip.IsShown():
            self._tool_tip.Hide()
        evt.Skip()

    def _on_input_press(self, evt: InputPressEvent):
        """Logic to run each time the input press event is run."""
        if evt.action_id == ACT_INSPECT_BLOCK:
            if not self._tool_tip.IsShown():
                self._show_gui()
            self._inspect_pressed = True
        evt.Skip()

    def _on_input_release(self, evt: InputReleaseEvent):
        if evt.action_id == ACT_INSPECT_BLOCK:
            self._inspect_pressed = False
            self._tool_tip.Hide()
        evt.Skip()

    def _hide_gui(self, evt: wx.MouseEvent) -> None:
        if self._tool_tip.IsShown():
            window = wx.FindWindowAtPoint(self.canvas.ClientToScreen(evt.GetPosition()))
            if window is None:
                self._inspect_pressed = False
            else:
                if window is self.canvas:
                    evt.Skip()
                    return
                top_window = window.GetTopLevelParent()
                if top_window is not self._tool_tip:
                    self._inspect_pressed = False
            self._tool_tip.Hide()
        evt.Skip()

    def _get_block_info_message(self) -> str:
        try:
            x, y, z = self._pointer_behaviour.pointer_base
            block = self.canvas.world.get_block(x, y, z, self.canvas.dimension)
            chunk = self.canvas.world.get_chunk(x >> 4, z >> 4, self.canvas.dimension)
            block_entity = chunk.block_entities.get((x, y, z), None)
            platform = self.canvas.world.level_wrapper.platform
            version = self.canvas.world.level_wrapper.version
            translator = self.canvas.world.translation_manager.get_version(
                platform,
                version,
            )
            (
                version_block,
                version_block_entity,
                _,
            ) = translator.block.from_universal(
                block, block_entity, block_location=(x, y, z)
            )
            if isinstance(version, tuple):
                version_str = ".".join(str(v) for v in version[:4])
            else:
                version_str = str(version)
            block_data_text = f"x: {x}, y: {y}, z: {z}\n\n{platform.capitalize()} {version_str}\n{version_block}"
            if version_block_entity:
                version_block_entity_str = str(version_block_entity)
                block_data_text = f"{block_data_text}\n{version_block_entity_str}"

            block_data_text = f"{block_data_text}\n\nUniversal\n{block}"
            if block_entity:
                block_entity_str = str(block_entity)
                block_data_text = f"{block_data_text}\n{block_entity_str}"

            if chunk.biomes.dimension == BiomesShape.Shape2D:
                biome = chunk.biomes[x % 16, z % 16]
                try:
                    block_data_text = f"{block_data_text}\n\n{lang.get('inspect.biome')}: {self.canvas.world.biome_palette[biome]}"
                except Exception as e:
                    log.error(e)
            elif chunk.biomes.dimension == BiomesShape.Shape3D:
                biome = chunk.biomes[(x % 16) // 4, y // 4, (z % 16) // 4]
                try:
                    block_data_text = f"{block_data_text}\n\n{lang.get('inspect.biome')}: {self.canvas.world.biome_palette[biome]}"
                except Exception as e:
                    log.error(e)

        except ChunkDoesNotExist:
            return "This chunk does not exist."
        except Exception as e:
            log.exception(e)
            return str(e)
        else:
            return block_data_text
