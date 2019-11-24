from __future__ import annotations

import wx
import traceback

import amulet
from amulet import world_interface
import amulet_nbt as nbt
import PyMCTranslate


class WorldSelectionDialog(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 450))
        self._world_dir = None
        self._create_ui()
        self.Show(True)

    def _create_ui(self):
        main_panel = wx.Panel(self)
        self._world_dir_label = wx.StaticText(main_panel, label="", pos=(25, 5))
        open_world_button = wx.Button(main_panel, label="Select World", pos=(0, 30))
        open_world_button.Bind(wx.EVT_BUTTON, self._choose_world)

        open_world_button = wx.Button(main_panel, label="Open World", pos=(115, 30))
        open_world_button.Bind(wx.EVT_BUTTON, self._click_open_world_button)

    def _choose_world(self, evt):
        dir_dialog = wx.DirDialog(None, "Choose world directory", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        try:
            if dir_dialog.ShowModal() == wx.ID_CANCEL:
                return
            self._world_dir = dir_dialog.GetPath()
            self._world_dir_label.Label = self._world_dir
        except Exception:
            wx.LogError('Failed to open directory!')
            raise
        finally:
            dir_dialog.Destroy()

    def _click_open_world_button(self, evt):
        self.Hide()
        world_window = WorldEditDialog(self, self._world_dir)


class WorldEditDialog(wx.Frame):
    def __init__(self, parent, world_path):
        try:
            self._world = world_interface.load_world(world_path)
        except Exception as e:
            traceback.print_exc()
            parent.Show(True)
            return
        wx.Frame.__init__(self, parent, title=world_path, size=(500, 450))
        self._create_ui()
        self.Bind(wx.EVT_CLOSE, self._exit)
        self.Show(True)

    def _create_ui(self):
        main_panel = wx.Panel(self)
        self._operation = wx.ComboBox(main_panel, choices=[
                                    'convert to other world'
                                 ],
                                      style=wx.CB_READONLY
                                      )
        self._operation.SetSelection(0)

        run_operation = wx.Button(main_panel, label="Run Operation", pos=(0, 30))
        run_operation.Bind(wx.EVT_BUTTON, self._run_operation)

        save_button = wx.Button(main_panel, label="Save World", pos=(0, 65))
        save_button.Bind(wx.EVT_BUTTON, self._save)

    def _run_operation(self, evt):
        mode = self._operation.GetStringSelection()
        if mode == 'convert to other world':
            dir_dialog = wx.DirDialog(None, "Choose other world directory", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
            try:
                if dir_dialog.ShowModal() == wx.ID_CANCEL:
                    return
                other_world_path = dir_dialog.GetPath()
            except Exception:
                wx.LogError('Failed to open directory!')
                return
            finally:
                dir_dialog.Destroy()

            try:
                other_format = world_interface.load_format(other_world_path)
            except:
                return

            self._world.save(other_format)
            print('Finished saving world')

    def _save(self, evt):
        self._world.save()

    def _exit(self, evt):
        self._world.close()
        self.Parent.Show()
        self.Destroy()


if __name__ == '__main__':
    app = wx.App(False)
    frame = WorldSelectionDialog(None, "Amulet Map Editor Alpha")
    app.MainLoop()
