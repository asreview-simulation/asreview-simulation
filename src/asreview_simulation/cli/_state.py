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
    def __init__(
        self,
        balancer=None,
        classifier=None,
        extractor=None,
        provided=None,
        querier=None,
        sampler=None,
        stopping=None,
    ):
        if balancer is not None:
            self.balancer = balancer
        else:
            self.balancer = Model(
                abbr="double",
                params={
                    "a": 2.155,
                    "alpha": 0.94,
                    "b": 0.789,
                    "beta": 1.0,
                },
            )

        if classifier is not None:
            self.classifier = classifier
        else:
            self.classifier = Model(
                abbr="nb",
                params={
                    "alpha": 3.822,
                },
            )

        if extractor is not None:
            self.extractor = extractor
        else:
            self.extractor = Model(
                abbr="tfidf",
                params={
                    "ngram_max": 1,
                    "stop_words": "english",
                },
            )

        if provided is not None:
            self.provided = provided
        else:
            self.provided = Provided()

        if querier is not None:
            self.querier = querier
        else:
            self.querier = Model(
                abbr="max",
                params={
                    "n_instances": 1,
                },
            )

        if sampler is not None:
            self.sampler = sampler
        else:
            self.sampler = Model(
                abbr="random",
                params={
                    "init_seed": None,
                    "n_excluded": 1,
                    "n_included": 1,
                },
            )

        if stopping is not None:
            self.stopping = stopping
        else:
            self.stopping = Model(
                abbr="min",
                params={},
            )

    def asdict(self):
        return {
            "balancer": self.balancer.asdict(),
            "classifier": self.classifier.asdict(),
            "extractor": self.extractor.asdict(),
            "querier": self.querier.asdict(),
            "sampler": self.sampler.asdict(),
            "stopping": self.stopping.asdict(),
        }
