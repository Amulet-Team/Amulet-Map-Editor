from __future__ import annotations

from functools import partial
from collections.abc import MutableMapping, MutableSequence

import wx

from amulet_map_editor.api.wx.ui import simple

import amulet_nbt as nbt

from amulet_map_editor.api import image

nbt_resources = image.nbt

NBT_FILE = b"\x0A\x00\x0B\x68\x65\x6C\x6C\x6F\x20\x77\x6F\x72\x6C\x64\x08\x00\x04\x6E\x61\x6D\x65\x00\x09\x42\x61\x6E\x61\x6E\x72\x61\x6D\x61\x00"


class NBTRadioButton(simple.SimplePanel):
    def __init__(self, parent, nbt_tag_class, icon):
        super(NBTRadioButton, self).__init__(parent, wx.HORIZONTAL)

        self.nbt_tag_class = nbt_tag_class

        self.radio_button = wx.RadioButton(self, wx.ID_ANY, wx.EmptyString)
        self.add_object(self.radio_button, 0, wx.ALIGN_CENTER | wx.ALL)

        self.tag_bitmap = wx.StaticBitmap(self, wx.ID_ANY, icon)
        self.tag_bitmap.SetToolTip(nbt_tag_class)

        self.add_object(self.tag_bitmap, 0, wx.ALIGN_CENTER | wx.ALL)

    def GetValue(self):
        return self.radio_button.GetValue()

    def SetValue(self, val):
        self.radio_button.SetValue(val)


class NBTEditor(simple.SimplePanel):
    def __init__(self, parent, nbt_data, root_tag_name="", callback=None):
        super(NBTEditor, self).__init__(parent)

        self.nbt_data = nbt_data

        self.image_list = wx.ImageList(16, 16)
        self.image_map = {
            nbt.TAG_Byte: self.image_list.Add(nbt_resources.nbt_tag_byte.bitmap()),
            nbt.TAG_Short: self.image_list.Add(nbt_resources.nbt_tag_short.bitmap()),
            nbt.TAG_Int: self.image_list.Add(nbt_resources.nbt_tag_int.bitmap()),
            nbt.TAG_Long: self.image_list.Add(nbt_resources.nbt_tag_long.bitmap()),
            nbt.TAG_Float: self.image_list.Add(nbt_resources.nbt_tag_float.bitmap()),
            nbt.TAG_Double: self.image_list.Add(nbt_resources.nbt_tag_double.bitmap()),
            nbt.TAG_String: self.image_list.Add(nbt_resources.nbt_tag_string.bitmap()),
            nbt.TAG_Compound: self.image_list.Add(
                nbt_resources.nbt_tag_compound.bitmap()
            ),
            nbt.NamedTag: self.image_list.ImageCount - 1,
            nbt.TAG_List: self.image_list.Add(nbt_resources.nbt_tag_list.bitmap()),
            nbt.TAG_Byte_Array: self.image_list.Add(
                nbt_resources.nbt_tag_array.bitmap()
            ),
            nbt.TAG_Int_Array: self.image_list.ImageCount - 1,
            nbt.TAG_Long_Array: self.image_list.ImageCount - 1,
        }
        self.other = self.image_map[nbt.TAG_String]

        self.tree = self.build_tree(root_tag_name)
        self.add_object(self.tree, 1, wx.ALL | wx.CENTER | wx.EXPAND)

        button_row = simple.SimplePanel(self, wx.HORIZONTAL)
        self.commit_button = wx.Button(button_row, label="Commit")
        self.cancel_button = wx.Button(button_row, label="Cancel")

        button_row.add_object(self.commit_button, space=0)
        button_row.add_object(self.cancel_button, space=0)

        self.commit_button.Bind(wx.EVT_BUTTON, self.commit)
        self.cancel_button.Bind(wx.EVT_BUTTON, self._close)

        self.add_object(button_row, space=0)

        self.callback = callback

    def commit(self, evt):
        self.callback(self.nbt_data)
        evt.Skip()

    def _close(self, evt):
        self.Close(True)
        evt.Skip()

    def build_tree(self, root_tag_name=""):
        def add_tree_node(_tree: wx.TreeCtrl, _parent, _items):
            for key, value in _items.items():
                new_child = None
                if isinstance(value, MutableMapping):
                    new_child = _tree.AppendItem(_parent, key)
                    add_tree_node(_tree, new_child, value)
                elif isinstance(value, MutableSequence):
                    new_child = _tree.AppendItem(_parent, key)

                    for i, item in enumerate(value):
                        child_child = _tree.AppendItem(new_child, f"{item.value}")
                        tree.SetItemData(child_child, (i, item))
                        tree.SetItemImage(
                            child_child,
                            self.image_map.get(item.__class__, self.other),
                            wx.TreeItemIcon_Normal,
                        )
                else:
                    new_child = _tree.AppendItem(_parent, f"{key}: {value.value}")

                tree.SetItemData(new_child, (key, value))
                tree.SetItemImage(
                    new_child, self.image_map.get(value.__class__, self.other)
                )

        tree = wx.TreeCtrl(self, style=wx.TR_DEFAULT_STYLE | wx.EXPAND | wx.ALL)
        tree.AssignImageList(self.image_list)

        root = tree.AddRoot(root_tag_name)
        tree.SetItemData(root, (root_tag_name, self.nbt_data))
        tree.SetItemImage(
            root,
            self.image_map.get(
                self.nbt_data.__class__, self.image_map[nbt.TAG_Compound]
            ),
            wx.TreeItemIcon_Normal,
        )

        add_tree_node(tree, root, self.nbt_data)

        tree.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.tree_right_click)

        return tree

    def _generate_menu(self, include_add_tag=False):
        menu = wx.Menu()

        menu_items = [
            wx.MenuItem(menu, text="Edit Tag", id=wx.ID_ANY),
            wx.MenuItem(menu, text="Delete Tag", id=wx.ID_ANY),
        ]

        if include_add_tag:
            menu_items.insert(0, wx.MenuItem(menu, text="Add Tag", id=wx.ID_ANY))

        for menu_item in menu_items:
            menu.Append(menu_item)

        op_map = {
            item.GetId(): item.GetItemLabelText().split()[0].lower()
            for item in menu_items
        }
        menu.Bind(wx.EVT_MENU, lambda evt: self.popup_menu_handler(op_map, evt))

        return menu

    def tree_right_click(self, evt):
        tag_name, tag_obj = self.tree.GetItemData(evt.GetItem())

        menu = self._generate_menu(
            isinstance(tag_obj, (MutableMapping, MutableSequence))
        )
        self.PopupMenu(menu, evt.GetPoint())
        menu.Destroy()
        evt.Skip()

    def popup_menu_handler(self, op_map, evt):
        op_id = evt.GetId()
        op_name = op_map[op_id]

        if op_name == "add":
            self.add_tag()
        elif op_name == "edit":
            self.edit_tag()
        else:
            selected_tag = self.tree.GetFocusedItem()

            if selected_tag == self.tree.GetRootItem():
                wx.MessageBox("Root nodes cannot be deleted currently", "Info", wx.OK)
                return

            name, _ = self.tree.GetItemData(selected_tag)
            parent = self.tree.GetItemParent(selected_tag)

            if parent == self.tree.GetRootItem():
                parent_data = self.nbt_data
            else:
                _, parent_data = self.tree.GetItemData(parent)

            del parent_data[name]

            self.tree.Delete(selected_tag)

    def add_tag(self):
        selected_tag = self.tree.GetFocusedItem()
        name, data = self.tree.GetItemData(selected_tag)

        def save_func(new_name, new_tag_value, new_tag_type, _):
            tag_type = [
                tag_class
                for tag_class in self.image_map
                if tag_class.__name__ == new_tag_type
            ][0]
            self.nbt_data[new_name] = nbt_tag = tag_type(new_tag_value)

            new_child = self.tree.AppendItem(
                selected_tag, f"{new_name}: {new_tag_value}"
            )
            self.tree.SetItemImage(new_child, self.image_map.get(tag_type, self.other))
            self.tree.SetItemData(new_child, (new_name, nbt_tag))

        add_dialog = EditTagDialog(
            self,
            "",
            nbt.TAG_Byte(0),
            [
                tag_type.__name__
                for tag_type in self.image_map.keys()
                if "TAG_" in tag_type.__name__
            ],
            create=True,
            save_callback=save_func,
        )
        add_dialog.Show()

    def edit_tag(self):
        selected_tag = self.tree.GetFocusedItem()
        name, data = self.tree.GetItemData(selected_tag)

        def save_func(new_name, new_tag_value, new_tag_type, old_name):
            tag_type = [
                tag_class
                for tag_class in self.image_map
                if tag_class.__name__ == new_tag_type
            ][0]

            self.nbt_data[new_name] = nbt_tag = tag_type(new_tag_value)
            self.tree.SetItemImage(
                selected_tag, self.image_map.get(tag_type, self.other)
            )
            self.tree.SetItemData(selected_tag, (new_name, nbt_tag))
            self.tree.SetItemText(selected_tag, f"{new_name}: {new_tag_value}")

            if new_name != old_name:
                del self.nbt_data[old_name]

        edit_dialog = EditTagDialog(
            self,
            name,
            data,
            [
                tag_type.__name__
                for tag_type in self.image_map.keys()
                if "TAG_" in tag_type.__name__
            ],
            save_callback=save_func,
        )
        edit_dialog.Show()


class EditTagDialog(wx.Frame):
    GRID_ROWS = 3
    GRID_COLUMNS = 4

    def __init__(
        self, parent, tag_name, tag, tag_types, create=False, save_callback=None
    ):
        super(EditTagDialog, self).__init__(
            parent, title="Edit NBT Tag", size=(500, 280)
        )

        self.save_callback = save_callback
        self.old_name = tag_name
        self.data_type_func = lambda x: x

        main_panel = simple.SimplePanel(self)

        name_panel = simple.SimplePanel(main_panel, sizer_dir=wx.HORIZONTAL)
        value_panel = simple.SimplePanel(main_panel, sizer_dir=wx.HORIZONTAL)
        tag_type_panel = simple.SimplePanel(main_panel)
        button_panel = simple.SimplePanel(main_panel, sizer_dir=wx.HORIZONTAL)

        name_label = wx.StaticText(name_panel, label="Name: ")
        self.name_field = wx.TextCtrl(name_panel)

        if tag_name == "" and not create:
            self.name_field.Disable()
        else:
            self.name_field.SetValue(tag_name)

        name_panel.add_object(name_label, space=0, options=wx.ALL | wx.CENTER)
        name_panel.add_object(self.name_field, space=1, options=wx.ALL | wx.EXPAND)

        value_label = wx.StaticText(value_panel, label="Value: ")
        self.value_field = wx.TextCtrl(value_panel)

        if isinstance(tag, (nbt.TAG_Compound, nbt.TAG_List)):
            self.value_field.Disable()
        else:
            self.value_field.SetValue(str(tag.value))

        value_panel.add_object(value_label, space=0, options=wx.ALL | wx.CENTER)
        value_panel.add_object(self.value_field, space=1, options=wx.ALL | wx.EXPAND)

        tag_type_sizer = wx.GridSizer(self.GRID_ROWS, self.GRID_COLUMNS, 0, 0)

        self.radio_buttons = []

        for tag_type in tag_types:
            rd_btn = NBTRadioButton(
                tag_type_panel,
                tag_type,
                parent.image_list.GetBitmap(parent.image_map[getattr(nbt, tag_type)]),
            )
            self.radio_buttons.append(rd_btn)
            rd_btn.Bind(wx.EVT_RADIOBUTTON, partial(self.handle_radio_button, tag_type))
            tag_type_sizer.Add(rd_btn, 0, wx.ALL, 0)

            if tag_type == tag.__class__.__name__:
                rd_btn.SetValue(True)

        tag_type_panel.SetSizerAndFit(tag_type_sizer)

        self.save_button = wx.Button(button_panel, label="Save")
        self.cancel_button = wx.Button(button_panel, label="Cancel")

        button_panel.add_object(self.save_button, space=0)
        button_panel.add_object(self.cancel_button, space=0)

        main_panel.add_object(name_panel, space=0, options=wx.ALL | wx.EXPAND)
        main_panel.add_object(value_panel, space=0, options=wx.ALL | wx.EXPAND)
        main_panel.add_object(tag_type_panel, space=0)
        main_panel.add_object(button_panel, space=0)

        self.save_button.Bind(wx.EVT_BUTTON, self.save)
        self.cancel_button.Bind(wx.EVT_BUTTON, lambda evt: self.Close())

        self.value_field.Bind(wx.EVT_TEXT, self.value_changed)

        self.SetSize((235, 260))
        self.Layout()

    def value_changed(self, evt):
        tag_value = evt.GetString()
        self.value_field.ChangeValue(str(self.data_type_func(tag_value)))

    def handle_radio_button(self, tag_type, evt):
        for rd_btn in self.radio_buttons:
            rd_btn.SetValue(rd_btn.nbt_tag_class == tag_type)
        self.change_tag_type_func(tag_type)

    def change_tag_type_func(self, tag_type):
        self.data_type_func = lambda x: x
        if tag_type in ("TAG_Int", "TAG_Long", "TAG_Short", "TAG_Short", "TAG_Byte"):
            self.data_type_func = lambda x: int(float(x))
        elif tag_type in ("TAG_Float", "TAG_Double"):
            self.data_type_func = float

        if tag_type not in ("TAG_Byte_Array", "TAG_Int_Array", "TAG_Long_Array"):
            self.value_field.ChangeValue(
                str(self.data_type_func(self.value_field.GetValue()))
            )

    def get_selected_tag_type(self):
        for rd_btn in self.radio_buttons:
            if rd_btn.GetValue():
                return rd_btn.nbt_tag_class
        return None

    def save(self, evt):
        self.save_callback(
            self.name_field.GetValue(),
            self.data_type_func(self.value_field.GetValue()),
            self.get_selected_tag_type(),
            self.old_name,
        )

        self.Close()


if __name__ == "__main__":
    import wx.lib.inspection

    app = wx.App()
    wx.lib.inspection.InspectionTool().Show()
    frame = wx.Frame(None)
    NBTEditor(frame, nbt.load(NBT_FILE), callback=lambda nbt_data: print(nbt_data))
    frame.Show()
    app.MainLoop()
