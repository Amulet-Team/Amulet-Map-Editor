import wx
import os
from amulet_map_editor import IMG_DIR

ADD_ICON = wx.Bitmap(os.path.join(IMG_DIR, "icon", "add.png"))
SUBTRACT_ICON = wx.Bitmap(os.path.join(IMG_DIR, "icon", "subtract.png"))
EDIT_ICON = wx.Bitmap(os.path.join(IMG_DIR, "icon", "edit.png"))
REFRESH_ICON = wx.Bitmap(os.path.join(IMG_DIR, "icon", "refresh.png"))


def scale_bitmap(bitmap, width, height):
    image = bitmap.ConvertToImage()
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    return image.ConvertToBitmap()
