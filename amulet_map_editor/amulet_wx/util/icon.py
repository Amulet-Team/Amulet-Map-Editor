import wx
import os
from amulet_map_editor import IMG_DIR

ADD_ICON = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "plus_green.png"))
SUBTRACT_ICON = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "minus_red.png"))
EDIT_ICON = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "edit.png"))
REFRESH_ICON = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "refresh.png"))

UP_ARROW = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "chevron-up.png"))
DOWN_ARROW = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "chevron-down.png"))

UP_CARET = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "caret-up.png"))
DOWN_CARET = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "caret-down.png"))

COLOUR_PICKER = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "color-picker.png"))
TRASH = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "trash.png"))
MAXIMIZE = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "arrows-maximize.png"))
MINIMIZE = wx.Bitmap(os.path.join(IMG_DIR, "icon", "tablericons", "arrows-minimize.png"))


def scale_bitmap(bitmap, width, height):
    image = bitmap.ConvertToImage()
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    return image.ConvertToBitmap()
