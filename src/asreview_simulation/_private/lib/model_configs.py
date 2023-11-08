from asreview_simulation._private.lib.model_config import ModelConfig


class ModelConfigs:
    def __init__(self, bal=None, cls=None, fex=None, qry=None, sam=None,stp=None):
        self.bal = bal or ModelConfig(abbr="bal-double", params={"a": 2.155, "alpha": 0.94, "b": 0.789, "beta": 1.0})
        self.cls = cls or ModelConfig(abbr="cls-nb", params={"alpha": 3.822})
        self.fex = fex or ModelConfig(abbr="fex-tfidf", params={
            "ngram_max": 1,
            "split_ta": False,
            "stop_words": "english",
            "use_keywords": False,
        })
        self.qry = qry or ModelConfig(abbr="qry-max", params={"n_instances": 1})
        self.sam = sam or ModelConfig(abbr="sam-random", params={"init_seed": None, "n_excluded": 1, "n_included": 1})
        self.stp = stp or ModelConfig(abbr="stp-rel", params={})

    def asdict(self):
        return {
            "bal": self.bal.asdict(),
            "cls": self.cls.asdict(),
            "fex": self.fex.asdict(),
            "qry": self.qry.asdict(),
            "sam": self.sam.asdict(),
            "stp": self.stp.asdict(),
        }
