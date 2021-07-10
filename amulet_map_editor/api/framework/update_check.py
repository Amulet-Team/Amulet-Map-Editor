from __future__ import annotations

import urllib.request
import threading
import json
import re
import webbrowser
from dataclasses import dataclass

import wx

from amulet_map_editor import lang

URL = "http://api.github.com/repos/Amulet-Team/Amulet-Map-Editor/releases"
VERSION_REGEX = re.compile(
    r"^v?(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)((b(?P<beta>\d+)(\.dev(?P<devnum>\d{12}))?)|(a(?P<alpha>\d+)))?(.*\.g(?P<commit_hash>[a-z\d]{7}))?"
)

_EVT_UPDATE_CHECK = wx.NewEventType()
EVT_UPDATE_CHECK = wx.PyEventBinder(_EVT_UPDATE_CHECK, 1)

FULL_RELEASE = 0
BETA_RELEASE = -1
ALPHA_RELEASE = -2


@dataclass
class Version:
    release_stage: int
    major: int
    minor: int
    patch: int
    alpha_number: int = -1
    beta_number: int = -1
    nightly_timestamp: int = -1
    has_commit_hash: bool = False

    def __gt__(self, other: Version):
        if self.version_tuple > other.version_tuple:
            return True
        if self.release_stage > other.release_stage:
            return True
        if self.release_stage == other.release_stage:
            if self.release_stage == -2:
                return self.alpha_number > other.alpha_number
            elif self.release_stage == -1:
                if self.beta_number > other.beta_number:
                    return True
                elif self.beta_number == other.beta_number and self.beta_number != -1:
                    return self.nightly_timestamp > other.nightly_timestamp
        return False

    @property
    def version_tuple(self):
        return self.major, self.minor, self.patch


def get_version(version_string: str) -> Version:
    """Parse the version into a more usable format

    :param version_string: The version string. Eg 1.2 or 1.2.3.4 or 1.2.3.4b0
    :return: (<release stage identifier>, (major, minor, patch)) beta will not exist if it is not a beta
    """
    version_match = VERSION_REGEX.match(version_string)
    if version_match:
        v = version_match.groupdict()
        major, minor, patch = int(v["major"]), int(v["minor"]), int(v["patch"])
        version = Version(FULL_RELEASE, major, minor, patch)

        if v.get("alpha") is not None:
            version.release_stage = ALPHA_RELEASE
            version.alpha_number = int(v["alpha"])
        elif v.get("beta") is not None:
            version.release_stage = BETA_RELEASE
            version.beta_number = int(v["beta"])
            if v.get("devnum") is not None:
                version.nightly_timestamp = int(v["devnum"])

        if v.get("commit_hash") is not None:
            version.has_commit_hash = True
        return version

    raise Exception(f"Invalid version string {version_string}")


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
                current_version = get_version(self.current_version)
            except Exception:
                return

            for release_version, release_data in sorted(
                map(lambda d: (get_version(d["tag_name"]), d), data),
                key=lambda t: t[0],
                reverse=True,
            ):
                if release_version > current_version:
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
    if get_version(current_version).has_commit_hash:
        print("Running from source, not showing update dialog")
        return
    UpdateDialog(parent, current_version, evt.GetVersion()).ShowModal()


def check_for_update(version, listening_parent):
    update_thread = CheckForUpdate(URL, version, listening_parent)
    update_thread.start()
