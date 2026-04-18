from typing import Optional, Tuple, List, Callable
import wx
import re
import json
from pathlib import Path

from amulet.api.data_types import PointCoordinates

from amulet_map_editor import lang
from amulet_map_editor.api import image

CoordRegex = re.compile(
    r"^"  # match the start
    r"\s*"  # leading whitespace
    r"(?P<x>-?[0-9]+\.?[0-9]*)"  # the x coordinate
    r"((?:,\s*)|(?:\s+))"  # separator 1
    r"(?P<y>-?[0-9]+\.?[0-9]*)"  # the y coordinate
    r"((?:,\s*)|(?:\s+))"  # separator 2
    r"(?P<z>-?[0-9]+\.?[0-9]*)"  # the z coordinate
    r",?\s*"  # trailing comma and whitespace
    r"$"  # matches the end
)

MAX_MRU = 10
COORD_FIELD_WIDTH = 135
CoordParseRegex = re.compile(
    r"^\s*"
    r"(?:/?tp\s+)?"
    r"(?:x\s*[:=]\s*)?(?P<x>-?[0-9]+\.?[0-9]*)"
    r"(?:\s*,\s*|\s+)"
    r"(?:y\s*[:=]\s*)?(?P<y>-?[0-9]+\.?[0-9]*)"
    r"(?:\s*,\s*|\s+)"
    r"(?:z\s*[:=]\s*)?(?P<z>-?[0-9]+\.?[0-9]*)"
    r"\s*$",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# MRU helpers — importable from anywhere in the program
# ---------------------------------------------------------------------------

def _get_tp_path(world_path) -> Optional[Path]:
    """Return the .tp file path adjacent to the world folder/file."""
    if world_path is None:
        return None
    p = Path(str(world_path).rstrip("/\\"))
    return p.parent / (p.name + ".tp")


def load_mru(world_path) -> List[Tuple[float, float, float]]:
    """Load the MRU list for *world_path* from its .tp file."""
    tp_path = _get_tp_path(world_path)
    if tp_path is None or not tp_path.is_file():
        return []
    try:
        data = json.loads(tp_path.read_text(encoding="utf-8"))
        return [
            (float(e["x"]), float(e["y"]), float(e["z"]))
            for e in data.get("mru", [])
        ]
    except Exception:
        return []


def save_mru(world_path, entries: List[Tuple[float, float, float]]):
    """Save *entries* to the .tp file for *world_path*."""
    tp_path = _get_tp_path(world_path)
    if tp_path is None:
        return
    data = {"mru": [{"x": x, "y": y, "z": z} for x, y, z in entries]}
    try:
        tp_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception:
        pass


def add_mru_entry(world_path, x: float, y: float, z: float):
    """Add a coordinate to the MRU list for *world_path*.

    Deduplicated and capped at MAX_MRU entries.  Can be called from anywhere
    in the program to record a teleport without going through the dialog.
    """
    entries = load_mru(world_path)
    new_entry = (round(x, 2), round(y, 2), round(z, 2))
    entries = [e for e in entries if e != new_entry]
    entries.insert(0, new_entry)
    save_mru(world_path, entries[:MAX_MRU])


# ---------------------------------------------------------------------------
# Non-modal window
# ---------------------------------------------------------------------------

def show_goto(
    parent: wx.Window,
    x: float,
    y: float,
    z: float,
    world_path=None,
    on_goto: Optional[Callable[[float, float, float], None]] = None,
    title: Optional[str] = None,
) -> "GoTo":
    """Create and show the non-modal GoTo window, returning it."""
    if title is None:
        title = lang.get("program_3d_edit.goto_ui.title")
    win = GoTo(parent, title, (x, y, z), world_path, on_goto)
    win.Show()
    return win


class GoTo(wx.Frame):
    def __init__(
        self,
        parent: wx.Window,
        title: str,
        start: PointCoordinates,
        world_path=None,
        on_goto: Optional[Callable[[float, float, float], None]] = None,
    ):
        super().__init__(
            parent,
            title=title,
            style=wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX | wx.FRAME_FLOAT_ON_PARENT,
        )
        self._world_path = world_path
        self._on_goto_cb = on_goto
        x, y, z = start

        panel = wx.Panel(self)
        self._panel = panel
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(main_sizer)

        # ── Coordinate row with copy, paste and GO ────────────────────────
        coord_sizer = wx.BoxSizer(wx.HORIZONTAL)

        x_text = wx.StaticText(panel, label=lang.get("program_3d_edit.goto_ui.x_label"))
        self.x = wx.SpinCtrlDouble(
            panel, min=-30000000, max=30000000, initial=float(x)
        )
        self.x.SetToolTip(lang.get("program_3d_edit.goto_ui.x_label_tooltip"))
        self.x.SetDigits(2)
        self.x.SetMinSize((COORD_FIELD_WIDTH, -1))

        y_text = wx.StaticText(panel, label=lang.get("program_3d_edit.goto_ui.y_label"))
        self.y = wx.SpinCtrlDouble(
            panel, min=-30000000, max=30000000, initial=float(y)
        )
        self.y.SetToolTip(lang.get("program_3d_edit.goto_ui.y_label_tooltip"))
        self.y.SetDigits(2)
        self.y.SetMinSize((COORD_FIELD_WIDTH, -1))

        z_text = wx.StaticText(panel, label=lang.get("program_3d_edit.goto_ui.z_label"))
        self.z = wx.SpinCtrlDouble(
            panel, min=-30000000, max=30000000, initial=float(z)
        )
        self.z.SetToolTip(lang.get("program_3d_edit.goto_ui.z_label_tooltip"))
        self.z.SetDigits(2)
        self.z.SetMinSize((COORD_FIELD_WIDTH, -1))

        copy_btn = wx.BitmapButton(
            panel, bitmap=image.icon.tablericons.copy.bitmap(20, 20)
        )
        copy_btn.Bind(wx.EVT_BUTTON, self._on_copy_button)
        copy_btn.SetToolTip(lang.get("program_3d_edit.goto_ui.copy_button_tooltip"))

        paste_btn = wx.BitmapButton(
            panel, bitmap=image.icon.tablericons.clipboard.bitmap(20, 20)
        )
        paste_btn.Bind(wx.EVT_BUTTON, self._on_paste_button)
        paste_btn.SetToolTip(lang.get("program_3d_edit.goto_ui.paste_button_tooltip"))

        go_btn = wx.Button(panel, label="GO")
        go_btn.Bind(
            wx.EVT_BUTTON,
            lambda evt: self._do_goto(
                self.x.GetValue(), self.y.GetValue(), self.z.GetValue()
            ),
        )

        coord_sizer.Add(x_text, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.TOP | wx.BOTTOM, 5)
        coord_sizer.Add(self.x, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        coord_sizer.Add(y_text, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM, 5)
        coord_sizer.Add(self.y, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        coord_sizer.Add(z_text, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM, 5)
        coord_sizer.Add(self.z, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        coord_sizer.Add(copy_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 3)
        coord_sizer.Add(paste_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 3)
        coord_sizer.Add(go_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 5)

        main_sizer.Add(coord_sizer, 0, wx.EXPAND | wx.ALL, 2)

        # ── MRU section ───────────────────────────────────────────────────
        main_sizer.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        self._mru_label = wx.StaticText(panel, label="Recent:")
        main_sizer.Add(self._mru_label, 0, wx.LEFT | wx.TOP, 5)

        self._mru_container = wx.Panel(panel)
        self._mru_sizer = wx.BoxSizer(wx.VERTICAL)
        self._mru_container.SetSizer(self._mru_sizer)
        main_sizer.Add(self._mru_container, 0, wx.EXPAND | wx.ALL, 2)

        self._rebuild_mru()

        self.x.Bind(wx.EVT_CHAR, self._on_text)
        self.y.Bind(wx.EVT_CHAR, self._on_text)
        self.z.Bind(wx.EVT_CHAR, self._on_text)
        self.Bind(wx.EVT_CHAR_HOOK, self._on_text)

        # Explicitly set values after full construction — wx.SpinCtrlDouble
        # ignores the `initial` kwarg on Windows until the window is realized.
        self._set_location_fields(float(x), float(y), float(z))

        self._fit_to_contents()

    def _do_goto(self, x: float, y: float, z: float):
        """Invoke the teleport callback and refresh the MRU list."""
        self._set_location_fields(x, y, z)
        if self._on_goto_cb:
            self._on_goto_cb(x, y, z)
        add_mru_entry(self._world_path, x, y, z)
        self._rebuild_mru()

    def _rebuild_mru(self):
        """Clear and rebuild all MRU rows from the saved file."""
        self._mru_sizer.Clear(delete_windows=True)
        entries = load_mru(self._world_path)
        self._mru_label.Show(bool(entries))
        for mx, my, mz in entries:
            row_panel = wx.Panel(self._mru_container)
            row_sizer = wx.BoxSizer(wx.HORIZONTAL)
            row_panel.SetSizer(row_sizer)
            lbl = wx.StaticText(row_panel, label=f"  {mx:.2f},  {my:.2f},  {mz:.2f}")
            row_go = wx.Button(row_panel, label="GO")
            row_del = wx.BitmapButton(
                row_panel, bitmap=image.icon.tablericons.trash.bitmap(20, 20)
            )
            row_del.SetToolTip("Delete this entry")
            row_go.Bind(
                wx.EVT_BUTTON,
                lambda evt, px=mx, py=my, pz=mz: self._do_goto(px, py, pz),
            )
            row_del.Bind(
                wx.EVT_BUTTON,
                lambda evt, px=mx, py=my, pz=mz: self._delete_entry(px, py, pz),
            )
            row_sizer.Add(lbl, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
            row_sizer.Add(row_go, 0, wx.ALL, 2)
            row_sizer.Add(row_del, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.RIGHT, 2)
            self._mru_sizer.Add(row_panel, 0, wx.EXPAND)
        self._mru_container.Layout()
        self._panel.Layout()
        self._fit_to_contents()

    def _fit_to_contents(self):
        self._panel.Layout()
        self._panel.Fit()
        best_size = self._panel.GetBestSize()
        self.SetClientSize(best_size)

    def _delete_entry(self, x: float, y: float, z: float):
        entries = load_mru(self._world_path)
        target = (round(x, 2), round(y, 2), round(z, 2))
        save_mru(self._world_path, [e for e in entries if e != target])
        self._rebuild_mru()

    def _set_location_fields(self, x: float, y: float, z: float):
        self.x.SetValue(float(x))
        self.y.SetValue(float(y))
        self.z.SetValue(float(z))
        self.x.Refresh()
        self.y.Refresh()
        self.z.Refresh()

    def set_location(self, x: float, y: float, z: float):
        self._set_location_fields(x, y, z)

    def _on_text(self, evt):
        if evt.GetKeyCode() == wx.WXK_ESCAPE:
            self.Close()
        elif evt.GetKeyCode() in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
            self._do_goto(
                self.x.GetValue(), self.y.GetValue(), self.z.GetValue()
            )
        elif evt.ControlDown() and evt.GetKeyCode() == 3:
            # Ctrl+C
            self._copy()
        elif evt.ControlDown() and evt.GetKeyCode() == 22:
            # Ctrl+V
            if not self._paste():
                evt.Skip()
        else:
            evt.Skip()

    def _copy(self):
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(
                wx.TextDataObject(
                    "{} {} {}".format(
                        round(self.x.GetValue(), 5),
                        round(self.y.GetValue(), 5),
                        round(self.z.GetValue(), 5),
                    )
                )
            )
            wx.TheClipboard.Flush()
            wx.TheClipboard.Close()

    def _on_copy_button(self, _evt):
        self._copy()

    def _on_paste_button(self, _evt):
        if not self._paste():
            wx.Bell()

    def _paste(self) -> bool:
        text = ""
        text_data = wx.TextDataObject()
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(text_data)
            wx.TheClipboard.Close()
            if success:
                text = text_data.GetText()
        match = CoordRegex.fullmatch(text) or CoordParseRegex.fullmatch(text)
        if match:
            self._set_location_fields(
                float(match.group("x")),
                float(match.group("y")),
                float(match.group("z")),
            )
            return True
        return False
