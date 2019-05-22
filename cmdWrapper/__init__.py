"""
a simple gui wrapper for command line programs
"""
import wx
import cmdWrapper.wxlib as lib
from typing import Callable


class Wrapper:
    """
    the wrapper object
    """
    def __init__(self, title: str, min_window_size=(300, 200)):
        self.app = wx.App()
        self.window = wx.Frame(None)
        self.window.SetMinSize(min_window_size)
        self.window.SetTitle(title)

        self.box = wx.BoxSizer(wx.VERTICAL)
        self.arglist = []
        self.call_function = None

    def add_int(self, name, default=0):
        """
        add a int entry to the window

        :param name: name of the entry
        :param default: the default value
        """
        assert type(default) == int
        entry = lib.IntEntry(self.window, name, default)
        self.box.Add(entry, 0, wx.ALL | wx.EXPAND, 2)
        self.arglist.append(entry)

    def add_float(self, name, default=0.0):
        """
        add a int entry to the window

        :param name: name of the entry
        :param default: the default value
        """
        assert type(default) == float
        entry = lib.FloatEntry(self.window, name, default)
        self.box.Add(entry, 0, wx.ALL | wx.EXPAND, 2)
        self.arglist.append(entry)

    def add_open_file(self, name, default=''):
        """
        add a int entry to the window

        :param name: name of the entry
        :param default: the default value
        """
        assert type(default) == str
        entry = lib.OpenFileEntry(self.window, name, default)
        self.box.Add(entry, 0, wx.ALL | wx.EXPAND, 2)
        self.arglist.append(entry)

    def add_save_file(self, name, default=''):
        """
        add a int entry to the window

        :param name: name of the entry
        :param default: the default value
        """
        assert type(default) == str
        entry = lib.SaveFileEntry(self.window, name, default)
        self.box.Add(entry, 0, wx.ALL | wx.EXPAND, 2)
        self.arglist.append(entry)

    def add_dir(self, name, default=''):
        """
        add a int entry to the window

        :param name: name of the entry
        :param default: the default value
        """
        assert type(default) == str
        entry = lib.DirEntry(self.window, name, default)
        self.box.Add(entry, 0, wx.ALL | wx.EXPAND, 2)
        self.arglist.append(entry)

    def add_boolean(self, name, default=False):
        """
        add a boolean entry to the window

        :param name: name of the entry
        :param default: the default value
        """
        assert type(default) == bool
        entry = lib.BooleanEntry(self.window, name, default)
        self.box.Add(entry, 0, wx.ALL | wx.EXPAND, 2)
        self.arglist.append(entry)

    def _go(self, e):
        """
        function bind to the button

        :param e: event
        """
        args = {}
        for entry in self.arglist:
            args[entry.get_name()] = entry.get_value()
        self.call_function(args)

    def show(self, size=(300, 300)):
        """
        show the window

        :param size: size of the window in pixels
        """
        if self.call_function is None:
            raise ReferenceError('please bind a call back function first!')
        but = wx.Button(self.window)
        but.SetLabel('GO!')
        but.Bind(wx.EVT_BUTTON, self._go)
        self.box.Add(but, 0, wx.ALL | wx.EXPAND, 4)
        self.window.SetSizer(self.box)
        self.window.SetSize(size)
        self.window.Show()
        self.app.MainLoop()

    def bind(self, function: Callable):
        """
        bind a function to the button

        the first argument is a dict which contain all arguments from user

        :param function: the function
        """
        self.call_function = function
