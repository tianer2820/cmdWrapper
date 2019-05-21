"""
implies all entries
"""
import wx


class Entry(wx.BoxSizer):
    """
    base class for all entries
    """
    def __init__(self, parent, name):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        self._name = name
        self._parent = parent

    def get_name(self) -> str:
        """
        get the argument name
        """
        return self._name

    def get_value(self):
        """
        get the value
        """
        return None


class TextEntry(Entry):
    """
    text based entry
    """
    def __init__(self, parent, name):
        Entry.__init__(self, parent, name)
        self._label = wx.StaticText(parent, wx.ID_ANY, name)
        self._entry = wx.TextCtrl(parent, wx.ID_ANY)
        self.Add(self._label, 0, wx.ALL | wx.EXPAND, 2)
        self.Add(self._entry, 1, wx.ALL | wx.EXPAND, 2)

    def get_value(self):
        """
        get the value
        """
        return self._entry.GetLineText(0)


class IntEntry(TextEntry):
    """
    int entry
    """
    def get_value(self):
        """
        get the value
        """
        value = self._entry.GetLineText(0)
        try:
            value = int(value)
            return value
        except ValueError:
            message = 'ValueError:' + self._name + 'must be an integer'
            wx.MessageDialog(self._parent, message).ShowModal()
            return None


class FloatEntry(TextEntry):
    """
    float entry
    """
    def get_value(self):
        """
        get the value
        """
        value = self._entry.GetLineText(0)
        try:
            value = float(value)
            return value
        except ValueError:
            message = 'ValueError:' + self._name + 'must be an real number'
            wx.MessageDialog(self._parent, message).ShowModal()
            return None


class OpenFileEntry(Entry):
    """
    entry that opens a existing file
    """
    def __init__(self, parent, name):
        Entry.__init__(self, parent, name)
        self._label = wx.StaticText(parent, wx.ID_ANY, name)
        self._entry = wx.TextCtrl(parent, wx.ID_ANY)
        self._button = wx.Button(parent, wx.ID_ANY, 'brows...')

        self._button.Bind(wx.EVT_BUTTON, self._brows_file)

        self.Add(self._label, 0, wx.ALL | wx.EXPAND, 2)
        self.Add(self._entry, 1, wx.ALL | wx.EXPAND, 2)
        self.Add(self._button, 0, wx.ALL | wx.EXPAND, 2)

    def _brows_file(self, e):
        dialog = wx.FileDialog(self._parent)
        ret = dialog.ShowModal()
        if ret == wx.ID_OK:
            self._entry.Clear()
            self._entry.AppendText(dialog.GetPath())

    def get_value(self):
        """
        get the value
        """
        return self._entry.GetLineText(0)


class DirEntry(OpenFileEntry):
    """
    entry that opens a directory
    """
    def _brows_file(self, e):
        dialog = wx.DirDialog(self._parent)
        ret = dialog.ShowModal()
        if ret == wx.ID_OK:
            self._entry.Clear()
            self._entry.AppendText(dialog.GetPath())


class SaveFileEntry(OpenFileEntry):
    """
    entry that select a not existing file
    """
    def _brows_file(self, e):
        dialog = wx.FileDialog(self._parent, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        ret = dialog.ShowModal()
        if ret == wx.ID_OK:
            self._entry.Clear()
            self._entry.AppendText(dialog.GetPath())

