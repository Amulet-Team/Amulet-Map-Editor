import os
import glob
import base64
import secrets
import shutil
import hashlib
import wx
from threading import Thread
import webbrowser
import logging
from typing import TYPE_CHECKING, Optional

from amulet import load_format
from amulet.api.level import BaseLevel

from amulet_map_editor import lang
from amulet_map_editor.api.wx.ui.simple import SimpleScrollablePanel
from amulet_map_editor.api.wx.ui.select_world import (
    minecraft_world_paths,
    get_world_image,
    world_images,
)
from amulet_map_editor.api.datatypes import MenuData
from amulet_map_editor.api.framework.programs import BaseProgram

if TYPE_CHECKING:
    from amulet.api.wrapper import WorldFormatWrapper

log = logging.getLogger(__name__)


class _WorldSummaryPanel(wx.Panel):
    def __init__(self, parent: wx.Window):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self._image = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(1, 1))
        sizer.Add(self._image, 0, wx.ALIGN_CENTER)

        self._name = wx.StaticText(self, wx.ID_ANY, "")
        name_font = self._name.GetFont()
        name_font.SetPointSize(max(10, name_font.GetPointSize() + 1))
        self._name.SetFont(name_font)
        sizer.Add(self._name, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 8)

        self._path = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_READONLY)
        sizer.Add(self._path, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 6)

    def set_data(self, image: wx.Bitmap, title: str, path: str):
        self._image.SetBitmap(image)
        self._name.SetLabel(title)
        self._path.SetValue(path)


class ConvertExtension(SimpleScrollablePanel, BaseProgram):
    _did_missing_icon_repair = False

    def __init__(self, container, world: BaseLevel):
        super().__init__(container)
        self._thread: Optional[Thread] = None
        self.world = world
        self._source_wrapper = self.world.level_wrapper
        self._source_platform = self._normalise_platform(self._source_wrapper.platform)
        self._target_platform = "java" if self._source_platform == "bedrock" else "bedrock"

        self._target_worlds = self._discover_target_worlds()
        self._target_worlds_by_label = {
            self._world_choice_label(wrapper): wrapper for wrapper in self._target_worlds
        }
        self._target_base_dir = self._find_target_base_directory()
        self._new_world_directory_name: Optional[str] = None
        self._repair_global_missing_icon_if_corrupted()

        root = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(root)

        progress_row = wx.BoxSizer(wx.HORIZONTAL)
        root.Add(progress_row, 0, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 12)

        self._progress_gauge = wx.Gauge(
            self,
            wx.ID_ANY,
            100,
            style=wx.GA_HORIZONTAL,
        )
        self._progress_gauge.SetValue(0)
        progress_row.Add(self._progress_gauge, 1, wx.EXPAND | wx.RIGHT, 8)

        self._progress_status = wx.StaticText(self, wx.ID_ANY, "Idle")
        progress_row.Add(self._progress_status, 0, wx.ALIGN_CENTER_VERTICAL)

        self._title = wx.StaticText(
            self,
            wx.ID_ANY,
            f"Convert {self._platform_title(self._source_platform)} -> {self._platform_title(self._target_platform)}",
        )
        title_font = self._title.GetFont()
        title_font.SetPointSize(max(12, title_font.GetPointSize() + 3))
        title_font.MakeBold()
        self._title.SetFont(title_font)
        root.Add(self._title, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.BOTTOM, 12)

        options_sizer = wx.BoxSizer(wx.VERTICAL)
        root.Add(options_sizer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 12)

        new_row = wx.BoxSizer(wx.HORIZONTAL)
        options_sizer.Add(new_row, 0, wx.BOTTOM, 8)
        self._new_world_radio = wx.RadioButton(self, wx.ID_ANY, "New World", style=wx.RB_GROUP)
        new_row.Add(self._new_world_radio, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        self._new_world_name = wx.TextCtrl(
            self,
            wx.ID_ANY,
            value=self._source_wrapper.level_name,
            size=wx.Size(240, -1),
        )
        new_row.Add(self._new_world_name, 0, wx.ALIGN_CENTER_VERTICAL)

        existing_row = wx.BoxSizer(wx.HORIZONTAL)
        options_sizer.Add(existing_row, 0)
        self._existing_world_radio = wx.RadioButton(self, wx.ID_ANY, "Existing World")
        existing_row.Add(self._existing_world_radio, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        self._existing_world_choice = wx.Choice(
            self,
            wx.ID_ANY,
            choices=list(self._target_worlds_by_label.keys()),
            size=wx.Size(240, -1),
        )
        if self._existing_world_choice.GetCount() > 0:
            self._existing_world_choice.SetSelection(0)
        existing_row.Add(self._existing_world_choice, 0, wx.ALIGN_CENTER_VERTICAL)

        views_sizer = wx.BoxSizer(wx.HORIZONTAL)
        root.Add(views_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        self._left_world_panel = _WorldSummaryPanel(self)
        views_sizer.Add(self._left_world_panel, 45, wx.EXPAND | wx.ALL, 6)

        arrow = wx.StaticText(self, wx.ID_ANY, "->")
        arrow_font = arrow.GetFont()
        arrow_font.SetPointSize(max(14, arrow_font.GetPointSize() + 6))
        arrow.SetFont(arrow_font)
        views_sizer.Add(arrow, 10, wx.ALIGN_CENTER | wx.ALL, 6)

        self._right_world_panel = _WorldSummaryPanel(self)
        views_sizer.Add(self._right_world_panel, 45, wx.EXPAND | wx.ALL, 6)

        self.convert_button = wx.Button(self, wx.ID_ANY, label="Convert")
        root.Add(self.convert_button, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.BOTTOM, 14)

        self._new_world_name.Bind(wx.EVT_TEXT, self._on_target_option_changed)
        self._new_world_radio.Bind(wx.EVT_RADIOBUTTON, self._on_target_option_changed)
        self._existing_world_radio.Bind(wx.EVT_RADIOBUTTON, self._on_target_option_changed)
        self._existing_world_choice.Bind(wx.EVT_CHOICE, self._on_target_option_changed)
        self.convert_button.Bind(wx.EVT_BUTTON, self._convert_event)

        if self._target_worlds:
            self._existing_world_radio.SetValue(True)
            self._new_world_radio.SetValue(False)
        else:
            self._new_world_radio.SetValue(True)
            self._existing_world_radio.SetValue(False)
            self._existing_world_radio.Disable()
            self._existing_world_choice.Disable()

        source_img = get_world_image(self._source_wrapper.world_image_path)[0]
        source_title = (
            f"{self._source_wrapper.level_name} "
            f"({self._platform_title(self._source_platform)})"
        )
        self._left_world_panel.set_data(source_img, source_title, self._source_wrapper.path)
        self._refresh_target_view()

    @staticmethod
    def _normalise_platform(platform_name: str) -> str:
        return str(platform_name).strip().lower()

    @staticmethod
    def _platform_title(platform_name: str) -> str:
        return "Java" if platform_name == "java" else "Bedrock"

    @staticmethod
    def _path_platform(path: str) -> Optional[str]:
        path_norm = path.replace("\\", "/").lower()
        if path_norm.endswith("/.minecraft/saves"):
            return "java"
        if "minecraftworlds" in path_norm:
            return "bedrock"
        return None

    def _discover_target_worlds(self):
        worlds_by_path = {}
        for _, directory in minecraft_world_paths:
            if not os.path.isdir(directory):
                continue
            for world_path in glob.glob(os.path.join(glob.escape(directory), "*")):
                if not os.path.isdir(world_path):
                    continue
                try:
                    world_format = load_format(world_path)
                except Exception:
                    continue
                if os.path.normcase(world_format.path) == os.path.normcase(self.world.level_path):
                    continue
                if self._normalise_platform(world_format.platform) != self._target_platform:
                    continue
                worlds_by_path[world_format.path] = world_format

        return sorted(
            worlds_by_path.values(),
            key=lambda wrapper: wrapper.level_name.lower(),
        )

    def _world_choice_label(self, wrapper) -> str:
        return (
            f"{wrapper.level_name} "
            f"({self._platform_title(self._normalise_platform(wrapper.platform))})"
        )

    def _find_target_base_directory(self) -> Optional[str]:
        for _, directory in minecraft_world_paths:
            if not os.path.isdir(directory):
                continue
            if self._path_platform(directory) == self._target_platform:
                return directory
        return None

    def _selected_existing_world(self):
        selection = self._existing_world_choice.GetStringSelection()
        return self._target_worlds_by_label.get(selection)

    def _new_world_path(self) -> Optional[str]:
        world_name = self._new_world_name.GetValue().strip()
        if not world_name:
            return None

        target_base_dir = self._preferred_target_base_directory()
        if not target_base_dir:
            return None

        if self._target_platform == "bedrock":
            directory_name = self._ensure_new_world_directory_name()
            if not directory_name:
                return None
            return os.path.join(target_base_dir, directory_name)

        return os.path.join(target_base_dir, world_name)

    def _preferred_target_base_directory(self) -> Optional[str]:
        selected_world = self._selected_existing_world()
        if selected_world is not None:
            return os.path.dirname(selected_world.path)

        if self._target_worlds:
            return os.path.dirname(self._target_worlds[0].path)

        return self._target_base_dir

    def _generate_bedrock_directory_name(self) -> str:
        target_base_dir = self._preferred_target_base_directory()
        if not target_base_dir:
            raise RuntimeError("Could not determine Bedrock world base directory.")

        while True:
            token = base64.urlsafe_b64encode(secrets.token_bytes(12)).decode("ascii")
            candidate = os.path.join(target_base_dir, token)
            if not os.path.exists(candidate):
                return token

    def _ensure_new_world_directory_name(self) -> Optional[str]:
        if self._target_platform != "bedrock":
            return None

        if self._new_world_directory_name is None:
            self._new_world_directory_name = self._generate_bedrock_directory_name()
        return self._new_world_directory_name

    def _refresh_target_view(self):
        new_mode = self._new_world_radio.GetValue()
        self._new_world_name.Enable(new_mode)
        self._existing_world_choice.Enable(not new_mode and self._existing_world_choice.GetCount() > 0)

        source_img = get_world_image(self._source_wrapper.world_image_path)[0]

        if new_mode:
            new_name = self._new_world_name.GetValue().strip() or self._source_wrapper.level_name
            out_path = self._new_world_path() or ""
            title = f"{new_name} ({self._platform_title(self._target_platform)})"
            self._right_world_panel.set_data(source_img, title, out_path)
            return

        wrapper = self._selected_existing_world()
        if wrapper is None:
            self._right_world_panel.set_data(source_img, "", "")
            return
        target_img = get_world_image(wrapper.world_image_path)[0]
        target_title = (
            f"{wrapper.level_name} "
            f"({self._platform_title(self._normalise_platform(wrapper.platform))})"
        )
        self._right_world_panel.set_data(target_img, target_title, wrapper.path)

    def _on_target_option_changed(self, _):
        self._refresh_target_view()

    def _invalidate_world_image_cache(self, world_path: str):
        try:
            wrapper = load_format(world_path)
            world_images.pop(wrapper.world_image_path, None)
        except Exception:
            return

    def _refresh_existing_world_choices(
        self,
        preferred_path: Optional[str] = None,
        invalidate_world_path: Optional[str] = None,
    ):
        if invalidate_world_path:
            self._invalidate_world_image_cache(invalidate_world_path)

        self._target_worlds = self._discover_target_worlds()
        self._target_worlds_by_label = {
            self._world_choice_label(wrapper): wrapper for wrapper in self._target_worlds
        }

        labels = list(self._target_worlds_by_label.keys())
        previous_selection = self._existing_world_choice.GetStringSelection()
        self._existing_world_choice.SetItems(labels)

        selected_index = wx.NOT_FOUND
        if preferred_path:
            for index, label in enumerate(labels):
                wrapper = self._target_worlds_by_label[label]
                if wrapper.path == preferred_path:
                    selected_index = index
                    break

        if selected_index == wx.NOT_FOUND and previous_selection in labels:
            selected_index = labels.index(previous_selection)
        if selected_index == wx.NOT_FOUND and labels:
            selected_index = 0

        if selected_index != wx.NOT_FOUND:
            self._existing_world_choice.SetSelection(selected_index)

        if labels:
            self._existing_world_radio.Enable()
            if not self._new_world_radio.GetValue():
                self._existing_world_choice.Enable()
        else:
            self._existing_world_choice.Disable()

        self._refresh_target_view()

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault(lang.get("menu_bar.help.menu_name"), {}).setdefault(
            "control", {}
        ).setdefault(
            lang.get("program_convert.menu_bar.help.user_guide"),
            lambda evt: self._help_controls(),
        )
        return menu

    def _help_controls(self):
        webbrowser.open(
            "https://github.com/Amulet-Team/Amulet-Map-Editor/blob/master/amulet_map_editor/programs/convert/readme.md"
        )

    def _update_loading_bar(self, chunk_index, chunk_total):
        if chunk_total <= 0:
            return
        value = int(max(0, min(100, (100 * chunk_index) / chunk_total)))
        wx.CallAfter(self._progress_gauge.SetValue, value)

    @staticmethod
    def _is_missing_icon_path(icon_path: Optional[str]) -> bool:
        if not icon_path:
            return True
        return os.path.basename(icon_path).lower() == "missing_world_icon.png"

    @staticmethod
    def _file_sha256(file_path: str) -> Optional[str]:
        try:
            hasher = hashlib.sha256()
            with open(file_path, "rb") as file:
                for chunk in iter(lambda: file.read(1024 * 1024), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception:
            return None

    def _find_missing_icon_path(self) -> Optional[str]:
        candidates = [self._source_wrapper, *self._target_worlds]
        for wrapper in candidates:
            icon_path = getattr(wrapper, "world_image_path", None)
            if self._is_missing_icon_path(icon_path):
                return icon_path
        return None

    def _repair_global_missing_icon_if_corrupted(self):
        if ConvertExtension._did_missing_icon_repair:
            return

        missing_icon_path = self._find_missing_icon_path()
        if not missing_icon_path or not os.path.isfile(missing_icon_path):
            return

        missing_hash = self._file_sha256(missing_icon_path)
        if missing_hash is None:
            return

        candidates = [self._source_wrapper, *self._target_worlds]
        matching_world_icon = False
        for wrapper in candidates:
            icon_path = getattr(wrapper, "world_image_path", None)
            if not icon_path or self._is_missing_icon_path(icon_path):
                continue
            if not os.path.isfile(icon_path):
                continue
            world_hash = self._file_sha256(icon_path)
            if world_hash == missing_hash:
                matching_world_icon = True
                break

        if not matching_world_icon:
            return

        try:
            bitmap = wx.Bitmap(128, 128)
            dc = wx.MemoryDC(bitmap)
            dc.SetBackground(wx.Brush(wx.Colour(90, 90, 90)))
            dc.Clear()
            dc.SetBrush(wx.Brush(wx.Colour(120, 120, 120)))
            dc.SetPen(wx.Pen(wx.Colour(120, 120, 120)))
            dc.DrawRectangle(0, 0, 64, 64)
            dc.DrawRectangle(64, 64, 64, 64)
            dc.SelectObject(wx.NullBitmap)
            bitmap.SaveFile(missing_icon_path, wx.BITMAP_TYPE_PNG)
            world_images.pop(missing_icon_path, None)
            ConvertExtension._did_missing_icon_repair = True
            log.info("Repaired corrupted global missing world icon file.")
        except Exception:
            log.warning("Failed to repair global missing world icon file.", exc_info=True)

    def _target_icon_path(self, out_world: "WorldFormatWrapper") -> Optional[str]:
        world_platform = self._normalise_platform(out_world.platform)
        if world_platform == "java":
            return os.path.join(out_world.path, "icon.png")
        if world_platform == "bedrock":
            return os.path.join(out_world.path, "world_icon.jpeg")
        return None

    def _copy_source_icon_to_target(self, out_world: "WorldFormatWrapper"):
        try:
            source_icon = self._source_wrapper.world_image_path
            target_icon = self._target_icon_path(out_world)
            if not source_icon or not target_icon:
                return
            if self._is_missing_icon_path(source_icon):
                return
            if not os.path.isfile(source_icon):
                return

            os.makedirs(os.path.dirname(target_icon), exist_ok=True)
            shutil.copy2(source_icon, target_icon)
        except Exception:
            log.warning("Failed to copy world icon to converted world.", exc_info=True)

    def _create_new_world_wrapper(self, out_world_path: str):
        if os.path.exists(out_world_path) and os.path.isdir(out_world_path):
            if next(os.scandir(out_world_path), None) is not None:
                raise RuntimeError("The destination directory must be empty for new world conversion.")

        template = self._selected_existing_world() or (self._target_worlds[0] if self._target_worlds else None)
        if template is None:
            raise RuntimeError(
                f"No discovered {self._platform_title(self._target_platform)} world exists to use as a format template."
            )

        wrapper = template.__class__(out_world_path)
        wrapper.create_and_open(self._target_platform, template.version, None, False)

        new_world_name = self._new_world_name.GetValue().strip()
        if new_world_name:
            wrapper.level_name = new_world_name

        return wrapper

    def _output_world_path(self) -> Optional[str]:
        if self._new_world_radio.GetValue():
            return self._new_world_path()
        selected = self._selected_existing_world()
        return selected.path if selected is not None else None

    def _convert_event(self, evt):
        out_world_path = self._output_world_path()
        if not out_world_path:
            wx.MessageBox("Please select a destination world or enter a new world name.")
            return
        if out_world_path == self.world.level_path:
            wx.MessageBox(lang.get("program_convert.input_output_must_different"))
            return

        self.convert_button.Disable()
        self._progress_gauge.SetValue(0)
        self._progress_status.SetLabel("Converting...")
        self._thread = Thread(
            target=self._convert_method,
            args=(out_world_path, self._new_world_radio.GetValue()),
            daemon=True,
        )
        self._thread.start()

    def _convert_method(self, out_world_path: str, create_new_world: bool):
        out_world = None
        conversion_succeeded = False
        try:
            if create_new_world:
                out_world = self._create_new_world_wrapper(out_world_path)
            else:
                out_world = load_format(out_world_path)
                out_world.open()

            log.info(f"Converting world {self.world.level_path} to {out_world.path}")
            out_world: WorldFormatWrapper
            self.world.save(out_world, self._update_loading_bar)
            self._copy_source_icon_to_target(out_world)
            out_world.save()
            out_world.close()
            wx.CallAfter(self._progress_gauge.SetValue, 100)
            wx.CallAfter(self._progress_status.SetLabel, "Done")
            conversion_succeeded = True
            message = lang.get("program_convert.conversion_completed")
            log.info(
                f"Finished converting world {self.world.level_path} to {out_world.path}"
            )
        except Exception as e:
            message = f"Error during conversion\n{e}"
            log.error(message, exc_info=True)

            if out_world is not None:
                try:
                    out_world.close()
                except Exception:
                    pass

        wx.CallAfter(self.convert_button.Enable)
        if not conversion_succeeded:
            wx.CallAfter(self._progress_gauge.SetValue, 0)
            wx.CallAfter(self._progress_status.SetLabel, "Failed")
        if conversion_succeeded:
            if create_new_world and self._target_platform == "bedrock":
                self._new_world_directory_name = None
            wx.CallAfter(
                self._refresh_existing_world_choices,
                out_world_path if create_new_world else None,
                out_world_path,
            )
        self._thread = None
        wx.CallAfter(wx.MessageBox, message)

    def can_close(self):
        if self._thread is not None:
            log.info(
                f"World {self.world.level_path} is still being converted. Please let it finish before closing"
            )
            return False
        return True
