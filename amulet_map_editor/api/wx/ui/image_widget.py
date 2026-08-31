import wx


class ImageWidget(wx.StaticBitmap):
    """An image widget that correctly scales the image to match the DPI."""

    def __init__(self, parent: wx.Window, image: wx.Image, size: wx.Size):
        if not image.IsOk():
            raise ValueError("Image is not valid")

        super().__init__(parent)
        self._image = image
        self._size = size

        self._set_bitmap()
        self.Bind(wx.EVT_DPI_CHANGED, self._set_bitmap)

    def _set_bitmap(self, evt=None) -> None:
        width = int(self._size.width * self.GetDPIScaleFactor())
        height = int(self._size.height * self.GetDPIScaleFactor())
        scaled_image = self._image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        bitmap = scaled_image.ConvertToBitmap()
        self.SetBitmap(bitmap)
        self.SetMinSize(wx.Size(width, height))
