from dataclasses import dataclass
from asreview_simulation._private.models import Models


@dataclass
class Provided:
    def __init__(
        self,
        balancer: bool = False,
        classifier: bool = False,
        extractor: bool = False,
        querier: bool = False,
        sampler: bool = False,
        stopping: bool = False,
    ):
        self.balancer = balancer
        self.classifier = classifier
        self.extractor = extractor
        self.querier = querier
        self.sampler = sampler
        self.stopping = stopping


@dataclass
class State:
    def __init__(self, models=None, provided=None):
        self.models: Models = models or Models()
        self.provided: Provided = provided or Provided()
