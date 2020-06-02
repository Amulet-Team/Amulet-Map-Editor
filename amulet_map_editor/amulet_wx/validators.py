import wx


class BaseValidator(wx.Validator):
    ''' Validates data as it is entered into the text controls. '''

    def __init__(self):
        super().__init__()
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        return self.__class__()

    def Validate(self, win):
        return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

    def OnChar(self, event):
        event.Skip()


class IntValidator(BaseValidator):
    def OnChar(self, event):
        keycode = int(event.GetKeyCode())
        if keycode > 256 or 48 <= keycode <= 57 or keycode == 45:
            event.Skip()


class FloatValidator(BaseValidator):
    def OnChar(self, event):
        keycode = int(event.GetKeyCode())
        if keycode > 256 or 45 <= keycode <= 57:
            event.Skip()
