import wx
from amulet_map_editor.amulet_wx.simple import SimpleDialog, SimpleScrollablePanel
from typing import Dict, Tuple, Optional, Any, Union

ModifierKeyType = int
KeyType = int
ModifierType = Tuple[ModifierKeyType, ...]
SerialisedKeyType = Tuple[ModifierType, KeyType]

_modifier_keys = {wx.WXK_CONTROL}


def serialise_key_event(evt: Union[wx.KeyEvent, wx.MouseEvent]) -> Optional[SerialisedKeyType]:
    modifier = []
    if isinstance(evt, wx.KeyEvent):
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
    elif isinstance(evt, wx.MouseEvent):
        key = evt.GetEventType()
        if key in wx.EVT_MOUSEWHEEL.evtType:
            if evt.GetWheelRotation() < 0:
                key *= -1
    else:
        return
    return tuple(modifier), int(key)


class KeyConfigModal(SimpleDialog):
    def __init__(self, parent: wx.Window, title='Key Select'):
        super().__init__(parent, title)
        self.sizer.Add(
            KeyConfig(parent)
        )


class KeyConfig(SimpleScrollablePanel):
    def __init__(self, parent: wx.Window):
        super().__init__(parent)

    @property
    def options(self) -> Dict[
        str,
        SerialisedKeyType
    ]:
        return {}


