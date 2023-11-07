from dataclasses import dataclass


@dataclass
class Model:
    def __init__(self, abbr: str, params: dict):
        self.abbr = abbr
        self.params = params

    def __repr__(self):
        return f"Model(abbr='{self.abbr}', params={self.params}"

    def asdict(self):
        return {
            "abbr": self.abbr,
            "params": self.params,
        }


balancer_default = Model(abbr="bal-double", params={"a": 2.155, "alpha": 0.94, "b": 0.789, "beta": 1.0})
classifier_default = Model(abbr="cls-nb", params={"alpha": 3.822})
extractor_default = Model(abbr="fex-tfidf", params={
    "ngram_max": 1,
    "split_ta": False,
    "stop_words":
    "english",
    "use_keywords": False
})
querier_default = Model(abbr="qry-max", params={"n_instances": 1})
sampler_default = Model(abbr="sam-random", params={"init_seed": None, "n_excluded": 1, "n_included": 1})
stopping_default = Model(abbr="stp-rel", params={})


@dataclass
class Models:
    def __init__(
        self,
        balancer: Model = None,
        classifier: Model = None,
        extractor: Model = None,
        querier: Model = None,
        sampler: Model = None,
        stopping: Model = None,
    ):
        self.balancer = balancer or balancer_default
        self.classifier = classifier or classifier_default
        self.extractor = extractor or extractor_default
        self.querier = querier or querier_default
        self.sampler = sampler or sampler_default
        self.stopping = stopping or stopping_default

    def asdict(self):
        return {
            "balancer": self.balancer.asdict(),
            "classifier": self.classifier.asdict(),
            "extractor": self.extractor.asdict(),
            "querier": self.querier.asdict(),
            "sampler": self.sampler.asdict(),
            "stopping": self.stopping.asdict(),
        }
