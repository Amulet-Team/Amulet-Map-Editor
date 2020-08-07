from __future__ import annotations

import urllib.request
import threading
import json
import re
import webbrowser

import wx

URL = "http://api.github.com/repos/Amulet-Team/Amulet-Map-Editor/releases"
TAG_REGEX = re.compile(
    r"^v(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)\.(?P<bugfix>\d+)$"
)
VERSION_REGEX = re.compile(
    r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)\.(?P<bugfix>\d+)$"
)

_EVT_UPDATE_CHECK = wx.NewEventType()
EVT_UPDATE_CHECK = wx.PyEventBinder(_EVT_UPDATE_CHECK, 1)


class ReleaseStageFilter:
    @staticmethod
    def pre_release_stage(d):
        return d["prerelease"]

    @staticmethod
    def release_stage(d):
        return not d["prerelease"]


class UpdateEvent(wx.PyCommandEvent):
    def __init__(self, etype, eid, new_version):
        wx.PyCommandEvent.__init__(self, etype, eid)
        self._new_version = new_version

    def GetVersion(self):
        return self._new_version


class CheckForUpdate(threading.Thread):
    def __init__(self, url, current_version, parent, release_stage):
        threading.Thread.__init__(self)
        self.url = url
        self.current_version = current_version
        self._parent = parent
        self._release_stage = release_stage
        self.data = None

    def run(self):
        try:
            conn = urllib.request.urlopen(self.url, timeout=5)
            data = conn.read()
            data = json.loads(data)
            version_match = VERSION_REGEX.match(self.current_version)
            if not version_match:
                return

            for release in data:
                match = TAG_REGEX.match(release["tag_name"])
                if not match:
                    continue
                tag_tuple = tuple(map(int, match.groups()))
                version_tuple = tuple(map(int, version_match.groups()))

                if not self._release_stage(release):
                    continue

                if tag_tuple > version_tuple:
                    self.data = (True, tag_tuple)
                    break

            if self.data[0]:
                evt = UpdateEvent(_EVT_UPDATE_CHECK, -1, self.data[1])
                wx.PostEvent(self._parent, evt)
        except Exception:
            pass


class UpdateDialog(wx.Dialog):
    def __init__(self, parent, current_version, new_version):
        wx.Dialog.__init__(self, parent)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        static_text_1 = wx.StaticText(
            self, label="A new version of Amulet has been released!"
        )
        static_text_2 = wx.StaticText(self, label=f"New Version: v{new_version}")
        static_text_3 = wx.StaticText(self, label=f"Your Version: v{current_version}")

        sizer_1.Add(static_text_1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_1.Add(static_text_2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_1.Add(static_text_3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        update_button = wx.Button(self, label="Go to Download Page")
        ok_button = wx.Button(self, label="Ok")

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

    def goto_download_page(self, new_version, _):
        webbrowser.open(
            f"https://github.com/Amulet-Team/Amulet-Map-Editor/releases/tag/v{new_version}"
        )


def show_update_window(parent, current_version, evt):
    new_version = ".".join(map(str, evt.GetVersion()))
    UpdateDialog(parent, current_version, new_version).ShowModal()


def check_for_update(
    version, listening_parent, release_stage=ReleaseStageFilter.pre_release_stage
):
    update_thread = CheckForUpdate(URL, version, listening_parent, release_stage)
    update_thread.start()
