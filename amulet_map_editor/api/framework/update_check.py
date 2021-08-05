from __future__ import annotations

import urllib.request
import threading
import json
import re
import webbrowser
from dataclasses import dataclass
from enum import IntEnum

import wx

from amulet_map_editor import lang

URL = "http://api.github.com/repos/Amulet-Team/Amulet-Map-Editor/releases"

"""
VERSION_REGEX Documentation

    This is not a documentation of regular expression syntax, just documentation on the subsequences that this regular expression looks for
    For an in-depth guide on regular expressions, see here: https://www.debuggex.com/cheatsheet/regex/python
    
    Our version scheme allows for an optional "v" prefix, so that subsequence is tested by "v?"
    
    Since we use the Semantic Versioning scheme, our version numbers follow this format: <major>.<minor>.<patch>
    with the <patch> number being optional (only if it's value would be 0 for that version)
    That is tested by "(?P<major>\d+)\.(?P<minor>\d+)(\.(?P<patch>\d+))?"
    
    - For the major and minor numbers, "(?P<major>\d+)" will match any non-zero number of digits and group them under the
        "major" group (in this instance)
    - "\." will then match the separating "." character
    - Since the patch number is optional, "(\.(?P<patch>\d+))?" is used instead, the second "." is included in the 
        optional group, but other wise the capturing group is the same as the major/minor numbers
        
    We then use an optional release type flag to denote whether the release is a beta or alpha release and it's number:
    "((a(?P<alpha>\d+))|(b(?P<beta>\d+)))?"
    
    For our nightly builds, we also denote a unique build number with the prefix of ".dev": "(\.dev(?P<devnum>\d{12}))?"
    
    Finally, our version scheme also denotes when Amulet is being ran from source, while this information isn't
    necessarily used for update checking, we use it to determine if the update dialog should be shown. If a commit 
    hash/count is found in the version string of the current Amulet instance, the dialog is not shown. Our regular 
    expression uses the following to detect that subsequence: 
        "(\+(?P<commit_count>\d+)\.g(?P<commit_hash>[a-z\d]+)(\.dirty)?)?"
        
    - "commit_count" group signifies the number of commits since the last release
    - "commit_hash" group is the current commit hash
    - ".dirty" denotes whether uncommitted changes have been made 
"""
VERSION_REGEX = re.compile(
    r"^v?(?P<major>\d+)\.(?P<minor>\d+)(\.(?P<patch>\d+))?((a(?P<alpha>\d+))|(b(?P<beta>\d+)))?(\.dev(?P<devnum>\d{12}))?(\+(?P<commit_count>\d+)\.g(?P<commit_hash>[a-z\d]+)(\.dirty)?)?$"
)

_EVT_UPDATE_CHECK = wx.NewEventType()
EVT_UPDATE_CHECK = wx.PyEventBinder(_EVT_UPDATE_CHECK, 1)


class Release(IntEnum):
    FULL = 0
    BETA = -1
    ALPHA = -2


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
            if self.release_stage == Release.ALPHA:
                return self.alpha_number > other.alpha_number
            elif self.release_stage == Release.BETA:
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
    :return: A Version object from the parsed version string
    """
    version_match = VERSION_REGEX.match(version_string)
    if version_match:
        v = version_match.groupdict()
        major, minor = int(v["major"]), int(v["minor"])
        if v["patch"] is None:
            patch = 0
        else:
            patch = int(v["patch"])
        version = Version(Release.FULL, major, minor, patch)

        if v.get("alpha") is not None:
            version.release_stage = Release.ALPHA
            version.alpha_number = int(v["alpha"])
        elif v.get("beta") is not None:
            version.release_stage = Release.BETA
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
    if get_version(current_version).has_commit_hash:
        print("Running from source, not showing update dialog")
        return
    UpdateDialog(parent, current_version, evt.GetVersion()).ShowModal()


def check_for_update(version, listening_parent):
    update_thread = CheckForUpdate(URL, version, listening_parent)
    update_thread.start()
