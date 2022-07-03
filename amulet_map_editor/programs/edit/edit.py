import wx
from typing import TYPE_CHECKING, Optional, Callable
import webbrowser

EDIT_CONFIG_ID = "amulet_edit"

from amulet_map_editor import log, lang
from amulet_map_editor.api.framework.programs import BaseProgram
from amulet_map_editor.api.datatypes import MenuData
from amulet_map_editor.api.wx.util.key_config import KeyConfigDialog
from amulet_map_editor.api.wx.ui.simple import SimpleDialog
from amulet_map_editor.programs.edit.api.canvas.edit_canvas import EditCanvas
from amulet_map_editor.programs.edit.api.key_config import (
    DefaultKeybindGroupId,
    PresetKeybinds,
    KeybindKeys,
)
from amulet_map_editor.api import config

if TYPE_CHECKING:
    from amulet.api.level import World


class EditExtension(wx.Panel, BaseProgram):
    def __init__(self, parent, world: "World", close_self_callback: Callable[[], None]):
        wx.Panel.__init__(self, parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetBackgroundColour(
            tuple(int(v * 255) for v in EditCanvas.background_colour)
        )
        self.SetSizer(self._sizer)
        self._world = world
        self._canvas: Optional[EditCanvas] = None
        self._close_self_callback = close_self_callback

        self._sizer.AddStretchSpacer(1)
        self._temp_msg = wx.StaticText(
            self, label=lang.get("program_3d_edit.canvas.please_wait")
        )
        self._temp_msg.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        self._sizer.Add(self._temp_msg, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
        self._temp_loading_bar = wx.Gauge(self, range=10000)
        self._sizer.Add(self._temp_loading_bar, 0, flag=wx.EXPAND)
        self._sizer.AddStretchSpacer(1)

    def enable(self):
        if self._canvas is None:
            self.Update()

            self._canvas = EditCanvas(self, self._world, self._close_self_callback)
            for arg in self._canvas.setup():
                if isinstance(arg, (int, float)):
                    self._temp_loading_bar.SetValue(int(min(arg, 1) * 10000))
                elif (
                    isinstance(arg, tuple)
                    and isinstance(arg[0], (int, float))
                    and isinstance(arg[1], str)
                ):
                    self._temp_loading_bar.SetValue(int(min(arg[0], 1) * 10000))
                    self._temp_msg.SetLabel(arg[1])
                self.Layout()
                self.Update()
                wx.Yield()

            edit_config: dict = config.get(EDIT_CONFIG_ID, {})
            self._canvas.camera.perspective_fov = edit_config.get("options", {}).get(
                "fov", 70.0
            )
            if self._canvas.camera.perspective_fov > 180:
                self._canvas.camera.perspective_fov = 70.0
            self._canvas.renderer.render_distance = edit_config.get("options", {}).get(
                "render_distance", 5
            )
            self._canvas.camera.rotate_speed = edit_config.get("options", {}).get(
                "camera_sensitivity", 2.0
            )

            self._sizer.Clear(True)
            self._sizer.Add(self._canvas, 1, wx.EXPAND)
            self._canvas.Show()

            self.Layout()
        self._canvas.Update()
        self._canvas.enable()

    def disable(self):
        if self._canvas is not None:
            self._canvas.disable()

    def close(self):
        """Fully close the UI. Called when destroying the UI."""
        if self._canvas is not None:
            self._canvas.close()

    def is_closeable(self) -> bool:
        """
        Check if it is safe to close the UI.
        :return: True if the program can be closed, False otherwise
        """
        if self._canvas is None:
            # if the edit program has never been opened then it can be closed
            return True
        else:
            if self._canvas.is_closeable():
                return self._check_close_world()
            log.info(
                f"The canvas in edit for world {self._world.level_wrapper.level_name} was not closeable for some reason."
            )
            return False

    def _check_close_world(self) -> bool:
        """
        Check if it is safe to close the world and prompt the user if it is not.
        :return: True if the world can be closed, False otherwise
        """
        unsaved_changes = self._world.history_manager.unsaved_changes
        if unsaved_changes:
            msg = wx.MessageDialog(
                self,
                f"""There {
                'is' if unsaved_changes == 1 else 'are'
                } {unsaved_changes} unsaved change{
                's' if unsaved_changes >= 2 else ''
                } in {
                self._world.level_wrapper.level_name
                }. Would you like to save?""",
                style=wx.YES_NO | wx.CANCEL | wx.CANCEL_DEFAULT,
            )
            response = msg.ShowModal()
            if response == wx.ID_YES:
                self._canvas.save()
                return True
            elif response == wx.ID_NO:
                return True
            elif response == wx.ID_CANCEL:
                log.info(
                    f"""Aborting closing world {
                    self._world.level_wrapper.level_name
                    } because the user pressed cancel."""
                )
                return False
        return True

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault(lang.get("menu_bar.file.menu_name"), {}).setdefault(
            "system", {}
        ).setdefault(
            f"{lang.get('program_3d_edit.menu_bar.file.save')}\tCtrl+s",
            lambda evt: self._canvas.save(),
        )
        # menu.setdefault(lang.get('menu_bar.file.menu_name'), {}).setdefault('system', {}).setdefault('Save As', lambda evt: self.GetGrandParent().close_world(self.world.world_path))

        menu.setdefault(
            lang.get("program_3d_edit.menu_bar.edit.menu_name"), {}
        ).setdefault("history", {}).update(
            {
                f"{lang.get('program_3d_edit.menu_bar.edit.undo')}\tCtrl+z": lambda evt: self._canvas.undo(),
                f"{lang.get('program_3d_edit.menu_bar.edit.redo')}\tCtrl+y": lambda evt: self._canvas.redo(),
            }
        )

        menu.setdefault(
            lang.get("program_3d_edit.menu_bar.edit.menu_name"), {}
        ).setdefault("operation", {}).update(
            {
                f"{lang.get('program_3d_edit.menu_bar.edit.cut')}\tCtrl+x": lambda evt: self._canvas.cut(),
                f"{lang.get('program_3d_edit.menu_bar.edit.copy')}\tCtrl+c": lambda evt: self._canvas.copy(),
                f"{lang.get('program_3d_edit.menu_bar.edit.paste')}\tCtrl+v": lambda evt: self._canvas.paste_from_cache(),
                f"{lang.get('program_3d_edit.menu_bar.edit.delete')}\tDelete": lambda evt: self._canvas.delete(),
            }
        )

        menu.setdefault(
            lang.get("program_3d_edit.menu_bar.edit.menu_name"), {}
        ).setdefault("shortcut", {}).update(
            {
                f"{lang.get('program_3d_edit.menu_bar.edit.goto')}\tCtrl+g": lambda evt: self._canvas.goto(),
                f"{lang.get('program_3d_edit.menu_bar.edit.select_all')}\tCtrl+A": lambda evt: self._canvas.select_all(),
            }
        )

        menu.setdefault(lang.get("menu_bar.options.menu_name"), {}).setdefault(
            "options", {}
        ).setdefault(
            lang.get("program_3d_edit.menu_bar.options.controls"),
            lambda evt: self._edit_controls(),
        )
        menu.setdefault(lang.get("menu_bar.options.menu_name"), {}).setdefault(
            "options", {}
        ).setdefault(
            lang.get("program_3d_edit.menu_bar.options.options"),
            lambda evt: self._edit_options(),
        )
        menu.setdefault(lang.get("menu_bar.help.menu_name"), {}).setdefault(
            "help", {}
        ).setdefault(
            lang.get("program_3d_edit.menu_bar.help.user_guide"),
            lambda evt: self._help_controls(),
        )
        return menu

    def _edit_controls(self):
        edit_config = config.get(EDIT_CONFIG_ID, {})
        keybind_id = edit_config.get("keybind_group", DefaultKeybindGroupId)
        user_keybinds = edit_config.get("user_keybinds", {})
        key_config = KeyConfigDialog(
            self, keybind_id, KeybindKeys, PresetKeybinds, user_keybinds
        )
        if key_config.ShowModal() == wx.ID_OK:
            user_keybinds, keybind_id, keybinds = key_config.options
            edit_config["user_keybinds"] = user_keybinds
            edit_config["keybind_group"] = keybind_id
            config.put(EDIT_CONFIG_ID, edit_config)
            self._canvas.buttons.clear_registered_actions()
            self._canvas.buttons.register_actions(keybinds)

    def _edit_options(self):
        if self._canvas is not None:
            fov = self._canvas.camera.perspective_fov
            render_distance = self._canvas.renderer.render_distance
            camera_sensitivity = self._canvas.camera.rotate_speed
            dialog = SimpleDialog(self, "Options")

            sizer = wx.FlexGridSizer(3, 2, 0, 0)
            dialog.sizer.Add(sizer, flag=wx.ALL, border=5)
            fov_ui = wx.SpinCtrlDouble(dialog, min=0, max=180, initial=fov)

            def set_fov(evt):
                self._canvas.camera.perspective_fov = fov_ui.GetValue()

            fov_ui.Bind(wx.EVT_SPINCTRLDOUBLE, set_fov)
            sizer.Add(
                wx.StaticText(dialog, label="Field of View"),
                flag=wx.LEFT | wx.TOP | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                border=5,
            )
            sizer.Add(
                fov_ui,
                flag=wx.LEFT | wx.TOP | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                border=5,
            )

            render_distance_ui = wx.SpinCtrl(
                dialog, min=0, max=50, initial=render_distance
            )

            def set_render_distance(evt):
                self._canvas.renderer.render_distance = render_distance_ui.GetValue()

            render_distance_ui.Bind(wx.EVT_SPINCTRL, set_render_distance)
            sizer.Add(
                wx.StaticText(dialog, label="Render Distance"),
                flag=wx.LEFT | wx.TOP | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                border=5,
            )
            sizer.Add(
                render_distance_ui,
                flag=wx.LEFT | wx.TOP | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                border=5,
            )

            camera_sensitivity_ui = wx.SpinCtrlDouble(
                dialog, min=0, max=10, initial=camera_sensitivity
            )

            def set_camera_sensitivity(evt):
                self._canvas.camera.rotate_speed = camera_sensitivity_ui.GetValue()

            camera_sensitivity_ui.Bind(wx.EVT_SPINCTRLDOUBLE, set_camera_sensitivity)
            sizer.Add(
                wx.StaticText(dialog, label="Camera Sensitivity"),
                flag=wx.LEFT | wx.TOP | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                border=5,
            )
            sizer.Add(
                camera_sensitivity_ui,
                flag=wx.LEFT | wx.TOP | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND,
                border=5,
            )

            dialog.Fit()

            response = dialog.ShowModal()
            if response == wx.ID_OK:
                edit_config: dict = config.get(EDIT_CONFIG_ID, {})
                edit_config.setdefault("options", {})
                edit_config["options"]["fov"] = fov_ui.GetValue()
                edit_config["options"][
                    "render_distance"
                ] = render_distance_ui.GetValue()
                edit_config["options"][
                    "camera_sensitivity"
                ] = camera_sensitivity_ui.GetValue()
                config.put(EDIT_CONFIG_ID, edit_config)
            elif response == wx.ID_CANCEL:
                self._canvas.camera.perspective_fov = fov
                self._canvas.renderer.render_distance = render_distance
                self._canvas.camera.rotate_speed = camera_sensitivity

    @staticmethod
    def _help_controls():
        webbrowser.open(
            "https://github.com/Amulet-Team/Amulet-Map-Editor/blob/master/amulet_map_editor/programs/edit/readme.md"
        )
