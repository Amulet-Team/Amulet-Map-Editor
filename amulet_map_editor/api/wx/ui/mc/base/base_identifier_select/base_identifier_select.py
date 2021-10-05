import wx

import PyMCTranslate

from amulet.api.data_types import VersionNumberTuple
from amulet_map_editor.api.image import COLOUR_PICKER
from amulet_map_editor.api.wx.ui.mc.state import BaseResourceIDState, StateHolder, State
from .events import (
    PickEvent,
)


class BaseIdentifierSelect(wx.Panel, StateHolder):
    """
    BaseIdentifierSelect is a base class for a UI containing
        a namespace choice
        a base name search
        a list of base names
    """

    state: BaseResourceIDState

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        state: BaseResourceIDState = None,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        show_pick: bool = False,
    ):
        if not isinstance(state, BaseResourceIDState):
            state = self._create_default_state(
                translation_manager,
                platform=platform,
                version_number=version_number,
                force_blockstate=force_blockstate,
                namespace=namespace,
                base_name=base_name,
            )
        StateHolder.__init__(self, state)
        wx.Panel.__init__(self, parent, style=wx.BORDER_SIMPLE)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 5)
        text = wx.StaticText(self, label="Namespace:", style=wx.ALIGN_CENTER)
        sizer.Add(text, 1, wx.ALIGN_CENTER_VERTICAL)
        self._namespace_combo = wx.ComboBox(self)
        sizer.Add(self._namespace_combo, 2)
        self._update_namespace()

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
        self._update_base_name()
        self._base_name_list_box.Bind(wx.EVT_LISTBOX, self._on_base_name_change)

    def _create_default_state(
        self,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
    ) -> BaseResourceIDState:
        raise NotImplementedError

    @property
    def type_name(self) -> str:
        raise NotImplementedError

    def _post_event(
        self,
        namespace: str,
        base_name: str,
    ):
        raise NotImplementedError

    def _on_state_change(self):
        if self.state.is_changed(State.Namespace) or self.state.is_changed(
            State.ForceBlockstate
        ):
            self._update_namespace()
        if self.state.is_changed(State.Namespace) or self.state.is_changed(
            State.BaseName
        ):
            self._update_base_name()

    def _update_namespace(self):
        self._namespace_combo.Set(self.state.valid_namespaces)
        namespace = self.state.namespace
        if namespace != self._namespace_combo.GetValue():
            index = self._namespace_combo.FindString(namespace)
            if index == wx.NOT_FOUND:
                self._namespace_combo.ChangeValue(namespace)
            else:
                self._namespace_combo.SetSelection(index)

    def _update_base_name(self):
        base_name = self.state.base_name
        if base_name in self.state.valid_base_names:
            # The base name is known
            location = self._base_name_list_box.FindString(base_name)
            if location == wx.NOT_FOUND:
                self._search.ChangeValue("")
                self._update_from_search()
                location = self._base_name_list_box.FindString(base_name)
            self._base_name_list_box.SetSelection(location)
        else:
            # The base name is not known
            self._search.ChangeValue(base_name)
            self._update_from_search()

    def _update_from_search(self) -> bool:
        """
        Update the base names based on the value in the search field.

        :return: True if the text in the field changed
        """
        search_str = self._search.GetValue()
        base_names = [bn for bn in self.state.valid_base_names if search_str in bn]
        exact = search_str in base_names

        if (search_str and not exact) or (not search_str and not base_names):
            # We have a search which is not a match or we don't have a search string or options
            base_names.insert(0, f'"{search_str}"')

        # find the previously selected string
        previous_string = None
        selection = self._base_name_list_box.GetSelection()
        if selection != wx.NOT_FOUND:
            previous_string = self._base_name_list_box.GetString(selection)

        self.Freeze()
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
        self.Thaw()

        return previous_string != self._base_name_list_box.GetString(
            self._base_name_list_box.GetSelection()
        )

    def _handle_namespace_change(self):
        namespace = self._namespace_combo.GetValue()
        if namespace != self.state.namespace:
            with self.state as state:
                state.namespace = namespace
            self._post_event(self.state.namespace, self.state.base_name)

    def _on_namespace_change(self, evt):
        self._handle_namespace_change()
        if isinstance(evt, wx.KeyEvent):
            evt.Skip()

    def _on_namespace_char(self, evt):
        wx.CallAfter(self._handle_namespace_change)
        evt.Skip()

    def _on_search_change(self, evt):
        if self._update_from_search():
            self._on_change()

    def _on_base_name_change(self, evt):
        self._on_change()

    def _on_change(self):
        base_name = self._base_name_list_box.GetString(
            self._base_name_list_box.GetSelection()
        )
        if (
            self._base_name_list_box.GetSelection() == 0
            and base_name not in self.state.valid_base_names
        ):
            base_name = base_name[1:-1]
        if base_name != self.state.namespace:
            with self.state as state:
                state.base_name = base_name
            self._post_event(self.state.namespace, self.state.base_name)
