# -*- coding: utf-8 -*-

###########################################################################
## Python code wostly generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## File has been manually edited, but care should be taken when modifying the _MainWindow class
###########################################################################

import wx
import wx.xrc

import sys


# noinspection PyUnresolvedReferences
import amulet
import PyMCTranslate

WORLD_PATH_LABEL = "World Path: <>"
WORLD_FORMAT_LABEL = "World Format/Version: <>"


class _MainWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=wx.EmptyString,
            pos=wx.DefaultPosition,
            size=wx.Size(560, 400),
            style=wx.CAPTION
            | wx.CLOSE_BOX
            | wx.MINIMIZE_BOX
            | wx.SYSTEM_MENU
            | wx.TAB_TRAVERSAL
            | wx.CLIP_CHILDREN,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.tab_holder = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0
        )

        # region converter panel
        self.converter_panel = wx.Panel(
            self.tab_holder,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        convert_panel_sizer = wx.GridBagSizer(5, 0)
        convert_panel_sizer.SetFlexibleDirection(wx.BOTH)
        convert_panel_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        convert_panel_sizer.SetEmptyCellSize(wx.Size(25, 25))

        self.input_panel = wx.Panel(
            self.converter_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_SUNKEN | wx.TAB_TRAVERSAL,
        )
        self.input_panel.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER)
        )

        input_panel_sizer = wx.GridBagSizer(0, 0)
        input_panel_sizer.SetFlexibleDirection(wx.BOTH)
        input_panel_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.input_world_label = wx.StaticText(
            self.input_panel,
            wx.ID_ANY,
            "Input World",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.input_world_label.Wrap(-1)

        input_panel_sizer.Add(
            self.input_world_label, wx.GBPosition(0, 0), wx.GBSpan(1, 5), wx.ALL, 5
        )

        self.in_world_path_label = wx.StaticText(
            self.input_panel,
            wx.ID_ANY,
            "World Path:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.in_world_path_label.Wrap(-1)

        input_panel_sizer.Add(
            self.in_world_path_label, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5
        )

        self.in_world_format_label = wx.StaticText(
            self.input_panel,
            wx.ID_ANY,
            "World Format/Version:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.in_world_format_label.Wrap(-1)

        input_panel_sizer.Add(
            self.in_world_format_label, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5
        )

        self.select_input_button = wx.Button(
            self.input_panel,
            wx.ID_ANY,
            "Select Input World",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        input_panel_sizer.Add(
            self.select_input_button, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5
        )

        self.input_panel.SetSizer(input_panel_sizer)
        self.input_panel.Layout()
        input_panel_sizer.Fit(self.input_panel)
        convert_panel_sizer.Add(
            self.input_panel,
            wx.GBPosition(0, 0),
            wx.GBSpan(1, 14),
            wx.EXPAND | wx.ALL,
            5,
        )

        self.output_panel = wx.Panel(
            self.converter_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.BORDER_SUNKEN | wx.TAB_TRAVERSAL,
        )
        self.output_panel.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR)
        )

        output_panel_sizer = wx.GridBagSizer(0, 0)
        output_panel_sizer.SetFlexibleDirection(wx.BOTH)
        output_panel_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.output_world_label = wx.StaticText(
            self.output_panel,
            wx.ID_ANY,
            "Output World",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.output_world_label.Wrap(-1)

        output_panel_sizer.Add(
            self.output_world_label, wx.GBPosition(0, 0), wx.GBSpan(1, 5), wx.ALL, 5
        )

        self.out_world_path_label = wx.StaticText(
            self.output_panel,
            wx.ID_ANY,
            "World Path:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.out_world_path_label.Wrap(-1)

        output_panel_sizer.Add(
            self.out_world_path_label, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5
        )

        self.out_world_format_label = wx.StaticText(
            self.output_panel,
            wx.ID_ANY,
            "World Format/Version:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.out_world_format_label.Wrap(-1)

        output_panel_sizer.Add(
            self.out_world_format_label, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5
        )

        self.select_output_button = wx.Button(
            self.output_panel,
            wx.ID_ANY,
            "Select Output World",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        output_panel_sizer.Add(
            self.select_output_button, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5
        )

        self.output_panel.SetSizer(output_panel_sizer)
        self.output_panel.Layout()
        output_panel_sizer.Fit(self.output_panel)
        convert_panel_sizer.Add(
            self.output_panel,
            wx.GBPosition(1, 0),
            wx.GBSpan(1, 14),
            wx.EXPAND | wx.ALL,
            5,
        )

        self.convert_button = wx.Button(
            self.converter_panel,
            wx.ID_ANY,
            "Convert",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        convert_panel_sizer.Add(
            self.convert_button,
            wx.GBPosition(2, 11),
            wx.GBSpan(1, 1),
            wx.ALL | wx.EXPAND,
            5,
        )

        self.close_button = wx.Button(
            self.converter_panel,
            wx.ID_ANY,
            "Close",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        convert_panel_sizer.Add(
            self.close_button,
            wx.GBPosition(2, 12),
            wx.GBSpan(1, 1),
            wx.ALL | wx.EXPAND,
            5,
        )

        self.converter_progress = wx.Gauge(
            self.converter_panel,
            wx.ID_ANY,
            100,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.GA_HORIZONTAL,
        )
        self.converter_progress.SetValue(0)
        convert_panel_sizer.Add(
            self.converter_progress,
            wx.GBPosition(2, 0),
            wx.GBSpan(1, 8),
            wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        for i in range(14):
            convert_panel_sizer.AddGrowableCol(i)

        convert_panel_sizer.AddGrowableRow(2)

        self.converter_panel.SetSizer(convert_panel_sizer)
        self.converter_panel.Layout()
        convert_panel_sizer.Fit(self.converter_panel)
        self.tab_holder.AddPage(self.converter_panel, "World Converter", False)

        # endregion

        # region modify panel
        self.modify_panel = wx.Panel(
            self.tab_holder,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        modify_panel_sizer = wx.BoxSizer(wx.VERTICAL)

        self.modify_world_note = wx.StaticText(
            self.modify_panel,
            wx.ID_ANY,
            "Note: this will modify the input world",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.modify_world_note.Wrap(-1)

        modify_panel_sizer.Add(self.modify_world_note, 0, wx.ALL, 5)

        operation_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.run_operation_cb = wx.CheckBox(
            self.modify_panel,
            wx.ID_ANY,
            "Run Operation",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        operation_sizer.Add(
            self.run_operation_cb, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        operation_sizer.Add((20, 0), 0, wx.EXPAND, 5)

        self.operation_label = wx.StaticText(
            self.modify_panel,
            wx.ID_ANY,
            "Operation:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.operation_label.Wrap(-1)

        operation_sizer.Add(
            self.operation_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        operation_chooser_choices = ["Replace", "Fill"]
        self.operation_chooser = wx.Choice(
            self.modify_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            operation_chooser_choices,
            0,
        )
        self.operation_chooser.SetSelection(0)
        operation_sizer.Add(
            self.operation_chooser, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        modify_panel_sizer.Add(operation_sizer, 1, wx.EXPAND, 5)

        # region boundary coordinates

        self.start_coordinate_label = wx.StaticText(
            self.modify_panel,
            wx.ID_ANY,
            "Start Coordinates:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.start_coordinate_label.Wrap(-1)

        modify_panel_sizer.Add(self.start_coordinate_label, 0, wx.ALL, 5)

        start_coordinate_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText43 = wx.StaticText(
            self.modify_panel, wx.ID_ANY, "X:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText43.Wrap(-1)

        start_coordinate_sizer.Add(
            self.m_staticText43, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        self.start_x = wx.SpinCtrl(
            self.modify_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SP_ARROW_KEYS,
            0,
            10,
            7,
        )
        self.start_x.SetToolTip("X Coordinate")

        start_coordinate_sizer.Add(
            self.start_x, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        start_coordinate_sizer.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText45 = wx.StaticText(
            self.modify_panel, wx.ID_ANY, "Y:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText45.Wrap(-1)

        start_coordinate_sizer.Add(
            self.m_staticText45, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        self.start_y = wx.SpinCtrl(
            self.modify_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SP_ARROW_KEYS,
            0,
            10,
            0,
        )
        self.start_y.SetToolTip("Y Coordinate")

        start_coordinate_sizer.Add(
            self.start_y, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        start_coordinate_sizer.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText46 = wx.StaticText(
            self.modify_panel, wx.ID_ANY, "Z:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText46.Wrap(-1)

        start_coordinate_sizer.Add(
            self.m_staticText46, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        self.start_z = wx.SpinCtrl(
            self.modify_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SP_ARROW_KEYS,
            0,
            10,
            10,
        )
        self.start_z.SetToolTip("Z Coordinate")

        start_coordinate_sizer.Add(
            self.start_z, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        modify_panel_sizer.Add(start_coordinate_sizer, 1, wx.EXPAND, 5)

        self.end_coordinate_label = wx.StaticText(
            self.modify_panel,
            wx.ID_ANY,
            "End Coordinates:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.end_coordinate_label.Wrap(-1)

        modify_panel_sizer.Add(self.end_coordinate_label, 0, wx.ALL, 5)

        end_coordinate_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText47 = wx.StaticText(
            self.modify_panel, wx.ID_ANY, "X:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText47.Wrap(-1)

        end_coordinate_sizer.Add(
            self.m_staticText47, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        self.end_x = wx.SpinCtrl(
            self.modify_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SP_ARROW_KEYS,
            0,
            10,
            0,
        )
        self.end_x.SetToolTip("X Coordinate")

        end_coordinate_sizer.Add(self.end_x, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        end_coordinate_sizer.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText48 = wx.StaticText(
            self.modify_panel, wx.ID_ANY, "Y:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText48.Wrap(-1)

        end_coordinate_sizer.Add(
            self.m_staticText48, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        self.end_y = wx.SpinCtrl(
            self.modify_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SP_ARROW_KEYS,
            0,
            10,
            0,
        )
        self.end_y.SetToolTip("Y Coordinate")

        end_coordinate_sizer.Add(self.end_y, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        end_coordinate_sizer.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText49 = wx.StaticText(
            self.modify_panel, wx.ID_ANY, "Z:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText49.Wrap(-1)

        end_coordinate_sizer.Add(
            self.m_staticText49, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        self.end_z = wx.SpinCtrl(
            self.modify_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SP_ARROW_KEYS,
            0,
            10,
            0,
        )
        self.end_z.SetToolTip("Z Coordinate")

        end_coordinate_sizer.Add(self.end_z, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        modify_panel_sizer.Add(end_coordinate_sizer, 1, wx.EXPAND, 5)

        # endregion

        # region specification selector

        specification_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.platform_label = wx.StaticText(
            self.modify_panel,
            wx.ID_ANY,
            "Platform:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.platform_label.Wrap(-1)

        specification_sizer.Add(
            self.platform_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        platform_choice_choices = []
        self.platform_choice = wx.Choice(
            self.modify_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            platform_choice_choices,
            0,
        )
        self.platform_choice.SetSelection(0)
        specification_sizer.Add(
            self.platform_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        specification_sizer.Add((20, 0), 0, wx.EXPAND, 5)

        self.version_label = wx.StaticText(
            self.modify_panel,
            wx.ID_ANY,
            "Version:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.version_label.Wrap(-1)

        specification_sizer.Add(
            self.version_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        version_choice_choices = []
        self.version_choice = wx.Choice(
            self.modify_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            version_choice_choices,
            0,
        )
        self.version_choice.SetSelection(0)
        specification_sizer.Add(
            self.version_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        modify_panel_sizer.Add(specification_sizer, 1, wx.EXPAND, 5)

        # endregion

        # region blockstate fields

        self.blockstate_sizer_1 = blockstate_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.fill_block_label = wx.StaticText(
            self.modify_panel,
            wx.ID_ANY,
            "Fill Block:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.fill_block_label.Wrap(-1)

        blockstate_sizer_1.Add(
            self.fill_block_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        self.fill_blockstate_field = wx.TextCtrl(
            self.modify_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.fill_blockstate_field.SetMinSize(wx.Size(380, -1))

        blockstate_sizer_1.Add(
            self.fill_blockstate_field, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        modify_panel_sizer.Add(blockstate_sizer_1, 1, wx.EXPAND, 5)

        self.blockstate_sizer_2 = blockstate_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.replace_block_label = wx.StaticText(
            self.modify_panel,
            wx.ID_ANY,
            "Replacement Block:",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.replace_block_label.Wrap(-1)

        blockstate_sizer_2.Add(
            self.replace_block_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        self.replace_blockstate_field = wx.TextCtrl(
            self.modify_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.replace_blockstate_field.SetMinSize(wx.Size(326, -1))

        blockstate_sizer_2.Add(
            self.replace_blockstate_field, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5
        )

        modify_panel_sizer.Add(blockstate_sizer_2, 1, wx.EXPAND, 5)

        self.modify_panel.SetSizer(modify_panel_sizer)
        self.modify_panel.Layout()
        modify_panel_sizer.Fit(self.modify_panel)
        self.tab_holder.AddPage(self.modify_panel, "Modify Input World", True)

        # endregion

        # endregion

        main_sizer.Add(self.tab_holder, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        self.tab_holder.SetSelection(0)

        self.blockstate_completer = BlockStateCompleter()
        self.fill_blockstate_field.AutoComplete(self.blockstate_completer)
        self.replace_blockstate_field.AutoComplete(self.blockstate_completer)

        # Connect Events
        self.select_input_button.Bind(
            wx.EVT_BUTTON, self.select_input_buttonOnButtonClick
        )
        self.select_output_button.Bind(
            wx.EVT_BUTTON, self.select_output_buttonOnButtonClick
        )
        self.convert_button.Bind(wx.EVT_BUTTON, self.convert_buttonOnButtonClick)
        self.close_button.Bind(wx.EVT_BUTTON, self.close_buttonOnButtonClick)
        self.operation_chooser.Bind(wx.EVT_CHOICE, self.operation_chooserOnChoice)
        self.platform_choice.Bind(wx.EVT_CHOICE, self.platform_choiceOnChoice)
        self.version_choice.Bind(wx.EVT_CHOICE, self.version_choiceOnChoice)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def select_input_buttonOnButtonClick(self, event):
        event.Skip()

    def select_output_buttonOnButtonClick(self, event):
        event.Skip()

    def convert_buttonOnButtonClick(self, event):
        event.Skip()

    def close_buttonOnButtonClick(self, event):
        event.Skip()

    def operation_chooserOnChoice(self, event):
        event.Skip()

    def platform_choiceOnChoice(self, event):
        event.Skip()

    def version_choiceOnChoice(self, event):
        event.Skip()


class MainWindow(_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.selected_platform = None

        self.translation_manager = PyMCTranslate.new_translation_manager()

        self.platform_choice.AppendItems(self.translation_manager.platforms())

        self.Show()

    def select_input_buttonOnButtonClick(self, event):
        self.choose_and_set_world(
            ("input_world_path", "in_world_path_label", "in_world_format_label")
        )

    def select_output_buttonOnButtonClick(self, event):
        self.choose_and_set_world(
            ("output_world_path", "out_world_path_label", "out_world_format_label")
        )

    def close_buttonOnButtonClick(self, event):
        self.Close()

    def operation_chooserOnChoice(self, event):
        op = event.GetString().lower()

        if op == "replace":
            self.blockstate_sizer_2.ShowItems(show=True)
            self.fill_block_label.SetLabelText("Original Block:")
            self.blockstate_sizer_1.Layout()
        elif op == "fill":
            self.blockstate_sizer_2.ShowItems(show=False)
            self.fill_block_label.SetLabelText("Fill Block:")
            self.blockstate_sizer_1.Layout()

    def platform_choiceOnChoice(self, event):
        self.selected_platform = selected_platform = event.GetString()
        self.version_choice.Clear()
        self.version_choice.AppendItems(
            [
                f"{v[0]}.{v[1]}.{v[2]}"
                for v in self.translation_manager.version_numbers(selected_platform)
            ]
        )

    def version_choiceOnChoice(self, event):
        if self.selected_platform is None:
            event.Skip()

        version_numbers = [i for i in map(int, event.GetString().split("."))]
        self.blockstate_completer.set_blockstate_subversion(
            self.translation_manager.get_sub_version(
                self.selected_platform, version_numbers, True
            )
        )

    def choose_and_set_world(self, fields):
        world_path_field, path_label_field, format_label_field = (
            fields[0],
            fields[1],
            fields[2],
        )

        world_path = self.choose_world()
        _format, version = amulet.world_interface.load_format(
            world_path
        )._max_world_version()

        try:
            version_obj = self.translation_manager.get_version(_format, version)
        except (AssertionError, amulet.api.errors.LoaderNoneMatched) as e:
            dialog = wx.MessageDialog(
                self,
                f'Couldn\'t find a valid loader for "{world_path}"',
                style=wx.OK_DEFAULT | wx.ICON_ERROR,
            )
            dialog.ShowModal()
            return

        setattr(self, world_path_field, world_path)
        getattr(self, path_label_field).SetLabelText(
            WORLD_PATH_LABEL.replace("<>", world_path)
        )
        platform, version = version_obj.platform, version_obj.version_number
        getattr(self, format_label_field).SetLabelText(
            WORLD_FORMAT_LABEL.replace(
                "<>",
                f"{platform} {'.'.join(map(str, version)) if isinstance(version, (list, tuple)) else version}",
            )
        )

    def choose_world(self):
        dir_dialog = wx.DirDialog(
            None,
            "Choose world directory",
            "",
            wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,
        )
        try:
            if dir_dialog.ShowModal() == wx.ID_CANCEL:
                return
            return dir_dialog.GetPath()
        except Exception:
            wx.LogError("Failed to open directory!")
            raise
        finally:
            dir_dialog.Destroy()


class BlockStateCompleter(wx.TextCompleterSimple):
    def __init__(self, max_results=25):
        super(BlockStateCompleter, self).__init__()
        self._max_results = max_results
        self._has_blockstates = False

        self._namespaces = []
        self._block_basenames = {}
        self._sub_version = None

    def set_blockstate_subversion(self, sub_version):
        self._has_blockstates = True
        self._sub_version = sub_version

        namespaces = sub_version.namespaces(mode="block")
        self._namespaces = [f"{ns}:" for ns in namespaces]
        self._block_basenames = {namespace: [] for namespace in namespaces}
        for namespace in namespaces:
            for basename in sub_version.base_names(mode="block", namespace=namespace):
                self._block_basenames[namespace].append(basename)

    def GetCompletions(self, prefix):
        if not self._has_blockstates:
            return []

        if ":" not in prefix:
            return self._namespaces

        valid_results = []
        separator = prefix.index(":")
        namespace = prefix[:separator]
        basename_prefix = prefix[separator + 1 :]
        for basename in self._block_basenames.get(namespace, []):

            if basename.startswith(basename_prefix):
                valid_results.append(f"{namespace}:{basename}")

                if len(valid_results) == self._max_results:
                    return valid_results

        if "[" in prefix and "]" not in prefix and self._sub_version is not None:
            prop_separator = prefix.index("[")
            basename = prefix[separator + 1 : prop_separator]
            try:
                specification = self._sub_version.get_specification(
                    mode="block", namespace=namespace, base_name=basename
                )
            except KeyError:
                return valid_results

            entered_properties = prefix[prop_separator + 1 :].split(",")
            in_progress_property = entered_properties[-1]
            entered_properties = entered_properties[:-1]
            entered_property_names = set(
                (prop.split("=")[0] for prop in entered_properties)
            )

            for property_name in specification["properties"]:

                if property_name in entered_property_names:
                    continue

                if property_name.startswith(in_progress_property):
                    valid_results.append(
                        f"{namespace}:{basename}[{','.join(entered_properties)}{',' if entered_properties else ''}{property_name}="
                    )
                elif "=" in in_progress_property:
                    entered_property = in_progress_property[
                        : in_progress_property.index("=")
                    ]
                    for value in specification["properties"].get(entered_property, ()):
                        valid_results.append(
                            f"{namespace}:{basename}[{','.join(entered_properties)}{',' if entered_properties else ''}{entered_property}={value}"
                        )

                if len(valid_results) == self._max_results:
                    return valid_results

        return valid_results


if __name__ == "__main__":
    app = wx.App()
    frame = MainWindow(None)
    app.MainLoop()
