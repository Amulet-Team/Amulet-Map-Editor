import wx
from typing import Tuple, List, Dict, Any

import PyMCTranslate

from amulet.api.data_types import VersionNumberTuple
from amulet_map_editor.api.image import COLOUR_PICKER
from ..api.resource_id import BaseMCResourceID
from .events import (
    PickEvent,
)


class BaseIdentifierSelect(wx.Panel, BaseMCResourceID):
    """
    BaseIdentifierSelect is a base class for a UI containing
        a namespace choice
        a base name search
        a list of base names
    """

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str,
        version_number: VersionNumberTuple,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        show_pick: bool = False,
        state: Dict[str, Any] = None,
    ):
        state = state or {}
        state.setdefault("translation_manager", translation_manager)
        state.setdefault("platform", platform)
        state.setdefault("version_number", version_number)
        state.setdefault("force_blockstate", force_blockstate)
        state.setdefault("namespace", namespace)
        state.setdefault("base_name", base_name)
        # This is the init call to the class that stores the internal state of the data.
        # This needs to be at the start to ensure that the internal state is set up before anything else is done.
        # It is not a direct call to init so that subclasses of this class can substitute in which state subclass is used.
        self._init_state(state)

        wx.Panel.__init__(self, parent, style=wx.BORDER_SIMPLE)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 5)
        text = wx.StaticText(self, label="Namespace:", style=wx.ALIGN_CENTER)
        sizer.Add(text, 1, wx.ALIGN_CENTER_VERTICAL)
        self._namespace_combo = wx.ComboBox(self)
        sizer.Add(self._namespace_combo, 2)
        self._populate_namespace()
        self._push_namespace()

        # This was previously done with EVT_TEXT but that is also triggered by the Set method.
        # This is a workaround so that it is only triggered by user input.
        self._namespace_combo.Bind(wx.EVT_CHAR, self._on_namespace_char)
        self._namespace_combo.Bind(wx.EVT_COMBOBOX, self._on_namespace_change)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(sizer, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)
        header_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(header_sizer, 0, wx.EXPAND | wx.BOTTOM, 5)
        header_sizer.Add(
            wx.StaticText(
                self,
                label=f"{self.type_name.capitalize()} name:",
                style=wx.ALIGN_CENTER,
            ),
            1,
            wx.ALIGN_CENTER_VERTICAL,
        )
        search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        header_sizer.Add(search_sizer, 2, wx.EXPAND)
        self._search = wx.SearchCtrl(self)
        search_sizer.Add(self._search, 1, wx.ALIGN_CENTER_VERTICAL)
        self._search.Bind(wx.EVT_TEXT, self._on_search_change)
        if show_pick:
            pick_button = wx.BitmapButton(self, bitmap=COLOUR_PICKER.bitmap(22, 22))
            search_sizer.Add(pick_button, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
            pick_button.Bind(
                wx.EVT_BUTTON,
                lambda evt: wx.PostEvent(self, PickEvent(self.GetId(), widget=self)),
            )
        self._base_name_list_box = wx.ListBox(self, style=wx.LB_SINGLE)
        sizer.Add(self._base_name_list_box, 1, wx.EXPAND)

        self._base_names: List[str] = []
        self._populate_base_name()
        self._push_base_name()
        self._base_name_list_box.Bind(wx.EVT_LISTBOX, self._on_base_name_change)

    def _init_state(self, state: Dict[str, Any]):
        """
        Call the init method of the state manager.
        This is here so that nested classes do not have to init the state managers multiple times.
        """
        BaseMCResourceID.__init__(self, **state)

    @property
    def type_name(self) -> str:
        raise NotImplementedError

    def _populate_namespace(self):
        raise NotImplementedError("This method should be overridden in child classes.")

    def _populate_base_name(self):
        raise NotImplementedError("This method should be overridden in child classes.")

    def _push_namespace(self):
        """Push the internal namespace to the UI."""
        namespace = self.namespace
        if namespace in self._namespace_combo.GetItems():
            self._namespace_combo.SetSelection(
                self._namespace_combo.GetItems().index(namespace)
            )
        else:
            self._namespace_combo.ChangeValue(namespace)

    def _push_base_name(self):
        """Push the internal base name to the UI."""
        if self.base_name in self._base_names:
            location = self._base_name_list_box.FindString(self.base_name)
            if location == wx.NOT_FOUND:
                self._search.ChangeValue("")
                self._update_from_search()
                location = self._base_name_list_box.FindString(self.base_name)
            self._base_name_list_box.SetSelection(location)
        else:
            self._search.ChangeValue(self.base_name)
            self._update_from_search()

    def _update_from_search(self) -> bool:
        """
        Update the base names based on the value in the search field.

        :return: True if the text in the field changed
        """
        search_str = self._search.GetValue()
        base_names = [bn for bn in self._base_names if search_str in bn]
        exact = search_str in base_names

        # I originally wrote this in one line but it was rather difficult to read.
        if exact:
            # if we have an exact match
            pass
        elif not search_str and base_names:
            # if the search string is blank but there are options
            pass
        else:
            base_names.insert(0, f'"{search_str}"')

        # find the previously selected string
        previous_string = None
        selection = self._base_name_list_box.GetSelection()
        if selection != wx.NOT_FOUND:
            previous_string = self._base_name_list_box.GetString(selection)

        self._base_name_list_box.SetItems(base_names)
        if exact:
            # if the searched text perfectly matches select that
            self._base_name_list_box.SetSelection(base_names.index(search_str))
        elif previous_string in base_names:
            # if the previously selected string is in the list select that
            index = base_names.index(previous_string)
            self._base_name_list_box.SetSelection(index)
        elif len(self._base_name_list_box.GetItems()) >= 2:
            self._base_name_list_box.SetSelection(1)
        else:
            self._base_name_list_box.SetSelection(0)

        return previous_string != self._base_name_list_box.GetString(
            self._base_name_list_box.GetSelection()
        )

    def _post_event(
        self,
        old_namespace: str,
        old_base_name: str,
        new_namespace: str,
        new_base_name: str,
    ):
        raise NotImplementedError

    def _on_namespace_change(self, evt):
        self._handle_namespace_change()
        if isinstance(evt, wx.KeyEvent):
            evt.Skip()

    def _handle_namespace_change(self):
        self.Freeze()
        old_namespace = self.namespace
        new_namespace = self._namespace_combo.GetValue()
        if new_namespace != old_namespace:
            self._set_namespace(new_namespace)

            self._populate_base_name()
            self._update_from_search()

            self._on_change(old_namespace)
        self.Thaw()

    def _on_namespace_char(self, evt):
        wx.CallAfter(self._handle_namespace_change)
        evt.Skip()

    def _on_search_change(self, evt):
        if self._update_from_search():
            self._on_change()

    def _on_base_name_change(self, evt):
        self._on_change()

    def _on_change(self, old_namespace=None):
        if old_namespace is None:
            old_namespace = self.namespace
        old_base_name = self.base_name
        new_base_name = self._base_name_list_box.GetString(
            self._base_name_list_box.GetSelection()
        )
        if self._base_name_list_box.GetSelection() == 0 and new_base_name.startswith(
            '"'
        ):
            new_base_name = new_base_name[1:-1]
        if old_namespace != self.namespace or old_base_name != new_base_name:
            self._set_base_name(new_base_name)
            self._post_event(
                old_namespace, old_base_name, self.namespace, new_base_name
            )

    def _on_push(self) -> bool:
        self._populate_namespace()
        self._push_namespace()
        self._populate_base_name()
        self._push_base_name()
        return True
