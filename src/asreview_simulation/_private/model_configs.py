class Model:
    def __init__(self, abbr: str, params: dict):
        self.abbr = abbr
        self.params = params

    def asdict(self):
        return {
            "abbr": self.abbr,
            "params": self.params
        }


class ModelConfigs:
    def __init__(self):
        self.balancer = Model(abbr="bal-double", params={"a": 2.155, "alpha": 0.94, "b": 0.789, "beta": 1.0})
        self.classifier = Model(abbr="cls-nb", params={"alpha": 3.822})
        self.extractor = Model(abbr="fex-tfidf", params={
            "ngram_max": 1,
            "split_ta": False,
            "stop_words": "english",
            "use_keywords": False,
        })
        self.querier = Model(abbr="qry-max", params={"n_instances": 1})
        self.sampler = Model(abbr="sam-random", params={"init_seed": None, "n_excluded": 1, "n_included": 1})
        self.stopping = Model(abbr="stp-rel", params={})

    def asdict(self):
        return {
            "balancer": self.balancer.asdict(),
            "classifier": self.classifier.asdict(),
            "extractor": self.extractor.asdict(),
            "querier": self.querier.asdict(),
            "sampler": self.sampler.asdict(),
            "stopping": self.stopping.asdict(),
        }
