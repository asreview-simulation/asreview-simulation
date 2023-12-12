class PluginQuad:
    def __init__(self, *, default_params=None, impl=None, pyll=None, subcommand=None):
        self.default_params = default_params
        self.impl = impl
        self.pyll = pyll
        self.subcommand = subcommand

    @property
    def impl(self):
        return self._impl

    @impl.setter
    def impl(self, impl):
        self._impl = impl

    @property
    def default_params(self):
        return self._default_params

    @default_params.setter
    def default_params(self, default_params):
        self._default_params = default_params

    @property
    def pyll(self):
        return self._pyll

    @pyll.setter
    def pyll(self, pyll):
        self._pyll = pyll

    @property
    def subcommand(self):
        return self._subcommand

    @subcommand.setter
    def subcommand(self, subcommand):
        self._subcommand = subcommand
