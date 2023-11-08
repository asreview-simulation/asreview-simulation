from asreview_simulation._private.lib.model_configs import ModelConfigs


class Provided:
    def __init__(self):
        self.bal = False
        self.cls = False
        self.fex = False
        self.qry = False
        self.sam = False
        self.stp = False


class State:
    def __init__(self):
        self.models = ModelConfigs()
        self.provided = Provided()
