import logging
from pathlib import Path


class foo(object):
    def __init__(self, folder_path=None, number=None):
        super().__init__()
        self.init_api(folder_path, number)
        self.initialized = False

    def init_api(self, folder_path, number):
        if not folder_path or not number:
            return
        self.initialized = True
        self.folder_path = Path(folder_path)
        self.name = f"sp{number}"

        cva_finder = list(self.folder_path.glob("**\*.cva"))
        self.cva_path = self.get_unique_result(cva_finder)

        exe_finder = list(self.folder_path.glob("**\*.exe"))
        self.exe_path = self.get_unique_result(exe_finder)

        self.installed_path = self.find_installed_path()

    def find_installed_path(self):
        os, plt = 'win', '64'
        self.installed_path = Path("C:")

    @staticmethod
    def get_unique_result(finder):
        if len(finder) != 1:
            raise Exception("find zero or found too many")
        else:
            return finder[0]

    def check_init(self):
        if not self.initialized:
            raise NameError("please init first")

    @property
    def folder_path(self):
        self.check_init()
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path):
        self._folder_path = folder_path

    @property
    def name(self):
        self.check_init()
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def cva_path(self):
        self.check_init()
        return self._cva_path

    @cva_path.setter
    def cva_path(self, cva_path):
        self._cva_path = cva_path

    @property
    def exe_path(self):
        self.check_init()
        return self._exe_path

    @exe_path.setter
    def exe_path(self, exe_path):
        self._exe_path = exe_path

    @property
    def installed_path(self):
        self.check_init()
        return self._installed_path

    @installed_path.setter
    def installed_path(self, installed_path):
        self._installed_path = installed_path

f = foo()
f.init_api('.', 123)