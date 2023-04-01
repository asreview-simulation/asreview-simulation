from dataclasses import dataclass
from ._model import Model


@dataclass
class State:
    balancer: Model = Model()
    classifier: Model = Model()
    extractor: Model = Model()
    querier: Model = Model()

