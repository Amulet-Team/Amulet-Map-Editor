import wx

import amulet_map_editor.resources as resources

tablericons = resources.img.icon.tablericons

ADD_ICON = tablericons.plus_green.bitmap()
SUBTRACT_ICON = tablericons.minus_red.bitmap()
EDIT_ICON = tablericons.edit.bitmap()
REFRESH_ICON = tablericons.refresh.bitmap()

UP_ARROW = tablericons.chevron_up.bitmap()
DOWN_ARROW = tablericons.chevron_down.bitmap()

UP_CARET = tablericons.caret_up.bitmap()
DOWN_CARET = tablericons.caret_down.bitmap()

COLOUR_PICKER = tablericons.color_picker.bitmap()
TRASH = tablericons.trash.bitmap()
MAXIMIZE = tablericons.arrows_maximize.bitmap()
MINIMIZE = tablericons.arrows_minimize.bitmap()


def scale_bitmap(bitmap, width, height):
    image = bitmap.ConvertToImage()
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    return image.ConvertToBitmap()
