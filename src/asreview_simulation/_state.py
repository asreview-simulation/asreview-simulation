from dataclasses import dataclass


@dataclass
class Model:
    def __init__(self, model: str, params: dict):
        self.model = model
        self.params = params

    def __repr__(self):
        return f"Model(model='{self.model}', params={self.params}"

    def asdict(self):
        return {
            "model": self.model,
            "params": self.params
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
    ):
        self.balancer = balancer
        self.classifier = classifier
        self.extractor = extractor
        self.querier = querier
        self.sampler = sampler


@dataclass
class State:
    def __init__(
        self,
        provided=None,
        balancer=None,
        classifier=None,
        extractor=None,
        querier=None,
        sampler=None,
    ):
        if provided is not None:
            self.provided = provided
        else:
            self.provided = Provided()

        if balancer is not None:
            self.balancer = balancer
        else:
            self.balancer = Model(
                "double",
                {
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
                "nb",
                {
                    "alpha": 3.822,
                },
            )

        if extractor is not None:
            self.extractor = extractor
        else:
            self.extractor = Model(
                "tfidf",
                {
                    "ngram_max": 1,
                    "stop_words": "english",
                },
            )

        if querier is not None:
            self.querier = querier
        else:
            self.querier = Model(
                "max",
                {},
            )

        if sampler is not None:
            self.sampler = sampler
        else:
            self.sampler = Model(
                "random",
                {
                    "init_seed": None,
                    "n_excluded": 1,
                    "n_included": 1,
                },
            )

    def asdict(self):
        return {
            "balancer": self.balancer.asdict(),
            "classifier": self.classifier.asdict(),
            "extractor": self.extractor.asdict(),
            "querier": self.querier.asdict(),
            "sampler": self.sampler.asdict()
        }
