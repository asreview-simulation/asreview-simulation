from asreview_simulation._private.model_configs import ModelConfigs


class Provided:
    def __init__(self):
        self.balancer = False
        self.classifier = False
        self.extractor = False
        self.querier = False
        self.sampler = False
        self.stopping = False


class State:
    def __init__(self):
        self.models = ModelConfigs()
        self.provided = Provided()
