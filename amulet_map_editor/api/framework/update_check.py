from __future__ import annotations

import urllib.request
import threading
import json
import webbrowser
import wx

from amulet_map_editor import lang
from amulet_map_editor.api.version import Version

URL = "http://api.github.com/repos/Amulet-Team/Amulet-Map-Editor/releases"

_EVT_UPDATE_CHECK = wx.NewEventType()
EVT_UPDATE_CHECK = wx.PyEventBinder(_EVT_UPDATE_CHECK, 1)


class UpdateEvent(wx.PyCommandEvent):
    def __init__(self, etype, eid, new_version: str):
        wx.PyCommandEvent.__init__(self, etype, eid)
        self._new_version = new_version

    def GetVersion(self) -> str:
        return self._new_version


class CheckForUpdate(threading.Thread):
    def __init__(self, url, current_version, parent):
        threading.Thread.__init__(self)
        self.url = url
        self.current_version = current_version
        self._parent = parent
        self._new_version = None

    def run(self):
        try:
            conn = urllib.request.urlopen(self.url, timeout=5)
            data = conn.read()
            data = json.loads(data)
            try:
                current_version = Version.from_string(self.current_version)
            except Exception:
                return

            for release_version, release_data in sorted(
                map(lambda d: (Version.from_string(d["tag_name"]), d), data),
                key=lambda t: t[0],
                reverse=True,
            ):
                if (
                    release_version > current_version
                    and release_version.release_stage >= current_version.release_stage
                ):
                    self._new_version = release_data["tag_name"]
                    break

            if self._new_version:
                evt = UpdateEvent(_EVT_UPDATE_CHECK, -1, self._new_version)
                wx.PostEvent(self._parent, evt)
        except Exception:
            pass


class UpdateDialog(wx.Dialog):
    def __init__(self, parent, current_version: str, new_version: str):
        wx.Dialog.__init__(self, parent)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        static_text_1 = wx.StaticText(
            self, label=lang.get("update_check.newer_version_released")
        )
        static_text_2 = wx.StaticText(
            self, label=f"{lang.get('update_check.new_version')} v{new_version}"
        )
        static_text_3 = wx.StaticText(
            self, label=f"{lang.get('update_check.current_version')} v{current_version}"
        )

        sizer_1.Add(static_text_1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_1.Add(static_text_2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_1.Add(static_text_3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        update_button = wx.Button(self, label=lang.get("update_check.update"))
        ok_button = wx.Button(self, label=lang.get("update_check.ok"))

        sizer_2.Add(update_button, 0, wx.ALL, 5)
        sizer_2.Add((0, 0), 1, wx.EXPAND, 5)
        sizer_2.Add(ok_button, 0, wx.ALL, 5)

        sizer_1.Add(sizer_2, 1, wx.EXPAND, 5)

        self.SetSizerAndFit(sizer_1)

        self.Centre()

        update_button.Bind(
            wx.EVT_BUTTON, lambda evt: self.goto_download_page(new_version, evt)
        )
        ok_button.Bind(wx.EVT_BUTTON, lambda evt: self.Close())

    @staticmethod
    def goto_download_page(new_version, _):
        webbrowser.open(
            f"https://github.com/Amulet-Team/Amulet-Map-Editor/releases/tag/{new_version}"
        )


def show_update_window(parent, current_version: str, evt: UpdateEvent):
    if Version.from_string(current_version).has_commit_hash:
        print("Running from source, not showing update dialog")
        return
    UpdateDialog(parent, current_version, evt.GetVersion()).ShowModal()


def check_for_update(version, listening_parent):
    update_thread = CheckForUpdate(URL, version, listening_parent)
    update_thread.start()
