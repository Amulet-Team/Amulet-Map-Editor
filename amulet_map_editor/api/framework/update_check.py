from __future__ import annotations

from typing import Optional
import urllib.request
import threading
import json
import webbrowser
import logging

import wx
from packaging.version import Version

from amulet_map_editor import lang

URL = "http://api.github.com/repos/Amulet-Team/Amulet-Map-Editor/releases"

_EVT_UPDATE_CHECK = wx.NewEventType()
EVT_UPDATE_CHECK = wx.PyEventBinder(_EVT_UPDATE_CHECK, 1)

log = logging.getLogger(__name__)


class UpdateEvent(wx.PyCommandEvent):
    def __init__(self, etype, eid, new_version: str):
        wx.PyCommandEvent.__init__(self, etype, eid)
        self._new_version = new_version

    def GetVersion(self) -> str:
        return self._new_version


class UpdateDialog(wx.Dialog):
    def __init__(self, parent, current_version: str, new_version: str):
        super().__init__(parent)

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


def _is_compatible(current_version: Version, release_version: Version) -> bool:
    """The release version is only compatible with the current version if it is newer and more stable."""

    # release > beta > beta.dev > alpha.dev
    #                > alpha > alpha.dev
    def get_release_stage(version: Version) -> int:
        if version.pre is None:
            return 3
        else:
            return {"a": 0, "b": 1, "rc": 2}[version.pre[0]]

    return (
        # The release version is newer than the current version
        release_version > current_version
        # the pre-release stage is newer or the same
        and get_release_stage(release_version) >= get_release_stage(current_version)
        # dev builds should only be suggested if the current version is a dev build
        and (release_version.dev is None or current_version.dev is not None)
    )


def _get_newest_version(url: str, current_version_str: str) -> Optional[str]:
    """Find a newer but compatible release than this one if one exists."""

    try:
        current_version = Version(current_version_str)

        if current_version.local is not None:
            # if the version has a local extension (eg. "+0.gee5780.dirty")
            log.info("Running from source, not showing update dialog")
            return

        conn = urllib.request.urlopen(url, timeout=5)
        data = conn.read()
        data = json.loads(data)

        # iterate through all release versions starting with the newest
        for release_version, release_data in sorted(
            map(lambda d: (Version(d["tag_name"]), d), data),
            key=lambda t: t[0],
            reverse=True,
        ):
            if _is_compatible(current_version, release_version):
                return str(release_version)

    except Exception:
        pass


def _check_for_update(
    listening_parent: wx.EvtHandler, url: str, current_version_str: str
):
    """Check if there is a newer release and post an UpdateEvent if there is."""
    release_version = _get_newest_version(url, current_version_str)
    if release_version is not None:
        evt = UpdateEvent(_EVT_UPDATE_CHECK, -1, str(release_version))
        wx.PostEvent(listening_parent, evt)


def check_for_update(listening_parent: wx.EvtHandler, current_version_str: str):
    update_thread = threading.Thread(
        target=_check_for_update, args=(listening_parent, URL, current_version_str)
    )
    update_thread.start()
