from asreview_simulation._private.lib.all_model_config import AllModelConfig


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
        self.models = AllModelConfig()
        self.provided = Provided()
