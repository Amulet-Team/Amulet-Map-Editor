import wx
from amulet_map_editor import resources

resources_icon = resources.img.icon

ADD_ICON = wx.Bitmap(resources_icon["add.png"])
SUBTRACT_ICON = wx.Bitmap(resources_icon["subtract.png"])
EDIT_ICON = wx.Bitmap(resources_icon["edit.png"])

def scale_bitmap(bitmap, width, height):
    image = bitmap.ConvertToImage()
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    return image.ConvertToBitmap()
