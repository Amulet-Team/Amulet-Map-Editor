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
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 370), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.tab_holder = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # region converter panel
        self.converter_panel = wx.Panel(self.tab_holder, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        convert_panel_sizer = wx.GridBagSizer(0, 0)
        convert_panel_sizer.SetFlexibleDirection(wx.BOTH)
        convert_panel_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        convert_panel_sizer.SetEmptyCellSize(wx.Size(25, 25))

        self.input_panel = wx.Panel(self.converter_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.BORDER_SUNKEN | wx.TAB_TRAVERSAL)
        self.input_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        input_panel_sizer = wx.GridBagSizer(0, 0)
        input_panel_sizer.SetFlexibleDirection(wx.BOTH)
        input_panel_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.input_world_label = wx.StaticText(self.input_panel, wx.ID_ANY, u"Input World", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.input_world_label.Wrap(-1)

        input_panel_sizer.Add(self.input_world_label, wx.GBPosition(0, 0), wx.GBSpan(1, 5), wx.ALL, 5)

        self.in_world_path_label = wx.StaticText(self.input_panel, wx.ID_ANY, u"World Path:", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.in_world_path_label.Wrap(-1)

        input_panel_sizer.Add(self.in_world_path_label, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.in_world_format_label = wx.StaticText(self.input_panel, wx.ID_ANY, u"World Format/Version:",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.in_world_format_label.Wrap(-1)

        input_panel_sizer.Add(self.in_world_format_label, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.select_input_button = wx.Button(self.input_panel, wx.ID_ANY, u"Select Input World", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        input_panel_sizer.Add(self.select_input_button, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.input_panel.SetSizer(input_panel_sizer)
        self.input_panel.Layout()
        input_panel_sizer.Fit(self.input_panel)
        convert_panel_sizer.Add(self.input_panel, wx.GBPosition(0, 0), wx.GBSpan(1, 14), wx.EXPAND | wx.ALL, 5)

        self.output_panel = wx.Panel(self.converter_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.BORDER_SUNKEN | wx.TAB_TRAVERSAL)
        self.output_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        output_panel_sizer = wx.GridBagSizer(0, 0)
        output_panel_sizer.SetFlexibleDirection(wx.BOTH)
        output_panel_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.output_world_label = wx.StaticText(self.output_panel, wx.ID_ANY, u"Output World", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.output_world_label.Wrap(-1)

        output_panel_sizer.Add(self.output_world_label, wx.GBPosition(0, 0), wx.GBSpan(1, 5), wx.ALL, 5)

        self.out_world_path_label = wx.StaticText(self.output_panel, wx.ID_ANY, u"World Path:", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.out_world_path_label.Wrap(-1)

        output_panel_sizer.Add(self.out_world_path_label, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.out_world_format_label = wx.StaticText(self.output_panel, wx.ID_ANY, u"World Format/Version:",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.out_world_format_label.Wrap(-1)

        output_panel_sizer.Add(self.out_world_format_label, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.select_output_button = wx.Button(self.output_panel, wx.ID_ANY, u"Select Output World", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        output_panel_sizer.Add(self.select_output_button, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.output_panel.SetSizer(output_panel_sizer)
        self.output_panel.Layout()
        output_panel_sizer.Fit(self.output_panel)
        convert_panel_sizer.Add(self.output_panel, wx.GBPosition(1, 0), wx.GBSpan(1, 14), wx.EXPAND | wx.ALL, 5)

        self.convert_button = wx.Button(self.converter_panel, wx.ID_ANY, u"Convert", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        convert_panel_sizer.Add(self.convert_button, wx.GBPosition(2, 11), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.close_button = wx.Button(self.converter_panel, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0)
        convert_panel_sizer.Add(self.close_button, wx.GBPosition(2, 12), wx.GBSpan(1, 1), wx.ALL, 5)

        self.converter_progress = wx.Gauge(self.converter_panel, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize,
                                           wx.GA_HORIZONTAL)
        self.converter_progress.SetValue(0)
        convert_panel_sizer.Add(self.converter_progress, wx.GBPosition(2, 0), wx.GBSpan(1, 8), wx.ALL | wx.EXPAND, 5)

        self.converter_panel.SetSizer(convert_panel_sizer)
        self.converter_panel.Layout()
        convert_panel_sizer.Fit(self.converter_panel)
        self.tab_holder.AddPage(self.converter_panel, u"World Converter", False)

        # endregion

        # region modify panel
        self.modify_panel = wx.Panel(self.tab_holder, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        modify_panel_sizer = wx.GridBagSizer(0, 0)
        modify_panel_sizer.SetFlexibleDirection(wx.BOTH)
        modify_panel_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.modify_world_note = wx.StaticText(self.modify_panel, wx.ID_ANY, u"Note: this will modify the input world",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.modify_world_note.Wrap(-1)

        modify_panel_sizer.Add(self.modify_world_note, wx.GBPosition(0, 0), wx.GBSpan(1, 2), wx.ALL, 5)

        self.run_operation_cb = wx.CheckBox(self.modify_panel, wx.ID_ANY, u"Run Fill Operation", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        modify_panel_sizer.Add(self.run_operation_cb, wx.GBPosition(1, 0), wx.GBSpan(1, 2), wx.ALL, 5)

        # region Coordinate panel

        self.start_coordinate_label = wx.StaticText(self.modify_panel, wx.ID_ANY, u"Start Coordinates (x,y,z):",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.start_coordinate_label.Wrap(-1)

        modify_panel_sizer.Add(self.start_coordinate_label, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.start_x = wx.SpinCtrl(self.modify_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.SP_ARROW_KEYS | wx.SP_WRAP, min=-29999984, max=299999984, initial=0)
        self.start_x.SetToolTip(u"X Coordinate")

        modify_panel_sizer.Add(self.start_x, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.start_y = wx.SpinCtrl(self.modify_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.SP_ARROW_KEYS | wx.SP_WRAP, min=-29999984, max=299999984, initial=0)
        self.start_y.SetToolTip(u"Y Coordinate")

        modify_panel_sizer.Add(self.start_y, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.start_z = wx.SpinCtrl(self.modify_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   wx.SP_ARROW_KEYS | wx.SP_WRAP, min=-29999984, max=299999984, initial=0)
        self.start_z.SetToolTip(u"Z Coordinate")

        modify_panel_sizer.Add(self.start_z, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.end_coordinate_label = wx.StaticText(self.modify_panel, wx.ID_ANY, u"End Coordinates (x,y,z):",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.end_coordinate_label.Wrap(-1)

        modify_panel_sizer.Add(self.end_coordinate_label, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.end_x = wx.SpinCtrl(self.modify_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 wx.SP_ARROW_KEYS | wx.SP_WRAP, min=-29999984, max=299999984, initial=0)
        self.end_x.SetToolTip(u"X Coordinate")

        modify_panel_sizer.Add(self.end_x, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.end_y = wx.SpinCtrl(self.modify_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 wx.SP_ARROW_KEYS | wx.SP_WRAP, min=-29999984, max=299999984, initial=0)
        self.end_y.SetToolTip(u"Y Coordinate")

        modify_panel_sizer.Add(self.end_y, wx.GBPosition(5, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.end_z = wx.SpinCtrl(self.modify_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 wx.SP_ARROW_KEYS | wx.SP_WRAP, min=-29999984, max=299999984, initial=0)
        self.end_z.SetToolTip(u"Z Coordinate")

        modify_panel_sizer.Add(self.end_z, wx.GBPosition(5, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        # endregion

        # region Blockstate chooser
        blockstate_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.fill_block_label = wx.StaticText(self.modify_panel, wx.ID_ANY, u"Fill Block:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.fill_block_label.Wrap(-1)

        blockstate_sizer.Add(self.fill_block_label, 0, wx.ALL, 5)

        self.fill_blockstate_field = wx.TextCtrl(self.modify_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.fill_blockstate_field.SetMinSize(wx.Size(380, -1))

        blockstate_sizer.Add(self.fill_blockstate_field, 0, wx.ALL | wx.EXPAND | wx.RIGHT, 5)

        modify_panel_sizer.Add(blockstate_sizer, wx.GBPosition(9, 0), wx.GBSpan(1, 3), wx.EXPAND, 5)

        # endregion

        # region Platform/Version specifier
        specification_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.platform_label = wx.StaticText(self.modify_panel, wx.ID_ANY, u"Platform:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.platform_label.Wrap(-1)

        specification_sizer.Add(self.platform_label, 0, wx.ALL, 5)

        platform_choiceChoices = []
        self.platform_choice = wx.Choice(self.modify_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         platform_choiceChoices, 0)
        self.platform_choice.SetSelection(0)
        specification_sizer.Add(self.platform_choice, 0, wx.ALL, 5)

        specification_sizer.Add((20, 0), 0, wx.EXPAND, 5)

        self.version_label = wx.StaticText(self.modify_panel, wx.ID_ANY, u"Version:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.version_label.Wrap(-1)

        specification_sizer.Add(self.version_label, 0, wx.ALL, 5)

        version_choiceChoices = []
        self.version_choice = wx.Choice(self.modify_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        version_choiceChoices, 0)
        self.version_choice.SetSelection(0)
        specification_sizer.Add(self.version_choice, 0, wx.ALL, 5)

        modify_panel_sizer.Add(specification_sizer, wx.GBPosition(7, 0), wx.GBSpan(1, 3), wx.EXPAND, 5)

        # endregion

        self.modify_panel.SetSizer(modify_panel_sizer)
        self.modify_panel.Layout()
        modify_panel_sizer.Fit(self.modify_panel)
        self.tab_holder.AddPage(self.modify_panel, u"Modify Input World", True)

        # endregion

        bSizer1.Add(self.tab_holder, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.tab_holder.SetSelection(0)

        self.blockstate_completer = BlockStateCompleter()
        self.fill_blockstate_field.AutoComplete(self.blockstate_completer)

        # Connect Events
        self.select_input_button.Bind(wx.EVT_BUTTON, self.select_input_buttonOnButtonClick)
        self.select_output_button.Bind(wx.EVT_BUTTON, self.select_output_buttonOnButtonClick)
        self.convert_button.Bind(wx.EVT_BUTTON, self.convert_buttonOnButtonClick)
        self.close_button.Bind(wx.EVT_BUTTON, self.close_buttonOnButtonClick)
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
        self.choose_and_set_world(('input_world_path', 'in_world_path_label', 'in_world_format_label'), event)

    def select_output_buttonOnButtonClick(self, event):
        self.choose_and_set_world(('output_world_path', 'out_world_path_label', 'out_world_format_label'), event)

    def close_buttonOnButtonClick(self, event):
        self.Close()

    def platform_choiceOnChoice(self, event):
        self.selected_platform = selected_platform = event.GetString()
        self.version_choice.Clear()
        self.version_choice.AppendItems(
            [f"{v[0]}.{v[1]}.{v[2]}" for v in self.translation_manager.version_numbers(selected_platform)])

    def version_choiceOnChoice(self, event):
        if self.selected_platform is None:
            event.Skip()

        version_numbers = [i for i in map(int, event.GetString().split('.'))]
        self.blockstate_completer.set_blockstate_subversion(
            self.translation_manager.get_sub_version(self.selected_platform, version_numbers, True))

    def choose_and_set_world(self, fields, event):
        world_path_field, path_label_field, format_label_field = fields[0], fields[1], fields[2]

        world_path = self.choose_world(event)
        _format, version = amulet.world_interface.load_format(world_path)._max_world_version()

        try:
            version_obj = self.translation_manager.get_version(_format, version)
        except (AssertionError, amulet.api.errors.LoaderNoneMatched) as e:
            dialog = wx.MessageDialog(self, f"Couldn't find a valid loader for \"{world_path}\"",
                                      style=wx.OK_DEFAULT | wx.ICON_ERROR)
            dialog.ShowModal()
            return

        setattr(self, world_path_field, world_path)
        getattr(self, path_label_field).SetLabelText(WORLD_PATH_LABEL.replace("<>", world_path))
        platform, version = version_obj.platform, version_obj.version_number
        getattr(self, format_label_field).SetLabelText(
            WORLD_FORMAT_LABEL.replace(
                "<>",
                f"{platform} {'.'.join(map(str, version)) if isinstance(version, (list, tuple)) else version}")
        )

    def choose_world(self, evt):
        dir_dialog = wx.DirDialog(None, "Choose world directory", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        try:
            if dir_dialog.ShowModal() == wx.ID_CANCEL:
                return
            return dir_dialog.GetPath()
        except Exception:
            wx.LogError('Failed to open directory!')
            raise
        finally:
            dir_dialog.Destroy()


class BlockStateCompleter(wx.TextCompleterSimple):

    def __init__(self, maxResults=25):
        super(BlockStateCompleter, self).__init__()
        self._maxResults = maxResults
        self._has_blockstates = False

        self._namespaces = []
        self._block_basenames = {}

    def set_blockstate_subversion(self, sub_version):
        self._has_blockstates = True

        namespaces = sub_version.namespaces(mode='block')
        self._namespaces = [f"{ns}:" for ns in namespaces]
        self._block_basenames = {namespace: [] for namespace in namespaces}
        for namespace in namespaces:
            for basename in sub_version.base_names(mode='block', namespace=namespace):
                self._block_basenames[namespace].append(basename)

    def GetCompletions(self, prefix):
        if not self._has_blockstates:
            return []

        if ':' not in prefix:
            return self._namespaces

        valid_results = []
        separator = prefix.index(':')
        namespace = prefix[:separator]
        basename_prefix = prefix[separator + 1:]
        for basename in self._block_basenames.get(namespace, []):

            if basename.startswith(basename_prefix):
                valid_results.append(f"{namespace}:{basename}")

                if len(valid_results) == self._maxResults:
                    return valid_results

        return valid_results


if __name__ == '__main__':
    app = wx.App()
    frame = MainWindow(None)
    app.MainLoop()
