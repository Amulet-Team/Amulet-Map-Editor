from __future__ import annotations

from typing import Tuple
import urllib.request
import threading
import json
import re
import webbrowser
import os
import sys
import zipfile
import subprocess
import glob
import platform

import wx

from amulet_map_editor.api.logging import log

URL = "http://api.github.com/repos/Amulet-Team/Amulet-Map-Editor/releases"

UPDATER_DOWNLOAD_URL = "https://github.com/Podshot/AmuletUpdater/releases/download/latest/AmuletUpdater.zip"
JAVA_DOWNLOAD_URL = "https://download.java.net/java/GA/jdk14.0.2/205943a0976c4ed48cb16f1043c5c647/12/GPL/openjdk-14.0.2_windows-x64_bin.zip"

NOT_RUNNING_FROM_SOURCE = getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")
AUTOUPDATER_SUPPORTED_OS = platform.system() in ("Windows",)

VERSION_REGEX = re.compile(
    r"^v?(?P<major>\d+)\.(?P<minor>\d+)(\.(?P<patch>\d+))?(\.(?P<bugfix>\d+))?(b(?P<beta>\d+))?$"
)

_EVT_UPDATE_CHECK = wx.NewEventType()
EVT_UPDATE_CHECK = wx.PyEventBinder(_EVT_UPDATE_CHECK, 1)


def get_version(version_string: str) -> Tuple[bool, Tuple[int, ...]]:
    """Parse the version into a more usable format

    :param version_string: The version string. Eg 1.2 or 1.2.3.4 or 1.2.3.4b0
    :return: (bool(full_version), (major, minor, patch, bugfix, <beta>)) beta will not exist if it is not a beta
    """
    version_match = VERSION_REGEX.match(version_string)
    if version_match:
        v = version_match.groupdict()
        version = (
            int(v["major"]),
            int(v["minor"]),
            int(v["patch"] or 0),
            int(v["bugfix"] or 0),
        )
        if v["beta"] is None:
            # full release
            return (True, version)
        else:
            # beta release
            return (False, version + (int(v["beta"]),))

    raise Exception(f"Invalid version string {version_string}")


class UpdateEvent(wx.PyCommandEvent):
    def __init__(self, etype, eid, new_version: str, is_beta: bool):
        wx.PyCommandEvent.__init__(self, etype, eid)
        self._new_version = new_version
        self._is_beta = is_beta

    def GetVersion(self) -> str:
        return self._new_version

    def GetIsBeta(self) -> bool:
        return self._is_beta


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
            except Exception as e:
                return

            for release in data:
                try:
                    release_version = get_version(release["tag_name"])
                except Exception:
                    continue

                if current_version[0] == release_version[0]:
                    # if they are both full releases or betas
                    if release_version[1] > current_version[1]:
                        self._new_version = release["tag_name"]
                        break
                elif not current_version[0]:
                    # if current is beta
                    if release_version[0]:
                        release_version = (
                            release_version[0],
                            release_version[1] + (float("inf"),),
                        )
                    if release_version[1] > current_version[1]:
                        self._new_version = release["tag_name"]
                        break

            if self._new_version:
                evt = UpdateEvent(
                    _EVT_UPDATE_CHECK, -1, self._new_version, current_version[0]
                )
                wx.PostEvent(self._parent, evt)
        except Exception:
            pass


class DownloadFileThread(threading.Thread):
    def __init__(self, url, filepath, unpack_path):
        threading.Thread.__init__(self)
        self._url = url
        self._filepath = filepath
        self._unpack_path = unpack_path

    def run(self) -> None:
        urllib.request.urlretrieve(self._url, self._filepath)

        with zipfile.ZipFile(self._filepath, "r") as z_ref:
            z_ref.extractall(self._unpack_path)


class UpdateDialog(wx.Dialog):
    def __init__(self, parent, current_version: str, new_version: str, is_beta: bool):
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

        update_page_button = wx.Button(self, label="Go to Download Page")
        if NOT_RUNNING_FROM_SOURCE and AUTOUPDATER_SUPPORTED_OS:
            updater_button = wx.Button(self, label="Run Auto Updater")
        ok_button = wx.Button(self, label="Ok")

        sizer_2.Add(update_page_button, 0, wx.ALL, 5)
        sizer_2.Add((0, 0), 1, wx.EXPAND, 5)
        if NOT_RUNNING_FROM_SOURCE and AUTOUPDATER_SUPPORTED_OS:
            sizer_2.Add(updater_button, 0, wx.ALL, 5)
            sizer_2.Add((0, 0), 1, wx.EXPAND, 5)
        sizer_2.Add(ok_button, 0, wx.ALL, 5)

        sizer_1.Add(sizer_2, 1, wx.EXPAND, 5)

        self.SetSizerAndFit(sizer_1)

        self.Centre()

        update_page_button.Bind(
            wx.EVT_BUTTON, lambda evt: self.goto_download_page(new_version, evt)
        )
        if NOT_RUNNING_FROM_SOURCE and AUTOUPDATER_SUPPORTED_OS:
            updater_button.Bind(
                wx.EVT_BUTTON,
                lambda evt: self.auto_update(
                    current_version, new_version, is_beta, evt
                ),
            )
        ok_button.Bind(wx.EVT_BUTTON, lambda evt: self.Close())

    @staticmethod
    def goto_download_page(new_version, _):
        webbrowser.open(
            f"https://github.com/Amulet-Team/Amulet-Map-Editor/releases/tag/{new_version}"
        )

    @staticmethod
    def auto_update(current_version, target_version, is_beta, _):
        working_directory = os.path.dirname(sys.executable)
        temp_dir = os.path.join(working_directory, "updater-tmp")
        os.makedirs(temp_dir, exist_ok=True)

        updater_zip_path = os.path.join(temp_dir, "AmuletUpdater.zip")
        java_zip_path = os.path.join(temp_dir, "openjdk_14.0.2.zip")

        updater_download_thread = DownloadFileThread(
            UPDATER_DOWNLOAD_URL, updater_zip_path, temp_dir
        )
        java_download_thread = DownloadFileThread(
            JAVA_DOWNLOAD_URL, java_zip_path, temp_dir
        )

        java_download_thread.start()
        updater_download_thread.start()

        java_download_thread.join()
        updater_download_thread.join()

        jars = glob.glob(os.path.join(temp_dir, "*.jar"))
        updater_jar = jars[0]
        log.info(f"Using AmuletUpdater jar: {updater_jar}")
        args = [
            os.path.join(temp_dir, "jdk-14.0.2", "bin", "java.exe"),
            "-jar",
            updater_jar,
            "-current_version",
            current_version,
            "-target_version",
            target_version,
            "-wd",
            working_directory,
            "-pid",
            str(os.getpid()),
        ]

        if is_beta:
            args.append("-install_beta")

        p = subprocess.Popen(args, shell=True, cwd=temp_dir)


def show_update_window(parent, current_version: str, evt: UpdateEvent):
    UpdateDialog(parent, current_version, evt.GetVersion(), evt.GetIsBeta()).ShowModal()


def check_for_update(version, listening_parent):
    update_thread = CheckForUpdate(URL, version, listening_parent)
    update_thread.start()
