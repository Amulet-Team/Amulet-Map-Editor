import wx
from typing import TYPE_CHECKING, Optional
import webbrowser

from amulet_map_editor import CONFIG
from amulet_map_editor.programs import BaseWorldProgram, MenuData
from amulet_map_editor.amulet_wx.key_config import KeyConfigDialog


from .canvas.edit_canvas import EditCanvas
from .key_config import DefaultKeybindGroupId, PresetKeybinds, KeybindKeys

if TYPE_CHECKING:
    from amulet.api.world import World

EDIT_CONFIG_ID = "amulet_edit"


class EditExtension(wx.Panel, BaseWorldProgram):
    def __init__(self, parent, world: "World"):
        wx.Panel.__init__(self, parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)
        self._world = world
        self._canvas: Optional[EditCanvas] = None
        self._temp = wx.StaticText(self, label="Please wait while the renderer loads")
        self._temp.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        self._sizer.Add(self._temp)

        self.Bind(wx.EVT_SIZE, self._on_resize)

    def enable(self):
        if self._canvas is None:
            self.Update()

            self._canvas = EditCanvas(self, self._world)
            self._sizer.Add(self._canvas, 1, wx.EXPAND)

            self._temp.Destroy()

            self.Layout()
        self._canvas.Update()
        self._canvas.enable()
        self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        self._canvas.draw()

    def disable(self):
        if self._canvas is not None:
            self._canvas.disable()

    def close(self):
        self.disable()
        if self._canvas is not None:
            self._canvas.close()

    def is_closeable(self):
        if self._canvas is not None:
            return self._canvas.is_closeable() and not bool(
                self._world.chunk_history_manager.unsaved_changes
            )
        return not bool(self._world.chunk_history_manager.unsaved_changes)

    def _close_world(self, _):
        unsaved_changes = self._world.chunk_history_manager.unsaved_changes
        if unsaved_changes:
            msg = wx.MessageDialog(
                self,
                f"There {'is' if unsaved_changes == 1 else 'are'} {unsaved_changes} unsaved change{'s' if unsaved_changes >= 2 else ''}. Would you like to save?",
                style=wx.YES_NO | wx.CANCEL | wx.CANCEL_DEFAULT,
            )
            response = msg.ShowModal()
            if response == wx.ID_YES:
                self._canvas.save()
            elif response == wx.ID_CANCEL:
                return
        self.GetGrandParent().GetParent().close_world(self._world.world_path)

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault("&File", {}).setdefault("system", {}).setdefault(
            "Save\tCtrl+s", lambda evt: self._canvas.save()
        )
        # menu.setdefault('&File', {}).setdefault('system', {}).setdefault('Save As', lambda evt: self.GetGrandParent().close_world(self.world.world_path))
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Undo\tCtrl+z", lambda evt: self._canvas.undo()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Redo\tCtrl+y", lambda evt: self._canvas.redo()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Cut\tCtrl+x", lambda evt: self._canvas.cut()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Copy\tCtrl+c", lambda evt: self._canvas.copy()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Paste\tCtrl+v", lambda evt: self._canvas.paste()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Delete\tDelete", lambda evt: self._canvas.delete()
        )
        menu.setdefault("&Edit", {}).setdefault("shortcut", {}).setdefault(
            "Goto\tCtrl+g", lambda evt: self._canvas.goto()
        )
        menu.setdefault("&Options", {}).setdefault("options", {}).setdefault(
            "Controls...", lambda evt: self._edit_controls()
        )
        menu.setdefault("&Help", {}).setdefault("help", {}).setdefault(
            "Controls", lambda evt: self._help_controls()
        )
        return menu

    def _edit_controls(self):
        edit_config = CONFIG.get(EDIT_CONFIG_ID, {})
        keybind_id = edit_config.get("keybind_group", DefaultKeybindGroupId)
        user_keybinds = edit_config.get("user_keybinds", {})
        key_config = KeyConfigDialog(self, keybind_id, KeybindKeys, PresetKeybinds, user_keybinds)
        if key_config.ShowModal() == wx.ID_OK:
            user_keybinds, keybind_id, keybinds = key_config.options
            edit_config["user_keybinds"] = user_keybinds
            edit_config["keybind_group"] = keybind_id
            CONFIG.put(EDIT_CONFIG_ID, edit_config)
            self._canvas.set_key_binds(keybinds)

    @staticmethod
    def _help_controls():
        webbrowser.open(
            "https://github.com/Amulet-Team/Amulet-Map-Editor/blob/master/amulet_map_editor/programs/edit/readme.md"
        )

    def _on_resize(self, event):
        if self._canvas is not None:
            self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        event.Skip()

    # TODO
    # def _cut(self) -> bool:
    #     return self._run_operation(os.path.join(os.path.dirname(plugins.__file__), 'internal_operations', 'cut.py'))
    #
    # def _copy(self) -> bool:
    #     return self._run_operation(os.path.join(os.path.dirname(plugins.__file__), 'internal_operations', 'copy.py'))
    #
    # def _paste(self) -> bool:
    #     self.show_operation_options(None)
    #     return self._run_operation(os.path.join(os.path.dirname(plugins.__file__), 'internal_operations', 'paste.py'))
    #
    # def _delete(self) -> bool:
    #     return self._run_operation(os.path.join(os.path.dirname(plugins.__file__), 'internal_operations', 'delete.py'))

    # def show_select_options(self, _):
    #     self._operation_options.Hide()
    #     self._select_options.enable()
    #     self.Layout()

    # def _show_operation_options(self, enable: Callable):
    #     self._select_options.Hide()
    #     enable()
    #     self.Layout()

    # def show_operation_options(self, _):
    #     self._show_operation_options(self._operation_options.enable_operation_ui)
    #
    # def show_import_options(self, _):
    #     self._show_operation_options(self._operation_options.enable_import_ui)
    #
    # def show_export_options(self, _):
    #     self._show_operation_options(self._operation_options.enable_export_ui)
