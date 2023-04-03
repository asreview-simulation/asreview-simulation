from dataclasses import dataclass


@dataclass
class Model:
    model: str
    params: dict


@dataclass
class Provided:
    balancer: bool = False
    classifier: bool = False
    extractor: bool = False
    querier: bool = False
    sampler: bool = False


@dataclass
class State:
    provided: Provided = Provided()
    balancer: Model = Model("double", {"a": 2.155, "alpha": 0.94, "b": 0.789, "beta": 1.0})
    classifier: Model = Model("nb", {"alpha": 3.822})
    extractor: Model = Model("tfidf", {"ngrams_max": 1, "stop_words": "english"})
    sampler: Model = Model("random", {"n_included": 1, "n_excluded": 1})
    querier: Model = Model("max", {})
